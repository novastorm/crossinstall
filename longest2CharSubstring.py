# -*- coding: utf-8 -*-
'''
Write a function that takes an input string and returns the longest
substring with two distinct characters. For example

longest2CharSubStr("ABCBCCCCDDDDEF") = "CCCCDDDD"
longest2CharSubStr("ABAACCAABBBCCDADDAABABABCBB") = "AABABAB"

Please consider the following constraints in your solution:
- The length of the input string is unknown and very very large (order of MB)
- The amount of memory available to your function is limited (order of Bytes)

Answer the following question in addition to your functional code
- What’s the runtime and space complexity of your solution
- How can you optimize your solution further?
- What test cases you’d write against your function?

'''
from collections import Counter

def longest2CharSubStr_1(str):
    '''
    - What’s the runtime and space complexity of your solution

    Time: quadratic O(N^2)
    Space: constant O(1)

    - How can you optimize your solution further?

    The program could use a rolling window and decrement and increment chars
    instead of rescanning the whole string from [i:j]

    - What test cases you’d write against your function?
    '''

    def numberOfChar(s):
        '''
        Time: Linear O(N)
        Space: Constant 0(26) => O(1)
        '''
        return len(Counter(s))

    i = 0
    j = 1

    maxSize = (1, 0, 0)

    while i < j <= len(str):
        tempLen = numberOfChar(str[i: j])

        if tempLen == 3:
            i += 1
        elif tempLen == 1 or tempLen == 2:
            if maxSize[0] < j-i:
                maxSize = (j-i, i, j)
            j += 1
        else:
            j += 1

    s, m, n = maxSize
    return (str[m:n])




###############################################################################

import unittest

class Test_Longest2CharSubStr_1(unittest.TestCase):

    def test_1(self):
        s = "ABCBCCCCDDDDEF"
        e = "CCCCDDDD"
        self.assertEqual(longest2CharSubStr_1(s), e)

    def test_2(self):
        s = "ABAACCAABBBCCDADDAABABABCBB"
        e = "AABABAB"
        self.assertEqual(longest2CharSubStr_1(s), e)

    def test_3(self):
        s = ""
        e = ""
        self.assertEqual(longest2CharSubStr_1(s), e)

    def test_4(self):
        s = "aaaaaaaa"
        e = "aaaaaaaa"
        self.assertEqual(longest2CharSubStr_1(s), e)

if __name__ == '__main__':
    unittest.main()

