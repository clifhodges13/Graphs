"""
Given an object/dictionary with keys and values that consist of both strings and integers, design an algorithm to calculate and return the sum of all of the numeric values.
For example, given the following object/dictionary as input:
{
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
Your algorithm should return 41, the sum of the values 23 and 18.
You may use whatever programming language you'd like.
Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.
"""

def return_sum(input):
    # initialize sum variable
    sum = 0

    # loop through dict
    for i in input.values():
        # check type of value in key/value pair
        if isinstance(i, int):
        # if its an integer, add it to the sum
            sum += i

    # return sum
    return sum

print(return_sum({
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}))