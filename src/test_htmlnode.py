import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank", }
        expected = ' href="https://www.google.com" target="_blank"'
        node = HTMLNode("a", "This is a link", None, props)
        self.assertEqual(expected, node.props_to_html())

    def test_eq(self):
        node = HTMLNode("p", "this is a paragraph")
        node2 = HTMLNode("p", "this is a paragraph")
        self.assertEqual(node.tag, node2.tag)
        self.assertEqual(node.value, node2.value)

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )


class TestLeafNode(unittest.TestCase):
    def test_leaf_node(self):
        leaf = LeafNode("p", "This is a paragraph")
        self.assertEqual(leaf.to_html(), '<p>This is a paragraph</p>')

    def test_leaf_link(self):
        props = {"href": "https://www.google.com", "target": "_blank", }
        expected = '<a href="https://www.google.com" target="_blank">This is a link</a>'
        leaf = LeafNode("a", "This is a link", props)
        self.assertEqual(leaf.to_html(), expected)

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_invalid_leaf(self):
        leaf = LeafNode("p", None)
        with self.assertRaises(ValueError):
            leaf.to_html()


class TestParentNode(unittest.TestCase):

    def test_parent_node(self):
        expected = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(expected, node.to_html())

    def test_parent_node_props(self):
        props = {"href": "https://www.google.com", "target": "_blank", }
        expected = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<a href="https://www.google.com" target="_blank">This is a link</a></p>'
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                LeafNode("a", "This is a link", props),
            ],
        )
        self.assertEqual(expected, node.to_html())

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()
