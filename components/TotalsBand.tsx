"use client";

import { useCollection } from "@/components/kit/useCollection";
import type { LedgerEntry } from "@/lib/db";
import { ledgerTotal } from "@/lib/output";

export default function TotalsBand() {
  const { items, status } = useCollection<LedgerEntry>("ledger");

  if (status === "loading") {
    return (
      <section className="totals-band" aria-labelledby="totals-band-title">
        <h2 id="totals-band-title">Totals</h2>
        <p className="totals-band__state" role="status">
          Reading the ledger&hellip;
        </p>
      </section>
    );
  }

  if (status === "error") {
    return (
      <section className="totals-band" aria-labelledby="totals-band-title">
        <h2 id="totals-band-title">Totals</h2>
        <p className="totals-band__state totals-band__state--error" role="alert">
          The entry could not be saved. Check the device and try again.
        </p>
      </section>
    );
  }

  if (items.length === 0) {
    return (
      <section className="totals-band" aria-labelledby="totals-band-title">
        <h2 id="totals-band-title">Totals</h2>
        <p className="totals-band__state">
          No output entries yet. Start with this quarter.
        </p>
      </section>
    );
  }

  const total = ledgerTotal(items.map((s) => s.value));

  return (
    <section className="totals-band" aria-labelledby="totals-band-title">
      <h2 id="totals-band-title">Totals</h2>
      <p className="totals-band__figure" role="status">
        {total.toLocaleString()}
      </p>
    </section>
  );
}
