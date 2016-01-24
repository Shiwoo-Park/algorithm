# https://leetcode.com/problems/integer-to-roman/

class Solution:
    # @param {integer} num
    # @return {string}
    def translate(self, num):
        if num in self.num_dic:
            return self.num_dic[num]

        ret = ""
        for num_key in self.num_key_list:
            while num >= num_key :
                ret += self.num_dic[num_key]
                num -= num_key
        return ret

    def intToRoman(self, num):
        self.num_dic = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}
        self.num_key_list = [1000, 500, 100, 50, 10, 5, 1]
        thousand = (num / 1000) * 1000
        num = num % 1000
        hundred = (num / 100) * 100
        num = num % 100
        ten = (num / 10) * 10
        num = num % 10
        one = num / 1
        check_nums = [thousand, hundred, ten, one]
        ret = ""
        for n in check_nums:
            if n != 0:
                ret += self.translate(n)
        return ret