# https://leetcode.com/problems/rectangle-area/

class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1 = (C-A) * (D-B)
        area2 = (G-E) * (H-F)
        if A==E and B==F and C==G and D==H:  # exact same
            return area1
        if C<=E or G<=A or D<=F or H<=B:  # no dup
            return area1 + area2
        else:  # dup
            x_list = [A,C,E,G]
            x_list.sort()
            y_list = [B,D,F,H]
            y_list.sort()
            dup_area = (x_list[2]-x_list[1]) * (y_list[2]-y_list[1])

            return area1 + area2 - dup_area
