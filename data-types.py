# NUMBERS
# int
x = 5
# float - accurate to 15 decimal places
y = 3.7
# complex - written as [real number] + [imaginary number j]
z = 2 + 9j

# LISTS [ ]
# lists are ORDERED sequences of data
# items do not need to be of the same type
list_of_things = [1, 'hello', 4.37, True, 82, 3.8]
# extract a single item with its [index] in the slicing operator [ ]
list_of_things[1]  # = 'hello'
# extract a segment with [starting index:index after last item]
# = [1, 'hello', 4.37] (list_of_things[3] = True is not included)
list_of_things[0:3]
# extract from one item to the end with [starting index:]
list_of_things[3:]  # = [True, 82, 3.8]
# lists are mutable, i.e., an element's value can be changed
# = list_of_things = [1, 'hello', 4.37, False, 82, 3.8]
list_of_things[3] = False

# TUPLES ( )
# tuples are ordered sequences like lists, except their data is immutable
# tuples are typically faster than lists because they cannot change dynamically
tuple_of_ints = (1, 2, 3, 4)
# all of the value extraction methods from lists can be used for tuples too
tuple_of_ints[0:3]  # = (1, 2, 3)
tuple_of_ints[3] = 7  # Error - values cannot be reassigned

# STRINGS ' ' or " "
# strings can be marked with single or double quotes; their data is immutable
this_is_a_string = 'i liek turtles'
this_is_a_string[4:6] = 'ke'  # Error - values cannot be reassigned
# multi-line strings are denoted with three sets of quotes (single or double)
multi_line_string = """Line One
Line Two"""
# the slicing operator can be used to extract characters from strings
this_is_a_string[4:6]  # = 'ek' (this_is_a_string[6] = ' ', not included)

# SETS { }
# sets are UNORDERED collections of UNIQUE items - duplicates are eliminated
set_of_ints = {2, 6, 3, 78, 2, 2, 3}  # becomes {2,6,3,78}
another_int_set = {5, 2, 82, 4}
yet_more_ints = {6, 2, 89}
# the slicing operator doesn't work on sets because they are unordered
set_of_ints[2]  # = Error
# Set.union() returns a new set with all DISTINCT elements from the constituent sets combined
united1 = set_of_ints.union(another_int_set)  # = {2, 6, 3, 78, 89}
# = {2, 6, 3, 78, 5, 82, 4, 89}
united2 = set_of_ints.union(another_int_set, yet_more_ints)
# unions can also be found with |
united_with_pipe = another_int_set | yet_more_ints  # = {5, 2, 82, 4, 6, 89}
# Set.intersection() returns a new set with all COMMON elements from the constituent sets
intersected = set_of_ints.intersection(yet_more_ints)  # = {2,6}
# intersecxtions can also be set with &
intersected_with_amp = set_of_ints & another_int_set  # = {2}

# DICTIONARIES {key:value}
# dictionaries are UNORDERED collections of key-value pairs
# keys and values can be of any type
websters_dict = {'word': 'definition', 1.2: 'float', 'int': 78}
# keys can be used to retrieve values, but not the other way around
websters_dict[1.2]  # = 'float'
websters_dict[78]  # Error, != 'int'

# DATA TYPE CONVERSIONS
# data types can be converted using various type conversion functions
float(7)  # = 7.0
int(4.89)  # = 4, decimals are truncated
# conversion between numbers and strings must contain compatible values
str(12)  # = '12'
float('9.8')  # = 9.8
int('3m')  # = Error
# data sequences can be converted too!
set([1, 2, 3])  # = {1, 2, 3}
tuple({5, 6, 7})  # = (5, 6, 7)
list('hi there')  # = ['h','i', ' ', 't', 'h', 'e', 'r', 'e']
# but to convert to dictionary, each element in the sequence must be a pair
dict([[1, 'one'], (2, 'two')])  # = {1:'one', 2:'two'}
# additionally, the type() function can be used with a single param to determine its...er...datatype
type(united_with_pipe)  # = <class 'set'>
