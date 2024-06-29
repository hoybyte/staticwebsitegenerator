import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_with_tag(self):
        leaf = LeafNode(tag="p", value="This is a paragraph.")
        expected_html = "<p>This is a paragraph.</p>"
        self.assertEqual(leaf.to_html(), expected_html)

    def test_leaf_without_tag(self):
        leaf = LeafNode(tag=None, value="Raw text content")
        self.assertEqual(leaf.to_html(), "Raw text content")

    def test_leaf_with_attributes(self):
        leaf = LeafNode(tag="a", value="Click me!", props={"href": "https://www.google.com"})
        expected_html = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(leaf.to_html(), expected_html)

    def test_leaf_with_missing_value(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="span", value=None)

if __name__ == "__main__":
    unittest.main()