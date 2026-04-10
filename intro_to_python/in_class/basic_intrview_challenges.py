# fibonacci sequence:
# zero doesn't count ( sorry )
# 0, 1, 1, 2, 3, 5, 8, 13
from threading import current_thread


def fibonacci_number(nth: int):
    # previous, current
    a, b = 0, 1
    if nth == 1:
        return b

    for i in range(nth-1):
    # temp = previous + concurrent
    # previous = current
    # current = temp
        a, b = b, a + b
    return b

# print(fibonacci_number(7))




def fibonacci_recursion(n):
    if -1 < n <= 1:
        return n
    return fibonacci_recursion(n-2) + fibonacci_recursion(n-1)

# print(fibonacci_recursion(7))

#        7
#       5 6
#     3 4 4 5
# 1 2 2 3 2 3 3 4
#  Keeps going ...


def fib_efficient(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_efficient(n-1, memo) + fib_efficient(n-2, memo)
    return memo[n]


# ---------------------------------------------

""" 
Create a function 'find_pair' 
The function will take 2 params
1st is a list of numbers (you can assume integers)
2nd is an int called sum
The function should return the numbers that are 
members of the list that added equal sum
A number cannot be added to itself
only 2 numbers can be used
if multiple variation, return first one found

[3, 6, 9, -2, 1], 12    -> 3, 9
[3, 6, 9, -2, 1], 13    ->  "not found" or None
[3, 6, 9, -2, 1], 4     ->  3, 1  OR  6, -2
[3, 6, 9, -2, 1], 6     ->  "not found" or None
[3, 3, 1, 4, 3], 6
"""

# nested loops - O(n^2)
# set OR dict to make more efficient - {} to make more efficient
# sort then use two pointer from left and right

def find_pair(list_of_nums, sum):
    # using nested loops
    length = len(list_of_nums)
    for n in range(length):
        for m in range(n+1, length):
            total = list_of_nums[n] + list_of_nums[m]
            if total == sum:
                return list_of_nums[n], list_of_nums[m]
    return None, "sum not found"

# print(find_pair([3, 6, 9, -2, 1], 12))    # -> 3, 9
# print(find_pair([3, 6, 9, -2, 1], 13) )   #     ->  "not found" or None
# print(find_pair([3, 6, 9, -2, 1], 4) )   #      ->  3, 1  OR  6, -2
# print(find_pair([3, 6, 9, -2, 1], 6) )   #      ->  "not found" or None
# print(find_pair([3, 3, 1, 4, 3], 6) )   #      -> 3,3

def find_pair_with_set(list_of_nums, sum):
    tried = set()   # lookup in set is O(1)
                    # lookup in list is O(n)

    for num in list_of_nums:
        needed = sum - num
        if needed in tried:
            return num, needed
        tried.add(num)
    return None, "sum not found"

# print(find_pair_with_set([3, 6, 9, -2, 1], 12))    # -> 3, 9
# print(find_pair_with_set([3, 6, 9, -2, 1], 13) )   #     ->  "not found" or None
# print(find_pair_with_set([3, 6, 9, -2, 1], 4) )   #      ->  3, 1  OR  6, -2
# print(find_pair_with_set([3, 6, 9, -2, 1], 6) )   #      ->  "not found" or None
# print(find_pair_with_set([3, 3, 1, 4, 3], 6) )   #      -> 3,3

def find_pair_with_pointers(list_of_nums, sum):
    sorted_list = sorted(list_of_nums)    # [-2, 1, 3, 6, 9]
    left, right = 0, len(list_of_nums) - 1

    while left < right:
        total = sorted_list[left] + sorted_list[right]
        if total == sum:
            return sorted_list[left] , sorted_list[right]
        elif total < sum:
            left += 1
        elif total > sum:
            right -= 1
    return None, "sum not found"

print(find_pair_with_pointers([3, 6, 9, -2, 1], 12))    # -> 3, 9
print(find_pair_with_pointers([3, 6, 9, -2, 1], 13) )   #     ->  "not found" or None
print(find_pair_with_pointers([3, 6, 9, -2, 1], 4) )   #      ->  3, 1  OR  6, -2
print(find_pair_with_pointers([3, 6, 9, -2, 1], 6) )   #      ->  "not found" or None
print(find_pair_with_pointers([3, 3, 1, 4, 3], 6) )   #      -> 3,3


# loop 1        left = 0 right = 4     list_of_nums[left] == -2
#                                       list_of_nums[right] == 9
#                        list_of_nums[left] + list_of_nums[right] = 7
#                                       is 7 == 13  -> NOPE
#                                       is 7 < 13 or > 13 ???
#                                       left += 1
# loop 2        left = 1 right 4        list_of_nums[left] == 1
#                                       list_of_nums[right] == 9
#                        list_of_nums[left] + list_of_nums[right] = 10
#                                       is 10 == 13  -> NOPE
#                                       is 10 < 13 or > 13 ???
#                                       left += 1
# loop 3        left = 2 right 4        list_of_nums[left] == 3
# #                                       list_of_nums[right] == 9
# #                        list_of_nums[left] + list_of_nums[right] = 12
# #                                       is 12 == 13  -> NOPE
# #                                       is 12 < 13 or > 13 ???
# #                                       left += 1
# loop 4        left = 3 right 4        list_of_nums[left] == 6
# # #                                       list_of_nums[right] == 9
# # #                        list_of_nums[left] + list_of_nums[right] = 15
# # #                                       is 15 == 13  -> NOPE
# # #                                       is 15 < 13 or > 13 ???
# # #                                                      right -= 1
# loop 5      left = 3 right = 3    ---> ABORT LOOP

# "I have a LARGE baloon!" --> False
# "Dammit, I'm mad!" --> True
# "Doc, note: I dissent. A fast never prevents a fatness. I diet on cod" --> True
# "12-343-21"
# "Do geese see God?"

def is_palindrome(sentence: str):
    # input can contain special chars, punctuation, numbers, and spaces
    sanitized = []
    for chr in sentence.lower():
        if chr.isalnum():
            sanitized.append(chr)

    # return sanitized == sanitized[::-1]

    # reversed_sentence = sanitized.copy()
    # reversed_sentence.reverse()
    # return sanitized == reversed_sentence

    # half = len(sanitized) // 2
    # return sanitized[:half] == sanitized[:half:-1]

    for i in range(len(sanitized)//2):
        # print(i, -1 * (i + 1))
        # print(sanitized[i], sanitized[-1 * (i + 1)])
        if sanitized[i] != sanitized[-1 * (i+1)]:
            return False
    return True

print(is_palindrome("12-343-21"))
print(is_palindrome("Do geese see God?"))
print(is_palindrome("I have a LARGE baloon!"))