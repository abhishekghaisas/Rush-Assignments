# Python Technical Test - Rush Project

This repository contains solutions for the Python Technical Test

## Assignments

### Assignment 1 (`rush-1-1/`)
Draws squares using `o`, `-`, and `|` characters.
- Corners: `o`
- Horizontal borders: `-`
- Vertical borders: `|`

**Example:** `rush(5, 3)`
```
o---o
|   |
o---o
```

### Assignment 2 (`rush-1-2/`)
Draws squares using `/`, `*`, and `\` characters.
- Top-left corner: `/`
- Top-right corner: `\`
- Bottom-left corner: `\`
- Bottom-right corner: `/`
- All borders: `*`

**Example:** `rush(5, 3)`
```
/***\
*   *
\***/
```

### Assignment 3 (`rush-1-3/`)
Draws squares using `A`, `B`, and `C` characters.
- Top corners: `A`
- Bottom corners: `C`
- All borders: `B`

**Example:** `rush(5, 3)`
```
ABBBA
B   B
CBBBC
```

### Assignment 4 (`rush-1-4/`)
Draws squares using `A`, `B`, and `C` characters.
- Left corners: `A`
- Right corners: `C`
- All borders: `B`

**Example:** `rush(5, 3)`
```
ABBBC
B   B
ABBBC
```

### Assignment 5 (`rush-1-5/`)
Draws squares using `A`, `B`, and `C` characters.
- Top-left corner: `A`
- Top-right corner: `C`
- Bottom-left corner: `C`
- Bottom-right corner: `A`
- All borders: `B`

**Example:** `rush(5, 3)`
```
ABBBC
B   B
CBBBA
```

## Repository Structure

```
.
├── README.md
├── rush-1-1/
│   └── rush1-1.py
├── rush-1-2/
│   └── rush1-2.py
├── rush-1-3/
│   └── rush1-3.py
├── rush-1-4/
│   └── rush1-4.py
└── rush-1-5/
    └── rush1-5.py
```

## Usage

Each assignment is contained in its own directory. The `rush()` function can be imported and called with two parameters:
# Example:

```python
from rush1-1 import rush

# Draw a 5x3 square
rush(5, 3)
```

### Function Signature

```python
def rush(x, y):
    """
    x: Width of the square (integer)
    y: Height of the square (integer)
    """
```

### Error Handling

If invalid dimensions are provided (x ≤ 0 or y ≤ 0), the function prints "Invalid size" to standard error and returns.

```python
rush(0, 5)   # Prints "Invalid size" to stderr
rush(-1, 3)  # Prints "Invalid size" to stderr
```

## Technical Requirements

- **Language:** Python
- **Allowed functions:** Only `print()` function is used
- **Output:** Terminal-based, character graphics
- **Error handling:** Invalid sizes print to stderr

## Edge Cases

All implementations handle the following edge cases:
- Single cell (1x1): Prints appropriate single character
- Single row (nx1): Prints horizontal line
- Single column (1xn): Prints vertical line
- Invalid dimensions: Error message to stderr

## Testing

To test any assignment, navigate to its directory and import the function:

```bash
cd rush-1-1
python
>>> from rush1-1 import rush
>>> rush(4, 4)
o--o
|  |
|  |
o--o
```

## Author

Abhishek Ghaisas

## License

This file is submitted as part of a technical assessment.