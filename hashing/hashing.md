# Hashing




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