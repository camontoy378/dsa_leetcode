class Node():

    def __init__(self, data):
        self.data   = data
        self.next   = None

class LRUCache():

    def __init__(self, capacity):
        self.capacity   = capacity
        self.num_items  = 0
        self.new        = None
        self.old        = None

    def delete_found_node(self, pre_search, search):
        if pre_search.next == None:
            self.new        = None
            self.old        = None

        elif pre_search == search:
            self.new = pre_search = search = pre_search.next
        
        elif pre_search.next.next == None:
            self.old        = pre_search
            self.old.next   = None

        else:
            pre_search.next = search.next

        self.num_items -= 1

    def get(self, key):

        found, pre_search, search = self.search(key)
        
        if not found:
            
            return -1
        
        else:
            found_value = search.data[1]
            self.update_cache(pre_search, search)
            return found_value

    def put(self, key, value):

        self.num_items += 1

        #If key in data, update key and reduce self.num_items
        found, pre_search, search = self.search(key)
        
        if found:
            search.data[1] = value
            self.num_items -= 1

            found_key   = search.data[0]
            found_value = search.data[1]

            self.update_cache(pre_search, search)

            return

        #New data
        if self.num_items > self.capacity:
            #Remove node from end
            search = self.new
            
            if search.next == None:
                self.new = None
                self.old = None
            else:
                while search.next != self.old:
                    search = search.next

                search.next = None
                self.old    = search 

            self.num_items = self.capacity

        #If no nodes
        if self.new == None:

            node = Node( [ key, value ] )

            self.new = self.old = node

        else:
            #Insert at head.
            node = Node( [ key, value ] )
            
            node.next   = self.new
            self.new    = node

    def search(self, key):
        #Create search pointer
        search      = self.new
        pre_search  = self.new
        found       = False

        #search for data[0] == key
        while (not found) and (search != None):

            if search.data[0] == key:
                found       = True

            elif pre_search == search:
                search = search.next

            else:
                search      = search.next
                pre_search  = pre_search.next
        
        return found, pre_search, search
    
    def update_cache(self, pre_search, search):

        found_key   = search.data[0]
        found_value = search.data[1]
        
        #Remove found node
        self.delete_found_node(pre_search, search)

        #put node
        self.put(found_key,found_value) 
        

        

