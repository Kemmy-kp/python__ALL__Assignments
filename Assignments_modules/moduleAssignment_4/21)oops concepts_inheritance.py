What are oops concepts? Is multiple inheritance supported in java.

-->Object-Oriented Programming (OOP) is a programming paradigm based on the
concept of "objects", which can contain data and code: data in the form of
fields (attributes), and code in the form of procedures (methods).The main OOP
concepts are:

1)Class and Object:

A class is a blueprint for creating objects. It defines the attributes
(data members) and methods (functions) that the objects of the class will have.
An object is an instance of a class.

2)Encapsulation:

Encapsulation is the bundling of data (attributes) and methods (functions)
that operate on that data into a single unit or class. It helps in controlling
access to the data.

3)Inheritance:

Inheritance is the mechanism by which one class can inherit the attributes
and methods of another class. It allows for code reuse and the creation of
hierarchies of classes.

4)Polymorphism:

Polymorphism allows objects to be treated as instances of their base class.
This means that a method defined in a base class can be overridden in a
subclass with a specific implementation.

5)Abstraction:

Abstraction involves hiding the implementation details of an object and
exposing only the relevant parts to the user. It focuses on what an object
does rather than how it does it.

-->Java does not support multiple inheritance of classes because it can lead
to problems like the diamond problem (where ambiguity arises when a class
inherits from two or more classes that have a common ancestor).

ex:
interface Interface1 {
    void method1();
}

interface Interface2 {
    void method2();
}

class MyClass implements Interface1, Interface2 {
    public void method1() {
        // ...
    }
    
    public void method2() {
        // ...
    }
}
Abstraction involves hiding the implementation details of an object and exposing only the relevant parts to the user. It focuses on what an object does rather than how it does it.
