#!python

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n)
    Memory usage: O(1)
    """
    return all(items[i] <= items[i + 1] for i in range(len(items)-1))

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n**2)
    Memory usage: O(1)
    """
    not_sorted = True
    while(not_sorted):
        not_sorted = False
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                 items[i], items[i+1] = items[i+1], items[i]
                 not_sorted = True
    return items

def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n**2)
    Memory usage: O(1)"""
    for i, item in enumerate(items):
        min_item = float('inf')
        min_index = -1
        j = i
        while j < len(items):
            temp = min_item
            min_item = min(items[j], min_item)
            if min_item != temp:
                min_index = j
            j+=1
        items[i], items[min_index] = items[min_index], items[i]
    return items

# I still don't understand this one fully.
def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n**2)
    Memory usage: O(1)
    """
    # REVIEW THIS ONE.
    for i, item in enumerate(items):
        currentUnsortedItem = item
        j = i
        while(j > 0 and currentUnsortedItem < items[j - 1]):
            items[j] = items[j - 1]
            j-=1
        items[j] = currentUnsortedItem
    return items

print("\nBUBBLE")
items = [4,3,4,2,3,]
print(items)
print(is_sorted(items))
items = bubble_sort(items)
print(is_sorted(items))
print(items)
print("\nSELECTION")
items = [4,3,4,2,3,]
print(items)
print(is_sorted(items))
items = selection_sort(items)
print(is_sorted(items))
print(items)
print("\nINSERTION")
items = [1,3,4,2,5,3]
print(is_sorted(items))
items = insertion_sort(items)
print(is_sorted(items))
print(items)
print()
