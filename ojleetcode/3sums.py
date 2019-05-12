class Triplet(object):
    elem_dic = dict()
    elem_sum = 0
    elem_cnt = 0

    def get_id(self):
        ret = []
        for k, v in self.elem_dic.items():
            ret.append("%s%s" % (k, v))
        return "".join(ret)

    def is_full(self):
        return self.elem_cnt == 3

    def get_cnt(self):
        return self.elem_cnt

    def get_sum(self):
        return self.elem_sum

    def get_list(self):
        ret = []
        for k, v in self.elem_dic.items():
            for i in range(v):
                ret.append(int(k))
        return ret

    def add(self, elem):
        self.elem_cnt += 1
        self.elem_sum += elem
        k = str(elem)
        if k in self.elem_dic:
            self.elem_dic += 1
        else:
            self.elem_dic[k] = 1


def get_key(_list):
    _list = sorted(_list)
    dic = dict()
    for elem in _list:
        selem = str(elem)
        if selem in dic:
            dic[selem] += 1
        else:
            dic[selem] = 1

    ret = list()
    for k, v in dic.items():
        ret.append("%s%s" % (k, v))
    return "".join(ret)


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        elem_cnt = len(nums)
        dup_dic = dict()
        ret = []
        for idx1 in range(elem_cnt):
            for idx2 in range(elem_cnt):
                if idx1 == idx2:
                    continue
                for idx3 in range(elem_cnt):
                    if (idx3 == idx1) or (idx3 == idx2):
                        continue
                    if (nums[idx1] + nums[idx2] + nums[idx3]) == 0:
                        zero_list = [nums[idx1], nums[idx2], nums[idx3]]
                        list_key = get_key(zero_list)
                        if list_key not in dup_dic:
                            dup_dic[list_key] = True
                            ret.append(zero_list)
        return ret

