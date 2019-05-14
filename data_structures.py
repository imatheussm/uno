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
        self.object, self.next = object, next

    def __repr__(self):
        """Object representation"""
        return "<LinkedNode object>\n{:>8}{}\n{:>8}{}".format("Object: ",self.object,"Type: ",type(self.object))


class DoublyLinkedNode(LinkedNode):
    """Node with pointers to previous and next elements."""
    def __init__(self,object,next=None,previous=None):
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
        self.previous=previous

    def __repr__(self):
        """Object representation"""
        return "<DoublyLinkedNode object>\n{:>8}{}\n{:>8}{}".format("Object: ",self.object,"Type: ",type(self.object))


class DoublyLinkedCircularList:
    """A doubly-linked, circular list which uses DoublyLinkedNodes"""
    def __init__(self,*arguments):
        """Class builder.
        
        Parameters
        ----------
        self : DoublyLinkedCircularList
            A DoublyLinkedCircularList object.
        *arguments : any
            Anything to be added into the DoublyLinkedCircularList instance.

        Returns
        -------
        DoublyLinkedCircularList
            A DoublyLinkedCircularList object with the desired elements (if any) already inserted.
        """
        self.reference, self.size = None, 0
        for argument in arguments: self.insert(argument)

    def insert(self,node,index=None):
        """Insert a Node object into the DoublyLinkedCircularList."""
        if index==None: index=self.size
        elif index>self.size: raise IndexError("Index out of range.")

        if not isinstance(node,DoublyLinkedNode): node = DoublyLinkedNode(node)

        if self.size==0: self.reference, node.previous, node.next = 3*[node]
        else:
            previous_pointer, pointer = None, self.reference
            for i in range(index-1): previous_pointer, pointer = pointer, pointer.next
            previous_pointer.next, node.previous, node.next, pointer.previous = node, previous_pointer, pointer, node