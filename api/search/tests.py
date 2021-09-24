from django.test import TestCase


class TryTests(TestCase):

    def test_if_true(self):
        self.assertTrue(True)

    def test_false_is_false(self):
        self.assertFalse(False)

    def fake_false_is_false(self):
        self.assertFalse(False)
