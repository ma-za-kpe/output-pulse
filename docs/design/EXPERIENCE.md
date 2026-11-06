# Output Pulse experience

## Information architecture

### `/`

The working ledger: enter this period's output metric, stamp it onto the ledger line, and read the running tally, stats, and totals for your org, all on this device. Primary task: Enter and stamp the org's output metric for the selected period, then review the running tally and totals.

| Section | Purpose | Layout | Components | Moment |
| --- | --- | --- | --- | --- |
| Entry Sheet | The core job, reachable from the top: enter the org's output metric for the selected period, with a note and a save control. | split | Entry Sheet, Period Selector, Note Field, Save Control | entry |
| Stamped Metric Line | The one place of boldness: the entered metric rendered as a tracked, stamped number on a ledger line, with the period and a short note. | band | Stamped Metric Line, Period Selector | stamp |
| Tally Record | The running ledger of every stamped metric, newest first, as ledger rows with period, value, note, and a remove action. | table | Tally Record | change |
| Stats Table | Plain computed figures for the selected period: count, total, average, best, and last entry, no charts and no sparklines. | table | Stats Table, Period Selector | change |
| Totals Band | The running total for the selected period, stated plainly as a single ledger figure. | band | Totals Band | change |
| Device Status | Reassure the analyst that data stays on this device and show the local store's state and last save time. | band | Device Status, Offline Banner | status |

### `/records`

The full tally: browse, filter, and manage every stamped metric across all periods, on this device. Primary task: Review and manage the complete tally record, including removing an entry.

| Section | Purpose | Layout | Components | Moment |
| --- | --- | --- | --- | --- |
| Period Selector | Filter the tally by period so the analyst can focus on one stretch of the ledger. | band | Period Selector | change |
| Tally Record | The complete ledger of stamped metrics as ledger rows, newest first, each with a remove action. | table | Tally Record | change |
| Stats Table | Computed figures for the filtered period: count, total, average, best, last entry. | table | Stats Table | change |
| Totals Band | The running total for the filtered period, stated as a single ledger figure. | band | Totals Band | change |
| Device Status | Show the local store's state and last save time for the records view. | band | Device Status, Offline Banner | status |

## Flows

- **Enter and stamp this period's output metric**: Open the home ledger at /; the Entry Sheet is at the top with the Period Selector set to the current period. → Type the org's output metric into the Entry Sheet number field; the field accepts a plain number and shows a live tick. → Add a short note in the Note Field (optional) to mark what the number covers. → Press the Save Control; the metric is written to the on-device store and stamped onto the Stamped Metric Line with the '
- **Review the running tally and totals**: Scroll from the Stamped Metric Line to the Tally Record to see every stamped metric, newest first. → Read the Stats Table for the selected period: count, total, average, best, and last entry. → Confirm the running total in the Totals Band. → Check the Device Status band to confirm the data is on this device and note the last save time.
- **Change the period and compare**: Open the Period Selector and choose a different period. → The Stamped Metric Line, Tally Record, Stats Table, and Totals Band all update to that period with the 'change' moment. → Compare the period's total and average against the current period. → Return to the current period when done.
- **Remove an entry from the tally**: Open /records and find the ledger row to remove in the Tally Record. → Press the row's remove action; the product asks for a plain confirmation. → Confirm; the row is removed from the on-device store and the tally, stats, and totals recompute with the 'change' moment → The Device Status band updates the last save time.

## Screen states

| Screen | empty | loading | error | success |
| --- | --- | --- | --- | --- |
| Entry Sheet | No metric entered for this period yet. Enter your org's output metric above to start the ledger. | Reading this period from this device… | That number could not be saved to this device. Check the value and try again. | Saved to this device. The metric is stamped on the ledger line below. |
| Stamped Metric Line | Nothing stamped for this period. The ledger line is waiting for your first entry. | Setting the ledger line… | The ledger line could not be updated. Your last saved metric is shown. | Stamped. The metric is tracked on the ledger line for this period. |
| Tally Record | No entries in the tally yet. Your first stamped metric will appear here. | Loading the tally from this device… | The tally could not be read from this device. Nothing was changed. | Tally is current. Every stamped metric is listed, newest first. |
| Stats Table | No figures yet for this period. Stats appear once you stamp a metric. | Computing figures… | Figures could not be computed. The last good figures are shown. | Figures are current for this period. |
| Totals Band | No total yet for this period. | Adding up the period… | The total could not be updated. The last saved total is shown. | Total is current for this period. |
| Device Status | This device is ready. No entries yet — your data will stay here. | Checking this device… | This device could not be reached. Your last saved data is still here. | On this device. Last saved just now. |

## Interactions

| Trigger | Response | Duration |
| --- | --- | --- |
| Typing a value into the Entry Sheet number field | The field shows a live tick as the number is accepted; invalid input is held back with a plain message. | `tick` |
| Pressing the Save Control | The metric is written to the on-device store and the Stamped Metric Line stamps the number onto the ledger line. | `stamp` |
| Changing the Period Selector | The Stamped Metric Line, Tally Record, Stats Table, and Totals Band recompute and settle to the new period. | `settle` |
| Removing a row from the Tally Record | After a plain confirmation, the row is removed and the tally, stats, and totals recompute. | `settle` |
| A save completes on the device | The Device Status band updates the last save time and the Offline Banner clears if it was showing. | `tick` |
| The device store becomes unavailable | The Offline Banner appears and the Device Status band moves to its error state; the last saved data stays visible. | `reveal` |
| A new metric is stamped | The Stamped Metric Line plays a short burst on the stamped number, then settles. | `burst` |
