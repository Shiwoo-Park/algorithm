class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer[]}
	def twoSum(self, nums, target):
		l = len(nums)

		dic = dict()
		for i in range(l):
			num = nums[i]
			if num not in dic:
				dic[num] = i

		for i in range(l):
			num = nums[i]
			other = target - num
			if other in dic:
				if dic[other] != i:
					ret = [dic[other]+1, i+1]
					ret.sort()
					return ret

		return []

if __name__ == "__main__":
	data = ( [3,2,4], 6 )
	s = Solution()
	print s.twoSum(data[0], data[1])
