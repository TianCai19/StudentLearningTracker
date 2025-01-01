"""Two Sum problem solution.

Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

Assumptions:
- Each input has exactly one solution
- Cannot use the same element twice
- Can return the answer in any order

Problem link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
"""


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []


# Test cases
def test_two_sum():
    """Test cases for two_sum function."""
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("All test cases passed!")


if __name__ == "__main__":
    test_two_sum()
