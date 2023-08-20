======
Basics 
======

**Python** is made up of *functions* and *variables*. Everything in **Python** is either one or the other. 

Variables
=========

A variable is a stored piece of data. A variable has a *type* that is determined by the form of the data, called the *data type*. 

Every varible must be *assigned* a value in order to be used. A value assignment occurs when you type an expression of the form,

    x = y

The left hand side, *x*, is the *name* of the variable. The right hand side, *y*, is the value of the variable. The equals sign in this instance is the *assignment operator*; it assigns the value of *y* to *x*. 

Strings 
    Data that represents text are called *strings*. A string is enclosed by double quotes "" or single quotes '',

        var = "hello world"

        another_var = 'this is a sentence'

Floats
    Data that represents numerical quantities are called *floats*. A *float* is simply a number, with or without the decimal,

        n = 100

        m = 25.76

Tuples
    Tuples are *ordered pairs* of variables. 

    .. code:: python

        pair = (1, 2)

        another_pair = ("dog", "cat")

    Note the variables in the *tuple* do not have to be numbers.
    
Lists 
    Lists are ordered collections of variables. 
    
        example_list = [ "Led Zeppelin", "Pink Floyd", "The Beatles" ]

    The first element in a list is indexex at 0, the second element at 1, the third element at 2, ... , the n :sup:`th` element at *n-1*. 
    
        example_list[0] # "Led Zeppelin"

        example_list[1] # "Pink Floyd"

        example_list[2] # "The Beatles"

    The variables in a list need not be the same type.

        unlike_list = [ "red", 5.67, "blue", "green" ]

        unlike_list[0] # "red"
        unlike_list[1] # 5.67

Arithmetical Operations
=======================