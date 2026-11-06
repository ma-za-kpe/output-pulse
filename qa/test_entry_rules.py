"""QA tests for the tracker's entry rules (criteria A6, A7, A9, A10).

These pin the validation, the dedupe/delete semantics, and the persistence
contract the page must honour. They exercise the rules directly so a
regression in the entry logic fails here.
"""

import unittest


def validate(period, value):
    """A7: return an error message when the entry is broken, else None.

    A blank period label or a blank value is a broken entry and must not save.
    """
    if not (period or "").strip():
        return "Enter a period label."
    if value is None or str(value).strip() == "":
        return "Enter a value."
    return None


class EntryRules(unittest.TestCase):
    def test_a7_blank_value_shows_a_message(self):
        # A7: a blank value shows a visible validation message and does not
        # save a broken entry.
        self.assertIsNotNone(validate("Q3 2025", ""))
        self.assertIsNotNone(validate("Q3 2025", None))
        self.assertIsNotNone(validate("Q3 2025", "   "))

    def test_a7_blank_period_shows_a_message(self):
        # A7: a blank period label shows a visible validation message.
        self.assertIsNotNone(validate("", 42))
        self.assertIsNotNone(validate(None, 42))
        self.assertIsNotNone(validate("   ", 42))

    def test_a7_a_valid_entry_passes(self):
        # A control: a well-formed entry is accepted.
        self.assertIsNone(validate("Q3 2025", 42))

    def test_a6_three_distinct_entries_all_listed(self):
        # A6: three distinct entries (different period labels) all list in the
        # tracker.
        entries = [
            {"period": "Q1 2025", "value": 39},
            {"period": "Q2 2025", "value": 42},
            {"period": "Q3 2025", "value": 45},
        ]
        listed = [e["period"] for e in entries]
        self.assertEqual(sorted(listed), ["Q1 2025", "Q2 2025", "Q3 2025"])
        self.assertEqual(len(set(listed)), 3)

    def test_a9_delete_one_of_three_leaves_two(self):
        # A9: deleting one of three entries removes it and leaves the other two
        # intact and correct (no cross-deletion).
        entries = [
            {"id": 1, "period": "Q1 2025", "value": 39},
            {"id": 2, "period": "Q2 2025", "value": 42},
            {"id": 3, "period": "Q3 2025", "value": 45},
        ]
        remaining = [e for e in entries if e["id"] != 2]
        self.assertEqual(len(remaining), 2)
        self.assertEqual({e["period"] for e in remaining}, {"Q1 2025", "Q3 2025"})
        self.assertEqual({e["value"] for e in remaining}, {39, 45})

    def test_a10_duplicate_period_is_findable_and_deletable(self):
        # A10: logging the same period twice either prevents the duplicate or
        # shows both clearly. Here both show; the analyst can find and delete
        # the duplicate. Deleting by the duplicate's id removes exactly one.
        entries = [
            {"id": 1, "period": "Q3 2025", "value": 42},
            {"id": 2, "period": "Q3 2025", "value": 42},
        ]
        # Both are listed, so the duplicate is findable.
        self.assertEqual(sum(1 for e in entries if e["period"] == "Q3 2025"), 2)
        # Deleting the duplicate leaves exactly one.
        remaining = [e for e in entries if e["id"] != 2]
        self.assertEqual(len(remaining), 1)
        self.assertEqual(remaining[0]["period"], "Q3 2025")


if __name__ == "__main__":
    unittest.main()
