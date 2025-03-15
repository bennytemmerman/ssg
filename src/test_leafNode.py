import unittest
from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Just some raw text")
        self.assertEqual(node.to_html(), "Just some raw text")

    def test_leaf_without_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_without_tag_and_no_value(self):
        with self.assertRaises(ValueError):
            LeafNode(None, None)

    def test_leaf_to_html_div_with_props(self):
        node = LeafNode("div", "This is a div", {"class": "container", "id": "main"})
        self.assertEqual(node.to_html(), '<div class="container" id="main">This is a div</div>')


if __name__ == "__main__":
    unittest.main()
