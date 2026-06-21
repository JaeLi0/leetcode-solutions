# Heap 堆 / 优先队列

---

## ⚡ 速查卡

**识别信号**
- 动态维护「第 K 大 / 小」
- 需要反复取最大值或最小值
- 合并 K 个有序列表
- Top K 问题

**Python 操作**

```python
import heapq

# Python 只有最小堆
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
top = heapq.heappop(heap)     # 弹出最小值 1
peek = heap[0]                 # 查看最小值（不弹出）

# 最大堆：存负数
heapq.heappush(heap, -val)
max_val = -heapq.heappop(heap)

# 列表直接建堆 O(n)
heapq.heapify(arr)

# 存元组，按第一个元素排序
heapq.heappush(heap, (priority, value))
```

**复杂度**：push / pop O(log n)，建堆 O(n)

---

## 完整入门

> 本专题开刷时填充。

---

## 经典题型（必刷）

| 题号 | 题目 | 难度 | 为什么经典 |
|------|------|------|-----------|
| 0215 | 数组中第 K 大元素 | Medium | 小顶堆维护 K 大，堆入门 |
| 0347 | 前 K 个高频元素 | Medium | 频率 + 堆，Counter 组合 |
| 0023 | 合并 K 个升序链表 | Hard | 堆经典应用，K 路归并 |
| 0295 | 数据流中位数 | Hard | 双堆维护中位数，设计题 |
| 0355 | 设计推特 | Medium | 堆 + 链表，综合设计 |

---

## 题目列表

| 题号 | 题目 | 难度 | 关键词 |
|------|------|------|--------|
