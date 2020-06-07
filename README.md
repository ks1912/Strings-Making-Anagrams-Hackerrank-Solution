# Strings-Making-Anagrams-Hackerrank-Solution
-----------------------------------------------------------------------
# QUESTION 

Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings, a and b,  that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

For example, if a = cde and b = dcf, we can delete e from string a and f from string b so that both the remaining strings are cd  and dc which are anageams.

# Function Description

Complete the makeAnagram function in the editor below. It must return an integer representing the minimum total characters that must be deleted to make the strings anagrams.
makeAnagram has the following parameter(s):

1.	a: a string

2.	b: a string

# Input Format

The first line contains a single string,a .

The second line contains a single string,b .

# Constraints

1.	1 < = |a|, |b| =< ( 10 power 4 ) 

2. 	The strings a and b consist of lowercase English alphabetic letters ascii[a-z].

# Output Format

Print a single integer denoting the number of characters you must delete to make the two strings anagrams of each other.

# Sample Input

cde
abc

# Sample Output

4

# Explanation
