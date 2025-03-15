import unittest
from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_without_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "child")])

    def test_to_html_without_children(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_to_html_multiple_children(self):
        child_node_1 = LeafNode("span", "child 1")
        child_node_2 = LeafNode("span", "child 2")
        parent_node = ParentNode("div", [child_node_1, child_node_2])
        self.assertEqual(parent_node.to_html(), "<div><span>child 1</span><span>child 2</span></div>")

    def test_to_html_no_props(self):
        child_node = LeafNode("p", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><p>child</p></div>")

    def test_to_html_with_props(self):
        child_node = LeafNode("p", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(parent_node.to_html(), '<div class="container"><p>child</p></div>')

if __name__ == "__main__":
    unittest.main()
