import unittest

from htmlnode import HTML_Node


class TestTextNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTML_Node(props={"href": "www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="www.google.com" target="_blank"')

    def test_props_to_html2(self):
        node = HTML_Node(props={"href": "www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="www.google.com" target="_blank"')

    def test_props_to_html3(self):
        node = HTML_Node(props={"href": "www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()
