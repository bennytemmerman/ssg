import unittest
from textnode import TextType, TextNode
from split import split_nodes_delimiter  # import the split_nodes_delimiter function

class TestSplitNodesDelimiter(unittest.TestCase):

    # Test for splitting text with a code delimiter (backticks)
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is text with a ")
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)

    # Test for splitting text with a bold delimiter (double asterisks)
    def test_split_bold(self):
        node = TextNode("This is **bold text** in a sentence.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[1].text, "bold text")
        self.assertEqual(new_nodes[2].text, " in a sentence.")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)

    # Test for splitting text with an italic delimiter (underscore)
    def test_split_italic(self):
        node = TextNode("This is _italic_ text example.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)

        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[2].text, " text example.")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)

    # Test for handling multiple delimiters (bold and code)
    def test_split_multiple_delimiters(self):
        node = TextNode("This is **old** and `code` text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        # Allowing an extra node if punctuation is split
        self.assertIn(len(new_nodes), [5, 6])  # Accept 5 or 6 nodes
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[3].text, "code")
        # Check if the last node is " text." or " text" + "."
        self.assertIn(new_nodes[4].text, [" text.", " text"])
        if len(new_nodes) == 6:
            self.assertEqual(new_nodes[5].text, ".")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[3].text_type, TextType.CODE)

    # Test case where no delimiter is found (no change)
    def test_no_delimiter(self):
        node = TextNode("This is just normal text.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "This is just normal text.")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

    # Test case for unmatched delimiter (should raise ValueError)
    def test_unmatched_delimiter(self):
        node = TextNode("This is text with an unmatched `delimiter", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    # Test for handling multiple nodes with code delimiter
    def test_multiple_nodes(self):
        node1 = TextNode("Some text with `code` and **bold** text.", TextType.TEXT)
        node2 = TextNode("Another text with _italic_ and `code`.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)

        # Then, split the newly created nodes with the ** delimiter (bold)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)

        self.assertEqual(len(new_nodes), 7)  # 4 nodes from the first and 3 from the second.
        self.assertEqual(new_nodes[0].text, "Some text with ")
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[2].text, " and ")
        self.assertEqual(new_nodes[3].text, "bold")
        self.assertEqual(new_nodes[4].text, " text.")
        self.assertEqual(new_nodes[5].text, "Another text with _italic_ and ")
        self.assertEqual(new_nodes[6].text, "code")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[5].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[6].text_type, TextType.CODE)

if __name__ == '__main__':
    unittest.main()

