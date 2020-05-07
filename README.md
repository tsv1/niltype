# Nil Type

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
