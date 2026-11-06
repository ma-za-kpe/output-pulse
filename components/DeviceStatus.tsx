"use client";

import { useEffect, useState } from "react";
import { useCollection } from "@/components/kit/useCollection";
import type { LedgerEntry } from "@/lib/db";

export default function DeviceStatus() {
  const { items, status } = useCollection<LedgerEntry>("ledger");
  const [lastSave, setLastSave] = useState<string | null>(null);

  useEffect(() => {
    if (items.length > 0) {
      const newest = items.reduce((a, b) => (a.period > b.period ? a : b));
      setLastSave(newest.period);
    }
  }, [items]);

  if (status === "loading") {
    return (
      <section className="device-status" aria-labelledby="device-status-title">
        <h2 id="device-status-title">Device Status</h2>
        <p className="device-status__state" role="status">
          Reading the ledger&hellip;
        </p>
      </section>
    );
  }

  if (status === "error") {
    return (
      <section className="device-status" aria-labelledby="device-status-title">
        <h2 id="device-status-title">Device Status</h2>
        <p className="device-status__state device-status__state--error" role="alert">
          Storage is unavailable. Your entry was not saved.
        </p>
      </section>
    );
  }

  return (
    <section className="device-status" aria-labelledby="device-status-title">
      <h2 id="device-status-title">Device Status</h2>
      <p className="device-status__copy">
        Your data stays on this device. Nothing is sent anywhere.
      </p>
      <dl className="device-status__details">
        <dt>Store</dt>
        <dd>{items.length} {items.length === 1 ? "entry" : "entries"}</dd>
        <dt>Last save</dt>
        <dd>{lastSave ?? "—"}</dd>
      </dl>
    </section>
  );
}
