# tensor-store

### The aim of the project
We aim to define a file format for storing tensors of data of different
type and arbitrary dimensionality. The initial scope of the project is
to support float and integer data types in C++ and Python languages. The
design of the format itself will try to foresee the needs of extending
this idea onto more data types (including various-sized ones, e.g.,
strings) and programming languages.

### What's not included

Performing operations on the stored data remains outside the project's
scope. We only facilitate efficient storing and loading the data to and 
from the most popular representation of the data in a given programming
language (such as numpy for Python).

### The key contribution

The key point of the framework is to make tensor-like data portable 
across different languages, without relying on any particular third
party library. By storing the data in a simple, independent
representation, one can easily introduce a support for any technology 
of interest.

### The current (prototype) approach

The trivial (current) approach for developing this project is 2-step:
1. define a format for storing the data
2. write a piece of code in each supported language to load and store
the data in the defined manner
   
### The target (production) approach

The target approach consists in creating a C/C++/Rust core of the
project and a bunch of APIs in a variety of programming languages to
send/retrieve the data to/from the core.