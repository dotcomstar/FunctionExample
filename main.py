#!/usr/bin/env python
import os
import sys

"""
Functions should generally be named as verbs. def main() is a special exception to this rule,
governed by convention.
"""

def main():
    print("Starting main()\n")
    say_hello()
    say_phrase("Boom, Big Shaq")
    get_factorial(10)  # This will get calculated, but nothing else will happen
        # because we don't do anything with the returned value.
    print(get_factorial(25))  # This will get printed.
    print("\nFinishing main()")

# ~~~~ The Functions ~~~~

def say_hello():
    print("Hello World!")

def say_phrase(phrase_to_say):
    print(phrase_to_say)

# We are assuming that the number passed in is a non-negative number.
# Note that this function does not output anything by itself.
def get_factorial(number_to_find_factorial_of):
    current_calculation = 1
    temporary_number = number_to_find_factorial_of
    while temporary_number > 0:
        current_calculation *= temporary_number
        temporary_number -= 1
    return current_calculation

# ~~~~ Don't worry about this for now ~~~~
if __name__ == "__main__":
    main()
