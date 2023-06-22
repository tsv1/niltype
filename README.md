# Nil Type

[![Codecov](https://img.shields.io/codecov/c/github/tsv1/niltype/master.svg?style=flat-square)](https://codecov.io/gh/tsv1/niltype)
[![PyPI](https://img.shields.io/pypi/v/niltype.svg?style=flat-square)](https://pypi.python.org/pypi/niltype/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/niltype?style=flat-square)](https://pypi.python.org/pypi/niltype/)
[![Python Version](https://img.shields.io/pypi/pyversions/niltype.svg?style=flat-square)](https://pypi.python.org/pypi/niltype/)

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

### Installation

```sh
pip3 install niltype
```
