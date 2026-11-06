// Pure logic for the Output Pulse ledger: totals, trend and the peer gap.
// The product's data stays on this device; these functions only compute.

export type Entry = {
  metric: string;
  period: string;
  value: number;
  note?: string;
};

export function sortEntries<T extends { period: string }>(items: T[]): T[] {
  return [...items].sort((a, b) => a.period.localeCompare(b.period));
}

export function totals(items: Entry[]) {
  const values = items.map((i) => i.value);
  const count = values.length;
  const total = values.reduce((a, b) => a + b, 0);
  const average = count === 0 ? 0 : total / count;
  const best = count === 0 ? 0 : Math.max(...values);
  const sorted = sortEntries(items);
  const last = sorted.length > 0 ? sorted[sorted.length - 1] : null;
  return { count, total, average, best, last };
}

export type Direction = "up" | "down" | "flat";

export function trendDirection(items: Entry[]): Direction {
  const sorted = sortEntries(items);
  if (sorted.length < 2) return "flat";
  const first = sorted[0].value;
  const last = sorted[sorted.length - 1].value;
  if (last > first) return "up";
  if (last < first) return "down";
  return "flat";
}

export function benchmarkGap(you: number, peers: number) {
  const gap = peers - you;
  const pct = you === 0 ? 0 : (gap / you) * 100;
  return { gap, pct };
}
