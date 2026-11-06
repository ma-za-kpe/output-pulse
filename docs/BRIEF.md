# Output Pulse: The analyst enters their org's output metric (a number they (first release)

The approved brief, as its issue states it.

## Product

**Output Pulse turns 'we have a productivity problem' into a number the analyst can defend: log your org's output metric per period, see the trend, and see the gap to a peer benchmark you enter, all on your own device with no server and no account. It is the team's own concept (F1), a working**

- For P1 Productivity analyst at a 400-person Canadian manufacturing firm: When the exec team asks whether our output per employee is improving and where we stand against peers, I want a local record of our output metric per period with a gap-to-peer-benchmark view, so I can defend a number and point to the one area to invest in.
- For P2 Analytics lead at a 50-person Canadian SaaS startup: When the founder asks whether output per engineer is going up as we hire, I want to log our output metric per sprint and see the trend against a peer benchmark I enter, so I can say 'we are at X, peers are at Y, here is the gap' in one screen.
- Wedge: Local output tracker with peer-benchmark gap view: the analyst records their org's output metric per period in a local browser app, sees the trend over time, and enters a peer benchmark to see the gap. Data stays on the device in IndexedDB. It is the only option that works offline with a local Why: O1 is the only option that works offline with a local database, serves P1 (the productivity analyst) directly, and converts the research's core frustration (E3, 'no actionable strategy') into a concrete, defensible number with a trend and a peer reference. It wins for P1 because the analyst can open
- Core feature: M1 Output tracker with peer-benchmark gap view, for Productivity analyst at a 400-person Canadian manufacturing firm; works offline (indexeddb).
- The full PRD is `docs/PRD.md`.

## User stories

### R1 Log a quarter's output and see the gap to a peer benchmark
- [ ] With a fresh app, entering metric name 'Output per employee', period 'Q3 2025', value 42, and peer benchmark 50, the tracker lists the entry and the gap view shows a number gap of 8 and a percentage gap of 16%.
- [ ] Entering a second period 'Q2 2025' with value 39 makes the trend view show the change against the prior period (up 8% over one quarter).
- [ ] The time from opening the app to the moment the saved entry plus the peer-benchmark gap is visible on screen is under 2 minutes.
- [ ] After closing the browser and reopening on the same device, the entries and benchmark are still present (100% offline persistence).
- [ ] With the browser in offline mode, adding an entry, viewing the trend, and viewing the gap all still function with no network call.
Covers: M1 Output tracker with peer-benchmark gap view (for Productivity analyst at a 400-person Canadian manufacturing firm)

### R2 Add a period entry with metric name, period label, and value
- [ ] Adding three distinct entries (different period labels) lists all three in the tracker and they persist after a page reload.
- [ ] Attempting to add an entry with a blank value or blank period label shows a visible validation message and does not save a broken entry.
- [ ] Adding an entry and then reloading the page leaves the new entry intact in IndexedDB.
Covers: M2 Period entry and deletion (for Productivity analyst at a 400-person Canadian manufacturing firm)

### R3 Delete an entry entered in error
- [ ] Deleting one of three entries removes it and leaves the other two intact and correct (no cross-deletion).
- [ ] Logging the same period twice (e.g. 'Q3 2025' entered twice) either prevents the duplicate or shows both entries clearly; if both show, the analyst can find and delete the duplicate in under 30 seconds.
Covers: M2 Period entry and deletion (for Productivity analyst at a 400-person Canadian manufacturing firm)

### R4 See the trend of the output metric over logged periods
- [ ] Entering three periods with increasing values (39, 42, 45) shows an upward line/bar across the three periods, readable as 'up over three quarters' at a glance.
- [ ] Entering three periods with equal values (40, 40, 40) shows a flat line, matching 'we are flat'.
- [ ] Entering periods out of chronological order still plots them in the correct period order, not entry order.
- [ ] Deleting the middle period from a three-period trend re-renders the trend with the remaining two periods and no stale data.
- [ ] With one entry, the trend shows a single point, not an invented line.
Covers: M3 Trend view (for Productivity analyst at a 400-person Canadian manufacturing firm)

### R5 Enter a peer benchmark and see the gap as a number and a percentage
- [ ] With own value 42 and benchmark 50, the gap view shows the number gap (8) and the percentage gap (16%).
- [ ] With own value 55 and benchmark 50, the gap is shown as a positive lead (5, 10%) or clearly labelled as ahead of peers, not a misleading negative.
- [ ] Changing the benchmark from 50 to 60 recalculates the gap (18, 30%) without needing to re-enter the own value.
- [ ] Entering a benchmark of 0 does not divide by zero or crash; it shows a sensible message or omits the percentage.
Covers: M4 Peer benchmark gap (for Productivity analyst at a 400-person Canadian manufacturing firm)

### R6 Leave the peer benchmark blank and keep logging output
- [ ] Leaving the benchmark blank shows the note 'Enter a benchmark from a published industry report or a peer you trust. If you do not have one, leave it blank and the trend still works.' and the trend view still renders.
- [ ] With the benchmark blank, adding a new period entry still saves and the trend updates without the gap view blocking the action.
Covers: M4 Peer benchmark gap (for Productivity analyst at a 400-person Canadian manufacturing firm)

### R7 See a clear empty state when no entries exist
- [ ] Opening the app with no entries (fresh profile or cleared IndexedDB) shows 'No output entries yet. Start with this quarter.' and a way to add the first entry.
- [ ] After the empty state, adding the first entry makes the empty state disappear and the tracker/trend render with the new data.
Covers: M5 Empty state and error handling (for Productivity analyst at a 400-person Canadian manufacturing firm)

### R8 See a visible message if IndexedDB is unavailable or quota is exceeded
- [ ] Running the app in a browser with IndexedDB disabled (or private mode where it is limited) shows a visible error message and no entry is lost silently; repeat in Chrome, Firefox, and Safari.
- [ ] Simulating a quota exceeded (e.g. fill storage or use a browser quota limit) shows a visible message telling the analyst the entry did not save, rather than a silent failure.
- [ ] After the error condition is resolved (IndexedDB re-enabled), reloading returns the app to normal and previously saved data is intact.
Covers: M5 Empty state and error handling (for Productivity analyst at a 400-person Canadian manufacturing firm)

## Out of scope

- No server, no account, no login, no payment, no live data feed, no third-party API.
- No cross-firm data sharing or benchmarking marketplace (needs a server and many users).
- No Ottawa policy-monitor or news feed (needs a live feed and would reproduce the 'endless talk' the research criticises).
- No mobile app; the product works in the browser.
- No export to PDF or CSV in the first release (the analyst can copy the numbers from the screen).

## Journeys

- **J1** (visitor) Know what Output Pulse is, who it is for, and the research it was designed from. Observed: The prototype status, the audience, the attributed research summary, the research status caveat, and the StartupTribunal source link are all visible on a phone without sideways scrolling.
- **J2** (visitor) Log this quarter's output metric and see the gap to a peer benchmark in under two minutes. Observed: The new entry appears in the trend, and the gap is shown as both a number and a percentage on the same screen, all on the device.
- **J3** (visitor) Add a new period entry and delete one entered in error without losing the others. Observed: The deleted entry is gone and the remaining entry is still listed with its value intact.
- **J4** (visitor) See the trend of the output metric over the periods logged. Observed: A line or bar trend of the output metric over the logged periods is visible, showing the direction of change.
- **J5** (visitor) Enter a peer benchmark and see the gap as a number and a percentage. Observed: The gap is displayed as both an absolute number and a percentage (e.g. 'we are at 42, peers are at 50, the gap is 8 or 16%').
- **J6** (visitor) See a clear empty state when no entries exist and a visible message if storage fails. Observed: The empty state reads 'No output entries yet. Start with this quarter.' and a visible message appears on storage failure so no entry is lost silently.
- **J7** (owner) Come back later to saved output entries and the peer benchmark. Observed: The previously logged entries and the peer benchmark are still present after a reload, with no server involved.

## Facts the site shows

- `F1`: Status: a working prototype; its features are the team's own concept, and its data stays on this device
- `F2`: Who it is for: Productivity and analytics teams and customers in Canada
- `F3`: StartupTribunal research reports: Industry insiders openly question whether Ottawa's latest rescue efforts are meaningful or merely performative, highlighting Canada's long-standing productivity crisis compared to peer nations. This stagnation directly suppresses wage growth, business investment, innovation, and international competitiveness. The core frustration is the sense that despite endless talk and policy announcements, Canada still lacks an effective, actionable strategy to…
- `F4`: Research status: rejected by the StartupTribunal AI Tribunal, published with caveats.
- `F5`: Research by StartupTribunal: https://startuptribunal.com/catalog/canadian-businesses-stalled-by-low-productivity-despite-ottawa-help

## Assumptions

- A public repository and a public site on GitHub Pages; no server or database.
- The frozen tests under `tests/` are the acceptance contract; changing them needs the owner's approval.
- Facts appear exactly as the brief gives them.
