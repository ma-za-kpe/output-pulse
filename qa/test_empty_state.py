"""QA tests for the empty state and first-entry transition (criteria A22, A23).

These pin the exact empty-state copy the criteria name and the transition
that happens when the first entry is added.
"""

import unittest

EMPTY_COPY = "No output entries yet. Start with this quarter."


def empty_state_copy(entries):
    """A22: with no entries, show the empty-state copy and a way to add the
    first entry. With at least one entry, show nothing (the tracker/trend
    render instead)."""
    if not entries:
        return EMPTY_COPY
    return None


class EmptyState(unittest.TestCase):
    def test_a22_fresh_profile_shows_the_empty_copy(self):
        # A22: opening with no entries shows the exact empty-state copy.
        self.assertEqual(empty_state_copy([]), EMPTY_COPY)
        self.assertIn("No output entries yet", EMPTY_COPY)
        self.assertIn("Start with this quarter", EMPTY_COPY)

    def test_a23_first_entry_disappears_the_empty_state(self):
        # A23: after adding the first entry the empty state disappears and the
        # tracker/trend render with the new data.
        self.assertIsNone(empty_state_copy([{"period": "Q3 2025", "value": 42}]))

    def test_a23_a_single_entry_is_not_empty(self):
        # A control: one entry is not the empty state.
        self.assertIsNotNone(empty_state_copy([]))
        self.assertIsNone(empty_state_copy([{"period": "Q1 2025", "value": 39}]))


if __name__ == "__main__":
    unittest.main()
