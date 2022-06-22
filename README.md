# Sorting-Algorithm-Visualiser | Index Alpha Version 0.0.1

<img width="902" alt="image" src="https://user-images.githubusercontent.com/48067761/173760095-b19680f7-fd24-43aa-a3a4-825822566651.png">

*An informative and visual/audible way to preview the efficiency of a particular sorting algorithm in order to observe how it sorts in real time<sup>1</sup> and to potentially give insight as to where improvements could be made.* 

## How to use
### Setup
Ensure packages matplotlib and numpy are installed using their respective "pip" command.

```shell
pip install package-name
```

Once installed, attempt to run the project with the following command.

```shell
python ./sorting-algorithm-visualiser.py
```

The number of elements and the random range can be set by changing `valueCount` to however many elements are required and the second argument in the `np.linspace(x, y, z)` function.

```python
# Change to have more or less elements to sort
valueCount = 100

# Change 1000 to be anything for a ceiling and 0 for a floor
arr = np.round(np.linspace(0, 1000, valueCount), 0) 
```

If everything runs smoothly, move to the next step.

### Creating a new algorithm
Adding a new or different algorithm is very simple provided the template is followed.

```python
class SomethingSort:
    algorithmName = "Something Sort"

    def somethingSort(self, array):
        [sorting code...]
```

As seen in the template, first a `class` must be created with the class name being preferably the name of the algorithm followed by sort (written in Pascal case), then create a variable called `algorithmName` and assign it the name of the desired algorithm with sort written afterwards, this will be our figure title.

Next, proceed to create any helper functions and also the main driver function that will be called later by using once again the name of the desired algorithm, followed by the suffix "Sort" written in camel case.

### Integrating a new algorithm
This can be done by importing the class into the `sorting-algorithm-visualiser.py` file, assigning the variable `sorter` (at line 101) the value of the desired algorithm's class. Finally, at line 106, replace any current algorithm's main function with the desired one's as such.

```python
...

startTime = time.perf_counter()
sorter.somethingSort(arr) # Here!
endTime = time.perf_counter() - startTime

...
```

To ensure everything works, run the initial command and enjoy seeing any desired algorithm visualised.

### Changing Themes
In order to change themes, simply comment out the undesired theme as such (lines 24-25).
```python
theme = Theme.dark
# theme = Theme.light
```
In this case, light theme is commented out resulting in the application being rendered in a dark theme.

## Features

### Sorting and UI
All algorithms sort and perform within their expected time complexity with no crashes or slowdowns.

The graph updates in real time showing the current index of interest and showing what is happening to the value based on colour coding: green, being for reading and red being for writing.

There is an array access counter to display in realtime an incremental counter on how many arrays are being accessed during sorting and also the time it took before the animation begins to actually sort using the current algorithm.

An algorithm's name, current index and associated value are labeled on each axis to help better get a scale of the data being sorted.

Finally, there are two themes as of now, a light and a dark theme.