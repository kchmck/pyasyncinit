# asyncinit -- Enable async `__init__`

[Documentation](http://kchmck.github.io/pdoc/asyncinit/)

This package provides the `asyncinit` decorator, which enables an asynchronous constructor
to be called like any other asynchronous function.

## Example

```python
from asyncinit import asyncinit

@asyncinit
class MyClass:
    async def __init__(self, param):
        self.val = await self.deferredFn(param)

    async def deferredFn(self, x):
        # ...
        return x + 2

obj = await MyClass(42)
assert obj.val == 44
```

## Installation

This package requires Python >= 3.5.0 and can be installed with `pip`:
```
pip install asyncinit
```
