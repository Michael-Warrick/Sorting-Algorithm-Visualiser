class HeapSort:
    algorithmName = "Heap Sort"

    def heapify(self, array, heapSize, index):
        root = index
        left = 2 * index + 1
        right = 2 * index + 2

        # Checks if left child of root exists and if it's greater than root
        if left < heapSize and array[index] < array[left]:
            root = left

        # Checks if right child of root exists and then sees if it's greater than index
        if right < heapSize and array[index] < array[right]:
            root = right

        # Swaps if root needs to be changed
        if root != index:
            array[index], array[root] = array[root], array[index]
            self.heapify(array, heapSize, root)

    def heapSort(self, array):
        size = len(array)

        # Construction of max heap
        for i in range(size//2, -1, -1):
            self.heapify(array, size, i)

        for i in range(size - 1, 0, -1):
            # Swap
            array[i], array[0] = array[0], array[i]

            # Heapify root element
            self.heapify(array, size, 0)
