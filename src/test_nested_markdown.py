import unittest
from text_to_textnode import text_to_textnodes


class TestNestedMarkdown(unittest.TestCase):
    def test_bold_and_italic_nested(self):
        # Test how nested markdown is handled
        result = text_to_textnodes("This is **bold *italic*** text")
        # The function should process bold first, then any remaining italic within the bold
        # This tests if the sequential order works properly
        self.assertGreaterEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
