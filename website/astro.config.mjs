// @ts-check
// SPDX-FileCopyrightText: Copyright (C) 2026 Nicolas Lamirault <nicolas.lamirault@gmail.com>
// SPDX-License-Identifier: Apache-2.0
import path from 'node:path';
import { defineConfig } from 'astro/config';

// NOTE: `site` is intentionally unset — Kortex has no public domain yet.
// Set it (and re-enable @astrojs/sitemap) once a domain exists.

// Entity directories that become published routes. Links into any other
// directory (projects/, people/, kb/) or to a root file (hot.md, index.md)
// are unwrapped to plain text, since those pages are not published.
const PUBLISHED = new Set(['concepts', 'domains', 'sources', 'organizations']);

/**
 * Remark plugin: resolve inter-wiki markdown links against the page's own
 * location in the bundle, then map them to site routes. A link is relative to
 * the file it sits in, so `agent2agent-a2a.md` from `concepts/x402.md` resolves
 * to `/concepts/agent2agent-a2a/`, and `../domains/ai-protocols.md` to
 * `/domains/ai-protocols/`. Links to unpublished targets become plain text.
 */
function remarkWikiLinks() {
  return (/** @type {any} */ tree, /** @type {any} */ file) => {
    const abs = file?.path ?? file?.history?.[0] ?? '';
    const ix = abs.lastIndexOf(`${path.sep}wiki${path.sep}`);
    const curDir = ix >= 0 ? path.posix.dirname(abs.slice(ix + 6).split(path.sep).join('/')) : '';

    /** @param {any} node @param {any} parent @param {number} index */
    const walk = (node, parent, index) => {
      if (node.type === 'link' && typeof node.url === 'string') {
        const url = node.url;
        const isRelativeMd =
          !/^(?:https?:|mailto:|tel:|\/|#)/.test(url) && /\.md(?:[#?].*)?$/.test(url);
        if (isRelativeMd) {
          const m = url.match(/^([^#?]*\.md)([#?].*)?$/);
          const target = m ? m[1] : url;
          const hash = m && m[2] && m[2].startsWith('#') ? m[2] : '';
          const resolved = path.posix.normalize(path.posix.join(curDir, target));
          const noExt = resolved.replace(/\.md$/, '');
          const top = noExt.split('/')[0];
          if (PUBLISHED.has(top)) {
            node.url = `/${noExt}/${hash}`;
          } else if (parent && Array.isArray(parent.children)) {
            parent.children.splice(index, 1, ...node.children);
            return;
          }
        }
      }
      if (Array.isArray(node.children)) {
        for (let i = node.children.length - 1; i >= 0; i--) walk(node.children[i], node, i);
      }
    };
    walk(tree, null, -1);
  };
}

/**
 * Remark plugin: drop the body's leading `# H1`. Every wiki page carries both a
 * `title:` in OKF frontmatter and a body `# H1` of the same name; the site
 * renders the title in the page header, so the duplicate body H1 is removed.
 */
function remarkStripLeadingH1() {
  return (/** @type {any} */ tree) => {
    const first = tree.children?.[0];
    if (first && first.type === 'heading' && first.depth === 1) {
      tree.children.shift();
    }
  };
}

// https://astro.build/config
export default defineConfig({
  markdown: {
    remarkPlugins: [remarkWikiLinks, remarkStripLeadingH1],
    shikiConfig: {
      theme: 'rose-pine-dawn',
      wrap: true,
    },
  },
});
