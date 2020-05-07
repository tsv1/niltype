# Nil Type

[![License](https://img.shields.io/github/license/nikitanovosibirsk/niltype.svg)](https://github.com/nikitanovosibirsk/niltype)
[![Codecov](https://img.shields.io/codecov/c/github/nikitanovosibirsk/niltype/master.svg)](https://codecov.io/gh/nikitanovosibirsk/niltype)
[![PyPI](https://img.shields.io/pypi/v/niltype.svg)](https://pypi.python.org/pypi/niltype/)
[![Python Version](https://img.shields.io/pypi/pyversions/niltype.svg)](https://pypi.python.org/pypi/niltype/)

Null value for cases when `None` is part of a data model

```python
from niltype import Nil

if x is Nil: # True only if x is Nil
    pass
```

### Example

```python
from niltype import Nil

def get(dictionary, key, default=Nil):
    try:
        return dictionary[key]
    except KeyError:
        if default is not Nil:
            return default
        raise

get({}, 'key')  # raises KeyError
get({}, 'key', None)  # returns None
```
