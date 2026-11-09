#similar to sum but we can include duplicates
#we just do where we take one element and then shuffle through the other elements in array
#Optimize: we recurse to bottom and build permutations back up as we add element into permutation we add it at every positble position creating a permutation.
#O(n!) -> we look at permutations and insertion


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        used = len(nums)*[False]

        self.backtrack([], nums, used)
        return self.results


    def backtrack(self, permutation, nums, used):
        if len(permutation) == len(nums):
            self.results.append(permutation.copy())
            return
        for i in range(len(nums)):
            if not used[i]:
                permutation.append(nums[i])
                used[i] = True
                self.backtrack(permutation, nums, used)
                permutation.pop()
                used[i] = False
            
        
            








        
        