# Output Pulse accessibility (U6)

- Targets are at least 44px in both directions (`--target-min`).
- Focus: A 2px focus ring in the focus colour (#1f3a5f) with a 2px offset, always visible on every interactive element — number field, Save Control, Period Selector, Note Field, and each Tally Record remove —;
- Live regions: One polite live region announces save results, period changes, and device status changes; one assertive live region announces errors only.
- The Entry Sheet number field is labelled 'Your org's output metric' and its error message is tied to the field with aria-describedby.
- The Stamped Metric Line is exposed as a labelled group with the period and value in text, so the stamped number is not decorative-only.
- The Tally Record is a real table with a caption and header row; each remove action is a labelled button, not an icon alone.
- The Period Selector is a labelled control whose change is announced in the polite live region.
- The Offline Banner and Device Status changes are announced in the live region, not only shown visually.
- Under reduced motion, the load, entry, save, change, stamp, and status moments do not move and nothing is hidden; content is present immediately.
- All motion stays at or under the locked durations (tick 120ms, settle 200ms, stamp 320ms, reveal 420ms, burst 480ms), so nothing exceeds 1600ms.
- Colour is never the only signal: success, warning, and danger states pair colour with a word and an icon (status, device, total).
- axe (WCAG 2.1 AA) is clean on every page, at phone and desktop widths, in both themes; the frozen browser check enforces it.
- 30 of 46 measured pairs are fit for body text; the rest are listed in brand/BRAND.md with their limits.
