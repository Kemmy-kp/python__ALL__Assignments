Can one block of except statements handle multiple exception?

try:
    # Some code that might raise an exception
    # ...
except ExceptionType1 as e:
    # Code to handle ExceptionType1
    # ...
except ExceptionType2 as e:
    # Code to handle ExceptionType2
    # ...
-->"try" contains the code that may raise exceptions.
-->Each "except" block is followed by the type of exception
(ExceptionType1, ExceptionType2, etc.) that it should catch.
-->We can place the code to handle exceptions of a particular type in the
indented block following each "except" block.
