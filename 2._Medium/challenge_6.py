'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        out = [""]* numRows

        if numRows == 1 or numRows >= len(s):
            return s

        n, i = 0, 0
        reverse = False
        for i in range(len(s)):
            
            out[n] += s[i]

            if n == numRows - 1:
                reverse = True
            if n == 0:
                reverse = False
            
            if reverse == True:
                n -= 1
            else:
                n += 1
            
            i += 1

        return "".join(out)