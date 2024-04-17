''' 

Write a function, uncompress, that takes in a string as an argument. The input string will be formatted into multiple groups according to the following pattern:

<number><char>

for example, '2c' or '3a'.

The function should return an uncompressed version of the string where each 'char' of a group is repeated 'number' times consecutively. You may assume that the input string is well-formed according to the previously mentioned pattern.
test_00:

uncompress("2c3a1t") # -> 'ccaaat'

'''
#Q1

# def uncompress(s):
#     i=0;
#     j=0;
#     numbers = '0123456789'
#     result = []
#     while j < len(s):
#         if s[j] in numbers:
#             j += 1
#         else:
#             num = int(s[i:j])
#             result.append(s[j]*num)
#             j += 1
#             i = j
#     print(''.join(result))

# uncompress('2j3k10o')


#Q3
'''
Write a function, compress, that takes in a string as an argument. The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character. Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'

You can assume that the input only contains alphabetic characters.
'''

def compress(s):
    s += '!'
    j=0
    i=0
    result = []
    while j < len(s):
        if (s[i] == s[j]):
            j += 1
        else:
            num = str(j-i) 
            if num == '1':
                result.append(s[i])
            else:
                result.extend(num+s[i])
            i = j
            j += 1
    print(''.join(result))

compress('ssssbbz')

#Q3
'''
Write a function, anagrams, that takes in two strings as arguments. 
The function should return a boolean indicating whether or not the strings are anagrams.
Anagrams are strings that contain the same characters, but in any order.
'''
