# Kevin Kokomani - Algorithms

# A priority queue using a binary heap. It is a min-heap represented as an array. It supports insert and delete_min.
# test_heap supplied by instructor Dimitri Lisin

# heap is the array containing the heap, currentSize is the current length of the array, and x is the element to be inserted.
# It adds x to the end of the heap array and the re-heapify's it (min heap makes sure parent node is smaller than the children)
def insert(heap, current_size, x):
    heap.append(x)
    while current_size // 2 > 0:
        if heap[current_size] < heap[current_size // 2]:
            z = heap[current_size // 2]
            heap[current_size // 2] = heap[current_size]
            heap[current_size] = z
        current_size = current_size // 2

# This function removes the first element of the heap, replaces it with the last element, and re-heapify's. The function
# returns the element it removed.
def delete_min(heap, current_size):
    min_element = heap[1]
    heap[1] = heap[current_size]
    current_size = current_size - 1
    heap.pop()

    i = 1
    while i * 2 <= current_size:
        if i * 2 + 1 > current_size:
            minimum_child = i * 2
        else:
            if heap[i * 2] < heap[i * 2 + 1]:
                minimum_child = i * 2
            else:
                minimum_child = i * 2 + 1
        if heap[i] > heap[minimum_child]:
            z = heap[i]
            heap[i] = heap[minimum_child]
            heap[minimum_child] = z
        i = minimum_child

    return min_element

# Provided by instructor Dimitri Lisin
def test_heap():
    inputArray = [5, 8, 1, 4, 2, 10, 3, 7, 6, 9]
    n = len(inputArray)
    outputArray = [0] * n
    currentSize = 0
    heap = [0]
    for x in inputArray:
        insert(heap, currentSize, x)
        currentSize += 1

    for i in range(n):
        y = delete_min(heap, currentSize)
        currentSize -= 1
        outputArray[i] = y

    return outputArray

def main():
    print("output:", test_heap())

main()