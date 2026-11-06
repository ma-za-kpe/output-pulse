# Output Pulse: product requirements

Output Pulse turns 'we have a productivity problem' into a number the analyst can defend: log your org's output metric per period, see the trend, and see the gap to a peer benchmark you enter, all on your own device with no server and no account. It is the team's own concept (F1), a working

## Problem and evidence

Canadian productivity and analytics teams are asked to 'move the needle' on output but have no local, defensible way to track their own org's output metric over time and compare it to a peer benchmark. The result is the frustration StartupTribunal describes (E3): 'endless talk and policy announcements' with 'no effective, actionable strategy to meaningfully move the needle on productivity.' This stagnation, per StartupTribunal (E2), suppresses wage growth, business investment, innovation, and international competitiveness, and Canada's long-standing productivity crisis vs peer nations (E1) is the backdrop. The team's gap is the absence of a local tool that turns 'we have a productivity problem' into a number with a trend and a peer reference.

- Industry insiders openly question whether Ottawa's latest rescue efforts are meaningful or merely performative, highlighting Canada's long-standing productivity crisis compared to peer nations. (StartupTribunal, E1)
- This stagnation directly suppresses wage growth, business investment, innovation, and international competitiveness. (StartupTribunal, E2)
- The core frustration is the sense that despite endless talk and policy announcements, Canada still lacks an effective, actionable strategy to meaningfully move the needle on productivity. (StartupTribunal, E3)

Who is hurt: Productivity and analytics teams and customers in Canada (F2).

## Personas and jobs to be done

### P1 Productivity analyst at a 400-person Canadian manufacturing firm

Reports to the COO on whether the firm's output per employee is improving, and is asked each quarter to 'show where the needle is moving.'

- Job to be done: When the exec team asks whether our output per employee is improving and where we stand against peers, I want a local record of our output metric per period with a gap-to-peer-benchmark view, so I can defend a number and point to the one area to invest in.
- Today's workaround: A spreadsheet of headcount and hours worked, no output metric, no peer reference; every quarter the analyst rebuilds it by hand and the COO asks 'but are we better than last year?'

### P2 Analytics lead at a 50-person Canadian SaaS startup

Tracks the team's output (commits shipped, tickets closed) per sprint and is asked by the founder whether the team is actually getting more done per person as they grow.

- Job to be done: When the founder asks whether output per engineer is going up as we hire, I want to log our output metric per sprint and see the trend against a peer benchmark I enter, so I can say 'we are at X, peers are at Y, here is the gap' in one screen.
- Today's workaround: A Jira export pasted into a spreadsheet; no trend view, no peer comparison, and the founder has to trust the analyst's verbal summary.

## Alternatives today

- Local output tracker with peer-benchmark gap view (chosen): the analyst records their org's output metric per period in a local browser app, sees the trend over time, and enters a peer benchmark to see the gap. Data stays on the device in IndexedDB. It is the only option that works offline with a

## Value proposition

Output Pulse turns 'we have a productivity problem' into a number the analyst can defend: log your org's output metric per period, see the trend, and see the gap to a peer benchmark you enter, all on your own device with no server and no account. It is the team's own concept (F1), a working

## Solution options and wedge

- O1: Local output tracker with peer-benchmark gap view: the analyst records their org's output metric per period in a local browser app, sees the trend over time, and enters a peer benchmark to see the gap. Data stays on the device in IndexedDB. It is the only option that works offline with a local
- O2: Ottawa policy-monitor dashboard: a dashboard that tracks and categorises Ottawa's productivity-related announcements and policy changes over time. Needs a live feed of government announcements (a network dependency, which the offline rule forbids) and would reproduce the 'endless talk' the research
- O3: Cross-firm benchmarking marketplace: a platform where multiple Canadian firms share anonymised output metrics to build a live peer benchmark. Needs many firms and a server to aggregate data, which the offline-first rule forbids; also cold-start problem: no benchmark exists until many firms join,

Wedge: O1, Local output tracker with peer-benchmark gap view: the analyst records their org's output metric per period in a local browser app, sees the trend over time, and enters a peer benchmark to see the gap. Data stays on the device in IndexedDB. It is the only option that works offline with a local Why: O1 is the only option that works offline with a local database, serves P1 (the productivity analyst) directly, and converts the research's core frustration (E3, 'no actionable strategy') into a concrete, defensible number with a trend and a peer reference. It wins for P1 because the analyst can open

## Core feature

M1 Output tracker with peer-benchmark gap view, for Productivity analyst at a 400-person Canadian manufacturing firm: P1 logs this quarter's output metric, sees the trend against last year, and sees the gap to the peer benchmark they entered, all on their own device, in under two minutes.

- Primary action: The analyst enters their org's output metric (a number they
- Offline, on the device (indexeddb): yes

## MVP scope

- M1 Output tracker with peer-benchmark gap view (P1): P1 logs this quarter's output metric, sees the trend against last year, and sees the gap to the peer benchmark they entered, all on their own device, in under two minutes.
- M2 Period entry and deletion (P1): P1 can add a new period entry (metric name, period label, value) and delete an entry they entered in error, without losing other entries.
- M3 Trend view (P1): P1 sees a simple line or bar trend of their output metric over the periods they have logged, so they can say 'we are up 8% over three quarters' or 'we are flat' in one glance.
- M4 Peer benchmark gap (P1): P1 enters a peer benchmark value (sourced from a published report or a peer) and sees the gap as a number and a percentage, so they can say 'we are at 42, peers are at 50, the gap is 8 or 16%.'
- M5 Empty state and error handling (P1): P1 sees a clear empty state when no entries exist ('No output entries yet. Start with this quarter.') and a visible message if IndexedDB is unavailable or quota is exceeded, so no entry is lost silently.

## Non-goals

- No server, no account, no login, no payment, no live data feed, no third-party API.
- No cross-firm data sharing or benchmarking marketplace (needs a server and many users).
- No Ottawa policy-monitor or news feed (needs a live feed and would reproduce the 'endless talk' the research criticises).
- No mobile app; the product works in the browser.
- No export to PDF or CSV in the first release (the analyst can copy the numbers from the screen).

## Success metrics

- Time to first defensible number: Under 2 minutes from opening the app to a saved entry plus a peer-benchmark gap shown. (measured by Timer from the analyst opening the app to the moment the gap is visible on screen, self-reported in a usability test with 5 analysts.)
- Entries logged in first week: At least 3 period entries per analyst in the first 7 days of use. (measured by Count of entries in IndexedDB per device, read by the analyst or by a test script that opens the app and counts items.)
- Peer benchmark entered: At least 1 peer benchmark value entered by 80% of analysts in the first 7 days. (measured by Boolean flag in IndexedDB per device, checked in a usability test with 5 analysts.)
- Offline persistence: 100% of entries survive a browser close and reopen on the same device. (measured by Automated test: save 5 entries, close the browser, reopen, count entries; pass if all 5 are present.)

## Risks

- Analyst does not know what output metric to use Test: In the usability test, ask each analyst to name the metric they would log before they open the app; if fewer than 3 of 5 can name one, add a short onboarding hint with 3 example metrics (revenue per employee, units per shift, commits per engineer).
- Analyst has no peer benchmark to enter Test: In the usability test, ask each analyst where they would source a peer benchmark; if fewer than 3 of 5 can name a source, add a note in the gap view: 'Enter a benchmark from a published industry report or a peer you trust. If you do not have one, leave it blank and the trend still works.'
- IndexedDB unavailable in the analyst's browser Test: Run the app in a browser with IndexedDB disabled (or in private mode where it is limited); verify the visible error message appears and no entry is lost silently. Repeat in Chrome, Firefox, and Safari.
- Analyst enters the same period twice Test: In the usability test, ask each analyst to log the same quarter twice; verify the app either prevents the duplicate or shows both entries clearly so the analyst can delete the wrong one. If the app shows both, confirm the analyst can find and delete the duplicate in under 30 seconds.

## Assumptions

- The analyst has a single output metric they care about Check: In the usability test, ask each analyst to name the one metric they would log; if more than 1 of 5 says 'I need two metrics,' add a second metric field to M1 in the next iteration.
- The analyst can source a peer benchmark from a published report or a peer Check: In the usability test, ask each analyst to name a source for a peer benchmark; if fewer than 3 of 5 can name one, treat R2's mitigation as required, not optional.
- The analyst uses the app in a desktop or laptop browser, not a phone Check: In the usability test, ask each analyst what device they would use; if more than 1 of 5 says 'my phone,' add a responsive layout to M1 in the next iteration.
- The research claims E1-E3 are directionally correct but are StartupTribunal's claims, not established fact Check: The PRD attributes every evidence item to StartupTribunal and notes the research was rejected by the StartupTribunal AI Tribunal and published with caveats (F4). The product does not depend on any single claim being true; it serves the persona's job regardless.

Research claims are the source's and are attributed; every feature is the team's own concept.
