import inspect
import multiprocessing
import os
import traceback
from typing import (
    Any,
    Callable,
    List,
)
from types import TracebackType


# WARNING: Think twice before experimenting with `fork`. The `fork` method does not work well with
# asyncio yet. This might change with Python 3.8 (See https://bugs.python.org/issue22087#msg318140)
MP_CONTEXT = os.environ.get('TRINITY_MP_CONTEXT', 'spawn')


# sets the type of process that multiprocessing will create.
ctx = multiprocessing.get_context(MP_CONTEXT)


class TracebackRecorder:
    """
    Wrap the given instance, delegating all attribute accesses to it but if any method call raises
    an exception it is converted into a ChainedExceptionWithTraceback that uses exception chaining
    in order to retain the traceback that led to the exception in the remote process.
    """

    def __init__(self, obj: Any) -> None:
        self.obj = obj

    def __dir__(self) -> List[str]:
        return dir(self.obj)

    def __getattr__(self, name: str) -> Any:
        attr = getattr(self.obj, name)
        if not inspect.ismethod(attr):
            return attr
        else:
            return record_traceback_on_error(attr)


def record_traceback_on_error(attr: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return attr(*args, **kwargs)
        except Exception as e:
            # This is a bit of a hack based on https://bugs.python.org/issue13831 to record the
            # original traceback (as a string, which is picklable unlike traceback instances) in
            # the exception that will be sent to the remote process.
            raise ChainedExceptionWithTraceback(e, e.__traceback__)

    return wrapper


class RemoteTraceback(Exception):

    def __init__(self, tb: str) -> None:
        self.tb = tb

    def __str__(self) -> str:
        return self.tb


class ChainedExceptionWithTraceback(Exception):

    def __init__(self, exc: Exception, tb: TracebackType) -> None:
        self.tb = (
            '\n"""\n'
            f"{''.join(traceback.format_exception(type(exc), exc, tb))}"
            '"""'
        )
        self.exc = exc

    def __reduce__(self) -> Any:
        return rebuild_exc, (self.exc, self.tb)


def rebuild_exc(exc, tb):  # type: ignore
    exc.__cause__ = RemoteTraceback(tb)
    return exc
