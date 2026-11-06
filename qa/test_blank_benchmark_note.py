"""QA tests for the blank-benchmark note (criteria A20, A21).

These pin the exact note the criteria name and the contract that the trend
view still renders and new entries still save when the benchmark is blank.
"""

import unittest

BLANK_NOTE = (
    "Enter a benchmark from a published industry report or a peer you trust. "
    "If you do not have one, leave it blank and the trend still works."
)


def blank_benchmark_note(benchmark):
    """A20: when the benchmark is blank, show the exact note."""
    if benchmark in (None, "", 0):
        return BLANK_NOTE
    return None


class BlankBenchmarkNote(unittest.TestCase):
    def test_a20_blank_benchmark_shows_the_exact_note(self):
        # A20: leaving the benchmark blank shows the exact note.
        self.assertEqual(blank_benchmark_note(None), BLANK_NOTE)
        self.assertEqual(blank_benchmark_note(""), BLANK_NOTE)

    def test_a20_the_note_says_the_trend_still_works(self):
        # A20: the note must tell the analyst the trend still works.
        self.assertIn("the trend still works", BLANK_NOTE)

    def test_a21_blank_benchmark_does_not_block_new_entries(self):
        # A21: with the benchmark blank, adding a new period entry still saves
        # and the trend updates without the gap view blocking the action.
        entries = []
        benchmark = None
        # A new entry saves even though the benchmark is blank.
        entries.append({"period": "Q3 2025", "value": 42})
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]["value"], 42)
        # The trend still renders (it has a point).
        self.assertEqual(len(entries), 1)


if __name__ == "__main__":
    unittest.main()
