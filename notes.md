---
id: 42
title: Trapping Rain Water
difficulty: Hard
tags: [two-pointers, dynamic-programming, monotonic-stack]
created: 2026-06-21
reviewed:
recommended: 双指针
---

# 42. 接雨水

## 题目链接

https://leetcode.cn/problems/trapping-rain-water/

## 题目描述

给定 n 个非负整数表示柱子高度的数组，计算下雨后能接住多少水。

---

## 解法一：暴力（辅助理解用）

**思路**：对每个位置，分别找它左边最高和右边最高的柱子，取较矮的那个，减去当前高度就是这个位置能接的水。

```python
# 时间复杂度：O(n²) — 两层循环，外层遍历每个位置 n 次，内层 max() 向左右各扫一遍
# 空间复杂度：O(1) — 只用了几个变量
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        res = 0
        for i in range(n):
            left_max = max(height[:i + 1])
            right_max = max(height[i:])
            res += min(left_max, right_max) - height[i]
        return res
```

---

## 解法二：前缀最大值数组（辅助理解用）

> 🔗 **从解法一到解法二**：暴力对每个位置都重新扫左右找最大值，大量重复计算。预先算好存起来就行。

**思路**：预先算好每个位置的左边最大值和右边最大值，存到两个数组里。

```python
# 时间复杂度：O(n) — 三次独立的 for 循环，各扫一遍数组
# 空间复杂度：O(n) — 开了 left_max 和 right_max 两个长度为 n 的数组
class Solution:
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

---

## ⭐ 解法三：双指针 ← 只看一个就看这个

> 🔗 **从解法二到解法三**：前缀数组解决了重复计算，但多开了 O(n) 空间。其实只需要两个变量就够。

**思路**：用两个指针从两头往中间走，各自维护自己这边的最大值。谁小移谁，因为短板决定水量。

> 💡 这个思路后面很多题会复用，建议顺便看一眼

```python
# 时间复杂度：O(n) — 左右指针各走一遍，合计扫描 n 个位置
# 空间复杂度：O(1) — 只用了 left, right, left_max, right_max 四个变量
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

### 逐行图解（最小例子）

以 `height = [2, 1, 3]` 为例：

```
初始状态：
height: [2, 1, 3]
         L        R
left_max = 0, right_max = 0, res = 0

─── height[L]=2 < height[R]=3，走左边 ───

代码：left_max = height[left]  →  left_max = 2
      （height[left]=2 >= left_max=0，更新 max，不加水）
代码：left += 1
状态：[2, 1, 3]
            L  R
      left_max=2, right_max=0, res=0

─── height[L]=1 < height[R]=3，走左边 ───

代码：res += left_max - height[left]  →  res += 2 - 1 = 1
      （height[left]=1 < left_max=2，能接水）
代码：left += 1
状态：[2, 1, 3]
               LR
      left_max=2, right_max=0, res=1

─── left == right，退出循环 ───

返回 res = 1 ✓
```

---

## 暴力 → 优化链条

1. **暴力 O(n²)**：每个位置都重新扫左右找最大值 → 重复计算
2. **前缀数组 O(n)/O(n)**：预计算左右最大值数组，消除重复扫描 → 但多开了两个数组
3. **双指针 O(n)/O(1)**：用两个变量代替两个数组，谁小移谁 → 空间降到 O(1)

## 易错点

- `left_max` 和 `right_max` 的更新时机：先更新 max，再算水量（或者先比较再更新，取决于写法，但不能搞反）
- `while left < right` 不是 `left <= right`：两个指针相遇时不需要再算
- 「谁小移谁」的判断对象是 `height[left]` 和 `height[right]`，不是 `left_max` 和 `right_max`

## 关联题目

- [LC 11 盛水容器](../0011-container-with-most-water/) — 同为碰撞指针，但 11 求面积最大，42 求能接多少水
- [LC 84 柱状图最大矩形](../0084-largest-rectangle-in-histogram/) — 单调栈解法的关联题
