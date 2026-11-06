# Output Pulse motion (U3)

Motion explains change; it never decorates. One orchestrated moment greets the visitor, every other motion answers something they did.

| Token | Duration |
| --- | --- |
| `--motion-tick` | 120ms |
| `--motion-settle` | 200ms |
| `--motion-stamp` | 320ms |
| `--motion-reveal` | 420ms |
| `--motion-burst` | 480ms |

| Token | Curve |
| --- | --- |
| `--ease-ledger` | cubic-bezier(0.2, 0, 0.2, 1) |
| `--ease-press` | cubic-bezier(0.3, 0, 0.7, 1) |
| `--ease-drift` | cubic-bezier(0.4, 0, 0.6, 1) |

## Moments

| Moment | Motion | Duration | Easing |
| --- | --- | --- | --- |
| load | masthead, entry sheet, stamped ledger line, and status band settle in as a staggered ledger arrival | `reveal` | `ledger` |
| entry | the output metric field gains a hairline underline and the tally column ticks as the analyst types | `tick` | `press` |
| save | the new row is committed to the on-device ledger and a small success stamp settles onto the row | `settle` | `press` |
| change | the total line re-tallies and the stamped metric re-stamps to the new value | `stamp` | `press` |
| stamp | the tracked output metric presses into the ledger line as a stamped number | `stamp` | `press` |
| status | the status band flashes once to confirm the device saved the entry | `settle` | `drift` |

## The load moment

In order, 120ms apart (`--reveal-step`, `components/kit/Reveal.tsx`): masthead → entry sheet → stamped ledger line → status band.

- Reduced motion: Under reduced motion, nothing moves and nothing is hidden: the ledger arrives fully formed and every stamp, tally, and status flash is shown in its final state.
- Without JavaScript: Without JavaScript the entry sheet and a static ledger state still render, but interactive tallying, on-device saving, and all motion moments are unavailable.
- Bursts: When many changes arrive at once, they coalesce into one tally update, one ledger restamp, and one status flash rather than independent animations.
- Focus: Focus is always visible on every control with at least a 44px target, drawn as a 2px #1f3a5f ring against paper or surface.
