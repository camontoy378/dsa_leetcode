import setup_paths

from lc_146_lru_cache import LRUCache

def test_solve():

    #Test 1

    instructions    = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    parameters      = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    output          = [None, None, None, 1, None, -1, None, -1, 3, 4]

    my_output       = []
    capacity        = parameters[0][0]

    lRUCache = LRUCache(capacity)
    my_output.append(None)

    lRUCache.put(1, 1);     # cache is {1=1}
    my_output.append(None)
    
    lRUCache.put(2, 2);     # cache is {1=1, 2=2}
    my_output.append(None)
    
    result = lRUCache.get(1);        # return 1
    my_output.append(result)

    lRUCache.put(3, 3);     # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    my_output.append(None)

    result = lRUCache.get(2);        # returns -1 (not found)
    my_output.append(result)

    lRUCache.put(4, 4);     # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    my_output.append(None)

    result = lRUCache.get(1);        # return -1 (not found)
    my_output.append(result)

    result = lRUCache.get(3);        # return 3
    my_output.append(result)

    result = lRUCache.get(4);        # return 4
    my_output.append(result)

    assert my_output == output


    #Test 2

    instructions    = ["LRUCache","put","get"]
    parameters      = [[1],[2,1],[2]]
    output          = [None, None, 1]

    my_output       = []
    capacity        = parameters[0][0]

    lRUCache = LRUCache(capacity)
    my_output.append(None)

    lRUCache.put(2, 1);     # cache is {2=1}
    my_output.append(None)

    result = lRUCache.get(2);        # return 1
    my_output.append(result)

    assert my_output == output

    #Test 3

    instructions    = ["LRUCache","put","get","put","get","get"]
    parameters      = [[1],[2,1],[2],[3,2],[2],[3]]
    output          = [None, None, 1, None, -1, 2]

    my_output       = []
    capacity        = parameters[0][0]

    lRUCache = LRUCache(capacity)
    my_output.append(None)

    lRUCache.put(2, 1);     # cache is {2=1}
    my_output.append(None)

    result = lRUCache.get(2);        # return 1
    my_output.append(result)

    lRUCache.put(3, 2);     # cache is {3=2}
    my_output.append(None)

    result = lRUCache.get(2);        # return -1
    my_output.append(result)

    result = lRUCache.get(3);        # return 2
    my_output.append(result)

    assert my_output == output

    #Test 4

    instructions    = ["LRUCache","get","put","get","put","put","get","get"]
    parameters      = [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
    output          = [None,-1,None,-1,None,None,2,6]

    my_output       = []
    capacity        = parameters[0][0]

    lRUCache = LRUCache(capacity)
    my_output.append(None)

    result = lRUCache.get(2);        # return -1
    my_output.append(result)

    lRUCache.put(2, 6);     # cache is {2=6}
    my_output.append(None)

    result = lRUCache.get(1);        # return -1
    my_output.append(result)

    lRUCache.put(1, 5);     # cache is {1=5, 2=6}
    my_output.append(None)

    lRUCache.put(1, 2);     # cache is {1=2, 2=6}
    my_output.append(None)

    result = lRUCache.get(1);        # return 2
    my_output.append(result)

    result = lRUCache.get(2);        # return 6
    my_output.append(result)

    assert my_output == output

    #Test 5

    instructions    = ["LRUCache","put","put","put","put","get","get"]
    parameters      = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
    output          = [None,None,None,None,None,-1,3]

    my_output       = []
    capacity        = parameters[0][0]

    lRUCache = LRUCache(capacity)
    my_output.append(None)

    lRUCache.put(2, 1);     # cache is {2=1}
    my_output.append(None)

    lRUCache.put(1, 1);     # cache is {1=1, 2=1}
    my_output.append(None)

    lRUCache.put(2, 3);     # cache is {2=3, 1=1}
    my_output.append(None)

    lRUCache.put(4, 1);     # cache is {4=1, 2=3}
    my_output.append(None)

    result = lRUCache.get(1);        # return -1
    my_output.append(result)

    result = lRUCache.get(2);        # return 3
    my_output.append(result)

    assert my_output == output