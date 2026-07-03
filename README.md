# MatOPs — A Pure-Python Matrix Class

A lightweight, dependency-free `Matrix` class implementing common linear algebra operations from scratch, using only nested Python lists.

## Features

- **Construction** — build a matrix by shape (zero-filled) or inject existing data
- **Interactive input** — populate a matrix by typing values at the console
- **Arithmetic operators** — `+`, `-`, `*` (scalar and matrix multiplication), `/` (scalar division), `**` (integer matrix powers)
- **Equality** (`==`) — element-wise comparison
- **Transpose**
- **Determinant** — recursive cofactor expansion
- **Trace**
- **Adjugate**
- **Inverse** — with a singularity check
- Clean, aligned `print()` output via `__str__`

## Requirements

- Python 3.9+ (uses the `list[list[float]]` type hint syntax)
- No external dependencies

## Installation

Just drop `MyMat.py` into your project and import it:

```python
from MatOps import Matrix
```

## Usage

### Creating a matrix

```python
# Empty 2x3 matrix (all zeros)
m = Matrix(2, 3)

# Matrix with predefined data
m = Matrix(2, 3, data=[[1, 2, 3], [4, 5, 6]])

# Or assign data directly
m = Matrix(2, 3)
m.data = [[1, 2, 3], [4, 5, 6]]
```

### Interactive input

```python
m = Matrix(2, 2)
m.set_value()  # prompts for each cell value in the terminal
```

### Printing

```python
print(m)
```

### Arithmetic

```python
a = Matrix(2, 2, data=[[1, 2], [3, 4]])
b = Matrix(2, 2, data=[[5, 6], [7, 8]])

a + b        # element-wise addition
a - b        # element-wise subtraction
a * b        # matrix multiplication
a * 3        # scalar multiplication
a / 2        # scalar division
a ** 2       # matrix raised to an integer power
a == b       # element-wise equality check
```

### Other operations

```python
a.transpose()   # returns the transpose as a new Matrix
a.det()         # determinant (square matrices only)
a.trace()       # sum of the diagonal (square matrices only)
a.adj()         # adjugate matrix (square matrices only)
a.inverse()     # inverse matrix (square, non-singular matrices only)
```

## API Reference

| Method | Description | Returns |
|---|---|---|
| `Matrix(rows, cols, data=None)` | Create a matrix, optionally pre-filled | `Matrix` |
| `set_value()` | Fill the matrix via console input | `None` |
| `__str__()` | Formatted string representation | `str` |
| `__add__(other)` | Element-wise addition | `Matrix` |
| `__sub__(other)` | Element-wise subtraction | `Matrix` |
| `__mul__(other)` | Scalar or matrix multiplication | `Matrix` |
| `__truediv__(other)` | Scalar division | `Matrix` |
| `__eq__(other)` | Element-wise equality | `bool` |
| `__pow__(power)` | Integer matrix exponentiation | `Matrix` |
| `transpose()` | Matrix transpose | `Matrix` |
| `get_cfm(row, col)` | Cofactor (minor) submatrix data, with `row`/`col` removed | `list[list[float]]` |
| `det()` | Determinant via cofactor expansion | `float` |
| `trace()` | Sum of diagonal elements | `float` |
| `adj()` | Adjugate matrix | `Matrix` |
| `inverse()` | Matrix inverse (prints a message and returns `None` if singular) | `Matrix \| None` |

## Notes & Known Limitations

- `det()` uses naive recursive cofactor expansion, so it runs in roughly `O(n!)` time — fine for small matrices, but slow for large ones.
- `__pow__` only supports non-negative integer powers and requires a square matrix.
- `inverse()` checks for a zero determinant, but on a singular matrix it just `print()`s "Matrix is singular" and implicitly returns `None`. Code that doesn't check the return value before using it further will hit an `AttributeError` on the `None` result — raising a `ValueError` instead would be more robust and idiomatic.
- Operations like `+`, `-`, and `*` assume compatible dimensions and raise `ValueError` otherwise.
