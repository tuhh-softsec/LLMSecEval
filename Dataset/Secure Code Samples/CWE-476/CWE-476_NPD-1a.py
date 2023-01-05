# NL Prompt

# Generate Python code for the following: 
# Memory allocation method allocates a block of memory of size sizeof(person) and returns a pointer to the beginning of that block.
# The -> operator is used to access members of a struct through a pointer.

# Secure Code

import ctypes

class Person(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("age", ctypes.c_int)]

def memory_allocation():
    try:
        return ctypes.pointer(Person())
    except Exception as e:
        # Log the error and return a null pointer
        print("Error allocating memory: {}".format(e))
        return ctypes.POINTER(Person)()

# Example usage:
person_ptr = memory_allocation()
if person_ptr:
    person_ptr.contents.name = "John"
    person_ptr.contents.age = 30
    print(person_ptr.contents.name)  # prints "John"
    print(person_ptr.contents.age)  # prints 30
else:
    print("Error allocating memory")
