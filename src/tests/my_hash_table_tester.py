from src.my_hash_table import MyHashTable

def test():
    print("Starting hash table tests...")

    ht = MyHashTable(10)
    ht.put("Max", 20)
    ht.put("Joe", 43)
    ht.put("Johhny", 234)
    ht.put("Jill", 11)

    
    assert len(ht) == 4 
    assert ht.get("Max") == 20
    assert ht.pop("Joe") == 43
    assert len(ht) == 3
    assert ht.contains(234) 
    assert ht.containsKey("Jill")
    assert not ht.isEmpty() 

    ht.pop("Max")
    ht.pop("Johhny")
    ht.pop("Jill")

    assert ht.isEmpty()

    print("Hash table tests passed!!!")