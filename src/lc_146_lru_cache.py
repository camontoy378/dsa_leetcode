class Node():

    def __init__(self, data):
        self.data   = data
        self.next   = None
        self.prev   = None

class LRUCache():

    def __init__(self, capacity):
        self.capacity   = capacity
        self.num_items  = 0
        self.new        = None
        self.old        = None
        #key : Address location of node containing key-value data
        self.key_loc    = {}

    def delete_found_node(self, node_loc):

        #One node
        if (node_loc == self.new) and (node_loc == self.old):
            self.new        = None
            self.old        = None

        #First node
        elif node_loc == self.new:
            self.new = node_loc.next
            self.new.prev = None
        
        #Last node
        elif node_loc == self.old:
            self.old = node_loc.prev
            self.old.next = None 

        else:
            node_loc.prev.next = node_loc.next
            node_loc.next.prev = node_loc.prev

        #Remove from hash map
        key = node_loc.data[0]
        self.key_loc.pop(key)

        #Decrease number of items in cache
        self.num_items -= 1

    def get(self, key):

        if key in self.key_loc:
            
            found_value = self.key_loc[key].data[1]
            
            self.update_cache(self.key_loc[key])

            return found_value

        else:
            return -1

    def put(self, key, value):
        
        #Key in cache
        if key in self.key_loc:

            #Update  key
            self.key_loc[key].data[1] = value

            self.update_cache(self.key_loc[key])

            return 


        #New data

        self.num_items += 1

        #Check capacity
        if self.num_items > self.capacity:
            
            #Remove node from end
            self.delete_found_node(self.old)

        
        #If no nodes
        if self.new == None:

            node = Node( [ key, value ] )

            self.new = self.old = node

            self.key_loc[key] = self.new

        else:
            #Insert at head.
            node = Node( [ key, value ] )
            
            node.next       = self.new
            self.new.prev   = node    
            self.new        = node

            self.key_loc[key] = self.new

    
    def update_cache(self, node_loc):

        found_key   = node_loc.data[0]
        found_value = node_loc.data[1]
        
        self.delete_found_node(node_loc)

        #Put node
        self.put(found_key,found_value) 
        

        

