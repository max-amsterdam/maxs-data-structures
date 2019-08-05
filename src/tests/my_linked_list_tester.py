from src.my_linked_list import MyLinkedList

def test():
    print("Starting linked list tests...")
    linkedList = MyLinkedList()

    linkedList.addLast(1)
    linkedList.addLast(2)
    # [1, 2] 
    linkedList.addFirst(3)
    linkedList.addFirst(4)
    # [4, 3, 1, 2]
    linkedList.add(2, "Hello")
    # [4, 3, "Hello", 1, 2]
    linkedList.set(4, "Last")
    # [4, 3, "Hello", 1, "Last"]

    assert linkedList.get(3) == 1 
    assert linkedList.get(2) == "Hello"
    assert linkedList.getFirst() == 4
    assert linkedList.getLast() == "Last" 
    assert len(linkedList) == 5
    assert linkedList.contains("Hello") is True
    assert linkedList.contains("Max") is False 
    assert linkedList.contains(4) is True 
    assert linkedList.contains(5) is False 

    linkedList.remove(3)
    # [4, 3, "Hello", "Last"]
    linkedList.removeFirst()
    # [3, "Hello", "Last"]
    linkedList.removeLast()
    # [3, "Hello"]

    other = MyLinkedList()
    other.addLast(3)
    other.addLast("Hello")

    assert linkedList == other
    assert len(linkedList) == 2

    # TODO check out of bounds stuff
    try:
        other.set(10, "OUT OF BOUNDS")  # This should throw an error
        assert True is False
    except IndexError as e:
        # Passed test
        pass

    print("Linked list tests passed!!")