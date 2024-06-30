from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        """
        Initializes a ParentNode object with the given properties.

        Args:
            tag (str): A string representing the HTML tag name (required).
            children (list): a list of HTMLNode objects representing the children of this node.
            props (dict): A dictionary of key-value pairs representing the attributes of the HTML tag.
        """
        if tag is None:
            raise ValueError("Tag must be provided for ParentNode")
        if not children:
            raise ValueError("ParentNode must have at least one child.")
        super().__init__(tag=tag, value=None, children=children, props=props)

        def to_html(self):
            """
            Renders the ParentNode and its children as an HTML string

            Returns:
                str: the HTML representation of the ParentNode and its children            
            """
            child_html= "".join(child.to_html() for child in self.children)
            return f"<{self.tag} {self.props_to_html()}>{child_html}</{self.tag}>"
