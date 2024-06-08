#What happens when „1‟== 1 is executed?

When you execute the expression "1" == 1, you are comparing a string ("1")
with an integer (1). In most programming languages, this will evaluate to false.

Here's a breakdown of what happens:

-->The left side of the comparison ("1") is a string literal, representing the
character "1".
-->The right side of the comparison (1) is an integer literal, representing the
numerical value one. Since the types are different, the language will attempt
to perform a type conversion to make the comparison meaningful. Depending on
the language, there might be implicit type conversions rules.

For example:
    in Python, the comparison "1" == 1 will evaluate to False because Python
    does not perform automatic type conversion in this context. In other words,
    a string and an integer are considered unequal.

-->If you want to compare them as numbers, you would need to explicitly convert
one of them, like this:

ex:
int("1") == 1
