"""
42. Trapping Rain Water | Hard
https://leetcode.cn/problems/trapping-rain-water/
Tags: two-pointers, dynamic-programming, monotonic-stack
"""


# ⭐ 解法一：双指针（推荐）
# 时间 O(n) — 左右指针各走一遍 | 空间 O(1) — 四个变量
class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
        return res


# 解法二：前缀最大值数组
# 时间 O(n) — 三次独立遍历 | 空间 O(n) — 两个辅助数组
class Solution2:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(left_max[i], right_max[i]) - height[i]
        return res


# 解法三：暴力
# 时间 O(n²) — 每个位置向左右各扫一遍找最大值 | 空间 O(1)
class Solution3:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        res = 0
        for i in range(n):
            left_max = max(height[:i + 1])
            right_max = max(height[i:])
            res += min(left_max, right_max) - height[i]
        return res
