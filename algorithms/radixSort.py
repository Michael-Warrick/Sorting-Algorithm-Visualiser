class RadixSort:
    algorithmName = "Radix Sort"

    # Helper function
    def countingSort(self, array, exponent):
    
        n = len(array)
    
        # The output array elements that will have sorted arr
        output = [0] * (n)
    
        # initialize count array as 0
        count = [0] * (10)
    
        # Store occurrences in count[]
        for i in range(0, n):
            index = (array[i] / exponent)
            count[int((index) % 10)] += 1
    
        # Change count[i] so that count[i] now contains true
        # position of digit in output array
        for i in range(1, 10):
            count[i] += count[i - 1]
    
        # Output array creation
        i = n - 1
        while i >= 0:
            index = (array[i] / exponent)
            output[ count[ int((index) % 10) ] - 1] = array[i]
            count[int((index) % 10)] -= 1

            i -= 1
    
        # Copying the output array to arr[],
        # so that arr now contains sorted numbers
        i = 0

        # Originally arr[i]
        for i in range(0, len(array)):
            array[i] = output[i]
    
    # Main function
    def radixSort(self, array):
    
        # Find the maximum number to know number of digits
        maxElement = max(array)
    
        # Do counting sort for every digit. Note that instead
        # of passing digit number, exp is passed. exp is 10^i
        # where i is current digit number
        exponent = 1

        while int(maxElement / exponent) > 0:
            self.countingSort(array, exponent)
            exponent *= 10