import pytest

from solutions.lowest_common_ancestor_of_a_binary_search_tree import Solution, TreeNode


@pytest.fixture
def problem_tree(request):
    data = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    return root


class TestLowestCommonAncestorBst:

    def test_problem_case1(self, problem_tree):
        expect = 6
        actual = Solution().lowest_common_ancestor(problem_tree, TreeNode(2), TreeNode(8)).val
        assert actual == expect

    def test_problem_case2(self, problem_tree):
        expect = 2
        actual = Solution().lowest_common_ancestor(problem_tree, TreeNode(2), TreeNode(4)).val
        assert actual == expect
