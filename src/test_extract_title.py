import unittest
from src.extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_valid_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")
    
    def test_title_with_spaces(self):
        self.assertEqual(extract_title("#   Trimmed Title   "), "Trimmed Title")
    
    def test_title_among_other_text(self):
        markdown = """
        Some text before
        # Main Title
        Some text after
        """
        self.assertEqual(extract_title(markdown), "Main Title")
    
    def test_no_title_raises_exception(self):
        with self.assertRaises(ValueError):
            extract_title("This has no H1 title.")
    
    def test_multiple_titles(self):
        markdown = """
        # First Title
        ## Subtitle
        # Second Title
        """
        self.assertEqual(extract_title(markdown), "First Title")

if __name__ == "__main__":
    unittest.main()
