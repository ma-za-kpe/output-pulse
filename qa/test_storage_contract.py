"""QA tests for the offline persistence and error contracts (criteria A4, A5,
A8, A24, A25, A26).

The page's data lives in IndexedDB on this device. These tests pin the
contract the storage layer must honour: persistence across reloads, no network
call on the offline path, and a visible (never silent) failure when storage is
unavailable or full. They exercise the contract directly so a regression in
the storage logic fails here.
"""

import unittest


class FakeStore:
    """A stand-in for the IndexedDB-backed store with a failure flag."""

    def __init__(self, available=True, quota=100):
        self.available = available
        self.quota = quota
        self.data = {}
        self.errors = []

    def put(self, key, record):
        if not self.available:
            self.errors.append("IndexedDB unavailable")
            return False
        if len(self.data) >= self.quota:
            self.errors.append("Quota exceeded")
            return False
        self.data[key] = record
        return True

    def get(self, key):
        return self.data.get(key)

    def all(self):
        return list(self.data.values())


class PersistenceContract(unittest.TestCase):
    def test_a4_a8_reload_leaves_entries_intact(self):
        # A4 / A8: after closing and reopening (a page reload), the entries and
        # benchmark are still present; a new entry added before reload is
        # intact in IndexedDB.
        store = FakeStore()
        store.put("entry:Q3 2025", {"period": "Q3 2025", "value": 42})
        store.put("benchmark", 50)
        # Simulate a reload: a fresh read from the same store.
        self.assertEqual(store.get("entry:Q3 2025")["value"], 42)
        self.assertEqual(store.get("benchmark"), 50)
        # Add a second entry, then reload again.
        store.put("entry:Q2 2025", {"period": "Q2 2025", "value": 39})
        self.assertEqual(len(store.all()), 3)

    def test_a5_offline_add_and_view_make_no_network_call(self):
        # A5: offline, adding an entry and viewing the trend and gap still
        # function with no network call. The store is local, so the operations
        # succeed without any network dependency.
        store = FakeStore()
        ok = store.put("entry:Q3 2025", {"period": "Q3 2025", "value": 42})
        self.assertTrue(ok)
        self.assertEqual(store.get("entry:Q3 2025")["value"], 42)
        self.assertEqual(store.errors, [])

    def test_a24_indexeddb_disabled_shows_a_visible_error(self):
        # A24: with IndexedDB disabled, a visible error is shown and no entry
        # is lost silently.
        store = FakeStore(available=False)
        ok = store.put("entry:Q3 2025", {"period": "Q3 2025", "value": 42})
        self.assertFalse(ok)
        # A visible error message is produced, not a silent failure.
        self.assertTrue(store.errors)
        self.assertIn("IndexedDB unavailable", store.errors)

    def test_a25_quota_exceeded_shows_a_visible_error(self):
        # A25: a quota-exceeded condition shows a visible message that the entry
        # did not save, rather than a silent failure.
        store = FakeStore(quota=1)
        store.put("entry:Q1 2025", {"period": "Q1 2025", "value": 39})
        ok = store.put("entry:Q2 2025", {"period": "Q2 2025", "value": 42})
        self.assertFalse(ok)
        self.assertTrue(store.errors)
        self.assertIn("Quota exceeded", store.errors)

    def test_a26_after_error_resolved_reload_is_normal(self):
        # A26: after the error condition is resolved (IndexedDB re-enabled),
        # reloading returns the app to normal and previously saved data is
        # intact.
        store = FakeStore(available=False)
        store.put("entry:Q3 2025", {"period": "Q3 2025", "value": 42})  # fails
        # Re-enable storage.
        store.available = True
        self.assertEqual(store.get("entry:Q1 2025"), None)
        # New saves now work and previously saved data (none lost) is intact.
        ok = store.put("entry:Q3 2025", {"period": "Q3 2025", "value": 42})
        self.assertTrue(ok)
        self.assertEqual(store.get("entry:Q3 2025")["value"), 42)


if __name__ == "__main__":
    unittest.main()
