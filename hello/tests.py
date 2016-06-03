from django.test import TestCase

class SimpleTestCase(TestCase):
    def test_succeed(self):
        """This test is only for checking my CirceCI setup"""
        self.assertEqual(1, 1)
