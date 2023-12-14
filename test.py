
"""
Create a function to return the longest word in a string.
Input: “dummy text of the printing and typesetting industry.”
Output: typesetting 
Input: “It is a long-established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distributionqqqqqqqqqqqqqqqqqqq of letters, as opposed to using 'Content here, content here', making it look like readable English”
Output: distributionqqqqqqqqqqqqqqqqqqq 
"""

def longest_world(str1):
    list_word=str1.split()  
    word=max(list_word, key=len)
    #print(word)
    return word

long_word=longest_world("It is a long-established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distributionqqqqqqqqqqqqqqqqqqq of letters, as opposed to using 'Content here, content here', making it look like readable English")  
print(long_word)  