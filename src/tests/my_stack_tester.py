from src.my_stack import MyStack

def test():
    print("Starting stack tests...")

    s1 = MyStack()
    s2 = MyStack()

    s1.push(1)
    s1.push(2)
    s1.push(3)

    assert str(s1) == "[1, 2, 3]"
    assert repr(s1) == "[1, 2, 3]"

    assert s1.pop() == 3 
    assert s1.pop() == 2 
    assert len(s1) == 1 

    s2.push(1)

    assert s1 == s2
    assert s1.peek() == 1


    print("Stack tests passed!!")