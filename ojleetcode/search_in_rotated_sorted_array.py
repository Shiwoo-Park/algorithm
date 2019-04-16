from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left = 0
        right = len(nums) - 1
        pivot = int(right / 2)
        
        while True:
            print("INDEX: left={} / pivot={} / right={}".format(left, pivot, right))
            print("VALUE: left={} / pivot={} / right={}".format(nums[left], nums[pivot], nums[right]))
            b = []
            for a in range(left, right + 1):
                b.append(nums[a])
            print(b)
            
            if nums[pivot] == target:
                return pivot
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            
            if right > 0 and nums[pivot + 1] == target:
                return pivot + 1
            
            if nums[pivot] < target:
                if nums[right] < nums[pivot]:
                    left = pivot
                elif nums[right] < target:  # 45[1]23 , find 5
                    right = pivot
                else:
                    left = pivot
            
            elif target < nums[pivot]:
                if nums[left] > nums[pivot]:
                    right = pivot
                elif target > nums[left]:
                    right = pivot
                else:
                    left = pivot
            
            new_pivot = int((left + right) / 2)
            if pivot == new_pivot:
                return -1
            pivot = new_pivot


s = Solution()
# l = [2, 3, 4,5, 1]
# n = 5

# l = [4,5,6,7,0,1,2]
# n = 1

# l=[4,5,6,7,0,1,2]
# n=5

# l = [1, 3, 5]
# n = 1

l_list = [
    [5, 1, 2, 3, 4],
    [2, 3, 4, 5, 6, 7, 8, 9, 1]
]
n_list = [1, 9]
a_list = [1, 7]

for i in range(len(l_list)):
    try:
        l = l_list[i]
        n = n_list[i]
        a = a_list[i]
        
        print("-----------------------")
        print("target: ", n)
        answer = s.search(l, n)
        if answer == a:
            print("Correct")
        else:
            print("Answer should be {}, not {}".format(a, answer))
    except AssertionError as e:
        print("hello")
