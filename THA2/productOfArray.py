from numpy import flip, cumprod
class Solution:
    def productExceptSelf(self, nums):
	    return cumprod([1] + nums[:-1]) * flip(cumprod(flip(nums[1:] + [1])))