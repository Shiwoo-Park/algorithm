import os
from ojleetcode.lowest_common_ancestor_of_a_binary_tree import Solution, Solution2, TreeNode

if __name__ == "__main__":
    s = Solution2()
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t1.left = t2

    tree = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree4 = TreeNode(4)
    tree5 = TreeNode(5)
    tree6 = TreeNode(6)
    tree.left = tree2
    tree.right = tree3
    tree2.left = tree4
    tree2.right = tree5
    tree3.left = tree6
    rets = s.lowestCommonAncestor(tree, tree4, tree6)
    print(rets)

    # for ret in rets:
    #     for row in ret:
    #         print(row)
    #     print("=====================")

    # files = os.listdir(".")
    # for file in files:
    # 	os.rename(file, file.replace("-", "_"))
