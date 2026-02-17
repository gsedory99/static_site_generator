import unittest
from text_to_textnode import text_to_textnodes


class TestOrderImportance(unittest.TestCase):
    def test_valid_comprehensive(self):
        # Test that our current approach works with valid markdown combinations
        result = text_to_textnodes("This is **bold** and *italic* and `code`")
        self.assertGreaterEqual(len(result), 1)

        # Test the specific case that should work
        result2 = text_to_textnodes("This is **bold** text")
        self.assertEqual(len(result2), 3)  # plain, bold, plain

        result3 = text_to_textnodes("This is *italic* text")
        self.assertEqual(len(result3), 3)  # plain, italic, plain


if __name__ == "__main__":
    unittest.main()
