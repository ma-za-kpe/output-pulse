# Output Pulse brand

Theme: **Output Ledger**. Canadian productivity ledgers, tally records, stats tables, and on-device analyst entry sheets

Boldness, spent in one place: The output metric is rendered as a tracked, stamped number on a ledger line, not a decorative dashboard

## Essence (B1)

| Tagline | Promise | Personality |
| --- | --- | --- |
| Track your output. Keep it on your device. | A working prototype that lets Canadian productivity and analytics teams enter their org's output metric and keep the data on the device. | plain, offline-first, cautious, ledger-like, Canadian, working |

| It is | It is not |
| --- | --- |
| A working prototype for productivity and analytics teams in Canada | Not a cloud dashboard |
| An on-device tool that keeps data on the device | Not a SaaS platform |
| A ledger for entering and tracking an org's output metric | Not a decorative analytics suite |
| Grounded in StartupTribunal research on Canadian productivity stagnation | Not a policy tool |
| Quiet, offline-first, and research-cautious | Not a finished product |

The decision, with the directions rejected, is in [DECISION.md](DECISION.md).

## Colour (B4)

22 primitives and 11 semantic roles in two themes; use the roles, never a primitive directly.

| Primitive | Value |
| --- | --- |
| `paper` | #f5f1e8 |
| `surface` | #fbf8f1 |
| `ink` | #182230 |
| `muted` | #5a6472 |
| `line` | #d8d0bf |
| `accent` | #b02a1e |
| `accent-ink` | #f5f1e8 |
| `focus` | #1f3a5f |
| `success` | #2c5a34 |
| `warning` | #8a5a12 |
| `danger` | #a5281c |
| `paper-dark` | #141a22 |
| `surface-dark` | #1c242f |
| `ink-dark` | #ece7db |
| `muted-dark` | #9aa3b0 |
| `line-dark` | #333d4a |
| `accent-dark` | #e06a5c |
| `accent-ink-dark` | #141a22 |
| `focus-dark` | #8fb2e0 |
| `success-dark` | #7cc08a |
| `warning-dark` | #e0a94e |
| `danger-dark` | #e88a7d |

| Role | Light | Dark |
| --- | --- | --- |
| `--color-ink` | #182230 | #ece7db |
| `--color-paper` | #f5f1e8 | #141a22 |
| `--color-surface` | #fbf8f1 | #1c242f |
| `--color-muted` | #5a6472 | #9aa3b0 |
| `--color-line` | #d8d0bf | #333d4a |
| `--color-accent` | #b02a1e | #e06a5c |
| `--color-accentInk` | #f5f1e8 | #141a22 |
| `--color-focus` | #1f3a5f | #8fb2e0 |
| `--color-success` | #2c5a34 | #7cc08a |
| `--color-warning` | #8a5a12 | #e0a94e |
| `--color-danger` | #a5281c | #e88a7d |

Every text role on every surface is measured in `contrast.json` (WCAG 2.x), and the crew repository's tests recompute it. These pairs are not for body text:

| Pair | Contrast | Use |
| --- | --- | --- |
| light: ink on accent | 2.44:1 | never |
| light: muted on accent | 1.10:1 | never |
| light: accentInk on paper | 1.00:1 | never |
| light: accentInk on surface | 1.06:1 | never |
| light: success on accent | 1.22:1 | never |
| light: warning on accent | 1.11:1 | never |
| light: danger on accent | 1.09:1 | never |
| light: focus on accent | 1.75:1 | never |
| dark: ink on accent | 2.67:1 | never |
| dark: muted on accent | 1.29:1 | never |
| dark: accentInk on paper | 1.00:1 | never |
| dark: accentInk on surface | 1.12:1 | never |
| dark: success on accent | 1.53:1 | never |
| dark: warning on accent | 1.56:1 | never |
| dark: danger on accent | 1.31:1 | never |
| dark: focus on accent | 1.51:1 | never |

Statuses never rely on colour alone: each has a word and an icon (docs/design/COMPONENTS.md), and success, warning and danger differ in lightness, so they read in greyscale.

## Type (B5)

| Role | Face | Package | Licence |
| --- | --- | --- | --- |
| display | Bricolage Grotesque Variable | @fontsource-variable/bricolage-grotesque | SIL Open Font License 1.1 (OFL-1.1), self-hosted from the pinned @fontsource package |
| body | IBM Plex Sans Variable | @fontsource-variable/ibm-plex-sans | SIL Open Font License 1.1 (OFL-1.1), self-hosted from the pinned @fontsource package |
| mono | JetBrains Mono Variable | @fontsource-variable/jetbrains-mono | SIL Open Font License 1.1 (OFL-1.1), self-hosted from the pinned @fontsource package |

| Token | Min | Max |
| --- | --- | --- |
| `--text-xs` | 12px | 12px |
| `--text-sm` | 14px | 14px |
| `--text-base` | 16px | 16px |
| `--text-lg` | 18px | 19px |
| `--text-xl` | 22px | 24px |
| `--text-2xl` | 30px | 34px |
| `--text-3xl` | 40px | 48px |
| `--text-4xl` | 56px | 72px |

- Display (Bricolage Grotesque) is for page titles and section heads only; keep it tight and let it carry the weight.
- Body (IBM Plex Sans) is the default for all reading text, labels and forms; never set body copy in the display face.
- Mono (JetBrains Mono) is reserved for figures, the stamped output metric, table columns and any number a user enters — it is how a number is recognised as data.
- The stamped output metric is always mono, set in a stamped band, and is the single loudest number on the page; no other figure may compete with it.
- Line-height: 1.15 for display, 1.5 for body, 1.3 for mono figures.
- Do not use the mono face for running prose; it is for numbers and code-like values only.

## Logo (B3)

A single ledger cell: a square ruled frame with a horizontal rule across the lower third, and a short stamped tally band sitting on that rule. The frame and rule are the dominant ink; the tally band is the one sharp accent. It reads as a st

The mark sits on a 64-unit grid. Keep clear space of a quarter of its width on every side; never show it under 16px (favicon) or the lockup under 120px wide.

| File | Use |
| --- | --- |
| `logo/mark.svg` | the mark on paper; the favicon |
| `logo/mark-on-dark.svg` | the mark on the ink background |
| `logo/mark-mono.svg` | one colour: stamps, embossing, small sizes |
| `logo/mark-state-success.svg` | the mark in the success state |
| `logo/wordmark.svg` | the name alone |
| `logo/lockup.svg`, `logo/lockup-on-dark.svg` | mark and name together |

Don't:

- Do not add a maple leaf, flag, or any national emblem to the mark.
- Do not set the wordmark in the mono face; it is a display wordmark, not a figure.
- Do not place the mark on a purple-to-blue gradient or any blurred blob background.
- Do not recolour the tally band to anything but the accent; it is the one loud element.
- Do not scale the mark below 16px; at 16px the frame and band must still read as a cell, not a blob.
- Do not add a drop shadow or bevel to the mark; it is flat ink on paper.

## Iconography

Outline icons on a 24 grid, 1.75px strokes, square corners, in `icons/ui/`: `entry`, `tally`, `device`, `ledger`, `total`, `status`.

## Pattern (B8)

`patterns/ruled-ledger.svg` tiles seamlessly. Use only as a quiet background for empty states, section dividers and the area behind the stamped metric band. Never place it behind data tables, figures or text, and never use it as a hero backdrop.

## Voice (B6)

1. **State the data location plainly.** — Your data stays on this device.
2. **Use the word 'output' for the metric, not 'performance' or 'KPI'.** — Enter your org's output metric.
3. **Acknowledge the prototype status without apology.** — This is a working prototype.
4. **Cite the research with its caveats.** — Based on StartupTribunal research, published with caveats.
5. **Keep sentences short and declarative.** — The number is saved.
6. **Avoid policy language; the tool tracks, it does not prescribe.** — Track your output. Do not wait for Ottawa.
7. **Use 'device' not 'machine' or 'computer'.** — Data is kept on the device.
8. **State the peer comparison without naming specific countries.** — Canada's productivity lags peer nations.

| Use | Avoid |
| --- | --- |
| output | seamless |
| device | revolutionize |
| ledger | unlock |
| track | empower |
| metric | next-gen |
| prototype | cutting-edge |
| offline | game-changer |
| Canadian | elevate |

Banned words: “seamless”, “revolutionize”, “revolutionise”, “unlock”, “empower”, “next-gen”, “cutting-edge”, “game-changer”, “game changing”, “elevate”, “synergy”, “supercharge”.

Copy for every product state:

| State | Copy |
| --- | --- |
| empty | No output metric entered yet. Enter your org's output metric to start the ledger. |
| loading | Reading the ledger… |
| error | The entry could not be saved. Check the device and try again. |
| success | The number is saved on this device. |
| offline | Offline. Data stays on this device. |

## Not this product (D21)

- Stock photos of Canadian landscapes or cityscapes
- Maple leaf emblems or national symbols
- Centred hero with a purple-to-blue gradient
- Three identical feature cards with emoji icons
- Inter or Roboto with no type contrast
- Glassmorphism panels on a blurred blob background
- Stock 'Get started' and 'Learn more' buttons side by side
- Dashboard widgets with animated sparklines
- a centred hero with a purple-to-blue gradient
- three identical feature cards with emoji icons
- Inter or Roboto with no type contrast
- glassmorphism panels on a blurred blob background
- stock 'Get started' and 'Learn more' buttons side by side

Never in copy: “seamless”, “revolutionize”, “revolutionise”, “unlock”, “empower”, “next-gen”, “cutting-edge”, “game-changer”, “game changing”, “elevate”, “synergy”, “supercharge”, “leverage”, “world-class”, “effortless”, “unleash”, “harness the power”, “in today's”, “look no further”, “one-stop”.
