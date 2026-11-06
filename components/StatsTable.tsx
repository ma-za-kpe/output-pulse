"use client";

import { useCollection } from "@/components/kit/useCollection";
import type { LedgerEntry } from "@/lib/db";
import { ledgerStats } from "@/lib/output";

export default function StatsTable() {
  const { items, status } = useCollection<LedgerEntry>("ledger");

  if (status === "loading") {
    return (
      <section className="stats-table" aria-labelledby="stats-table-title">
        <h2 id="stats-table-title">Stats Table</h2>
        <p className="stats-table__state" role="status">
          Reading the ledger&hellip;
        </p>
      </section>
    );
  }

  if (status === "error") {
    return (
      <section className="stats-table" aria-labelledby="stats-table-title">
        <h2 id="stats-table-title">Stats Table</h2>
        <p className="stats-table__state stats-table__state--error" role="alert">
          The entry could not be saved. Check the device and try again.
        </p>
      </section>
    );
  }

  if (items.length === 0) {
    return (
      <section className="stats-table" aria-labelledby="stats-table-title">
        <h2 id="stats-table-title">Stats Table</h2>
        <p className="stats-table__state">
          No output entries yet. Start with this quarter.
        </p>
      </section>
    );
  }

  const stats = ledgerStats(items.map((s) => s.value));

  return (
    <section className="stats-table" aria-labelledby="stats-table-title">
      <h2 id="stats-table-title">Stats Table</h2>
      <table className="stats-table__table">
        <tbody>
          <tr>
            <th scope="row">Entries</th>
            <td>{stats.count}</td>
          </tr>
          <tr>
            <th scope="row">Total</th>
            <td>{stats.total.toLocaleString()}</td>
          </tr>
          <tr>
            <th scope="row">Average</th>
            <td>{stats.average.toLocaleString()}</td>
          </tr>
          <tr>
            <th scope="row">Best</th>
            <td>{stats.best.toLocaleString()}</td>
          </tr>
          <tr>
            <th scope="row">Last entry</th>
            <td>
              {stats.last ? `${stats.last.period} — ${stats.last.value.toLocaleString()}` : "—"}
            </td>
          </tr>
        </tbody>
      </table>
    </section>
  );
}
