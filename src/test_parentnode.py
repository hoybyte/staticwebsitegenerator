import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_valid_parent_with_children(self):
        bold_leaf = LeafNode(tag="b", value="Bold text")
        normal_leaf1 = LeafNode(tag="None", value="Normal text")
        italic_leaf = LeafNode(tag="i", value="Italic text")
        normal_leaf2 = LeafNode(tag=None, value="Normal text")

        parent_node = ParentNode(tag="p", children=[bold_leaf, normal_leaf1, italic_leaf, normal_leaf2])
        expected_html = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(parent_node.to_html(), expected_html)


    def test_invalid_parent_without_tag(self):
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[LeafNode(tag="span", value="Child Text")])


    def test_invalid_parent_without_children(self):
        with self.assertRaises(ValueError):
            ParentNode(tag="div", children=[])


if __name__ == "__main__":
    unittest.main()
