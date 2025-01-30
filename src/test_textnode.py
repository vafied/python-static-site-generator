import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_none_url(self):
        node = TextNode("This is a text node", TextType.BOLD, None)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node",
                        TextType.BOLD, "http://example.com/")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


class TestTextoHTML(unittest.TestCase):

    def test_text_to_html(self):
        node = TextNode("This is a text node",
                        TextType.TEXT, "http://example.com/")

        to_text = text_node_to_html_node(node)
        self.assertEqual(to_text.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_image(self):
        expected_dic = {
            'src': 'http://example.com/image.jpg', 'alt': 'Alt Text'}
        node = TextNode("Alt Text", TextType.IMAGES,
                        "http://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props, expected_dic)


if __name__ == "__main__":
    unittest.main()
