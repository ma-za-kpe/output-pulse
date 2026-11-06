# Progress: Output Pulse

As of this commit. Trusted code writes this file from the job's journal; every role reads it first (`AGENTS.md`, Start here).

0 of 5 features pass.

## Features

| Feature | Title | Page | Status | Passes |
| --- | --- | --- | --- | --- |
| M1 | Output tracker with peer-benchmark gap view | `index` | in-progress | no |
| M2 | Period entry and deletion | `index` | in-progress | no |
| M3 | Trend view | `index` | in-progress | no |
| M4 | Peer benchmark gap | `index` | in-progress | no |
| M5 | Empty state and error handling | `index` | in-progress | no |

## Current sprint

Sprint contract: Design direction: home page and shared style

Done means, for each feature:

- [ ] M1 Output tracker with peer-benchmark gap view: P1 logs this quarter's output metric, sees the trend against last year, and sees the gap to the peer benchmark they entered, all on their own device, in under two minutes. (on `index`, working offline)
- [ ] M2 Period entry and deletion: P1 can add a new period entry (metric name, period label, value) and delete an entry they entered in error, without losing other entries. (on `index`, working offline)
- [ ] M3 Trend view: P1 sees a simple line or bar trend of their output metric over the periods they have logged, so they can say 'we are up 8% over three quarters' or 'we are flat' in one glance. (on `index`, working offline)
- [ ] M4 Peer benchmark gap: P1 enters a peer benchmark value (sourced from a published report or a peer) and sees the gap as a number and a percentage, so they can say 'we are at 42, peers are at 50, the gap is 8 or 16%.' (on `index`, working offline)
- [ ] M5 Empty state and error handling: P1 sees a clear empty state when no entries exist ('No output entries yet. Start with this quarter.') and a visible message if IndexedDB is unavailable or quota is exceeded, so no entry is lost silently. (on `index`, working offline)

Checked by the implementer, on the exact head:

- `npm run build`
- `python tests/site_view.py && python -m unittest discover -s tests`
- `node tests/browser/qa.mjs`

Judged by the evaluator, on the rendered product: every criterion (design, originality, depth, craft, functionality) scores at least 7 of 10, and so do its 6 hidden rubric categories. Below that the task holds; it never merges.

## Recent commits

- `55ebfaabdbef` on `feature/issue-2-home`: docs: product requirements, architecture and design system
- `29cf0fbb0685` on `feature/issue-2-home`: docs: brief, plan, decisions, handoff and run record
