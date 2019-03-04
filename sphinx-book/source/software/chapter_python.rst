.. index::
   double: Python; introduction

Introduction to Python
======================

In this chapter  [1]_, we will examine the basic facilities of the
Python programming language, and go on to the more advanced features in
the next.

.. index::
   double: Python; characteristics

Characteristics of Python
~~~~~~~~~~~~~~~~~~~~~~~~~

Here is a high-level look at the features of Python, for those with a
background in programming languages.

.. index::
   single: scripting

Scripting
'''''''''

Python is a scripting language. This loosely means that you do not have
to compile Python programs; Python can execute them directly. In fact,
you can type lines directly into the Python interpreter and have it
execute them interactively. Python does compile programs into code it
interprets, but it will handle the compilation itself, without troubling
you.

.. index::
   single: nondeclarative

Nondeclarative
''''''''''''''

Python programs consist of executable statements. They don’t have
declarations. In most languages, you declare a function; in Python, you
execute a statement that creates a function object and assigns it to a
variable. In other languages, you call a function by giving its name and
an argument list. The Python call looks exactly the same, but instead of
the name of the function, you specify the name of the variable
containing the function as its value.

.. index::
   single: typeless
   single: dynamically typed
   single: dynamic typing

Typeless or dynamically typed language
''''''''''''''''''''''''''''''''''''''

That means that variables do not have static (declared)types; values
have types. Variables are not declared. A value of any type may be
assigned to any variable.

High-Level
''''''''''

Python is a high-level language. It has high-level data structures built
into the language, such as dictionaries that allow you to associate
values with objects. As of Python2, Python has had a garbage collector.
You allocate objects whenever you need them, but you don’t have to
delete them. When there is no way left for the program to access the
object, when there are no pointers left that point to it, Python
automatically frees its storage. Older versions of Python also
deallocate objects automatically with a reference count scheme, which
will not reclaim storage of circularly linked, inaccessible structures.

Modular
'''''''

Python programs are organized as collections of modules kept in
libraries. Each module is kept in a separate file, and the libraries in
directories. A good programming practice, when writing larger programs,
is to use as many preexisting modules as possible and to divide the code
you do write into general-purpose modules. These modules can be debugged
individually and can be reused in other programs.

Object-Oriented
'''''''''''''''

Python has facilities that allow object-oriented programming. It has
classes and inheritance, as any proper object-oriented programming
language should. But Python is not perfectly object oriented. Python
does not provide private or otherwise restricted scopes for names. The
information-hiding aspects of object-oriented programming are on the
honor system.

With Operator Declarations
''''''''''''''''''''''''''

Python allows you to create functions for the built-in operators, to be
used when the operators are applied to instances of certain classes.
This allows you to implement abstract data types, new types of objects
with their own set of operators. The operators include subscripting
operators, so you can implement new types of objects that behave like
arrays.

With Metaprogramming Facilities
'''''''''''''''''''''''''''''''

What Python calls metaprogramming, other languages refer to as
introspection or reflection. The program itself can examine and modify
its interpreter’s own state and components while it is running. This is
useful for debugging and for changing the running program under program
control.

Executing Programs
~~~~~~~~~~~~~~~~~~

Interactive Use
'''''''''''''''

You can execute Python from the command line in a command window. It
will come up with a greeting and a command prompt (``>>>``).  [2]_

::

   $ python
   Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
   [GCC 7.3.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> 

You type Python statements at the command prompt, and Python executes
them immediately. If you type an expression, Python will evaluate it and
type out the value.

::

   >>> 12+14+20
   46

We will use the command interpreter to try out Python features to show
how they work.

Python statements can extend beyond the end of a line, in which case the
interpreter will give a different prompt (``...``) for the continuation:

::

   >>> (1+2
   ...   )*3
   9

Python can’t always figure out that you wish to continue a statement to
another line. The way you force it to continue to the next line is to
put a backslash, \\, as the last character on a line. This is customary
in Unix-like systems. It incorporates the following character, the
newline, into the current line as white space.

Scripts in Files
''''''''''''''''

You can also place programs in files and execute them from there. For
example, you can edit a file SayHi in the current directory, containing:

.. code:: python

   #!/usr/bin/env python

   print("Hello")

Then set SayHi’s execute permissions and execute it:

::

   chmod a+x SayHi.py

::

   $./SayHi.py
   Hello

You can also run the script *explicitly* with Python:

::

   $ python3 SayHi.py
   Hello

is a comment to the shell, the command interpreter on Linux. It tells
the shell that the way to execute this file is to execute the program in
file ``/usr/bin/python`` , and pass it the rest of the file as its
input. The print statement tells Python to write out the string Hello on
the standard output, which will write it to you. The ``print`` is
required when Python is executing a script in a file. When you are
typing directly to it, Python knows to write out the values of
expressions, but when it is executing scripts, it assumes you do not
want the value of every expression you execute cluttering up your
output, so it will not write out the values of expressions.

Arithmetic Expressions
~~~~~~~~~~~~~~~~~~~~~~

Arithmetic Types
''''''''''''''''

Python has four built-in arithmetic data types:

#. fixed sized (at least 32-bit) signed integers

#. variably sized, unbounded precision signed integers

#. floating point approximations to real numbers

#. complex numbers (with real and imaginary parts) for engineering
   calculations. We will not consider complex numbers further, since
   they are not typically relevant to Web enterprise applications.

Integer literals can be written in decimal, octal, or hexadecimal (base
16) format using the same syntax as in C or C++:

-  Octal integers begin with 0 and contain only octal digits (0-7).
   Strangely, that means zero is written in octal.

-  Decimal integers begin with a decimal digit other than zero and
   contain only decimal digits.

-  Hexadecimal integers begin with 0x or 0X. The prefix is followed by a
   string of hexadecimal digits, 0-9, a-f, A-F. The letters A, B, …F, of
   course, represent the values, 10, 11, …15.

::

   >>> 20
   20
   >>> 020
   020
   >>> 0x20
   16

Long integers are written as an integer followed with an L (in uppercase
or lowercase, but lowercase is too hard to distinguish from the digit
one). The difference between integer and long integer is that integers
are fixed sized. Integer arithmetic will overflow if the results get too
large. Long integers occupy as much storage as they need. Long integer
arithmetic does not overflow.  [3]_ For example, :math:`2^{32}` cannot
be represented in 32 bits. So here is what happens when we try to take
two to the 32nd power, written ``2**32`` in Python:

::

   >>> 2**32
   4294967296

::

   >>> 2L**32
   4294967296L

Since integers occupy single machine words, computers perform integer
arithmetic very fast. Long integer arithmetic typically requires much
more time.

Floating point numbers are written with a decimal point or an exponent,
or both. For example: ``.2``, ``2.0``, ``20.``, ``2000e-1``, ``2E3``.

Python allows mixed-mode arithmetic, as we saw above with ``2L**32``. If
the two operands of an arithmetic operator have different types, Python
will convert them to a common type. Python converts the operand whose
type has the smaller range of values to the type of the operand with the
wider range of values. (This is called a widening coercion: The
“narrower” operand is forced to be the type of the wider.) So, if they
are mixed in expressions, integers will be converted to long integers or
floats, and long integers will be converted to floats. The conversions
to float may lose some low-order digits.

Table TODO is a complete list of Python operators and their precedence
levels. Some of the operators won’t be discussed until later sections;
we’ll refer to the table then. The operators with higher precedence
levels are performed before those with lower precedence.

The arithmetic operators in Python are much the same as those in C or
C++. They are at precedence levels 9 through 12. The bit-wise operators
(ANDs, ORs, shifts) are mostly at levels 5 through 8. Since they are not
used much in Web enterprise applications, we won’t discuss them further.

We will discuss the logical and comparison operators later when we
discuss ``while`` loops.


.. list-table:: Operators and Precedence
   :widths: 15 10 30
   :header-rows: 1

   * - Precedence
     - Operator(s)
     - Comments

   * - 1
     - ``x or y``
     - This is the logical OR operation. It will return true if either ``x`` or ``y`` is true, i.e. non-zero. Like the ``||`` operator in C, it is short-circuited: It will not evaluate ``y`` if ``x`` determines the value of the expression. It first evaluates ``x`` and returns the value of ``x`` if ``x`` is not zero. If ``x`` is zero, it evaluates and returns the value of ``y``. By “x is zero” we mean that it would be considered zero in an ``if`` or ``while`` expression.  Other values than a number zero also count as zero.

   * - 2 
     - ``x and y``
     - This is the logical AND operation. It will return true if both ``x`` and ``y`` are true, i.e. non-zero. Like the ``&&`` operator in C, it is short-circuited: It will not evaluate ``y`` if ``x`` determines the value of the expression. It first evaluates x and returns ``x`` if ``x`` is zero. If ``x`` is not zero, it evaluates and returns the value of ``y``. By “x is zero” we mean that it would be considered zero in an ``if`` or ``while`` expression. Other values than a number zero also count as zero.

   * - 3 
     - ``not x`` 
     - This is the logical NOT operator. It returns 1 if ``x`` is zero; it returns 0 if ``x`` is anything else.  * - 4 & ``x < y``, ``x > y``, ``x <= y``, and ``x >= y`` & The relational operators are much like they are in other languages. Operators ``!=`` and ``<>`` both mean not equal.

   * - 
     - ``x == y``, ``x != y``, ``x <> y`` 
     -  Testing for equality, ``==`` and ``!=``, can be applied to structured objects as discussed later.  They attempt to find out if the structured objects have equal components.

   * - 
     - ``x is y``, ``x is not y``, ``x in y``, ``x not in y`` 
     -  Operators ``x is y`` and ``x is not y`` test whether two names reference the same object, so they will be much faster than ``==`` and ``!=`` for structured objects, but they don’t perform the same test. We will discuss ``x in y`` and ``x not in y`` later, when we discuss sequence types.

   * - 5 
     -  ``x | y`` 
     - This is the bitwise OR operation, ORing the XORing the corresponding bits in two integers.

   * - 7 
     - ``x & y``
     - This is the bitwise AND operation, ANDing the corresponding bits in two integers.

   * - 8 
     - ``x << y``, ``x >> y`` 
     -  These are the shift operators. They apply to integers or long integers. The bits in ``x`` are shifted left ( ``<<`` ) or right ( ``>>`` ) the number of positions indicated by ``y``. The right shifts are arithmetic: The sign bit will be shifted in at the top, preserving the sign of the ``x`` operand.  * - 9 & ``x + y``, ``x - y`` & Addition and subtraction. Operator ``+`` also performs concatenation on sequences, as we will see later.

   * - 10 
     - ``x * y``, ``x / y``, ``x % y`` -
     - Multiplication, division, and modulus (or remainder). Operator ``%`` will also work with floating point numbers. Operator ``*`` also applies to sequence types, and operator ``%`` has a special function for strings. We will look at these other uses later.

   * - 11 
     - ``-y``,  ``y``, ``+y`` 
     - Negation, bitwise complement, and unary plus (no operation for numbers).

   * - 12 
     - ``x ** y``
     -  Exponentiation, :math:`x^y`

   * - 13
     - ``f(...)``
     - Function call

   * -
     - ``x.attr``
     - attribute access

   * -
     - ``x[i]``
     - subscripting

   * - 
     - ``x[i:j]``
     - slicing

   * - 14
     - ``(...)``
     - construct tuple

   * - 
     - ``[...]``
     - construct list

   * -
     - ``{...}``
     - construct dictionary

   * - 
     - :literal:`\`...\`` 
     - construct string

Built-in Arithmetic Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python has a number of built-in functions you can call. Other
mathematical functions can be found in module ``math``. Complex
arithmetic functions are in module ``cmath``.

.. list-table:: Mathematical Functions
   :widths: 15 45
   :header-rows: 1

   * - Function
     - Explanation

   * - ``v = abs(x)``
     - the absolute value of ``x``

   * - ``v = cmp(x, y)``
     - ompares ``x`` and ``y`` and assigns ``v`` a negative value if ``x<y`` , zero if ``x==y`` , and positive if ``x>y``

   * - ``u,v = coerce(x, y)``
     - Determines the common type for ``x`` and ``y`` required for arithmetic operators then assigns ``x`` converted to that type to ``u`` and ``y`` converted to that type to ``v``

   * - ``u,v = divmod(x,y)``
     - are integers or long integers, it assigns ``u=x/y`` and ``v=x%y``. If ``x`` and ``y`` are floating point numbers, it assigns , the largest integer less than or equal to ``x/y,``

   * - ``v=float(x)``
     - the value of ``x`` converted to a floating point value

   * - ``v=int(x)``
     - the value of ``x`` converted to an integer value

   * - ``v=long(x)``
     - the value of ``x`` converted to a long integer value

   * - ``v=complex(x)`` and ``v=complex(x,y)``
     - Converts ``x`` to a complex number, or ``x`` to the real part and ``y`` to the imaginary part of a complex number

   * - ``v=max(x1, x2,...)``
     - Assigns ``v`` with the largest value of x1, x2,...

   * - ``v=min(x1, x2,...)``
     - Assigns ``v`` with the smallest value of x1, x2,...

   * - ``v=pow(x,y)``
     - Assigns v the value of ``x`` raised to the ``y`` power, ``x**y``

   * - ``v=pow(x, y, z)``
     - Assigns v the value of ``x`` raised to the ``y`` power modulus ``z`` , i.e., ``x**y%z``

   * - ``v=round(x)``
     - Assigns v the the floating point number ``x`` rounded to have ``n`` digits after the decimal point. If you omit ``y``, it defaults to zero.

Assignments and Variables
~~~~~~~~~~~~~~~~~~~~~~~~~

Variables are not declared. You create a variable simply by assigning a
value to it. The simplest form of an assignment is:

::

   variable = expression

For example

::

   >>> a=10
   >>> a
   10
   >>> b=a+2
   >>> b
   12

Variable names and other identifiers in Python are composed of letters,
digits, and underscore characters. The first character of the identifier
must not be a digit. The letters are the ISO-Latin characters A-Z and
a-z.  [4]_

You can also do several assignments on the same line; for example let’s
swap the values of ``a`` and ``b`` :

::

   >>> a,b
   (10, 12)
   >>> a,b = b,a
   >>> a,b
   (12, 10)

We will look at this again later. Note also that we can list more than
one expression on a line in interactive mode and Python will write out
all their values. Both the multiple assignments and the multiple values
on a line use tuples, a kind of sequence which we will discuss in
`Tuples <chap2.html#92836>`__.

Creating Functions
~~~~~~~~~~~~~~~~~~

You may create a function and assign it to a variable with the ``def``
statement, for example:

::

   >>> def diff(x,y):
   ...    return abs(x-y)
   ...
   >>> diff(-10.5)
   15

creates a function ``diff`` that returns the absolute difference between
values ``x`` and ``y``. There are several things to note about this
function creation:

#. The ``def`` line introduces the code for the function. It gives the
   name we will call the function, ``diff`` , and the argument list. The
   function will be called with two arguments, ``x`` and ``y``. The
   ``def`` line is terminated with a colon.

#. The name ``diff`` is not exactly the name of the function. It is a
   variable that is assigned the function as a value. It is an
   assignment as much as assigning ``diff=value`` would be, and indeed,
   ``diff`` can be reassigned.

#. The body of the function is indented. All statements in the same
   group of statements must be indented the same amount. Soon we’ll look
   at ``while`` statements, whose bodies must be indented beneath the
   ``while``.

#. The function returns a value with a ``return`` statement.

#. If there is no ``return`` statement, the function does not return a
   value, and the call of the function should be used only as a
   statement, not within an expression.

#. A function is called by the form ``f(args)`` where ``f`` is a
   variable containing the function and ``args`` are the arguments being
   passed in.

When you use a variable name in a function, Python will look in three
places to try to find what it means:

#. The function’s local variables. The arguments are already placed
   there; other variables assigned values in the function are also
   placed there.

#. The module variables. These are the variables assigned values in the
   interactive session or in the file that Python is executing.

#. The built-in names in the Python system. For example, the function
   ``abs()`` is a built-in name in Python.

The scopes  [5]_ are pictured in `See Scopes for Names Known in a
Function. <chap2.html#83458>`__. The search for a name starts in the
innermost scope and proceeds outward until the name is found or until
there are no more scopes. To find the name referenced in a function, at
most three scopes will be searched. When a variable is assigned a value
in a function, its name will be placed in the local scope if it is not
already there. For example, in `See Scopes for Names Known in a
Function. <chap2.html#83458>`__, if the function looks up the value of
``x`` , it will get 1, the value of variable ``x`` in the function
itself. The variable ``x`` with a value 2 is in the global scope and is
hidden by the local ``x``. If the function tries to look up ``y`` , it
won’t find it in the local scope, but will find it in the module scope
with a value 3.

Modules
~~~~~~~

As we discussed in `Scripts in Files <chap2.html#30113>`__, you can put
Python programs in files and execute them. However, the primary reason
to put Python programs in files is to allow other Python programs to
import and use the functions. A Python program that is used by other
Python programs is called a *module*.

The way you access a module is by the ``import`` statement:

::

   import moduleName

The ``import`` statement sees if the module has already been imported.
If it hasn’t been imported yet, Python finds the file that contains the
module. It will have the name ``moduleName.py``, and will be found in
one directory in a list of directories (path). Python’s built-in library
of modules is on the path, so you can use all the modules in Python’s
library without difficulty.

Whether or not the module gets loaded, the ``import`` statement assigns
a module object to a variable in the local scope that has the same name
as the module, i.e., it behaves the same way as an assignment statement.
So

::

   import moduleName

behaves like

::

   moduleName = moduleObject

When Python loads a module, Python reads in the module’s file executing
the commands. The commands assign values to variables within the
module’s namespace that it puts the names in. These are available in the
module object, so you can access the names defined in the module by the
expression

::

   moduleName.variable

For example, the module ``string`` has a built-in function ``atof()`` to
convert strings to floating point numbers. It also has a string variable
``hexdigits`` that contains all the hexadecimal digits. So,

::

   >>> import string
   >>> string.atof
   built-in function
   >>> string.atof("314e-2")
   3.14
   >>> string.hexdigits
   '0123456789abcdefABCDEF'

If you wanted to refer to the function by its own name directly, rather
than prefixed by the module name, you could assign it to a local
variable with the same name

::

   >>> atof=string.atof
   >>> atof(``314e-2'')
   3.14

or you could just import the names you want from the module:

::

   >>> from string import atof, hexdigits
   >>> hexdigits
   `0123456789abcdefABCDEF'

If you are using an interactive session to debug modules, you will have
to reload the module after every change. You reload a module using the
built-in ``reload()`` function:

::

   >>> reload(moduleObject)

This will look up, load, and initialize the module. The new definitions
of variables within the module will override the previous definitions.
The module object will be changed in place, so all parts of the program
that have variables pointing to that module (i.e., all that have
imported it) will see the new definitions when referencing its
attributes through the module name, ``moduleName.variable``.

However, there are problems that may force you to start a new
interactive session. If you use the ``from-import`` statement,

::

   from moduleName import name

will have been done when the ``from-import`` statement was executed and
``name`` will have the value of ``moduleName.name`` at that time. It
won’t automatically be updated. After reloading ``moduleName`` , you
will have to execute the ``from-import`` again to have the new value of
the attribute assigned to ``name``. If names from module ``A`` are
imported into module ``B`` and you change module ``A`` , you will need
to reload module ``A`` to get the new definitions and then reload module
``B`` to assign the new definitions to local names. This can quickly get
confusing.

Python2 provides the ability to import modules and assign them to
variables with different names (i.e., not the name of the module), or
import functions, classes, and variables from modules assigning them to
local variables with different names. The syntax is

::

   import module as name
   from module import name1 as name2

Files
~~~~~

As with all programming languages, Python allows you to read and write
files. Python uses file objects for the operations. You create a file
object by calling the built-in function ``open()``

::

   f = open(name, mode)

where the ``name`` string gives a path to the file and the ``mode``
string indicates whether the file is to be read from or to be written.
The ``mode`` is a string. Here’s a list of the modes:

-  ``'r'``: Open for reading. This is the default.

-  ``'w'``: Open for writing. This will replace a current file with the
   same name.

-  ``'a'``: Open for appending. Data will be added to the end of a
   currently existing file.

-  ``'r+'``: Open for both reading and writing.

You may omit the ``mode`` parameter if you are opening the file for
reading.

File objects have methods for reading and writing and other operations.
A method is a function attached to the object. The method has a syntax
that differs a bit from regular functions. The object the method
operates on precedes the function call, separated by a dot:

::

   object.function(args)

This syntax has a couple of virtues:

-  It makes clear which object the method is operating on. Otherwise,
   the object would have to be one of the arguments, and you couldn’t be
   sure which.

-  It allows different kinds of objects to have methods with the same
   name; the system can find the correct one for the object. Many
   objects have similar operations. It would be a pain to have to invent
   different names for those operations, or to have to keep changing a
   single function to test what kind of object it has been given and
   execute some specific code for it.

There are three methods you especially need to know for files:

#. Reads the next line from a text file and returns it in a string. The
   string ends with the line termination character or characters, on
   Linux the newline character ``‘\n’``. Empty lines thus consist of a
   single newline character. On end of file, ``readline()`` returns an
   empty string, ``”``.

#. Writes a string to the file. The ``string`` is not made into a line,
   i.e., the newline character is not appended. If you want it, you will
   have to write it yourself.

#. Finishes processing the file, either reading or writing it. All
   system resources the file was using are freed up. No further methods
   can be called for the file.

We will present a complete list of the file operations in
` <chap4.html#22958>`__ of Chapter 4.

print Statement
~~~~~~~~~~~~~~~

The print statement  [6]_ writes to the standard output. You can find
the standard output file object in the ``sys`` module, ``sys.stdout``

::

   print(e1, e2,...)
   print(e1, e2,...,)
   print(e1, e2,..., sep=separator_text)

The expressions are evaluated and converted into strings and written out
with a blank between each pair. If the print statement does not end with
a comma, the output line is terminated after the last expression is
written (a newline character is written). If it does end in a comma, the
line is not terminated, so the next print will continue to fill in the
line.

The expressions are optional. You use a print with no expressions to
write out a newline.

Python 2 allowed printing to a file. This has been subsumed by writing
to a file. We recommend using the ``write()`` method on file objects to
achive this.

while loops
~~~~~~~~~~~

.. _while-statement:

while
'''''

The form of the ``while`` loop is

::

   while expression :
    indented body

The ``expression`` is evaluated to get a truth value. Python considers
zero to be false and any non-zero value to be true. It considers empty
strings (and other sequences) to be false, nonempty ones, true. If the
expression evaluates to true, the body of the loop is executed once and
the loop is restarted. As soon as the expression evaluates false, Python
stops evaluating the loop and goes on to the statement following it.

The statements in the body of the loop must be indented a uniform amount
of space beneath the ``while`` statement proper. Of course, if any of
the contained statements are ``while`` statements, their bodies must be
indented further.

Example: listfile
'''''''''''''''''

Here is an example of the use of a ``while`` statement in listing a text
file. If you want to follow along, you will need the Python interpreter
to be executing in the same directory as your code files. You can get
Python to your directory by

::

   >>> import os
   >>> os.chdir("directory")

in module ``os`` changes the current working directory. Now, suppose the
following code is in a file ``listfile.py`` :

::

   def listfile(name):
     f=open(name)
     L=f.readline()
     while L:
       print(L,)
       L=f.readline()
     f.close()

We can import it and use it to list itself:

::



   def listfile(name):
     from listfile import listfile
     listfile("listfile.py")
     f=open(name)
     L=f.readline()
     while L :
       print(L,)
     L=f.readline()
     f.close()

The code should be pretty obvious except for two points.

#. ``while L:`` Python considers an empty string to be false and a
   nonempty string to be true. That makes this loop easy, since
   end-of-file results in ``readline()`` returning an empty string. In
   general, structured objects can sometimes be considered equivalent to
   zero for logical tests. We’ll try to point out these cases as we
   discuss them. Here, while we are discussing logical operators, we
   will just say zero and non-zero, or false and true, and not keep
   repeating that some things other than the number zero are also
   considered to be false.

#. ``print(L,)`` The final comma prevents Python from inserting a
   newline following the string that has been written. Since the lines
   returned by ``readline()`` all are terminated by newlines anyway,
   they come out single-spaced. If the comma weren’t there, the lines
   would come out double-spaced.

Relational Expressions
''''''''''''''''''''''

Theh expressions in ``while`` statements most commonly use relational
operators to compare operands. The result of a relational operation is
Boolean: True or False.

::

   >>> 1 < 2
   True
   >>> 1 > 2
   False

Unlike most other languages, Python allows relational operators to be
cascaded:

::

   >>> -2 < -1 < 0
   True
   >>> (-2 < -1) < 0
   False

The first of the two expressions is equivalent to
``-2 < -1 and -1 < 0``. Python duplicates the value between the two
operators and does both comparisons separately. In the second
expression, ``(-2 < -1)`` yields ``True`` , then ``True<0`` yields
``False``.

If you find any of this confusing, just remember that True and False can
be converted as neeeded to 1 and 0, respectively. You can use these
values almost anywhere an integer is expected. Try this:

::

   >>> False + False
   0
   >>> False + True
   1
   >>> True + True
   2
   >>> True - False
   1
   >>> True - True
   0

Logical Expressions
'''''''''''''''''''

Python provides the usual three logical operators, ``or``, ``and``, and
``not``, at the low precedence levels, 1, 2, and 3. See
tabletab:logical-operators.

#. ``x or y``–The lowest precedence Python operator is ``or``. The
   expression ``x or y`` is short-circuited: It will not evaluate ``y``
   if ``x`` determines the value of the expression. It first evaluates
   ``x`` and returns the value of ``x`` if ``x`` is not considered
   false. If ``x`` counts as false,\ `2 <#pgfId-123468>`__ it evaluates
   and returns the value of ``y``. So the true value it may return is
   either the value of ``x`` or the value of ``y``.

#. ``x and y``–The ``and`` operator, like ``or`` , is short-circuited:
   It will not evaluate ``y`` if ``x`` determines the value of the
   expression. It first evaluates ``x`` and returns ``x`` if ``x``
   counts as false. If ``x`` is true, it evaluates and returns the value
   of ``y``. That has the effect of returning zero if either ``x`` or
   ``y`` is zero. If neither ``x`` nor ``y`` is zero, it returns the
   value of ``y`` to represent true.

#. ``not x``–The ``not`` operator, at precedence level 3, although a
   unary operator, has a much lower precedence than the other unary
   operators at precedence 12. In fact, it is a lot more useful at a low
   precedence level. If it had a high precedence level, we would usually
   have to put parentheses around its operand. It returns 1 if ``x`` is
   zero; it returns 0 if ``x`` is anything else.

Lists
~~~~~

Lists in Python are like arrays in other languages. Actually, they are
flex arrays, arrays whose size can change during program execution.

Lists can be created with a display. Just list the values between
opening and closing brackets:

:math:`\lbrack e_0, e_1, \ldots, e_{n-1} \rbrack`

A list of length ``n`` is created. The expressions :math:`e_0`,
:math:`e_1`, …\ :math:`e_{n-1}` are evaluated and their values placed in
the list.

In addition, Python (2 and beyond) has a moresophisticated form of
display, the list comprehension. We will discuss it later, after we’ve
discussed the ``for`` and ``if`` statements it is based on.

Like arrays, lists can be subscripted by following the list’s name with
the index of the item in brackets, thus

::

   python3
   Python 3.7.0 (default, Jun 28 2018, 13:15:42) 
   [GCC 7.2.0] :: Anaconda, Inc. on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> L=["a", "b", "c"]
   >>> L[1]
   'b'
   >>> L[0]
   'a'
   >>> L[2]
   'c'
   >>> L[3]
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   IndexError: list index out of range
   >>> 

The positions in the list are numbered from zero, left to right. You can
also assign to positions in a list

::

   >>> L[1] = 1
   >>> L
   ['a', 1, 'c']

Notice that the items in a list do not need to be of the same data type.
Python lists, like variables, are typeless. Also notice that Python is
able to write out an entire list when you ask for it, certainly more
convenient than the arrays in some languages that you have to write out
in a loop.

You can check the length of a list with the ``len()`` function:

::

   >>> len(L)
   3

Often you will need a list with successive integers in it. Python has a
built-in function, ``range()`` , to give that to you.

::

   >>> range(10)
   range(0, 10)
   >>> list(range(10))
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   >>> range(-10, 0)
   range(-10, 0)
   >>> list(range(-10,0))
   [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

Calling ``range(i, j)`` gives you an iterator of integers from ``i`` up
to, but not including, ``j``. Call ``range(n)`` is the same as
``range(0,n)``. Why “up to, but not including”? It is compatible with
the indexing of lists, where a list of length n has indices 0 through
n-1.

Beginning with Python 3, ``range(i, j)`` is not evaluated until
necessary. To get a list of values, you need to use the ``list()`` to
demand the values from the iterator.

You can also create a list of values some step size apart, not just
sequential, by specifying the step size as the third argument to
``range()`` :

::

   >>> list(range(0, 10, 2))
   [0, 2, 4, 6, 8]

If you are using lists as arrays, you obviously have to be able to
create a list of some length. The length you need may be computed as the
program runs, so you obviously can’t always use a list display. How do
you create a list of length n?

You use the replication operator, ``*``. Of course, this is the same as
the multiplication operator. If one operand of the ``*`` operator is a
list, L, and the other is a number, ``n`` , then ``L*n`` concatenates
``n`` copies of ``L`` together.

::

   >>> L
   ['a', 1, 'c']
   >>> L*3
   ['a', 1, 'c', 'a', 1, 'c', 'a', 1, 'c']
   >>> 2*L
   ['a', 1, 'c', 'a', 1, 'c']

A way to allocate an array of length 10 is

::

   >>> ary=[0]*10
   >>> ary
   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

You can concatenate two lists by using the ``+`` operator:

::

   >>> L+["d","e"]
   ['a', 1, 'c', 'd', 'e']

You can compare two lists for identity or for equality. The ``is``
operator compares two objects to see if they are identical, i.e., really
the same object. The ``==`` operator compares objects for equality. Two
lists are considered equal if their contents are equal. The equality
test can be a lot slower than the identity test.

::

   >>> [1,2] is [1,2]
   False

These two displays create separate lists, so ``is`` returns false, but
the two lists are equal:

::

   >>> [1,2] == [1,2]
   True

Other relational operators work on lists as well. They operate
lexicographically. The comparison works left to right through the lists,
comparing the elements at the same positions, until it finds elements
that are unequal, whereupon it uses the relationship of those elements
as the relationship of the lists, for example

::

   >>> [1,2,3] < [1,4,3]
   True

   >>> [1,2,3] < [1,0,3]
   False    

There are two special operators to test for list membership: ``x in y``
reports true if ``x`` is in the list ``y`` and false otherwise;
``x not in y`` reports just the opposite.

::

   >>> 2 in [1,2,3]
   True
   >>> 2 not in [1,2,3]
   False  

You can get a copy of a part of a list using slicing. Slicing is like
subscripting, but it specifies a range of indices.

``r=range(10)``

::

   >>> r = range(10)
   >>> list(r)
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   >>> r = list(r)
   >>> r[3]
   3
   >>> r[3:4]
   [3]
   >>> r[3:6]
   [3, 4, 5]
   >>> r[3:1]
   []

Notice a few things:

-  Subscripting, ``r[3]``, returns the object that is at that position.

-  Slicing, e.g., ``r[3:4]``, returns a list.

-  The slice extends from thestarting index up to,
   ``but not including``, the ending index.

-  If the ending index of a slice is less than or equal to the starting
   index, slicing returns the empty list.

You can use negative indices to indicate positions from the end of the
list:

::

   >>> r = list(range(10))
   >>> r[-1]
   9
   >>> r[-10]
   0
   >>> r[-3:-1]
   [7, 8]  

If you leave out the start or the end positions when specifying a slice,
they default to the beginning or the end of the list:

::

   >>> r[:5]
   [0, 1, 2, 3, 4]
   >>> r[5:]
   [5, 6, 7, 8, 9]
   >>> r[:]
   [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    

The ``r[:]`` may seem pointless, but it is a way to make a copy of a
list. This can also be achieved with ``list(r)``.

Consider the following.

::

   >>> r = list(range(10))
   >>> s = r[:]
   >>> s == r
   True
   >>> s is r
   False
   >>> t = list(r)
   >>> t == r
   True
   >>> t is r
   False  

In this example, we use the two different ways of copying list ``r`` as
``s`` and ``t``. Observe that in both cases, the resulting ``copy``
compares equal but is clearly a different list object.

You can assign to a slice of a list by specifying the slice on the left-
hand side of an assignment and a list on the right-hand side.

::

   >>> L
   ['a', 'c']
   >>> L[1:1]=['b']
   >>> L
   ['a', 'b', 'c']
   >>> L[0:2]=L[1:3]
   >>> L
   ['b', 'c', 'c']  

Assigning to a slice gives you a way of deleting elements:

>>> r = list(range(10)) >>> r[3:5] = [] >>> r [0, 1, 2, 5, 6, 7, 8, 9]

You can also delete an item from a listusing the ``del`` statement:

::

   >>> r = list(range(10))
   >>> del(r[3])
   >>> r
   [0, 1, 2, 4, 5, 6, 7, 8, 9]
   >>>
   >>> l = list(range(10))
   >>> del(r[3:5])
   >>> r
   [0, 1, 2, 6, 7, 8, 9]

List objects have a number of methods you can call, as shown in table
`See List Methods. <chap2.html#20881>`__. They fall into several groups.
Two of the methods add elements to the list. Method call ``L.append(x)``
adds an element ``x`` to the end of the list ``L`` (the new highest
position). Method call ``L.insert(i,x)`` inserts an element ``x`` at any
position ``i`` in the list ``L``. All elements previously at that
position or beyond are moved up one position. The index ``i`` can be at
the end of the list, whereupon ``insert()`` behaves like ``append()``.


.. list-table:: List Methods
   :widths: 15 45
   :header-rows: 1

   * - Method
     - Description

   * - ``L.append(x)``
     - Places ``x`` at the end of the list ``L``, increasing the length of ``L`` by one.
 
   * - ``L.extend(x)``
     - Places the list of elements ``x`` at the end of the list ``L`` , increasing the length of ``L`` by the length of ``x``. ``L.extend(x)`` is equivalent to ``L[len(L):]=x``.


   * - ``L.insert(i,x)``
     - Inserts item ``x`` at position ``i`` in list ``L``. All items in ``L`` at positions ``i`` and above are moved to the right, i.e., their indices increase by one. ``L.insert(len(L),x)`` is equivalent to ``L.append(x)``.

   * - ``L.pop()`` or ``L.pop(i)``
     - Removes and returns an item from the list. If an index, ``i`` , is provided, ``pop()`` removes and returns the item at that position. If no index is provided, it removes and returns the last item–the index defaults to -1.

   * - ``L.remove(x)``
     - Removes the first item in ``L`` that is equal to ``x``. It is an error if ``x`` doesn’t occur in ``L``.

   * - ``L.count(x)``
     - Counts the number of items in ``L`` that are equal to ``x``.
 
   * - ``L.index(x)``
     - Returns the index of the first item in ``L`` that is equal to ``x``. It is an error if ``x`` doesn’t occur in ``L``.

   * - ``L.reverse()``
     - Reverses the order of the elements of the list ``L`` in place.

   * - ``L.sort()`` or ``L.sort(cmpfn)``
     - Sorts the elements of the list ``L`` in place into non- decreasing order. Function ``cmpfn(x,y)`` is called to compare ``x`` and ``y`` and return a negative integer if ``x`` precedes ``y`` in the desired ordering, 0 if they are to be considered equal, and a positive integer if ``x`` follows ``y``. To sort into descending order, you could use: ``def cmpfn(x, y): return -cmp(x,y)``.


Method call ``L.remove(x)`` finds the first (lowest indexed) occurrence
of ``x`` in list ``L`` and removes it. All elements with higher indices
are moved down one. If you know the position, ``i`` , of the element you
wish to remove, use ``del L[i]``. If you want to examine the item at a
particular position and remove it, use ``L.pop(i)``. If you want to
examine the last item and remove it, use ``L.pop()``.

To use ``L`` as a stack, use ``L.append(x)`` to push ``x`` on the stack,
and ``x=L.pop()`` to pop it off. To use ``L`` as a queue, use
``L.append(x)`` to enqueue ``x`` and ``x=L.pop(0)`` to dequeue it.

Two methods examine the list for elements equal to a particular value.
Call ``L.count(x)`` returns a count of the number of occurrences of
value ``x`` in list ``L``. Call ``L.index(x)`` returns the position of
the first occurrence of ``x`` in ``L``. Remember, the expressions ``x``
``in L`` and ``x not in L`` test to see if the list ``L`` contains
element ``x``.

Two methods permute the order of the elements of the list, in place.
``L.reverse()`` reverses the order of the elements of the list ``L``.
``L.sort()`` sorts the elements of ``L`` into nondecreasing order.

Example: Self-Organizing List

In a self-organizing list, you move items that are accessed to the front
so you can find them more quickly in subsequent searches. Here’s how you
could implement self-organizing lists using list methods:

::

   >>> def reorder(L, x):
   ...    L.remove(x)
   ...    L.insert(0, x)
   ...
   >>> r = list(range(10))
   >>> reorder(r, 5)
   >>> r
   [5, 0, 1, 2, 3, 4, 6, 7, 8, 9]

Example: Median Value of a List of Numbers

The median number in a list is the middle number in the sorted list, if
there is an odd number of items. If there is an even number, the median
is the average of the two middle numbers. Here is a function to compute
the median:

::

     >>> def median(L):
     ...   s = L[:]
     ...   s.sort()
     ...   n = len(s)
     ...   return (s[n//2]+s[(n-1)//2])/2.0

There are a couple of things to note about this code:

-  Rather than modify the array, ``L`` , we make a copy before sorting
   it.

-  Whether the number, ``n``, of elements is even or odd, we compute the
   median by averaging the elements at positions ``n//2`` and
   ``(n-1)//2``. This gives the correct answer in either case.

``for`` loops
~~~~~~~~~~~~~

In Python, loops exist to allow an index variable to take on each
element in a list, or other sequence (iterable) object. (We’ll discuss
other sequences below.) The form of a ``for`` loop is:

::

   for var in sequence:
      body statement
      ...
      body statement  

Probably the most common form of ``for`` loop is

::

   for i in range(len(L)):
      # do something with L[i]  

where ``i`` takes on the index of each item in the list, ``L``. If you
only need to examine the items in the list but do not need to know their
positions, you can use the loop:

::

   for item in L:
      # do something with each item in L

continue
~~~~~~~~

If you decide that you are finished with the current iteration of a
loop, you can execute the continue statement. It consists of the single
word

::

   continue  

It will immediately end the current iteration and jump back to the top
of the loop and start the next iteration. If there are no more
iterations to do, of course, it falls out of the loop.

One major use for the ``continue`` statement is to filter the items in
the loop. Suppose we wish to print only those strings in a list that are
at least five letters long; we might do it as follows:

::

   >>> x = ["book","placid","right","table","mother","gone"]
   >>> for s in x:
   ...    if len(s) <= 5:
   ...       continue
   ...    print(s)
   ...
   placid
   mother  

We’ll eventually see how many for loops can be replaced with *filters*
and *lambda expressions*. For now, here is the equivalent formulation
where we iterate over a filtered result:

::

   >>> for result in filter(lambda s: len(s) > 5, x):
   ...     print(result)
   ...
   placid
   mother  

break and else in loops
~~~~~~~~~~~~~~~~~~~~~~~

Often you will use a loop to search for something. Once you’ve found it,
you want to escape from the loop. If you don’t find it, you often need
to take some default action. Python makes it easy to do both of these.

If in the midst of a loop you wish to stop iterating, you can execute
the ``break`` statement. It consists of the keyword ``break`` :

::

   break  

If you want to execute some code if the loop terminated normally, i.e.,
if it didn’t exit by a ``break`` , you can attach an ``else`` clause on
the end of the loop. Loops with ``else`` clauses have the form:

::

   while expr :
      indented loop body containing break 
   else :
      indented code to execute
      if the loop exits normally

or

::

   for var in sequence:
      indented loop body containing break
   else:
      indented code to execute
      if the loop exits normally

Of course the keyword ``else`` is usually used in ``if`` statements. It
is in Python too. It is perhaps not the best word to express the concept
of *on normal termination*, but it is what Python uses.

.. [1]
   This chapter is adapted from Thiruvathukal, Christopher, and Shafaee,
   *Web Programming in Python*, 2002. Rights have been reverted to the
   authors for this out-of-print work. It is also being updated for
   Python 3, which is what we use exclusively in this book.

.. [2]
   Python is easy to run on Linux, OS X, and Windows. For Windows, we
   recommend installing Windows Subsystem for Linux to get a complete
   Linux shell environment. To be covered in preliminaries section.

.. [3]
   GKT: Latest releases of Python 2 and 3 do not overflow. This needs to
   be revised.

.. [4]
   Python also provides full UNICODE support.

.. [5]
   Need to add figure 2-1 from original book by redrawing it.

.. [6]
   Now entirely a function in Python 3. Also need to include info about
   key useful options, e.g. the separator.
