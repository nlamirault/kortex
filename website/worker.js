// SPDX-FileCopyrightText: Copyright (C) 2026 Nicolas Lamirault <nicolas.lamirault@gmail.com>
// SPDX-License-Identifier: Apache-2.0

/**
 * Cloudflare Worker: Markdown content negotiation for AI agents.
 *
 * The Kortex website is a static Astro build served from the ASSETS binding.
 * When a request carries `Accept: text/markdown`, the Worker fetches the built
 * HTML page, strips non-content chrome via HTMLRewriter, converts the remainder
 * back to Markdown, and returns it as `text/markdown`. This lets agents read the
 * knowledge garden as clean Markdown — close to the underlying OKF source — while
 * humans get the rendered page. All other requests pass through untouched.
 */

export default {
  /** @param {Request} request @param {{ ASSETS: Fetcher }} env */
  async fetch(request, env) {
    const accept = request.headers.get('Accept') ?? '';

    // Not a markdown request — serve the static asset as-is.
    if (!accept.includes('text/markdown')) {
      return env.ASSETS.fetch(request);
    }

    const response = await env.ASSETS.fetch(request);
    const contentType = response.headers.get('Content-Type') ?? '';

    // Only convert HTML; pass CSS/JS/images/fonts through unchanged.
    if (!contentType.includes('text/html')) {
      return response;
    }

    // Strip the head and non-content chrome, then convert the body. The page
    // already renders its own title (an <h1>) and description, so the Markdown
    // needs no synthetic front matter.
    const cleaned = new HTMLRewriter()
      .on('head, nav, footer, script, style, noscript, aside, form, [aria-hidden="true"]', {
        element(el) {
          el.remove();
        },
      })
      .transform(response);

    const html = await cleaned.text();
    const markdown = htmlToMarkdown(html);
    const tokenCount = Math.ceil(markdown.length / 4);

    return new Response(markdown, {
      status: 200,
      headers: {
        'Content-Type': 'text/markdown; charset=utf-8',
        Vary: 'Accept',
        'x-markdown-tokens': String(tokenCount),
        'Cache-Control': 'public, max-age=3600',
      },
    });
  },
};

/**
 * Convert cleaned HTML to Markdown with lightweight regex transforms.
 * @param {string} html
 * @returns {string}
 */
function htmlToMarkdown(html) {
  let md = html;

  md = md.replace(/<h1[^>]*>([\s\S]*?)<\/h1>/gi, (_, t) => `\n# ${innerText(t)}\n`);
  md = md.replace(/<h2[^>]*>([\s\S]*?)<\/h2>/gi, (_, t) => `\n## ${innerText(t)}\n`);
  md = md.replace(/<h3[^>]*>([\s\S]*?)<\/h3>/gi, (_, t) => `\n### ${innerText(t)}\n`);
  md = md.replace(/<h4[^>]*>([\s\S]*?)<\/h4>/gi, (_, t) => `\n#### ${innerText(t)}\n`);

  md = md.replace(
    /<a\b[^>]*\bhref=["']([^"']*)["'][^>]*>([\s\S]*?)<\/a>/gi,
    (_, href, text) => {
      const t = innerText(text).trim();
      return t ? `[${t}](${href})` : '';
    },
  );

  md = md.replace(
    /<pre[^>]*><code[^>]*>([\s\S]*?)<\/code><\/pre>/gi,
    (_, c) => `\n\`\`\`\n${decodeHtmlEntities(c)}\n\`\`\`\n`,
  );
  md = md.replace(/<code[^>]*>([\s\S]*?)<\/code>/gi, (_, c) => `\`${decodeHtmlEntities(c)}\``);

  md = md.replace(/<(?:strong|b)[^>]*>([\s\S]*?)<\/(?:strong|b)>/gi, (_, c) => `**${c}**`);
  md = md.replace(/<(?:em|i)[^>]*>([\s\S]*?)<\/(?:em|i)>/gi, (_, c) => `_${c}_`);

  md = md.replace(/<li[^>]*>([\s\S]*?)<\/li>/gi, (_, c) => `\n- ${innerText(c).trim()}`);
  md = md.replace(/<\/?[uo]l[^>]*>/gi, '\n');

  md = md.replace(/<p[^>]*>([\s\S]*?)<\/p>/gi, (_, c) => `\n${c.trim()}\n`);
  md = md.replace(/<hr[^>]*\/?>/gi, '\n---\n');
  md = md.replace(/<br\s*\/?>/gi, '\n');

  md = md.replace(/<[^>]+>/g, '');
  md = decodeHtmlEntities(md);

  md = md.replace(/\t/g, ' ');
  md = md.replace(/[ \t]{2,}/g, ' ');
  md = md.replace(/^ +/gm, '');
  md = md.replace(/\n{3,}/g, '\n\n');
  md = md.trim();

  return md;
}

/** Strip all HTML tags from a string. @param {string} html */
function innerText(html) {
  return decodeHtmlEntities(html.replace(/<[^>]+>/g, ''));
}

/** Decode common HTML entities. @param {string} str */
function decodeHtmlEntities(str) {
  return str
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;|&apos;/g, "'")
    .replace(/&nbsp;/g, ' ')
    .replace(/&#(\d+);/g, (_, code) => String.fromCharCode(Number(code)));
}
