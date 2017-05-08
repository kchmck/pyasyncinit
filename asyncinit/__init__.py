"""
This package provides the `asyncinit` decorator, which enables an asynchronous constructor
to be called like any other asynchronous function.

## Example

```python3
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
"""

import functools
import inspect

def asyncinit(obj):
    """
    Add async `__init__` functionality to the given class.
    """

    if not inspect.isclass(obj):
        raise ValueError("decorated object must be a class")

    if obj.__new__ is object.__new__:
        cls_new = _new
    else:
        cls_new = _force_async(obj.__new__)

    cls_init = _force_async(obj.__init__)

    @functools.wraps(obj.__new__)
    async def new(cls, *args, **kwargs):
        self = await cls_new(cls, *args, **kwargs)
        await cls_init(self, *args, **kwargs)

        return self

    obj.__new__ = new

    return obj

# Force the given function to be `await`-able.
def _force_async(fn):
    if inspect.iscoroutinefunction(fn):
        return fn

    async def wrapped(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapped

# Wraps `object.__new__` in a coroutine, only passing it the class object. This kludge is
# required because that function throws `TypeError: object() takes no parameters` if
# passed any other parameters.
async def _new(cls, *args, **kwargs):
    return object.__new__(cls)

def _test_asyncinit():
    import asyncio

    async def deferredFn(z):
        return z * 4

    @asyncinit
    class TestAsyncInit:
        async def __init__(self, x):
            self.num = x
            self.deferred = await deferredFn(x)

    @asyncinit
    class TestNormalInit:
        def __init__(self, x):
            self.num = x
            self.derived = 4 * x

    async def mainTask():
        test = await TestAsyncInit(3)
        assert test.num == 3
        assert test.deferred == 12

        test = await TestNormalInit(42)
        assert test.num == 42
        assert test.derived == 168

    eventLoop = asyncio.get_event_loop()
    eventLoop.run_until_complete(mainTask())
