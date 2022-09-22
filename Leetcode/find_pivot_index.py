# CHALLENGE: FIND PIVOT INDEX
# ----------------------------
## Given an array of integers nums, calculate the pivot index of this array.

## The pivot index is the index where the sum of all the numbers strictly to
## the left of the index is equal to the sum of all the numbers strictly to
## the index's right.

## Return the leftmost pivot index. If no such index exists, return -1.


# TEST CASE 1:
# ------------
## Input: [1,7,3,6,5,6,]
## Output: 3

# TEST CASE 2:
# ------------
## Input: [1,2,3]
## Output: -1

# TEST CASE 3:
# ------------
## Input: [2,1,-1]
## Output: 0

# PSEUDOCODE:
# ------------
## within a class, write a function that takes in a list of nums (and self)
## assign the sum of right nums and set it to the sum of all nums
## assign a variable for the sum of the left side and set it to 0
## write a for loop that takes in each num and in the range of the length of nums
## subtract the num from the right sum
### if the sum of the left side is equal to the right,
### return that number
## continue to increase the sum of the left side by num 
## else return -1

class PivotIndex(object):
    def find_pivot_index(self, nums):

        sumR = sum(nums)
        sumL = 0

        for num in range(len(nums)):
            #subtract the current num from the right sum
            sumR -= nums[num]

            if sumL == sumR:
                return num
            
            #update the left sum
            sumL += nums[num]

        return -1


# RUNTIME COMPLEXITY:
# -------------------
## I belive that this is an O(N) runtime as we are only looping through the list once.