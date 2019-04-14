from typing import List


class Solution:
    answer_cnt = 0

    def get_grid_info(self, grid):
        ret = {
            'start_point': None,
            'required_visit_cnt': 1  # start point
        }
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    ret['start_point'] = (x, y)
                if grid[x][y] == 0:
                    ret['required_visit_cnt'] += 1
        return ret

    def visit(self, x, y, grid, cnt_info):
        # print("({}, {}) / {}".format(x,y,cnt_info))
        # for row in grid:
        #     print(row)

        if x < 0 or y < 0:
            return
        if x >= len(grid) or y >= len(grid[0]):
            return
        if grid[x][y] in [-1, 3]:
            return
        if grid[x][y] == 2:
            if cnt_info['full'] == cnt_info['current']:
                self.answer_cnt += 1
            return

        cnt_info['current'] += 1
        org_val = grid[x][y]
        grid[x][y] = 3
        self.visit(x - 1, y, grid, cnt_info)
        self.visit(x + 1, y, grid, cnt_info)
        self.visit(x, y - 1, grid, cnt_info)
        self.visit(x, y + 1, grid, cnt_info)
        grid[x][y] = org_val
        cnt_info['current'] -= 1

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        info = self.get_grid_info(grid)
        print("info:", info)
        x, y = info['start_point']
        count_info = {'current': 0, 'full': info['required_visit_cnt']}
        self.visit(x, y, grid, count_info)
        return self.answer_cnt


if __name__ == '__main__':
    input_grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
    answer = Solution().uniquePathsIII(input_grid)
    print(answer)
