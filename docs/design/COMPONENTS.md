# Output Pulse components (U4, U5)

## Entry Sheet

The on-device analyst entry sheet where the analyst records one org output metric for a period; it is the core action, reachable from the top of the page.

Anatomy: sheet header (period label + device tag), metric label row, metric input (mono, 44px min target), unit suffix, note field, save control.

| State | Treatment |
| --- | --- |
| default | Surface #fbf8f1 panel on paper #f5f1e8, 1px line #d8d0bf border, ink #182230 text, mono input empty with a muted #5a6472 placeholder '0.0'. |
| focus | Focused input shows a 2px focus #1f3a5f outline offset 2px; the sheet header tag shifts to focus #1f3a5f; no other element moves. |
| active | While typing, the metric input caret is accent #b02a1e and each keystroke triggers the entry moment (tick 120ms) on the tally counter beside it. |
| error | Invalid or non-numeric entry: input border becomes danger #a5281c, a status icon (status) in danger #a5281c appears at the right, and the note line reads 'That’ |
| success | After a valid save, the sheet header tag turns success #2c5a34 and the save control shows the status icon in success #2c5a34 for one settle (200ms). |
| disabled | When a record is locked for the period, inputs are muted #5a6472 with 50% opacity, the save control is disabled, and the header tag reads 'Locked'. |
| offline | A device icon in warning #8a5a12 appears in the header with the word 'On-device'; all entry still works because data stays on this device. |

## Stamped Metric Line

The bold move: renders the entered output metric as a tracked, stamped number on a ledger line rather than a decorative dashboard figure.

Anatomy: ledger rule (top line #d8d0bf), period cell (mono), metric cell (bricolage-grotesque display, tracked), unit cell (mono), stamp mark (accent #b02a1e), ledger rule (bottom line #d8d0bf).

| State | Treatment |
| --- | --- |
| default | Two ledger rules frame the line; the metric cell shows the current value in bricolage-grotesque display, letter-spaced, ink #182230; the stamp mark is a faint 2 |
| focus | When the line is the active record, a 2px focus #1f3a5f outline wraps the whole line and the period cell text turns focus #1f3a5f. |
| active | On save, the stamp moment (stamp 320ms) plays: the stamp mark scales from 1.15 to 1.0 and settles into accent #b02a1e over the metric, like a ledger stamp. |
| empty | No value yet: the metric cell shows a muted #5a6472 dash '—' and the stamp mark is hidden; the rules remain so the line reads as a blank ledger row. |
| error | If the saved value failed validation, the metric cell turns danger #a5281c and the stamp mark is replaced by a status icon in danger #a5281c. |
| success | A confirmed value: stamp mark fully in accent #b02a1e, metric in ink #182230, and a thin success #2c5a34 underline ticks in under the metric (settle 200ms). |
| offline | A small device icon in warning #8a5a12 sits at the right of the line with the word 'saved on-device'; the value and stamp are unchanged. |

## Tally Record

A single tally row in the running record of entries, so the analyst can see each logged metric as a ledger line, not a card.

Anatomy: index cell (mono, muted #5a6472), period cell (mono), metric cell (mono, ink #182230), unit cell (mono), status cell (status icon + word).

| State | Treatment |
| --- | --- |
| default | One ledger row separated by a 1px line #d8d0bf; index and period in muted #5a6472, metric in ink #182230 mono, status icon in its colour role. |
| focus | Keyboard focus puts a 2px focus #1f3a5f outline on the row and the index cell turns focus #1f3a5f. |
| selected | The selected row gets a 3px accent #b02a1e left bar and a surface #fbf8f1 fill; the metric cell stays ink #182230. |
| empty | No records yet: the row area shows a muted #5a6472 tally icon and the line 'No entries on this device yet.' in the body type. |
| error | A row that failed to save shows the status icon in danger #a5281c and the metric cell in danger #a5281c. |
| offline | A device icon in warning #8a5a12 appears in the status cell with the word 'on-device'; the row is otherwise normal. |

## Stats Table

A stats table summarising the org’s output across periods (count, latest, total, change), in ledger vernacular rather than dashboard widgets.

Anatomy: table head (mono, muted #5a6472, uppercase), row grid (period, metric, unit, delta), delta cell (mono, signed), total row (bold, top rule 2px ink #182230).

| State | Treatment |
| --- | --- |
| default | Head row in muted #5a6472 mono; body rows in ink #182230 mono with 1px line #d8d0bf separators; the total row is bold with a 2px ink #182230 top rule. |
| focus | A focused row shows a 2px focus #1f3a5f outline and the period cell turns focus #1f3a5f. |
| empty | No data: the body collapses to one muted #5a6472 line 'Nothing tallied yet — enter a metric above.' with a tally icon. |
| loading | While the on-device total is computed, the total row shows a muted #5a6472 shimmer-free placeholder '—' and a small status icon in muted #5a6472; no animated sp |
| error | If a period’s value is invalid, that row’s delta cell turns danger #a5281c with a status icon in danger #a5281c. |
| offline | A device icon in warning #8a5a12 sits in the table head with the word 'on-device'; all figures remain readable. |

## Device Status

A compact on-device indicator that tells the analyst where the data lives and whether the device is ready, reinforcing offline-first.

Anatomy: device icon (device), state word (mono), storage hint (muted #5a6472).

| State | Treatment |
| --- | --- |
| default | Device icon in ink #182230, state word 'On-device' in ink #182230 mono, storage hint in muted #5a6472. |
| focus | A 2px focus #1f3a5f outline wraps the indicator and the state word turns focus #1f3a5f. |
| offline | Device icon and state word turn warning #8a5a12 with the word 'Offline — data stays here'; the status moment (settle 200ms) plays once. |
| error | If the on-device store is unavailable, the icon and word turn danger #a5281c with the word 'Store unavailable'. |
| success | When the store is confirmed writable, the icon turns success #2c5a34 with the word 'Ready'. |

## Offline Banner

A full-width band that appears when the device is offline, stating plainly that entry and saving still work on this device.

Anatomy: device icon (device), message (body, ink #182230), dismiss control (44px target).

| State | Treatment |
| --- | --- |
| default | Paper #f5f1e8 band with a 2px warning #8a5a12 left bar; device icon in warning #8a5a12; message in ink #182230. |
| focus | The dismiss control shows a 2px focus #1f3a5f outline; the band itself does not move. |
| active | On dismiss, the band collapses with the reveal moment (420ms) and the Device Status returns to default. |
| offline | This is the banner’s resting state: warning #8a5a12 bar, device icon, and the word 'Offline — everything you enter stays on this device.' |
| success | When connection returns, the bar and icon turn success #2c5a34 with the word 'Back online — data was kept on-device' for one settle (200ms) before it dismisses. |
| disabled | While a save is committing, the banner is suppressed (hidden) so it does not flicker mid-save; the dismiss control is disabled and the Device Status carries the |
| loading | While the connection state is being checked on load, the bar and device icon are muted #5a6472 and the message reads 'Checking device…' in muted #5a6472; no mo |

## Save Control

The primary action that commits the entered metric to the on-device ledger and triggers the stamp.

Anatomy: label (mono, 'Save to ledger'), status icon slot (status), control body (44px min height).

| State | Treatment |
| --- | --- |
| default | Accent #b02a1e fill with accentInk #f5f1e8 label, 1px ink #182230 border, mono type. |
| hover | Fill darkens one step toward ink #182230 (still accent-led); label stays accentInk #f5f1e8; no motion. |
| focus | A 2px focus #1f3a5f outline offset 2px wraps the control; the label remains accentInk #f5f1e8. |
| active | Pressed: the save moment (settle 200ms) plays and the status icon slot shows a status icon in accentInk #f5f1e8. |
| disabled | Muted #5a6472 fill at 50% opacity, label in muted #5a6472, no pointer; used when the field is empty or the record is locked. |
| loading | While committing to the on-device store, the label reads 'Saving…' in accentInk #f5f1e8 and a status icon in accentInk #f5f1e8 pulses once (tick 120ms); no spin |
| error | On a failed save, the fill turns danger #a5281c, the label reads 'Not saved' in accentInk #f5f1e8, and the status icon is in accentInk #f5f1e8. |
| success | On a successful save, the fill turns success #2c5a34, the label reads 'Saved' in accentInk #f5f1e8, and the status icon is in accentInk #f5f1e8 for one settle ( |

## Period Selector

Lets the analyst choose which period the entry sheet and stamped line refer to, as a ledger tab rather than a dropdown of cards.

Anatomy: tab strip (mono labels), active tab (accent #b02a1e underline), period label (mono), chevron/status slot (status).

| State | Treatment |
| --- | --- |
| default | Tabs in muted #5a6472 mono over a 1px line #d8d0bf; the active tab is ink #182230 with a 2px accent #b02a1e underline. |
| hover | A non-active tab turns ink #182230 on hover; no motion. |
| focus | The focused tab shows a 2px focus #1f3a5f outline and its label turns focus #1f3a5f. |
| selected | The selected tab keeps the 2px accent #b02a1e underline and ink #182230 label; the change moment (settle 200ms) slides the underline to the new tab. |
| disabled | A locked period tab is muted #5a6472 at 50% opacity with no underline and a status icon in muted #5a6472. |
| empty | If no periods exist, the strip shows one muted #5a6472 tab 'No periods' with a tally icon. |

## Note Field

A short free-text line on the entry sheet for the analyst’s context (source, caveat, method), kept in the ledger’s plain voice.

Anatomy: label (mono, muted #5a6472), input (body, ink #182230, 44px min target), character hint (mono, muted #5a6472).

| State | Treatment |
| --- | --- |
| default | Body-type input on surface #fbf8f1 with a 1px line #d8d0bf border; placeholder 'Source or caveat…' in muted #5a6472. |
| focus | A 2px focus #1f3a5f outline offset 2px; the label turns focus #1f3a5f. |
| active | While typing, the character hint counts up in muted #5a6472 mono (tick 120ms per keystroke). |
| error | If the note exceeds the limit, the border turns danger #a5281c and the hint reads 'Too long' in danger #a5281c. |
| empty | Empty is a valid resting state: placeholder in muted #5a6472, no error. |
| disabled | When the record is locked, the input is muted #5a6472 at 50% opacity and not editable. |

## Totals Band

A full-width band that breaks the grid and shows the running total and latest metric as ledger figures, using the total icon, not a chart.

Anatomy: total icon (total), total figure (bricolage-grotesque display, ink #182230), latest figure (mono, ink #182230), period label (mono, muted #5a6472).

| State | Treatment |
| --- | --- |
| default | Paper #f5f1e8 band with a 2px ink #182230 top rule; total icon in accent #b02a1e; figures in ink #182230. |
| focus | If the band is focusable (e.g. to copy the total), a 2px focus #1f3a5f outline wraps it and the total figure turns focus #1f3a5f. |
| empty | No entries: both figures show a muted #5a6472 dash '—' and the period label reads 'No periods tallied.' |
| loading | While the total recomputes, the total figure shows a muted #5a6472 '—' and a status icon in muted #5a6472; no animated sparkline. |
| success | After a save, the total figure ticks to the new value with the change moment (settle 200ms) and a thin success #2c5a34 underline appears under it. |
| offline | A device icon in warning #8a5a12 sits at the right with the word 'on-device'; figures are unchanged. |

## Status

Every status is a word, an icon and a colour, never colour alone.

| Status | Word | Icon | Colour role |
| --- | --- | --- | --- |
| Logged | Logged | `ledger` | `--color-success` |
| Pending | Pending | `tally` | `--color-warning` |
| Failed | Failed | `status` | `--color-danger` |
| On-device | On-device | `device` | `--color-muted` |
| Totalled | Totalled | `total` | `--color-accent` |
