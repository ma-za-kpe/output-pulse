"use client";

import { useCollection } from "@/components/kit/useCollection";
import type { LedgerEntry } from "@/lib/db";
import { latestEntry } from "@/lib/output";

export default function StampedMetric() {
  const { items, loading, error } = useCollection<LedgerEntry>("ledger");

  if (loading) {
    return (
      <section className="stamped-metric" aria-labelledby="stamped-metric-title">
        <h2 id="stamped-metric-title">Stamped Metric</h2>
        <p className="stamped-metric__state" role="status">
          Reading the ledger…
        </p>
      </section>
    );
  }

  if (error) {
    return (
      <section className="stamped-metric" aria-labelledby="stamped-metric-title">
        <h2 id="stamped-metric-title">Stamped Metric</h2>
        <p className="stamped-metric__state stamped-metric__state--error" role="alert">
          The entry could not be saved. Check the device and try again.
        </p>
      </section>
    );
  }

  const latest = latestEntry(items);

  if (!latest) {
    return (
      <section className="stamped-metric" aria-labelledby="stamped-metric-title">
        <h2 id="stamped-metric-title">Stamped Metric</h2>
        <p className="stamped-metric__state">
          No output metric entered yet. Enter your org&rsquo;s output metric to start the
          ledger.
        </p>
      </section>
    );
  }

  return (
    <section className="stamped-metric" aria-labelledby="stamped-metric-title">
      <h2 id="stamped-metric-title">Stamped Metric</h2>
      <div className="stamped-metric__line">
        <span className="stamped-metric__value">{latest.value.value.toLocaleString()}</span>
        <span className="stamped-metric__period">{latest.value.period}</span>
        {latest.value.note && <span className="stamped-metric__note">{latest.value.note}</span>}
      </div>
    </section>
  );
}
