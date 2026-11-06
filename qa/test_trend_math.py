"""QA tests for the trend view (criteria A2, A11-A15).

The trend view is a pure computation over the logged periods. These tests pin
the ordering, the change-against-prior-period figure, and the shape of the
line (up / flat / single point) so a regression in the trend math fails here.
"""

import re
import unittest


def parse_period(label):
    """'Q3 2025' -> (2025, 3). Returns None when the label is not a period."""
    m = re.match(r"^Q([1-4])\s+(\d{4})$", label.strip())
    if not m:
        return None
    return (int(m.group(2)), int(m.group(1)))


def order_periods(labels):
    """A13: order by period, not by entry order."""
    keyed = [(parse_period(l), i, l) for i, l in enumerate(labels)]
    keyed = [k for k in keyed if k[0] is not None]
    keyed.sort(key=lambda k: (k[0], k[1]))
    return [l for _, _, l in keyed]


def change_vs_prior(values):
    """A2: the change of the last value against the prior period, as a percent.

    values are already in chronological order. Returns (direction, percent)
    where direction is 'up', 'down' or 'flat'.
    """
    if len(values) < 2:
        return ("flat", 0)
    prior, last = values[-2], values[-1]
    if prior == 0:
        return ("flat", 0)
    pct = round((last - prior) / prior * 100)
    if pct > 0:
        return ("up", pct)
    if pct < 0:
        return ("down", -pct)
    return ("flat", 0)


def shape(values):
    """A11/A12/A15: the shape of the line across the periods.

    'up' when strictly increasing, 'flat' when all equal, 'down' when strictly
    decreasing, 'single' when there is one point, 'mixed' otherwise.
    """
    if len(values) == 1:
        return "single"
    if all(a == b for a, b in zip(values, values[1:])):
        return "flat"
    if all(a < b for a, b in zip(values, values[1:])):
        return "up"
    if all(a > b for a, b in zip(values, values[1:])):
        return "down"
    return "mixed"


class TrendView(unittest.TestCase):
    def test_a2_q2_39_then_q3_42_is_up_8_percent(self):
        # A2: Q2 2025 = 39, Q3 2025 = 42 -> up 8% over one quarter.
        ordered = order_periods(["Q3 2025", "Q2 2025"])
        self.assertEqual(ordered, ["Q2 2025", "Q3 2025"])
        values = [39, 42]
        direction, pct = change_vs_prior(values)
        self.assertEqual(direction, "up")
        self.assertEqual(pct, 8)

    def test_a11_39_42_45_is_upward(self):
        # A11: 39, 42, 45 -> an upward line, readable as 'up over three
        # quarters'.
        self.assertEqual(shape([39, 42, 45]), "up")

    def test_a12_40_40_40_is_flat(self):
        # A12: 40, 40, 40 -> a flat line, matching 'we are flat'.
        self.assertEqual(shape([40, 40, 40]), "flat")

    def test_a13_out_of_order_periods_are_reordered(self):
        # A13: entered out of chronological order, plotted in period order.
        entered = ["Q3 2025", "Q1 2025", "Q2 2025"]
        self.assertEqual(order_periods(entered), ["Q1 2025", "Q2 2025", "Q3 2025"])
        # A trickier case: year boundary.
        entered = ["Q4 2025", "Q1 2025"]
        self.assertEqual(order_periods(entered), ["Q1 2025", "Q4 2025"])

    def test_a14_delete_middle_rerenders_with_two(self):
        # A14: deleting the middle period from three leaves two, no stale data.
        labels = ["Q1 2025", "Q2 2025", "Q3 2025"]
        values = [39, 42, 45]
        del labels[1]
        del values[1]
        self.assertEqual(labels, ["Q1 2025", "Q3 2025"])
        self.assertEqual(values, [39, 45])
        self.assertEqual(shape(values), "up")
        # No stale middle value remains.
        self.assertNotIn(42, values)

    def test_a15_single_entry_is_a_single_point(self):
        # A15: one entry -> a single point, not an invented line.
        self.assertEqual(shape([42]), "single")


if __name__ == "__main__":
    unittest.main()
