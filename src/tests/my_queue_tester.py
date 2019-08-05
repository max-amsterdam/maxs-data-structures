from src.my_queue import MyQueue


def test():
    print("Starting queue tests...")

    q = MyQueue()

    q.enqueue("Max")
    q.enqueue("Joe")
    q.enqueue("Jill")
    q.enqueue("Jack")
    
    assert str(q) == "[Jack, Jill, Joe, Max]"
    assert repr(q) == "[Jack, Jill, Joe, Max]"

    assert len(q) == 4
    assert q.dequeue() == "Max"
    assert q.dequeue() == "Joe"
    while not q.isEmpty():
        q.dequeue()
    assert q.isEmpty()
    assert len(q) == 0

    try:
        q.dequeue()
        raise Exception(
            "Test failed: queue should throw an error when dequeue is called on an empty queue.")
    except IndexError:
        pass

    print("Queue tests passed!!")
