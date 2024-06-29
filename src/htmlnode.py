class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        """
        
        Initializes a HTMLNode Object with the given properties

        Args:
            tag (str): A string representing the HTML tag names (e.g. "p", "a", "h1", etc)
            value (str): A string representing the value of the HTML tag (e.g. the text inside a paragraph)
            children (list): a list of HTMLNode objects representing the children of this node
            props (dict): A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com}
        """

        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child classes will override this method to render themselves as HTML.")
    
    
    def props_to_html(self):
        # Create a list of attribute strings
        attribute_strings = []
        for key, value in self.props.items():
            attribute_strings.append(f"{key}=\"{value}\"")

        # Join the attribute strings with spaces
        return " ".join(attribute_strings)
    

    def __repr__(self):
        """

        Returns a string representation of the HTMLNode object

        Returns:
            str: A formatted string representing the HTMLNode object
        """
        return f"HTMLNode({self.tag!r}, {self.value!r}, {self.children!r}, {self.props!r})"