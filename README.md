# 42 Tools

A small repo of tools created to help work with creating 42 tests. Used during my thesis on finding bugs in the [42 compiler](https://github.com/ElvisResearchGroup/L42).

# TestHelper

This a simple website used to wrap a 42 program in Java code that is used as a test in the 42 test suite. It can convert from 42 code to a Java test, and from a test to 42 code.

# TestIncrementer

A simple Python program used to randomly mutate string and integer variables in a 42 program. This can be used to easily generate large numbers of 42 programs which can allow for the finding of edge cases in the 42 implementation. It can also be used to deterministically append to strings or increment numbers by a set amount.

```
python incrementer.py input.L42 output.L42 // Change values randomly.
python incrementer.py input.L42 output.L42 "foo" // Change values by adding "foo".
```
