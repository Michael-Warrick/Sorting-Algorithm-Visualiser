class InsertionSort:
    algorithmName = "Insertion Sort"

    def insertionSort(self, array):
        i = 1

        while (i < len(array)):
            j = i

            while ((j > 0) and (array[j - 1] > array[j])):
                temp = array[j - 1]
                array[j - 1] = array[j]
                array[j] = temp

                j -= 1

            i += 1
