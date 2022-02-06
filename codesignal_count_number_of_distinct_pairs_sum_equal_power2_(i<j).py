# Given an array of distinct integers a, your task is to find the number of pairs of indices (i, j) such that i ≤ j and the sum a[i] + a[j] is equal to some power of two.

# Note: numbers 20 = 1, 21 = 2, 22 = 4, 23 = 8, etc. are considered to be powers of two.

# Example

# For a = [1, -1, 2, 3], the output should be solution(a) = 5.
# There is one pair of indices where the corresponding elements sum up to 20 = 1:
# (1, 2): a[1] + a[2] = -1 + 2 = 1.
# There are two pairs of indices where the corresponding elements sum up to 21 = 2:
# (0, 0): a[0] + a[0] = 1 + 1 = 2;
# (1, 3): a[1] + a[3] = -1 + 3 = 2.
# There are two pairs of indices where the corresponding elements sum up to 22 = 4:
# (0, 3): a[0] + a[3] = 1 + 3 = 4;
# (2, 2): a[2] + a[2] = 2 + 2 = 4;
# In total, there are 1 + 2 + 2 = 5 pairs summing up to powers of two.
# For a = [2], the output should be solution(a) = 1.
# The only pair of indices is (0, 0) and the sum of corresponding elements is equal to 22 = 4. So the answer is 1.
# For a = [-2, -1, 0, 1, 2], the output should be solution(a) = 5.
# There are two pairs of indices where the corresponding elements sum up to 20 = 1: (2, 3) and (1, 4).
# There are two pairs of indices where the corresponding elements sum up to 21 = 2: (2, 4) and (3, 3).
# There is one pair of indices where the corresponding elements sum up to 22 = 4: (4, 4).
# In total, there are 2 + 2 + 1 = 5 pairs summing up to powers of two.
# Input/Output

# [execution time limit] 6 seconds (py3)

# [input] array.integer a

# An array of distinct integers.

# Guaranteed constraints:
# 1 ≤ a.length ≤ 105,
# -106 ≤ a[i] ≤ 106.

# [output] integer

# The number of pairs of indices (i, j) such that i ≤ j and the sum of the corresponding elements is equal to some power of two.

def number_pairs(a):
    count=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if bin(a[i]+a[j]).count("1")==1:
                count+=1
    return count