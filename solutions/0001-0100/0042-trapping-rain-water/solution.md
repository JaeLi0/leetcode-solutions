---
id: 42
title: Trapping Rain Water
difficulty: Hard
tags: [two-pointers, dynamic-programming, monotonic-stack]
created: 2026-06-21
reviewed: []
mastery: 复习中
pass: 1
recommended: 双指针
---

# 42. Trapping Rain Water — 接雨水

**Hard** | [LeetCode CN](https://leetcode.cn/problems/trapping-rain-water/) | `two-pointers` `dynamic-programming` `monotonic-stack`

---

## Problem

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

**Example 1:**

```text
Input:  height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```

**Example 2:**

```text
Input:  height = [4,2,0,3,2,5]
Output: 9
```

**Constraints:**
- `1 <= n <= 2 * 10⁴`
- `0 <= height[i] <= 10⁵`

---

## 优化链条

| 解法 | 时间 | 空间 | 核心思路 |
|------|------|------|----------|
| 暴力 | O(n²) | O(1) | 每个位置各扫左右找最大值 |
| 前缀数组 | O(n) | O(n) | 预计算左右最大值，空间换时间 |
| ⭐ 双指针 | O(n) | O(1) | 两变量代替两数组，谁小移谁 |

> 暴力对每个位置都重新扫左右，重复计算。前缀数组把这个提前算好存起来，时间降到 O(n)，但多开了两个数组。双指针用两个变量代替两个数组，空间也降到 O(1)。

---

## ⭐ 解法三：双指针（推荐）

**思路**：两个指针从两头往中间走，各自维护自己这边的最大值。谁小移谁，因为短板决定水量。

> [!TIP]
> **为什么「谁小移谁」是对的？**
> 当 `height[left] < height[right]` 时，左边是短板。此时不管右边的柱子有多高，左侧位置能接的水只由 `left_max` 决定。所以可以直接结算左边，然后 `left += 1`。

```python
class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
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
```

**复杂度**
- 时间 O(n)：左右指针各走一遍，合计扫描 n 个位置
- 空间 O(1)：只用了 left / right / left_max / right_max 四个变量

### 逐行图解

以 `height = [2, 1, 3]` 为例：

```text
初始状态：
  height:   [2,  1,  3]
  index:     0   1   2
             L           R
  left_max=0, right_max=0, res=0

━━━ 第 1 轮：height[L]=2 < height[R]=3，走左边 ━━━

  height[left]=2 >= left_max=0 → 更新 left_max=2（新高度，不接水）
  left += 1

  height:   [2,  1,  3]
              *   L   R
  left_max=2, right_max=0, res=0

━━━ 第 2 轮：height[L]=1 < height[R]=3，走左边 ━━━

  height[left]=1 < left_max=2 → res += 2-1 = 1（接到水了）
  left += 1

  height:   [2,  1,  3]
              *   *  LR
  left_max=2, right_max=0, res=1

━━━ left == right，退出 ━━━

返回 res = 1 ✓
```

---

<details>
<summary>解法二：前缀最大值数组（辅助理解，点击展开）</summary>

> 从解法一到解法二：暴力对每个位置都重新扫左右找最大值，大量重复计算。把这些结果预先算好存起来就行。

**思路**：预先算好每个位置的左边最大值和右边最大值，存到两个数组里，然后一次遍历结算水量。

```python
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
```

- 时间 O(n)：三次独立遍历
- 空间 O(n)：两个长度为 n 的数组

</details>

<details>
<summary>解法一：暴力 O(n²)（点击展开）</summary>

**思路**：对每个位置，分别找它左边最高和右边最高的柱子，取较矮那个减去当前高度。

```python
class Solution3:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        res = 0
        for i in range(n):
            left_max = max(height[:i + 1])
            right_max = max(height[i:])
            res += min(left_max, right_max) - height[i]
        return res
```

- 时间 O(n²)：两层循环，外层 n 次，内层 max() 各扫一遍
- 空间 O(1)

</details>

---

## 易错点

> [!WARNING]
> **`left_max` / `right_max` 更新时机**：必须先比较当前高度和 max，再决定接水还是更新 max，顺序不能反。

> [!WARNING]
> **循环条件是 `left < right`，不是 `left <= right`**：两指针相遇时位置已处理过，不需要再算。

> [!NOTE]
> **「谁小移谁」判断的是 `height[left]` vs `height[right]`，不是 `left_max` vs `right_max`**：是当前柱子高度决定移动方向，不是历史最大值。

---

## 关联题目

- [LC 11 盛水容器](../0011-container-with-most-water/) — 同为碰撞指针，11 求面积最大，42 求能接多少水
- [LC 84 柱状图最大矩形](../0084-largest-rectangle-in-histogram/) — 单调栈解法的关联题
