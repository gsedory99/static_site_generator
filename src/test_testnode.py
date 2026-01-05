import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode(
            "this is a text node", TextType.ITALIC_TEXT, url="www.google.com"
        )
        node2 = TextNode(
            "this is a text node", TextType.PLAIN_TEXT, url="www.google.com"
        )
        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.LINK, url="www.google.com")
        node2 = TextNode("This is a text node", TextType.LINK, url="www.google.com")
        self.assertEqual(node, node2)

    def test_text(self):
        node_1 = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node_1 = text_node_to_html_node(node_1)
        node_2 = TextNode("This is bold text", TextType.BOLD_TEXT)
        html_node_2 = text_node_to_html_node(node_2)
        self.assertEqual(html_node_1.tag, None)
        self.assertEqual(html_node_1.value, "This is a text node")
        self.assertEqual(html_node_2.tag, "b")


if __name__ == "__main__":
    unittest.main()
