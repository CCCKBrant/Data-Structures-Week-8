class Contact:
    def __init__(self, name, value):
        self.name = name
        self.number = value
    def __str__(self):
        return f"{self.name}: {self.number}"
    
contact_1 = Contact("Riley", "123-456-7890")
print(contact_1) # Riley: 123-456-7890 
   

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

contact_1 = Contact("Riley", "123-456-7890")
node_1 = Node(contact_1.name, contact_1)
print(node_1.key) # Riley 
print(node_1.value) # Riley: 123-456-7890 
print(node_1.next) # None 

class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size
    def hash_function(self, key):
        total = 0 
        for char in key:
            total += ord(char)
        return total % self.size
    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.data[index]
        if self.data[index] is None:
            self.data[index] = Node(key, value)
            return
        while current:
            if current.key == key:
                current.value = value
                return
            if current.next is None:
                break
            current = current.next
        current.next = Node(key, value)
    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return f"{current.key}: {current.value}"
            current = current.next
        return None
    def print_table(self):
        for i, node in enumerate(self.data):
            print(f"Index {i}:", end="")
            if not node:
                print("Empty")
            else:
                current = node
                while current:
                    print(f"- {current.key}: {current.value}", end="")
                    current = current.next
                print()
        
# Test your hash table implementation here.  
table = HashTable(10)
table.print_table()
'''
Index 0: Empty
Index 1: Empty
Index 2: Empty
Index 3: Empty
Index 4: Empty
Index 5: Empty
Index 6: Empty
Index 7: Empty
Index 8: Empty
Index 9: Empty 
'''
# Add some values
table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
# Print the new table structure 
table.print_table()
'''
Index 0: Empty
Index 1: Empty
Index 2: Empty
Index 3: Empty
Index 4: Empty
Index 5: Empty
Index 6: Empty
Index 7: - Rebecca: 111-555-0002 
Index 8: Empty
Index 9: - John: 909-876-1234 
'''
# Search for a value
contact = table.search("John") 
print("\nSearch result:", contact)  # Search result: John: 909-876-1234 

# Continuation of code from above
# Edge Case #1 - Hash Collisons (assuming these hash to the same index) 
table.insert("Amy", "111-222-3333") 
table.insert("May", "222-333-1111")  # May collide with Amy depending on hash function 
table.print_table()
'''
Index 0: Empty
Index 1: Empty
Index 2: Empty
Index 3: Empty
Index 4: Empty
Index 5: - Amy: 111-222-3333 - May: 222-333-1111 
Index 6: Empty
Index 7: - Rebecca: 111-555-0002 
Index 8: Empty
Index 9: - John: 909-876-1234 
'''
# Edge Case #2 - Duplicate Keys 
table.insert("Rebecca", "999-444-9999")  # Should update Rebecca's number 
table.print_table()
'''
Index 0: Empty
Index 1: Empty
Index 2: Empty
Index 3: Empty
Index 4: Empty
Index 5: - Amy: 111-222-3333 - May: 222-333-1111 
Index 6: Empty
Index 7: - Rebecca: 999-444-9999 
Index 8: Empty
Index 9: - John: 909-876-1234 
'''
# Edge Case #3 - Searching for a value not in the table
print(table.search("Chris")) # None