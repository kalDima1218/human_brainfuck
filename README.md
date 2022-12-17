# What is this?
This code provides translating from easy-to-read dialect of brainfuck (will be described below) to real brainfuck
# Easy-to-read brainfuck
This dialect adding functions to brainfuck (but it's more of macro) that you can use with classic brainfuck syntax
### Definition of function
- Firstly you mark start of definition with ? (question mark)
- After ? you typeing name of function
- Finally you typeing code of function in {} (braces)
#### Example
?name{[->+<]}
### Usage of function
- Firstly you mark start of usage with ! (exclamation mark)
- After ! you typeing name of function
- Finally you mark of end of usage with ! (exclamation mark)
#### Example
!name!
# TODO
I think i might add static arguments of functions, but this requires thinking through the logic of making this
