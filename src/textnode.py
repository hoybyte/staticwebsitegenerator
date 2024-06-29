class TextNode:
    def __init__(self, text, text_type, url=None):
        """

        Initializes a TextNode object with the given properties

        Args:

            text (str): The text content of the node.
            text_type(str): The type of text this node contains (e.g., "bold", or "italic").
            url (str, optional): The URL of the link or image (Default is None).

        """ 

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        """
        
        Compares two TextNode objects for equality.

        Args: other (TextNode): Another TextNode object to compare with.

        Returns:
            bool: True if all properties are equal, False otherwise if they do not match.
        """   

        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def __repr__(self):
        """
        
        Returns a string representation of the TextNode object.

        Returns:
            str: A formatted string representing the TextNode.
        """

        return f"TextNode({self.text!r}, {self.text_type!r}, {self.url!r})"