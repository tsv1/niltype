# NilType

**NilType** is a Python package that provides a `Nil` singleton object to represent a null or missing value in situations where `None` is a valid data value and cannot be used to signify the absence of data. This is especially useful in data models or functions where `None` might be a meaningful value, and a distinct placeholder is needed to indicate 'no value' or 'missing data'.

## Installation

Install `niltype` using pip:

```sh
pip3 install niltype
```

## Introduction

In Python, `None` is often used to represent the absence of a value. However, there are cases where `None` is a valid and meaningful value within your data model. In such situations, you need a different sentinel value to represent 'no value' or 'missing data'. This is where `NilType` comes into play by providing a `Nil` object.

## Usage

### Importing Nil

First, import `Nil` from the `niltype` package:

```python
from niltype import Nil
```

### Checking for Nil

You can check if a variable is `Nil` using the `is` operator:

```python
if x is Nil:
    # x is missing or undefined
    pass
```

This check will only be `True` if `x` is exactly `Nil`.

### Example Usage

Here's an example of using `Nil` to provide a default value in a function:

```python
from niltype import Nil

def get(dictionary, key, default=Nil):
    try:
        return dictionary[key]
    except KeyError:
        if default is not Nil:
            return default
        raise

# Example usages:
get({}, 'key')            # Raises KeyError because no default is provided
get({}, 'key', None)      # Returns None
get({}, 'key', 'default') # Returns 'default'
```

In this example, the `get` function behaves similarly to `dict.get()`, but it raises a `KeyError` if the key is not found and no default value is provided. By using `Nil` as the default default value, you can distinguish between when a default has been provided (`None` or any other value) and when it hasn't.

### Nil and Truthiness

The `Nil` object evaluates to `False` in boolean contexts:

```python
if not Nil:
    print("Nil is Falsey")  # This will print
```

### Using Nil in Type Annotations

You can use the `Nilable` type to indicate that a variable can be either a specific type or `Nil`:

```python
from niltype import Nilable

def process(value: Nilable[int]) -> None:
    if value is Nil:
        print("Value is missing")
    else:
        print(f"Value is {value}")

process(10)    # Output: Value is 10
process(Nil)   # Output: Value is missing
```

The `Nilable` type is a type alias that allows for a value of type `_T` or `NilType`, providing better type hints and checks when using type annotations.

## When to Use Nil

Use `Nil` when you need a unique sentinel value to represent missing or undefined data, especially in the following scenarios:

- **Default Parameters**: Distinguish between an explicit `None` and an unspecified parameter.
- **Data Models**: When `None` is a valid value within your data model, and you need to represent the absence of a value.
- **Optional Values**: Clearly indicate optional values without overloading `None`.
