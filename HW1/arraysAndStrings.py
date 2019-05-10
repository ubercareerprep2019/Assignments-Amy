def is_string_permutation(s1, s2):
    """ Takes in two strings and returns true if one string is a permutation of the other, false otherwise """
    if len(s1) == len(s2):  # must be same size to be a permutation of the other string
        s1_lst = list(s1)
        s2_lst = list(s2)
        for currentChr in s1_lst:
            if currentChr in s2_lst:
                s2_lst.remove(currentChr)  # remove current element from second list to account for it
            else:
                return False  # no same character found, not a permutation
        return True
    else:
        return False


def pairs_that_equal_sum(inputArray, targetSum):
    """ Takes in an array of integers and a target integer to which the array elements must sum. Returns an array of
        all pairs of integers from the input array whose sum equals the target """
    pairs = []
    for num in inputArray:
        diff = targetSum - num
        if diff in inputArray:
            if [num, diff] and [diff, num] not in pairs:
                pairs.append([num, diff])
    return pairs


# Sample calls to functions

# Examples of strings as a permutation of the other
print(is_string_permutation("", ""))
print(is_string_permutation("racecar", "carrace"))
print(is_string_permutation("h ello", "hlle o"))

# Examples of non - permutations
print(is_string_permutation("not a permutation", "not permutation !"))
print(is_string_permutation("hllo", "hlle"))
print(is_string_permutation("aabbc", "aabcc"))

# Sample calls to function that finds pairs of integers that equal a target sum
print(pairs_that_equal_sum([], 5))  # Output should be [], no pairs
print(pairs_that_equal_sum([1, 5, 3, 3, 2, 3, 4], 6))  # Output should be [[1, 5], [3, 3], [2, 4]]
print(pairs_that_equal_sum([1, 9, 3, 4, 5, 6], 10))  # Output should be [[1, 9], [4, 6], [5, 5]]
print(pairs_that_equal_sum([-2, 4, 2, 4, -4, 3], 0))  # Output should be [[-2, 2], [4, -4], [4, -4]]
