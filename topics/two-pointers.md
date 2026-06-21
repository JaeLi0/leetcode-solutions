# Two Pointers 双指针

---

## ⚡ 速查卡

**识别信号**
- 排序数组 + 找两数之和 / 差 / 最大面积
- 需要同时追踪两端关系（左边界 + 右边界）
- 链表判环 / 找中点
- 数组原地去重 / 移动零

**两大模板**

```python
# 碰撞指针（左右向中间）
left, right = 0, len(arr) - 1
while left < right:
    if 满足条件:
        # 处理结果
    elif 左边太小:
        left += 1
    else:
        right -= 1

# 快慢指针（同方向）
slow, fast = 0, 0
while fast < len(arr):
    if 满足条件:
        arr[slow] = arr[fast]
        slow += 1
    fast += 1
```

**复杂度**：时间 O(n)，空间 O(1)

**什么时候不适合用**：无序且不能排序 / 需要三个及以上指针 / 需要知道所有组合（用回溯）

---

## 完整入门

### 为什么双指针有效？

暴力枚举两端 = O(n²)。双指针能降到 O(n) 的前提是：**移动一个指针之后，某些候选项可以被永久排除**。

以 LC 11 盛水容器为例：容积 = min(左高, 右高) × 宽。当左边比右边矮时，无论右指针往左移到哪里，宽度变小，容积只会更小。所以「移动短板」这个操作可以安全跳过所有以当前长板为端点的组合，消除 O(n) 的候选项，总共消除 n 次 = O(n)。

**核心：在维持某种不变量的前提下，每次移动都能永久淘汰一批候选。**

---

### 碰撞指针（左右向中间收缩）

**适用场景**：排序数组、需要找两端关系、答案依赖于最大/最小边界。

**判断移动哪边**：取决于题目的「短板逻辑」
- LC 11：谁小移谁（短板制约面积）
- LC 42：谁小移谁（短板决定水量上限）
- LC 167：和太大移右，和太小移左

**模板细节**

```python
left, right = 0, len(arr) - 1
while left < right:
    cur = compute(arr[left], arr[right])
    if cur == target:
        # 找到答案
        return ...
    elif need_larger:
        left += 1    # 左边太小，右移增大
    else:
        right -= 1   # 右边太大，左移减小
```

**本类型题目**

- [0011 - 盛水容器](../solutions/0001-0100/0011-container-with-most-water/) | Medium | 谁小移谁，短板制约面积
- [0042 - 接雨水](../solutions/0001-0100/0042-trapping-rain-water/) | Hard | 维护左右最大值，LC11 升级版
- [0167 - 两数之和 II](../solutions/0101-0200/0167-two-sum-ii-input-array-is-sorted/) | Medium | 排序数组，和太大移右、太小移左

---

### 快慢指针（同方向，一快一慢）

**适用场景**：链表操作、数组原地修改。

**链表用法**

```python
# 找链表中点
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
# 循环结束时 slow 在中点

# 判断链表有环
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False
```

**数组原地修改用法**

```python
# 移除重复元素（数组已排序）
slow = 0
for fast in range(len(nums)):
    if nums[fast] != nums[slow]:
        slow += 1
        nums[slow] = nums[fast]
return slow + 1
```

slow 始终指向「已处理的有效部分的末尾」，fast 负责探索新元素。

**本类型题目**

- [0141 - 链表有环](../solutions/0101-0200/0141-linked-list-cycle/) | Easy | Floyd 判环入门
- [0876 - 链表中点](../solutions/0801-0900/0876-middle-of-the-linked-list/) | Easy | 快慢指针找中点
- [0283 - 移动零](../solutions/0201-0300/0283-move-zeroes/) | Easy | 原地修改，slow 维护有效区间

---

### 常见陷阱

- **循环条件**：碰撞指针用 `left < right`（不含等于），等于时两指针指向同一个元素，无意义
- **死循环**：每次循环必须保证至少有一个指针移动
- **排序前提**：碰撞指针通常要求数组有序，无序数组要先排序

---

## 经典题型（必刷）

| 题号 | 题目 | 难度 | 为什么经典 |
|------|------|------|-----------|
| [0011](../solutions/0001-0100/0011-container-with-most-water/) | 盛水容器 | Medium | 碰撞指针入门，「谁小移谁」逻辑最干净 |
| [0042](../solutions/0001-0100/0042-trapping-rain-water/) | 接雨水 | Hard | 碰撞指针进阶，维护左右最大值，是 LC11 的升级版 |
| [0167](../solutions/0101-0200/0167-two-sum-ii-input-array-is-sorted/) | 两数之和 II | Medium | 排序数组双指针，最基础的收缩逻辑 |
| [0141](../solutions/0101-0200/0141-linked-list-cycle/) | 链表有环 | Easy | 快慢指针判环，Floyd 算法入门 |
| [0876](../solutions/0801-0900/0876-middle-of-the-linked-list/) | 链表中点 | Easy | 快慢指针找中点，链表题高频前置技能 |
| [0283](../solutions/0201-0300/0283-move-zeroes/) | 移动零 | Easy | 快慢指针原地修改，slow 维护有效区间 |

> 按子方法分类的完整题目索引见上方「碰撞指针 / 快慢指针」各小节末尾。
