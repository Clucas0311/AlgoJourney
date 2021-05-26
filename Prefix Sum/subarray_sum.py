"""
Prefix Sum is the sum of the elements from 0 to i 
REMEMBER TWO SUM UNSORTED 
The trick to this problem is to create a dictionary that we will look into to 
see if the running sum is located in the array
If the sum is located in the array we will add the occurences to our result variable thus
giving us the total subarrays for that sum 
PSEUDOCODE:
First create hashMap that will initalize at 0: 1 because our sum start out at 0 we can manually place that sum into the dictionary
Next Create a variable to help calculate the amount of subarray sums and a variable to get the current sum
Both variables will be intialized at 0
iterate through the array 
update the current_sum variable to be each element as we iterare through the array 
if the current_sum minus target is in the dictionary 
add the value of that to the result variable 
if the value is not found then just add one to the hashMap[current_sum]
lastly return the result
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # initialize hash_map to have 0 and 1
        hash_map = {0 : 1}
        prefix_sum = 0
        result = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            # if the prefix_sum is in the hash_map
            if prefix_sum - k in hash_map:
                result += hash_map[prefix_sum - k]
            #Construct hash_map
            if prefix_sum in hash_map:
                hash_map[prefix_sum] += 1
            else:
                hash_map[prefix_sum] = 1
        # return the result
        return result