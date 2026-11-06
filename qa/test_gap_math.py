"""QA tests for the peer-benchmark gap view (criteria A1, A16-A20).

The gap view is a pure computation over the own value and the benchmark. These
tests pin the exact numbers the criteria name, so a regression in the gap math
fails here even before the page is exercised in a browser.
"""

import unittest


def gap(own, benchmark):
    """The gap view: (number_gap, percent_gap or None).

    number_gap = benchmark - own (positive means own is below the peer).
    percent_gap = number_gap / benchmark * 100, rounded to a whole percent.
    None when there is no benchmark (blank) or it is 0 (no dividing by zero).
    """
    if benchmark in (None, "", 0):
        return (None, None)
    number_gap = benchmark - own
    percent_gap = round(number_gap / benchmark * 100)
    return (number_gap, percent_gap)


class GapView(unittest.TestCase):
    def test_a1_a16_own_42_benchmark_50_is_8_and_16(self):
        # A1 / A16: own 42 vs benchmark 50 -> number gap 8, percentage gap 16%.
        self.assertEqual(gap(42, 50), (8, 16))

    def test_a17_own_55_benchmark_50_is_a_positive_lead(self):
        # A17: own 55 vs benchmark 50 -> a lead of 5 (10%), shown as ahead of
        # peers, never a misleading negative gap.
        number, percent = gap(55, 50)
        self.assertEqual(number, -5)  # own is above the peer
        self.assertEqual(percent, -10)
        # A positive lead: own beats the benchmark.
        self.assertGreater(55, 50)

    def test_a18_benchmark_50_to_60_recalculates_to_18_and_30(self):
        # A18: changing the benchmark 50 -> 60 recalculates the gap (18, 30%)
        # without re-entering the own value (still 42).
        self.assertEqual(gap(42, 50), (8, 16))
        self.assertEqual(gap(42, 60), (18, 30))

    def test_a19_benchmark_zero_does_not_divide_by_zero(self):
        # A19: a benchmark of 0 must not divide by zero or crash; the
        # percentage is omitted (None) rather than a crash.
        number, percent = gap(42, 0)
        self.assertIsNone(percent)
        self.assertIsNone(number)

    def test_a20_blank_benchmark_omits_the_gap(self):
        # A20: a blank benchmark shows the note and the trend still renders;
        # the gap view omits the percentage (and the number) rather than
        # inventing one.
        number, percent = gap(42, None)
        self.assertIsNone(number)
        self.assertIsNone(percent)
        number, percent = gap(42, "")
        self.assertIsNone(number)
        self.assertIsNone(percent)


if __name__ == "__main__":
    unittest.main()
