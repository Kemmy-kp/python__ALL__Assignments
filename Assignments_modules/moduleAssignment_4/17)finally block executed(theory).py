#When is the finally block executed?


-->finally block is always executed after leaving the try statement. In case
if some exception was not handled by except block, it is re-raised after
execution of finally block.
-->finally block is used to deallocate the system resources.
-->One can use finally just after try without using except block, but no
exception is handled in that case.

try:
    # Code that might raise an exception
except SomeException:
    # Code to handle the exception
finally:
    # Code that will always be executed, whether an exception occurred or not
