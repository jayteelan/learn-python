# SYNTAX
def function_name(parameters):
    """docstring"""
    statement(s)
# def is the keyword that marks the start of a function header
# : marks the end of the header
# docstring is optionally used to describe what the function does
# statements must all have the same level of intentation
# an optional return statement can be used to return a value; otherwise, a None object is returned

# DEFAULT ARGUMENTS
# arguments for a function can be given a default value if no other value is given when the function is called. A function can take multiple default arguments, but they must appear after any other (non-default) arguments.


def greet(name, msg="nice to meet you!"):
    print("Hello" + name + ", " + msg)


greet("Mike")  # >>> "Hello Mike, nice to meet you!"
greet("Alice", "nice weather, eh?")  # >>> "Hello Alice, nice weather, eh?"

# KEYWORD ARGUMENTS
# functions can also be called with explicitly-labelled arguments (rather than having them assigned just by their position within the parens); this allows the arguments to be placed in any order
greet(name="Joe", msg="sup?")  # >>> "Hello Joe, sup?"
greet(msg="sup?", name="Joe")  # >>> "Hello Joe, sup?"
# positional and keyword arguments can be combined in the same call, but keywords MUST follow positional arguments
greet(name="Joe", "sup?")  # >>> Error

# ARBITRARY ARGUMENTS
# a function can be written for an unspecified number of arguments by starting the param with an asterisk


def greet(*names):
    for name in names:
        print("Hello", name)


# the arguments are then passed into the function as a tuple ( ) in the call
greet("Monica", "Joey", "Chandler", "Phoebe")
