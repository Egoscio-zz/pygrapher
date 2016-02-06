# PyGrapher
<!-- Open this file in a MarkDown viewer to see optimized output -->

## Requirements:
This project requires a Mac or Linux with Python 3 installed.

## Instructions:
To graph an expression, execute graph.py with a string argument containing your desired expression, like so:

```
python3 ./graph.py 'expression, ie: x/2'
```

Your argument must be a python expression, standard web based math syntax is not compatible with this program.

## Supported Functions:
  - abs(), and other python native methods.
  - math.pow(), and all the other static methods of the math module.

## Example Expressions:
  - Numbers: `10`
  - Linear functions: `1 / 4 * x + 5`
  - Absolute value functions `abs(x - 5) + 5`
  - Vertex form: `(x ** 2 - 10) + 5`
  - Intercept form: `(9 - x) * (5 - x)`
  - Rational functions: `25 / x`
  - Trig functions: `math.sin(x) * 2`
