"use client";

import { useState } from "react";
import { useCollection } from "@/components/kit/useCollection";
import type { LedgerEntry } from "@/lib/db";

export default function EntrySheet() {
  const { items, loading, error, add, remove } = useCollection<LedgerEntry>("ledger");
  const [metricName, setMetricName] = useState("");
  const [period, setPeriod] = useState("");
  const [value, setValue] = useState("");
  const [note, setNote] = useState("");
  const [saved, setSaved] = useState(false);

  const canSave = metricName.trim() !== "" && period.trim() !== "" && Number(value) > 0;

  async function onSave() {
    if (!canSave) return;
    const entry: LedgerEntry = {
      metricName: metricName.trim(),
      period: period.trim(),
      value: Number(value),
      note: note.trim(),
    };
    const ok = await add(entry);
    if (ok) {
      setMetricName("");
      setPeriod("");
      setValue("");
      setNote("");
      setSaved(true);
      setTimeout(() => setSaved(false), 3000);
    }
  }

  return (
    <section className="entry-sheet" aria-labelledby="entry-sheet-title">
      <h2 id="entry-sheet-title">Entry Sheet</h2>
      <p className="entry-sheet__hint">
        Enter your org&rsquo;s output metric for the selected period, with a note and a save
        control.
      </p>
      {loading ? (
        <p className="entry-sheet__state" role="status">
          Reading the ledger&hellip;
        </p>
      ) : error ? (
        <p className="entry-sheet__state entry-sheet__state--error" role="alert">
          The entry could not be saved. Check the device and try again.
        </p>
      ) : (
        <form
          className="entry-sheet__form"
          onSubmit={(e) => {
            e.preventDefault();
            void onSave();
          }}
        >
          <label className="entry-sheet__field">
            <span>Metric name</span>
            <input
              type="text"
              value={metricName}
              onChange={(e) => setMetricName(e.target.value)}
              required
            />
          </label>
          <label className="entry-sheet__field">
            <span>Period label</span>
            <input
              type="text"
              value={period}
              onChange={(e) => setPeriod(e.target.value)}
              placeholder="Q1 2025"
              required
            />
          </label>
          <label className="entry-sheet__field">
            <span>Value</span>
            <input
              type="number"
              min="0"
              step="any"
              value={value}
              onChange={(e) => setValue(e.target.value)}
              required
            />
          </label>
          <label className="entry-sheet__field">
            <span>Note</span>
            <input
              type="text"
              value={note}
              onChange={(e) => setNote(e.target.value)}
            />
          </label>
          <button type="submit" className="entry-sheet__save" disabled={!canSave}>
            Save to ledger
          </button>
          {saved && (
            <span className="entry-sheet__saved" role="status">
              Saved.
            </span>
          )}
        </form>
      )}
    </section>
  );
}
