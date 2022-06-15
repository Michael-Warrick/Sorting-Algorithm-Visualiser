from enum import Enum
from os import environ
import time

import numpy as np
import scipy as sp

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Theme(Enum):
    dark = 0
    light = 1

theme = Theme.dark
# theme = Theme.light

# Colour theme, [inside color, outside colour]

if theme == Theme.dark:
    figColour = "#1A1E23"
    axisColour = "#121619"
    textColour = "dark_background"

if theme == Theme.light:
    figColour = "#ffffff"
    axisColour = "#ffffff"
    textColour = "default"

plt.style.use(textColour)
plt.rcParams["interactive"] == True
plt.rcParams["figure.figsize"] = (12, 8) # Setting default figure size
plt.rcParams["font.size"] = 16

FPS = 60.0

valueCount = 30
arr = np.round(np.linspace(0, 1000, valueCount), 0) # Rounding to ensure int values only
np.random.seed(0)
np.random.shuffle(arr)

# Transparent Class to record every attribute of the state of the array
class TrackedArray():
    def __init__(self, arr):
        self.arr = np.copy(arr)
        self.reset()
    
    def reset(self):
        self.indices = [] # Checks index being R/W to
        self.values = [] # Checks R/W value at a given index
        self.access_type = [] # Defining access type (get or set)
        self.full_copies = [] # Storing the entire array (better visualisation)

    def track(self, key, access_type):
        self.indices.append(key)
        self.values.append(self.arr[key])
        self.access_type.append(access_type)
        self.full_copies.append(np.copy(self.arr))

    # If an index is passed, function returns a tuple of the accessed index and
    # access type and if no index is passed, function returns a list of tuples of
    # how each element was accessed.
    def getCurrentActivity(self, index = None):
        if isinstance(index, type(None)):
            return [(i, op) for (i, op) in zip(self.indices, self.access_type)]
        else:
            return(self.indices[index], self.access_type[index])


    # Magic functions built into python to set/get element values and returning
    # the array
    def __getitem__(self, key):
        self.track(key, "get")
        return self.arr.__getitem__(key)

    def __setitem__(self, key, value):
        self.arr.__setitem__(key, value)
        self.track(key, "set")

    def __len__(self):
        return self.arr.__len__()


arr = TrackedArray(arr)

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
insertionSort(arr)
endTime = time.perf_counter() - startTime

print(f"{currentAlgorithm}")
print(f"sorted array in {endTime * 1E3:.1f} ms")

fig, ax = plt.subplots()
container = ax.bar(np.arange(0, len(arr), 1), arr, align = "edge", width = 0.8)
ax.set(xlabel = "Index", ylabel = "Value", title = f"{currentAlgorithm}")
ax.set_xlim([0, valueCount])


ax.set_facecolor(axisColour)
fig.patch.set_facecolor(figColour)

def update(currentFrame):

    for (rectangle, height) in zip(container.patches, arr.full_copies[currentFrame]):
        rectangle.set_height(height)
        rectangle.set_color("#1f77b4")

    return (*container,)

# Only redraws when something changes (blit) and the full_copies[] array stores
# how many frames are needed.
animation = FuncAnimation(fig, update, frames = range(len(arr.full_copies)), blit = True, interval = 1000.0/FPS, repeat = False)
plt.show()