"use client";

import { useCollection } from "@/components/kit/useCollection";
import type { LedgerEntry } from "@/lib/db";
import { sortEntries } from "@/lib/output";

export default function TallyRecord() {
  const { items, status, remove } = useCollection<LedgerEntry>("ledger");

  if (status === "loading") {
    return (
      <section className="tally-record" aria-labelledby="tally-record-title">
        <h2 id="tally-record-title">Tally Record</h2>
        <p className="tally-record__state" role="status">
          Reading the ledger&hellip;
        </p>
      </section>
    );
  }

  if (status === "error") {
    return (
      <section className="tally-record" aria-labelledby="tally-record-title">
        <h2 id="tally-record-title">Tally Record</h2>
        <p className="tally-record__state tally-record__state--error" role="alert">
          The entry could not be saved. Check the device and try again.
        </p>
      </section>
    );
  }

  if (items.length === 0) {
    return (
      <section className="tally-record" aria-labelledby="tally-record-title">
        <h2 id="tally-record-title">Tally Record</h2>
        <p className="tally-record__state">
          No output entries yet. Start with this quarter.
        </p>
      </section>
    );
  }

  const rows = sortEntries(items.map((s) => s.value));

  return (
    <section className="tally-record" aria-labelledby="tally-record-title">
      <h2 id="tally-record-title">Tally Record</h2>
      <table className="tally-record__table">
        <thead>
          <tr>
            <th scope="col">Period</th>
            <th scope="col">Metric</th>
            <th scope="col">Value</th>
            <th scope="col">Note</th>
            <th scope="col">Remove</th>
          </tr>
        </thead>
        <tbody>
          {rows.map((entry) => (
            <tr key={entry.id}>
              <td>{entry.value.period}</td>
              <td>{entry.value.metricName}</td>
              <td>{entry.value.value.toLocaleString()}</td>
              <td>{entry.value.note || ""}</td>
              <td>
                <button
                  type="button"
                  className="tally-record__remove"
                  onClick={() => void remove(entry.id)}
                >
                  Remove
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}
