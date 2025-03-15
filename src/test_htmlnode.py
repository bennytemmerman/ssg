import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode(
            tag="a", 
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')

    def test_empty_props(self):
        node = HTMLNode(tag="p", props={})
        self.assertEqual(node.props_to_html(), '')

    def test_no_props(self):
        node = HTMLNode(tag="div")
        self.assertEqual(node.props_to_html(), '')

if __name__ == "__main__":
    unittest.main()

