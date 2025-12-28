import unittest

from htmlnode import HTML_Node, LeafNode, ParentNode


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

    def test_leaf_to_html(self):
        node = LeafNode("p", "www.google.com", {"target": "_blank"})
        print(node.to_html())
        self.assertEqual(node.to_html(), '<p target="_blank">www.google.com</p>')

    def test_to_hetml_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_hetml_with_children2(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(), "<div><span><b>grandchild</b></span></div>"
        )


if __name__ == "__main__":
    unittest.main()
