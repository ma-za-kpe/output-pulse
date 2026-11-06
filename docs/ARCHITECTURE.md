# Output Pulse: architecture

## Information architecture

| Page | Purpose | Primary task | Features |
| --- | --- | --- | --- |
| `index` Output Pulse | The analyst logs their org's output metric per period, sees the trend, and sees the gap to a peer benchmark, all on their own device. | Output tracker with peer-benchmark gap view | M1 Output tracker with peer-benchmark gap view, M2 Period entry and deletion, M3 Trend view, M4 Peer benchmark gap, M5 Empty state and error handling |

## Content per page

### Output Pulse (`index`)

1. hero: One line: 'Turn your productivity problem into a number you can defend.'
2. problem: Summarise the research context: Canadian productivity stagnation (E1-E3), attributed to StartupTribunal, with the caveat that the research was rejected by the AI Tribunal and published with caveats (F4).
3. form: M2: Add a new period entry. Fields: metric name (text), period label (text, e.g. 'Q1 2025'), value (number). Submit button. Validation: value must be a number > 0; period label must not be empty.
4. chart: M3: Trend view. A simple line chart of the output metric value over the logged periods, sorted by period label. Shows direction of change (up, down, flat).
5. results: M4: Peer benchmark gap. Input field for peer benchmark value (number). Displays: 'You are at X, peers are at Y, the gap is Z (W%).' If no benchmark entered, shows a hint: 'Enter a benchmark from a published industry report or a peer you trust.'
6. list: M2: List of all logged entries, each showing metric name, period label, value, and a delete button. Deleting an entry removes it from IndexedDB and updates the chart and gap view.
7. caveats: M5: Empty state and error handling. When no entries exist, show: 'No output entries yet. Start with this quarter.' If IndexedDB is unavailable or quota is exceeded, show a visible error message: 'Storage is unavailable. Your entry was not saved.'
8. source: Attribution: 'Research by StartupTribunal: Canadian Businesses Stalled By Low Productivity Despite Ottawa Help. Status: rejected by the StartupTribunal AI Tribunal, published with caveats. Link: https://startuptribunal.com/catalog/canadian-businesses-stalled-by-low-productivity-despite-ottawa-help'

## Content model

- **OutputEntry** (indexeddb): id (string, uuid), metricName (string), periodLabel (string), value (number), createdAt (ISO 8601 string). The analyst creates these entries; they must persist across browser sessions on the same device. IndexedDB supports queries (sort by periodLabel, filter by metricName) and has a much larger quota than localStorage.
- **PeerBenchmark** (indexeddb): id (string, uuid), value (number), source (string, optional), createdAt (ISO 8601 string). The analyst enters this value; it must persist across sessions. Only one active benchmark is needed, but storing it as an entity allows future extension to multiple benchmarks.

## Decisions

### ADR-1 Store data in IndexedDB

- Context: The product must work offline, on the device, with no server. The analyst logs entries and a peer benchmark that must survive browser close and reopen.
- Decision: Use IndexedDB for all user-created data (OutputEntry, PeerBenchmark).
- Rejected: localStorage: rejected because it has a 5 MB quota, no query support, and is synchronous, which can block the UI.
- Rejected: A hosted database: rejected because the PRD forbids a server, account, or login, and the offline-first rule requires all data to stay on the device.
- Consequences: IndexedDB is asynchronous, so all reads and writes must be handled with Promises. The app must handle the case where IndexedDB is unavailable (e.g., private browsing) with a visible error message (M5).

### ADR-2 Single-page architecture

- Context: The PRD's success metric is 'under two minutes from opening the app to a saved entry plus a peer-benchmark gap shown.' The journeys (J1-J7) all resolve on one working surface.
- Decision: Use a single page (index) with all interactive blocks in a vertical sequence: hero, problem, form, chart, results, list, caveats, source.
- Rejected: Multi-page with separate pages for entry, trend, and benchmark: rejected because it adds navigation overhead, contradicts the 'under two minutes' metric, and complicates the offline, single-device constraint.
- Consequences: The page must be well-structured with clear visual hierarchy so the analyst can find the form, chart, and gap view quickly. The page must be responsive enough to work on a phone without sideways scrolling (J1).

### ADR-3 Client-side-only computation

- Context: The trend and gap calculations are simple arithmetic (sorting, subtraction, percentage). No server is available.
- Decision: Compute the trend and gap entirely in the browser, client-side, using the data from IndexedDB.
- Rejected: A server-side computation: rejected because the PRD forbids a server.
- Rejected: A third-party API: rejected because the PRD forbids third-party APIs and the offline rule requires no network dependency.
- Consequences: The app must handle the case where there are fewer than two entries (no trend) and where no peer benchmark is entered (no gap) gracefully.

## Non-functional requirements

- The app loads and renders the empty state within 1 second on a mid-range laptop browser (Chrome, Firefox, Safari).
- The entry form validates and saves an entry within 200 ms of the submit button being clicked.
- The trend chart updates within 100 ms of an entry being added or deleted.
- The peer-benchmark gap updates within 100 ms of the benchmark value being entered.
- The app is fully accessible: all interactive elements are keyboard-navigable, form fields have labels, and the chart has a text alternative (e.g., a table of values).
- The app works offline: all data is stored in IndexedDB, and no network requests are made after the initial page load.
- The app respects the user's reduced-motion preference: if prefers-reduced-motion is set, the chart does not animate.
- The app is responsive: it works on a phone (320 px wide) without sideways scrolling, and on a desktop (1280 px wide) with a comfortable layout.
