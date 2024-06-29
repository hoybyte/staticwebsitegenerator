from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        """
        Initializes a LeafNode object with the given properties

        Args:
            tag (str): a String representing the HTML tag name (e.g., "p", "a", "span").
            value (str): a string representing the value of the HTMl tag (required).
            props (dict): a dictionary of key-value pairs representing the attributes of the HTML tag.
        """

        super().__init__(tag=tag, value=value, children=None, props=props)

    
    def to_html(self):
        """
        Renders the LeafNode as an HTML string.

        Returns:
            str: The HTML representation of the LeafNode.        
        """

        if self.value is None:
            raise ValueError("LeafNode value cannot be None.")
        
        if self.tag is None:
            # Return the value as raw text
            return self.value
        
        else:
            # Render an HTML tag with attributes
            attributes = self.props_to_html()
            return f"<{self.tag} {attributes}>{self.value}</{self.tag}>"


