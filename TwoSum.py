class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            tambah1 = nums[i]
            for j in range(i+1,len(nums)):
                tambah2 = nums[j]
                jumlah = tambah1 + tambah2
                if jumlah == target:
                    break            
            if jumlah == target:
                    return [i,j]
                    break    