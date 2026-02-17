import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from text_to_textnode import text_to_textnodes
from textnode import TextType


class TestTextToTextnodes(unittest.TestCase):
    def test_simple_text(self):
        result = text_to_textnodes("just plain text")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "just plain text")
        self.assertEqual(result[0].text_type, TextType.PLAIN_TEXT)

    def test_bold_text(self):
        result = text_to_textnodes("this is **bold** text")
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "this is ")
        self.assertEqual(result[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD_TEXT)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.PLAIN_TEXT)

    def test_italic_text(self):
        result = text_to_textnodes("this is *italic* text")
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "this is ")
        self.assertEqual(result[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(result[1].text, "italic")
        self.assertEqual(result[1].text_type, TextType.ITALIC_TEXT)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.PLAIN_TEXT)

    def test_code_text(self):
        result = text_to_textnodes("this is `code` text")
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "this is ")
        self.assertEqual(result[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(result[1].text, "code")
        self.assertEqual(result[1].text_type, TextType.CODE_TEXT)
        self.assertEqual(result[2].text, " text")
        self.assertEqual(result[2].text_type, TextType.PLAIN_TEXT)

    def test_image_text(self):
        result = text_to_textnodes("this is an ![image](https://example.com/image.png)")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "this is an ")
        self.assertEqual(result[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(result[1].text, "image")
        self.assertEqual(result[1].text_type, TextType.IMAGE)
        self.assertEqual(result[1].url, "https://example.com/image.png")

    def test_link_text(self):
        result = text_to_textnodes("this is a [link](https://example.com)")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].text, "this is a ")
        self.assertEqual(result[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(result[1].text, "link")
        self.assertEqual(result[1].text_type, TextType.LINK)
        self.assertEqual(result[1].url, "https://example.com")

    def test_multiple_elements(self):
        result = text_to_textnodes("this is **bold** and *italic* and `code`")
        self.assertEqual(len(result), 6)

    def test_complex_mixed_text(self):
        result = text_to_textnodes(
            "This is **bold** with *italic* and `code` and an ![image](img.png) and [link](url)"
        )
        self.assertEqual(len(result), 10)


if __name__ == "__main__":
    unittest.main()
