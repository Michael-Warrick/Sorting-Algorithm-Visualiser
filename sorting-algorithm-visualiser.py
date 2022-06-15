from os import environ
import time

import numpy as np
import scipy as sp

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"

if __name__ == "__main__":
    suppress_qt_warnings()
    
    # Init QT etc...

plt.rcParams['interactive'] == True
plt.rcParams["figure.figsize"] = (12, 8) # Setting default figure size
plt.rcParams["font.size"] = 16

# TO DO: Make a nice dark theme for the program...
# plt.style.use('dark_background')

valueCount = 50
arr = np.round(np.linspace(0, 1000, valueCount), 0) # Rounding to ensure int values only
np.random.seed(0)
np.random.shuffle(arr)

fig, ax = plt.subplots()

ax.bar(np.arange(0, len(arr), 1), arr, align = "edge", width = 0.8)
ax.set(xlabel = "Index", ylabel = "Value", title = "Unsorted Array")
ax.set_xlim([0, valueCount])

currentAlgorithm = ""

def setSortType(sortName):
    global currentAlgorithm
    currentAlgorithm = sortName

##################
### RADIX SORT ###
##################

# Dependent function
def countingSort(array, exponent):
   
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
    for i in range(1,10):
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

    for i in range(0, len(array)):
        arr[i] = output[i]
 
# Main function
def radixSort(array):
 
    # Find the maximum number to know number of digits
    maxElement = max(array)
 
    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exponent = 1

    while int(maxElement / exponent) > 0:
        countingSort(array, exponent)
        exponent *= 10
    
    setSortType("Radix Sort")

######################
### INSERTION SORT ###
######################

def insertionSort(array):
    i = 1

    while (i < len(array)):
        j = i

        while ((j > 0) and (array[j - 1] > array[j])):
            temp = array[j - 1]
            array[j - 1] = array[j]
            array[j] = temp

            j -= 1

        i += 1
    
    setSortType("Insertion Sort")

startTime = time.perf_counter()
radixSort(arr)
endTime = time.perf_counter() - startTime

print(f"Array sorted in {endTime * 1E3:.1f} ms")

fig, ax = plt.subplots()
ax.bar(np.arange(0, len(arr), 1), arr, align = "edge", width = 0.8)
ax.set(xlabel = "Index", ylabel = "Value", title = f"{currentAlgorithm} - Sorted Array")
ax.set_xlim([0, valueCount])

plt.show()