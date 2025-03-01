class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1]=0

        count=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[count]=nums[i]
                count+=1
        while count < len(nums):
            nums[count]=0
            count+=1         
        return nums