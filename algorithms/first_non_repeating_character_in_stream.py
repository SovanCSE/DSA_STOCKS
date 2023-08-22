## Queue based approach for first non-repeating character in a stream
## Given a stream of characters and we have to find the first non-repeating character each time a character is inserted in the stream.
## Pseudocode steps -
## 1. Create a count array of size 26(assuming only lower case characters are present) and initialize it with zero.
## 2. Create a queue with char data type
## 3. Store each character in queue and increase its frequency in the hash array
## 4. For every character of the queue, we check front of the queue
## 5. If frequency of character at front of the queue is one then that will be first non-repeating character.
## 6. If frequency is more than 1 then we pop that element
## 7. If queue become empty then there is no non-repecting character, we will return -1

###########################################################################################
##
## Category: Dynamic String Programming
## Title: Leetcode - 387 - Find  first non-repeating character in the stream in python
## Short notes:
## Time complexity: O(n^2)
## Youtube Link: https://www.geeksforgeeks.org/videos/queue-based-approach-for-first-non-repeating-character-in-a-stream/
## Input string: AQIZQAZPN ## Output string: AAAAAIIII
## Input string: AAAC ## Output: A-1-1C
############################################################################################

def find_first_non_repeating_character_in_stream(str_values):
    hash_array = [0 for _ in range(26)]
    queue_list = []
    
    if not all(c.isalpha() for c in str_values):
        print('String contains other letter than alphabet')
        return None
    
    #traverse the whole stream
    for char in str_values:

        ## Push each character in queue
        queue_list.append(char)

        ## Increment frequency in hash array
        if char.isupper():
            starting_ascii_value = 65
        else:
            starting_ascii_value = 97
        hash_array[ord(char)-starting_ascii_value] += 1

        ## Check for non repeating character
        while queue_list:
            ## If frequency of front item of the queue is more than 1 then we pop that element
            if hash_array[ord(queue_list[0])-starting_ascii_value] > 1:
                queue_list.pop(0)
            else:
                print(queue_list[0], end=' ')
                break
        if not queue_list:
            print(-1, end=' ')
find_first_non_repeating_character_in_stream('AQIZQAZPN') ## output: A A A A A I I I I
