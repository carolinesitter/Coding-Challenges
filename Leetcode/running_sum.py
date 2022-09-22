# CHALLENGE: RUNNING SUM OF 1D ARRAY
# -----------------------------------
## Given an array nums. We define a running sum of an array as 
## runningSum[i] = sum(nums[0]…nums[i]).

## Return the running sum of nums.

# TEST CASE 1:
# ------------
## Input: [1,2,3,4]
## Output: [1,3,6,10]

# TEST CASE 2:
# ------------
## Input: [1,1,1,1,1,]
## Output: [1,2,3,4,5]

# TEST CASE 3:
# ------------
## Input: [1,4,5,8]
## Output: [1,5,9,13]

# PSEUDOCODE:
# ------------
## write a function that takes in an array of nums
## create an empty list and assign it to a variable called running_sum
## write a for loop that iterates through each number,
## and adds the previous number in the array.
## add this sum to the new list (append)

# CODE:
# -----
class RunSum(object):
    def get_running_sum(self, nums):

        running_sum = []
        temp_sum = 0

        for num in nums:
            temp_sum += num
            running_sum.append(temp_sum)

        return running_sum


# RUNTIME COMPLEXITY:
# --------------------
## The runtime complexity for this solution is O(N)/Linear as we are only looping
## through the array once, adding it to a new list, and returning the new list.