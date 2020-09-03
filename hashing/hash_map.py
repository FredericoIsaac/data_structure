class Linked_list:
    def __init__(self, key, value):
        # Indentified the student
        self.key = key
        # Value is what you want to keep (height of students)
        self.value = value
        # The pointer
        self.next = None

class HashMap:
    def __init__(self, initial_size = 11): 
        self.bucket_array = [None for _ in range(initial_size)] # Create an array of None's the size of the initial_size
        self.p = 31  # Normaly use prime numbers to unsure all the slots will eventually be visited
        self.num_entries = 0 # Gives the numbers of entries in the array
        self.load_factor = 0.7 # keeping low so that the risk of collision is lower

    def put(self, key, value):
        """
        Ill put a new value in to the array
        """
        # Get the hash code that ill be the index
        bucket_index = self.get_hash_code(key)

        # Create a new node for the new key-value
        new_node = Linked_list(key,value)
        # Pointer to the head of the bucket
        head = self.bucket_array[bucket_index]

        # Check if key is already present in the map, and update its value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        
        # Key not found in the chain, create a new entry and place it in the head of the chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        head = new_node
        # Increment the number of entries
        self.num_entries += 1

        # Check load factor
        current_load_factor = self.num_entries / len(self.bucket_array)
        # if passed, create a larger array
        if current_load_factor > self.load_factor:
            self.num_entries = 0
            self._rehash()

    def _rehash(self):
        # Get the size of the oldest array
        old_num_buckets = len(self.bucket_array)
        # Copy old array
        old_bucket_array = self.bucket_array
        # Calculate the size of the new array
        num_buckets = 2 * old_num_buckets
        # Change old array with the size num_buckets and give None values
        self.bucket_array = [None for _ in range(num_buckets)]

        # Pass through the elements of the oldest array
        for head in old_bucket_array:
            while head is not None:
                # Get the key & value of the older array
                key = head.key
                value = head.value
                # Put again now in the new array the value (rehash)
                self.put(key, value)
                # move forward
                head = head.next


    def get_hash_code(self, key):
        """
        ill give the index
        """
        key = str(key)
        # Get the size of the array
        num_buckets = len(self.bucket_array)
        # An way to reduce collision
        current_coefficient = 1
        
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            # Compress hash_code
            hash_code = hash_code % num_buckets
            # Gives another current coefficient
            current_coefficient *= self.p
            # I dont think you need this but if you want give more randoms - Compress coefficient
            current_coefficient = current_coefficient % num_buckets
            
        # One last compression before returning
        return hash_code % num_buckets

    def get(self, key):
        """
        Ill return the value (height of the students)
        """
        # Get the hash index
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        
        # Iterate over to see if key in the bucket
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        # Not found
        raise ValueError("Not found")

    def size(self):
        """
        Ill give the number of values in the current array
        """
        return self.num_entries

    def delete(self, key):
        """
        Delete entry
        """
        # Find where the key is the array
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        # Create a pointer to get the previous node
        previous = None
        # Iterate over the bucket
        while head is not None:
            if head.key == key:
                # if the key is in the beggining
                if previous == None:
                    # link to the next
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                    self.num_entries -= 1
                    return
            else:
                # Get the previous to the current node
                previous = head
                # pass the current node to the next
                head = head.next


