import platform
import time

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
from matplotlib.animation import FuncAnimation
from enum import Enum

# Import desired algorithm from file in folder
from algorithms.heapSort import HeapSort
from algorithms.insertionSort import InsertionSort
from algorithms.radixSort import RadixSort
##############################################

os = platform.system()

class Theme(Enum):
    dark = 0
    light = 1

# Set theme by commenting out the undesired theme
theme = Theme.dark
# theme = Theme.light
#################################################

if theme == Theme.dark:
    figColour = "#1A1E23"
    axisColour = "#121619"
    textColour = "dark_background"

if theme == Theme.light:
    figColour = "#ffffff"
    axisColour = "#f6f6f6"
    textColour = "default"

plt.style.use(textColour)
plt.rcParams["interactive"] == True
plt.rcParams["figure.figsize"] = (12, 8) # Setting default figure size
plt.rcParams["font.size"] = 16

# Creates an array of size(valueCount) of elements varying from 0-1000 in random order 
valueCount = 100
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

def selectAlgorithm(name):
    print(f"{name}")

# Select from the imported algorithm, the class name
sorter = InsertionSort()
setSortType(sorter.algorithmName)

# After using the class name, call the main algorithm function.
startTime = time.perf_counter()
sorter.insertionSort(arr)
endTime = time.perf_counter() - startTime

fig, ax = plt.subplots()

container = ax.bar(np.arange(0, len(arr), 1), arr, align = "edge", width = 0.8)
ax.set(xlabel = "Index", ylabel = "Value")
ax.set_xlim([0, valueCount])

plt.get_current_fig_manager().set_window_title(f"Index Alpha Version 0.0.1 - {os} 64-Bit")
plt.title(currentAlgorithm, fontweight = "bold")

ax.set_facecolor(axisColour)
fig.patch.set_facecolor(figColour)

accessCounter = ax.text(valueCount * 0.01, 1000, "", fontsize = 12)
sortTime = ax.text(valueCount * 0.785, 1000, f"Array sorted in {endTime * 1E3:.1f} ms", fontsize = 12)

def update(currentFrame):
    accessCounter.set_text(f"{currentFrame} accesses")

    for (rectangle, height) in zip(container.patches, arr.full_copies[currentFrame]):
        rectangle.set_height(height)
        rectangle.set_color("#1f77b4")

    index, operation = arr.getCurrentActivity(currentFrame)
    if operation == "get":
        container.patches[index - 1].set_color("#50C878") # Green
    elif operation == "set":
        container.patches[index - 1].set_color("#FF2500") # Red

    return (*container, accessCounter)

# Only redraws when something changes (blit) and the full_copies[] array stores
# how many frames are needed.
animation = FuncAnimation(fig, update, frames = range(len(arr.full_copies)), blit = True, interval = 0, repeat = False)
plt.show()