import unittest

from markdown_to_blocks import BlockType, block_to_block_type, markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
This is  **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(markdown)
        self.failureException(
            blocks,
            [
                "This is  **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```python"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- Item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. Item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("Paragraph"), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
