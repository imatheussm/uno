from data_structures import *
from random import randint


#################
#   EXECUTION   #
#################


# Some lists are created here.
empty_list      = DoublyLinkedCircularList()                       # len(empty_list)    = 0
empty_list.insert(40)
empty_list.insert(50)
empty_list.insert(60)
empty_list.insert(30,0)
small_list      = DoublyLinkedCircularList(randint(1,100),   # len(small_list)    = 5
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100))
medium_list     = DoublyLinkedCircularList(randint(1,100),   # len(medium_list)   = 10
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100))
big_list        = DoublyLinkedCircularList(randint(1,100),   # len(big_list)      = 15
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100),
                                           randint(1,100))

increasing_list = DoublyLinkedCircularList(1,             # len(increasing_list)  = 5
                                           2,
                                           3,
                                           4,
                                           5)