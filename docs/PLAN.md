# Plan

## Pages

| Page | Title | Purpose | Facts |
|---|---|---|---|
| `/` | Output Pulse | The analyst logs their org's output metric per period, sees the trend, and sees the gap to a peer benchmark, all on their own device. | F1, F2, F3, F4, F5 |

## Tasks

Status as of this commit.

| Issue | Task | Status |
|---|---|---|
| [#2](https://github.com/ma-za-kpe/output-pulse/issues/2) | Design direction: home page and shared style | In progress |

## How the work is planned

Build one feature at a time, in this order, each to its sprint contract: M1 Output tracker with peer-benchmark gap view on index; M2 Period entry and deletion on index; M3 Trend view on index; M4 Peer benchmark gap on index; M5 Empty state and error handling on index

## Experience

Output Pulse (index): The analyst logs their org's output metric per period, sees the trend, and sees the gap to a peer benchmark, all on their own device.
  1. hero: One line: 'Turn your productivity problem into a number you can defend.'
  2. problem: Summarise the research context: Canadian productivity stagnation (E1-E3), attributed to StartupTribunal, with the caveat that the research was rejected by the AI Tribunal and published with caveats (F4).
  3. form: M2: Add a new period entry. Fields: metric name (text), period label (text, e.g. 'Q1 2025'), value (number). Submit button. Validation: value must be a number > 0; period label must not be empty.
  4. chart: M3: Trend view. A simple line chart of the output metric value over the logged periods, sorted by period label. Shows direction of change (up, down, flat).
  5. results: M4: Peer benchmark gap. Input field for peer benchmark value (number). Displays: 'You are at X, peers are at Y, the gap is Z (W%).' If no benchmark entered, shows a hint: 'Enter a benchmark from a published industry report or a peer you trust.'
  6. list: M2: List of all logged entries, each showing metric name, period label, value, and a delete button. Deleting an entry removes it from IndexedDB and updates the chart and gap view.
  7. caveats: M5: Empty state and error handling. When no entries exist, show: 'No output entries yet. Start with this quarter.' If IndexedDB is unavailable or quota is exceeded, show a visible error message: 'Storage is unavailable. Your entry was not saved.'
  8. source: Attribution: 'Research by StartupTribunal: Canadian Businesses Stalled By Low Productivity Despite Ottawa Help. Status: rejected by the StartupTribunal AI Tribunal, published with caveats. Link: https://startuptribunal.com/catalog/canadian-businesses-stalled-by-low-productivity-despite-ottawa-help'
The design system: docs/design/ and brand/; the tokens: app/tokens.css.
