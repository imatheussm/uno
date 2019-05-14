class LinkedNode:
    """Node with a pointer to the next element."""
    def __init__(self,object,next=None):
        """Subclass builder.

        Parameters
        ----------
        object : any
            Object to be incapsulated in a Node.
        next : any
            Pointer to the next Node (optional)
        Returns
        -------
        Node
            A Node object containing the incapsulated object and a pointer to the next Node.
        """
        self.object=object
        self.next=next

    def __repr__(self):
        """Object representation"""
        return "<LinkedNode object>\n{:>8}{}\n{:>8}{}".format("Object: ",self.object,
                                                              "Type: ",type(self.object))


class DoublyLinkedNode(LinkedNode):
    """Node with pointers to previous and next elements."""
    def __init__(self,object,next=None,prev=None):
        """DoublyLinkedNode constructor.

        Parameters
        ----------
        self : DoublyLinkedNode
            A DoublyLinkedNode object.
        object : any
            The object to be incapsulated into a Node.
        next : Node or NoneType (default: None)
            Pointer to the next Node (if any).
        prev : Node or NoneType (default: None)
            Pointer to the previous Node (if any).

        Returns
        -------
        DoublyLinkedNode
            A DoublyLinkedNode object with the desired object incapsulated in it.
        """
        super().__init__(object,next)
        self.prev=prev

    def __repr__(self):
        """Object representation"""
        return "<DoublyLinkedNode object>\n{:>8}{}\n{:>8}{}".format("Object: ",self.object,
                                                                    "Type: ",type(self.object))