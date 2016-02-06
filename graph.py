# Python Graphing

# Import modules.
import os
import sys
import math

# Declare width and height variables with the console's dimensions. (Mac and Linux only)
width = int(os.popen('tput cols', 'r').readline())
height = int(os.popen('tput lines', 'r').readline())

# Odd Positions. (Ternary Statements)
oWidth = width - 1 if width % 2 == 0 else width
oHeight = height - 1 if height % 2 == 0 else height

# Half Positions (rounded as int[egers]).
hWidth = int(oWidth / 2)
hHeight = int(oHeight / 2)

# Creating horizontal padding and final line.
line_buffer = []
for i in range(hWidth):
    line_buffer += [' ']
line = line_buffer + ['|'] + line_buffer

# Declare list which will contain the lines of the final buffer.
lines_buffer = []

# Fill up window_buffer.
for i in range(oHeight):
    # Make the middle of the buffer list a horiontal line.
    tmpLine = list(line)
    if i is (hHeight + 1): # + 1 to offset up, fix from previous calculations.
        tmpLine2 = []
        for j in range(oWidth):
            tmpLine2 += ['-']
        tmpLine = tmpLine2
    lines_buffer += [tmpLine]

# This list will contain all the results evaluated.
evals = []

# The function that's plugged in.
def myFunc(x):
    return eval(' '.join(sys.argv[1:])) if len(sys.argv) > 0 else '0'

# Defines the range of x values and plug n' chugs them into our function.
for i in range(int(-hWidth), int(hWidth)):
    try:
        evals += [(i, int(myFunc(i)))]
    except ZeroDivisionError: # Ignore errors obtained when dividing by zero.
        ''

# Add eval results to buffer.
for x, y in evals:
    try:
        lines_buffer[y + hHeight + 1][x + hWidth] = '*'
    except IndexError: # Sometimes it'll crash because of non-existing indexes.
        ''

# Flip the graph sequence so it displays properly.
lines_buffer.reverse()

# Render the graph in the Terminal view.
for i in lines_buffer:
    print(''.join(i))
