import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # Test with sample props
        node_props = {"href": "https://www.google.com", "target": "_blank"}
        my_node = HTMLNode(tag="a", value="Click me!", props=node_props)
        expected_html = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(my_node.props_to_html(), expected_html)

        # Test with empy props
        empty_props_node = HTMLNode(tag="div")
        self.assertEqual(empty_props_node.props_to_html(), "")

    def test_repr(self):
        # Test __repr__ method
        node_props = {"class": "my-class", "data-id": "123"}
        my_node = HTMLNode(tag="div", value="Hello, world!", props=node_props)
        expected_repr = "HTMLNode(tag=div, value=Hello, world!, children=[], props={'class': 'my-class', 'data-id': '123'})"
        self.assertEqual(repr(my_node), expected_repr)

    def test_default_values(self):
        # Test default values
        default_node = HTMLNode()
        self.assertIsNone(default_node.tag)
        self.assertIsNone(default_node.value)
        self.assertEqual(default_node.children, [])
        self.assertEqual(default_node.props, {})

if __name__ == "__main__":
    unittest.main()