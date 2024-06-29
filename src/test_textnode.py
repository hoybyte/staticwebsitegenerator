import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_equality(self):
        # Create two TextNode objects with the same properties
        node1 = TextNode("This is a test", "bold", "https://google.com")
        node2 = TextNode("This is a test", "bold", "https://google.com")

        # Check if they are equal
        self.assertEqual(node1, node2)

    
    def test_repr(self):
        # Create a TextNode object
        node = TextNode("This is a test", "bold", "https://google.com")

        # Check if the repr matches the expected format
        expected_repr = "TextNode('This is a test', 'bold', 'https://google.com')"
        self.assertEqual(repr(node), expected_repr)

    def test_default_url(self):
        # Create a TextNode object without specifying a URL
        node = TextNode("This is a test message", "bold")

        # Check if the default URL is None
        self.assertIsNone(node.url)

    def test_text_type_not_italic(self):
        # Create a TextNode object with different text types
        bold_node = TextNode("bold.text", "bold")
        italic_node = TextNode ("Italic Text", "italic")

        # Check if the text_type is not "italic"
        self.assertNotEqual(bold_node.text_type, "italic")
        self.assertNotEqual(italic_node.text_type, "italic")

        
if __name__ == "__main__":
    unittest.main()