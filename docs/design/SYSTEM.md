# Output Pulse design system: shape and depth (U1, U2)

The tokens live in `app/tokens.css` (and `brand/tokens.css`); pages use them only.

## Spacing

| Token | Value |
| --- | --- |
| `--space-1` | 0.25rem |
| `--space-2` | 0.5rem |
| `--space-3` | 1rem |
| `--space-4` | 1.5rem |
| `--space-5` | 2rem |
| `--space-6` | 3rem |
| `--space-7` | 4rem |

## Radius

| Token | Value |
| --- | --- |
| `--radius-none` | 0px |
| `--radius-hairline` | 2px |
| `--radius-sheet` | 4px |

## Elevation

| Token | Offset | Blur | Opacity |
| --- | --- | --- | --- |
| `--shadow-rest` | 0px | 0px | 0 |
| `--shadow-lift` | 2px | 6px | 0.12 |
| `--shadow-stamp` | 0px | 0px | 0.28 |

## Widths and grid

- Content reaches 1120px (`--content-max`) in a 12-column grid from 960px, 6 columns from 640px and one column on a phone.
- Prose keeps a measure of 72ch (`--measure`).
- Nothing is wider than the viewport: the browser check fails any sideways scroll at 320px.

Type: Bricolage Grotesque Variable for display, IBM Plex Sans Variable for body and JetBrains Mono Variable for figures; see brand/BRAND.md.
