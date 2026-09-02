# Kortex Website

Publishes the `wiki/` synthesis layer as a browsable static site with a
**bespoke Astro theme** — the "devops-graphite" design (flat surfaces, emerald
accent, Space Grotesk / Inter / IBM Plex Mono), ported from
[portefaix-website](https://github.com/portefaix/portefaix-website). Features a
hero landing, docs layout with a generated sidebar, light/dark toggle, and
[Pagefind](https://pagefind.app) full-text search.

## How it works

`build.sh` is the single source of truth used by both local preview and CI:

1. Regenerates `wiki/kb/` entity pages via `scripts/build_knowledge_base.py`.
2. `prepare_content.py` syncs `wiki/` into `src/content/docs/`:
   - drops `hot.md` and `skill-impact.md` (session / internal scratch)
   - guarantees a frontmatter `title` on every page (used for nav + `<title>`)
   - rewrites relative `.md` links to pretty URLs (`foo.md` → `foo/`)
3. `astro build` → `website/dist/`, then `pagefind --site dist` builds the
   search index.

### Layout

| File | Role |
|------|------|
| `src/pages/index.astro` | Landing hero + section cards (built from the collection) |
| `src/pages/[...slug].astro` | Renders every wiki page; builds the sidebar + prev/next |
| `src/layouts/Layout.astro` | Base HTML, fonts, theme toggle |
| `src/layouts/DocsLayout.astro` | Docs shell: sidebar, search, prose styles |
| `src/styles/global.css` | devops-graphite design tokens + components |
| `src/content.config.ts` | `docs` collection (glob loader, permissive schema) |

`wiki/index.md` is excluded from the docs routes — the landing renders its own
hero instead.

## Local preview

```bash
make site-preview        # dev server on http://localhost:4321
# or
./website/build.sh --serve
```

Requires **Node + npm** and **Python 3**:

```bash
brew install node
```

> Search only works in a full build (Pagefind runs post-build), not in `--serve`.

## Deploy

Pushing to `main` (touching `wiki/`, `website/`, or the build script) triggers
`.github/workflows/deploy-wiki.yml`, which builds and publishes to GitHub Pages
at <https://nlamirault.github.io/kortex/>.

**One-time setup:** repo *Settings → Pages → Source = "GitHub Actions"*.
Trigger a first run manually from the *Actions* tab (workflow_dispatch).

## Configuration

- Site URL + base path → [`astro.config.mjs`](astro.config.mjs) (`base: "/kortex"`)
- Colors, fonts, components → [`src/styles/global.css`](src/styles/global.css)
- Pinned dependencies → [`package.json`](package.json) / `package-lock.json`

The site is served from a sub-path because it deploys to a GitHub Pages project
site; internal links and assets are prefixed with the (slash-normalised) base.

## Attribution

The visual theme is adapted from `portefaix-website` (© Nicolas Lamirault,
Apache-2.0).

## Known limitation

`## Relations` tables use `[[type:slug]]` wikilinks (machine-readable, parsed by
`/graph` and the KB builder). Astro renders these as literal text. Human-facing
prose uses standard markdown links and renders correctly. The generated
`knowledge-base` + `kb/` pages provide the browsable entity/glossary view.
