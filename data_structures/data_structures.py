class Node:
    """Just a Node, fundamental part of many data structures."""
    def __init__(self,object,next=None):
        """Subclass builder.

        Parameters
        ----------
        object : any
            Object to be incapsulated in a Node.
        
        Returns
        -------
        Node
            A Node object containing the incapsulated object.
        """
        self.object = object

    def __eq__(self,other):
        """Object comparison.
        
        Attempts to compare the values of the Nodes and their types to see if they are the same.

        Parameters
        ----------
        self : Node
            A Node (or any of its subclasses)
        other : Node
            A Node (or any of its subclasses)

        Returns
        -------
        bool
            The result of the comparison.
        """
        try: return self.object==other.object and isinstance(self,type(other))
        except: return False

    def __repr__(self):
        """Object representation.

        Parameters
        ----------
        self : Node
            A Node object.

        Returns
        -------
        str
            A string representation of the Node object.
        """
        return "<Node object>\n{:>8}{}\n{:>8}{}".format("Object: ",self.object,"Type: ",type(self.object))


class LinkedNode(Node):
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
        LinkedNode
            A LinkedNode object containing the incapsulated object and a pointer to the next Node (if any).
        """
        super().__init__(object)
        self.next = next

    def __repr__(self):
        """Object representation.

        Parameters
        ----------
        self : LinkedNode
            A LinkedNode object.

        Returns
        -------
        str
            A string representation of the LinkedNode object.
        """
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
            A DoublyLinkedNode object with the desired object incapsulated in it and pointers to the previous and the next Nodes (if any).
        """
        super().__init__(object,next)
        self.previous=previous

    def __repr__(self):
        """Object representation
        
        Parameters
        ----------
        self : DoublyLinkedNode
            A DoublyLinkedNode object.

        Returns
        -------
        str
            A string representation of the DoublyLinkedNode object.
        """
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
        for argument in arguments:
            if type(argument)==list or type(argument)==tuple:
                for item in argument: self.insert(DoublyLinkedNode(item))
            else: self.insert(argument)
    
    def __eq__(self,other):
        """Object comparison.

        Checks if two DoublyLinkedCircularLists are the same.

        Parameters
        ----------
        self : DoublyLinkedCircularList
            A DoublyLinkedCircularList object.
        other : DoublyLinkedCircularList
            A DoublyLinkedCircularList object.

        Returns
        -------
        bool
            The result of the comparison.
        """
        try: 
            if not self.size == other.size and self.reference == other.reference: return False
        except: return False
        self_pointer, other_pointer = self.reference, other.reference
        for i in range(self.size):
            self_pointer, other_pointer = self_pointer.next, other_pointer.next
            if self_pointer != other_pointer: return False
        return True

    def __repr__(self):
        """Object representation.
        
        Parameters
        ----------
        self : DoublyLinkedCircularList
            A DoublyLinkedCircularList object.

        Returns
        -------
        str
            A string representation of the DoublyLinkedCircularList object.
        """
        if self.reference==None: return ""
        pointer, representation = self.reference, "{} ".format(self.reference.object)
        while id(pointer.next)!=id(self.reference):
            pointer = pointer.next
            representation += str(pointer.object) + " "
        return representation[:-1]

    def insert(self,node,index=None):
        """Insert a Node object into the DoublyLinkedCircularList.
        
        Parameters
        ----------
        self : DoublyLinkedCircularList
            A DoublyLinkedCircularList object.
        node : any
            The object to be inserted. If not a DoublyLinkedNode, it will be automatically incapsulated into one.
        index : int (default = self.size)
            The index in which to insert the node parameter in the list. If not provided, will default to self.size. In other words, will be inserted at the end of the list.
        """
        if index==None: index=self.size
        if index>self.size: raise IndexError("Index out of range.")
        if not isinstance(node,DoublyLinkedNode): node = DoublyLinkedNode(node)
        if self.size==0: self.reference, node.previous, node.next = 3*[node]
        elif self.size==1: self.reference.previous, self.reference.next, node.previous, node.next = 2*[node] + 2*[self.reference]
        else:
            previous_pointer, pointer = self.reference.previous, self.reference
            for i in range(index): previous_pointer, pointer = pointer, pointer.next
            previous_pointer.next, node.previous, node.next, pointer.previous = node, previous_pointer, pointer, node
            if index==0: self.reference=node
        self.size+=1

    def remove(self,index=0):
        """Remove a Node from the DoublyLinkedCircularList.

        Parameters
        ----------
        self : DoublyLinkedCircularList
            A DoublyLinkedCircularList object.
        index : int (default = 0)
            Index whose Node is to be removed. If not provided, it will default to 0. In other words, it will remove the first item of the list.
        """
        if index>self.size-1: raise IndexError("Index out of range.")
        elif self.size==1: self.reference=None
        else:
            pointer = self.reference
            for i in range(index): pointer = pointer.next
            pointer.previous.next, pointer.next.previous = pointer.next, pointer.previous
            if index==0: self.reference=self.reference.next
        self.size-=1