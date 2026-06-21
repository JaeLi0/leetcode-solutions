# Two Pointers（双指针）

## 核心思路

双指针分两大类：

**碰撞指针**（左右向中间收缩）：用于排序数组或需要找两端关系的问题。核心判断：谁小移谁 / 谁不满足条件移谁。

**快慢指针**（同方向，一快一慢）：用于链表（找中点、判环）和数组原地操作（去重、移动零）。

## 通用模板

```python
# 碰撞指针
left, right = 0, len(arr) - 1
while left < right:
    # 根据条件决定移动哪边
    if 某个条件:
        left += 1
    else:
        right -= 1
```

## 题目列表

| 题号 | 题目 | 难度 | 关键词 |
|------|------|------|--------|
| 0011 | [盛水容器](../solutions/0001-0100/0011-container-with-most-water/) | Medium | 碰撞指针，谁小移谁 |
| 0042 | [接雨水](../solutions/0001-0100/0042-trapping-rain-water/) | Hard | 碰撞指针，维护左右最大值 |
| 0167 | [两数之和 II](../solutions/0101-0200/0167-two-sum-ii-input-array-is-sorted/) | Medium | 碰撞指针，排序数组 |
