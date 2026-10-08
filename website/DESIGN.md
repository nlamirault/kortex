---
# ─────────────────────────────────────────────────────────────────────────────
# Kortex Website — Design System · "Digital Garden"
# Machine-readable design tokens. This frontmatter is the SINGLE SOURCE OF TRUTH.
# Edit a value here, then run `make tokens` to regenerate src/styles/global.css.
# `make tokens-check` fails CI if global.css drifts from these values.
# Human-readable rationale lives in the markdown body below.
# ─────────────────────────────────────────────────────────────────────────────

meta:
  name: "Kortex"
  description: "Personal knowledge garden — warm paper canvas, terracotta ink, growth stages drawn from OKF status + confidence."
  platform: "web"
  colorScheme: "light"
  # cssExtras — compound/structural CSS custom properties (rgba, shadows,
  # container sizing, font stacks) that fall outside the color/spacing/radius
  # token schema but still need a single source of truth. Edit here, run `make tokens`.
  cssExtras:
    rust-border: "rgba(181, 96, 58, 0.22)"
    shadow: "rgba(61, 43, 31, 0.08)"
    shadow-subtle: "rgba(43, 40, 36, 0.05)"
    shadow-lift: "rgba(61, 43, 31, 0.14)"
    focus-ring: "rgba(181, 96, 58, 0.30)"
    container-max: "1180px"
    container-pad: "clamp(20px, 5vw, 72px)"
    measure: "66ch"
    font-serif: "\"Fraunces Variable\", \"Fraunces\", Georgia, \"Times New Roman\", serif"
    font-sans: "\"Inter Variable\", \"Inter\", system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    font-mono: "\"JetBrains Mono Variable\", ui-monospace, \"SFMono-Regular\", Menlo, monospace"

# The palette is broader than any single component needs: growth-stage colors,
# muted/subtle inks and alt surfaces are consumed directly in CSS and body guidance.
colors:
  # — Brand: terracotta ink pressed into warm paper —
  primary: "#b5603a"          # Terracotta — primary brand anchor, links, CTAs
  brand: "#b5603a"            # Terracotta — alias
  brandDark: "#8f4529"        # Burnt Sienna — gradient stop, pressed, hover
  brandSoft: "#f3e4da"        # Clay Wash — chips, soft fills

  # — Canvas: never pure white; the page is paper —
  background: "#faf8f3"       # Warm Paper — page canvas
  surface: "#fffdfb"          # Pressed Card — content cards
  surfaceElevated: "#ffffff"  # Pure White — insets, high-contrast panels
  surfaceAlt: "#f2efe7"       # Linen — alternating section bands
  border: "#e8e2d6"           # Deckle Edge — hairline rules, card borders

  # — Ink: warm near-black, never cold grey —
  textPrimary: "#2b2824"      # Ink — headings
  text: "#433f38"             # Walnut — body copy
  textMuted: "#6d675d"        # Driftwood — secondary text, captions
  textSubtle: "#938c7f"       # Ash — placeholders, disabled

  # — Growth stages (OKF status + confidence → garden metaphor) —
  seedling: "#6b7f6e"         # Sage — draft (just planted)
  seedlingSoft: "#e7efe6"
  budding: "#c08a2e"          # Amber — stable but not fully verified
  buddingSoft: "#f5ecd9"
  evergreen: "#3f7a4f"        # Fern — stable + high confidence (trusted)
  evergreenSoft: "#e4efe5"
  archived: "#938c7f"         # Ash — deprecated / retired
  archivedSoft: "#eeeae1"

  # — Semantic (orthogonal to brand accent) —
  success: "#3f7a4f"
  warning: "#c08a2e"
  error: "#b23a3a"
  info: "#4a6d84"
  link: "#b5603a"
  linkBorder: "#e3c3b2"       # under-link border tint

spacing:
  2xs: "4px"
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  2xl: "48px"
  3xl: "72px"
  hero: "104px"

rounded:
  sm: "6px"
  md: "10px"
  lg: "14px"
  xl: "20px"
  hero: "28px"
  pill: "999px"
---

# Kortex — Design System

> **Digital Garden.** Kortex is a personal knowledge base built on the LLM Wiki
> protocol, serialized as an OKF v0.2 bundle. The website is its public face: a
> garden of interlinked notes that grow from seedling to evergreen as they are
> verified. The visual language is warm, editorial, unhurried — paper, ink, and
> the quiet green of things that keep growing.

This file is the **single source of truth** for the design tokens. The YAML
frontmatter above owns every value; `hack/gen-design-tokens.py` renders the
`:root { … }` block of `src/styles/global.css` from it. Never hand-edit the
generated token block — edit the frontmatter and run `make tokens`.

## Direction

- **Paper, not screen.** The canvas is `--paper` (`#faf8f3`), never `#ffffff`.
  Cards sit a half-shade brighter. White is reserved for insets that must pop.
- **Terracotta ink.** One warm accent carries brand, links and calls to action.
  Boldness lives in the accent; everything around it stays quiet.
- **Serif headings.** Fraunces (optical-size variable) gives the garden its
  editorial, hand-set voice. Inter carries body copy; JetBrains Mono renders
  frontmatter, code and the `[[type:slug]]` relations.

## Typography

| Role | Face | Token | Use |
|------|------|-------|-----|
| Display / headings | Fraunces Variable | `--font-serif` | page titles, section heads, card titles |
| Body / UI | Inter Variable | `--font-sans` | prose, navigation, labels |
| Code / data | JetBrains Mono Variable | `--font-mono` | frontmatter, code blocks, relations tables |

Keep running text near `--measure` (66ch). Headings use `text-wrap: balance`.
Uppercase eyebrows (entity type, domain) get `letter-spacing: 0.12em`.

## Growth stages — the garden rule

Every entity page shows a **growth badge** derived from its OKF frontmatter.
This mapping is implemented once in `src/lib/growth.ts` and must match this table:

| Stage | Emoji | OKF condition | Token | Meaning |
|-------|-------|---------------|-------|---------|
| **Seedling** | 🌱 | `status: draft` | `--seedling` | just planted, unverified |
| **Budding** | 🌿 | `status: stable` and `confidence` ∈ {low, medium} | `--budding` | growing, partially verified |
| **Evergreen** | 🌳 | `status: stable` and `confidence: high` | `--evergreen` | trusted, multiple sources agree |
| **Archived** | 🍂 | `status: deprecated` | `--archived` | retired; links to replacement |

Staleness is orthogonal: a page past its `stale_after` instant also carries a
muted "needs re-verify" marker, regardless of stage.

## Color roles

- `--rust` / `--rust-dark` — brand, links, primary buttons, hovered states.
- `--paper` / `--card` / `--white` / `--surface-alt` — layered surfaces.
- `--ink` / `--text` / `--muted` / `--subtle` — type hierarchy, warm greys only.
- `--seedling|budding|evergreen|archived` (+ `-soft`) — growth badges, status pills.
- `--success|warning|error|info` — semantic feedback, kept separate from `--rust`.

## Layout

One centered column, `--container-max` wide, with `--container-pad` side gutters
that never drop below 20px. Sibling groups use flex/grid + `gap`, never stacked
margins. Entity cards share identical edges, inner padding and badge placement.
Cards earn border + radius + subtle shadow; section bands use `--surface-alt`.

## Regenerating tokens

```sh
make tokens        # DESIGN.md frontmatter → src/styles/global.css :root block
make tokens-check  # fail if global.css is out of sync (run in CI)
```
