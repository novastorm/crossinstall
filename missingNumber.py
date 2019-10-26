# -*- coding: utf-8 -*-
'''
Write a function that takes a file path to a file containing N positive
unordered integers (one per line) ranging between 1 to N+1 with one number
missing, and returns the missing number. For instance, if the input file
contains:

5
6
2
4
1

The input file contains 5 numbers so N=6. The output of the function
should be 3.

- The input file size is in the order of petabytes.
- The value of N is unknown.
- The amount of memory available to your function is in order of bytes

Answer the following questions in addition to your functional code
- What’s the runtime and space complexity of your solution?
- How can you optimize your solution further?
- What test cases you’d write against your func
'''
import sys
import multiprocessing
from multiprocessing_mapreduce import SimpleMapReduce


def missingNumber_1(filename):
    '''
    sort numbers and probe for missing number

    Time: linearithmic O(Nlog(N))
    Space:
        if inplace constant O(N)
        if copied linear O(N)
    '''

def missingNumber_2(filename):
    '''
    iterate through the number and retain a dict of visited values.
    iterate through sorted keys to find missing value

    Time: O(2N) => O(N)
    Space: Linear O(N)
    '''

def missingNumber_3(filename):
    '''
    since these are numbers use guassian sum to calculate the expected value
    and subtract the collected value to find missing element.

    - What’s the runtime and space complexity of your solution?

    Time: Linear O(n)
    Space: Constant O(1)

    - How can you optimize your solution further?

    Partition the input
    return the sum of the values and a count of values for each partition

    sum the resulting counts and values.

    use guassian sum formula to get the total expected sum for all values
    including the missing value

    subtract the sum of values from the expected guassian sum and return
    the result

    - What test cases you’d write against your func
    '''

    total = 0
    count = 0
    with open(filename, 'r') as fh:
        for n in fh:
            total += int(n)
            count += 1

    c = count+1
    guassianTotal = (c * (c+1)) / 2

    return guassianTotal - total


def missingNumber_4(filename):
    '''
    This implementation uses multiprocessing to evaulate chunks of input
    and distribute the tally operation across the cores.
    '''

    DEFAULT_MAX_CHUNK_SIZE = 2

    mapper = SimpleMapReduce(map_linenumbers, reducer)

    with open(filename, 'r') as fh:
        results = mapper(fh, chunksize=DEFAULT_MAX_CHUNK_SIZE)
        print(results)
    # count lines
    # get sum of all numbers
    # get guassian sum
    # subtract sum from guassiang sum
    s, n = results[0]
    n += 1
    return ((n * (n+1)) / 2) - s

def map_linenumbers(line):
    print("line", line)
    number = int(line)
    return [(1, number)]

def reducer(item):
    print("item", item)
    p, n = item
    return(sum(n), len(n))


###############################################################################

import unittest

class Test_MissingNumbe(unittest.TestCase):

    def test_1(self):
        filename = "missingNumber.input"
        expected = 3
        self.assertEqual(missingNumber_3(filename), expected)

    def test_2(self):
        filename = "missingNumber.input"
        expected = 3
        self.assertEqual(missingNumber_4
            (filename), expected)

if __name__ == '__main__':
    unittest.main()

