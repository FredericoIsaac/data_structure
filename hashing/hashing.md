# Hashing

* A good hash function should:
        - Use only the data being hashed
        - Use all of the data being hashed
        - Be deterministic (if we pass the same data hundred times the result is the same)
        - Uniformly distribute data
        - Generate very different hash codes for every similar data

* It's better to find a good hash table in the internet, because its more a art than a science
* Resolving collisions (occurs when two pieces of data, when run through the hash function, yield the same hash code):
    - Linear Probing:
        - In this method, if we have a collision, we try to place the data in the next consecutive element in the array (wrapping around to the beginning if necessary) until we find a vacancy. (hashCode + 1)
    - Chaining:
        - If each element of the array is a pointer to the head of a linked list, then multiple pieces of data can yield tha same hash code and we'll be able to store it all!

* Insertion is a two-step process - hash, then add
* Deletion is easy - once you find the element
* Lookup is on average than with linked lists because you have the benefit of a real-world constant factor
* Not an ideal data structure if sorting is the goal - just use an array
* Can run the gamut of size

### Chaining

Now, the entire time complexity essentialy depends on the linked list traversal. In the worst case, all entries would go to the same bucket index and our linked list at that index would be huge. Therefore, the time complexity in that scenario would be  𝑂(𝑛) . However, hash functions are wisely chosen so that this does not happen.
On average, the distribution of entries is such that if we have n entries and b buckets, then each bucket does not have more than n/b key-value pair entries.

Therefore, because of our choice of hash functions, we can assume that the **time complexity is  𝑂(𝑛𝑏)**. This number which determines the load on our bucket array n/b is known as load factor.

### Load Factor

For example 6 of the 11 slots are now occupied. This is referred to as the load factor, and is commonly denoted by:

    lambda = (number_of_items) / table_size
    lambda = 6/11

Generally, we try to keep our load factor around or less than 0.7. This essentially means that if we have a bucket array of size 10, then the number of key-value pair entries will not be more than 7.

**What happens when we get more entries and the value of our load factor crosses 0.7?**

In that scenario, we must increase the size of our bucket array. Also, we must recalculate the bucket index for each entry in the hash map.

**Note:** the hash code for each key present in the bucket array would still be the same. However, because of the compression function, the bucket index will change.

Therefore, we need to rehash all the entries in our hash map. This is known as **Rehashing.**

# Usefull Links

https://runestone.academy/runestone/books/published/pythonds/SortSearch/Hashing.html
https://cs50.harvard.edu/x/2020/notes/5/
