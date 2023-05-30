import unittest
from ../translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
    def test_e2f(self):
        self.assertRaises(ValueError, englishToFrench, None)
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

class TestFrenchToEnglish(unittest.TestCase):
    def test_f2e(self):
        self.assertRaises(ValueError, frenchToEnglish, None)
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

if __name__ == "__main__":
    unittest.main()
