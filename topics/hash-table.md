# Hash Table 哈希表

---

## ⚡ 速查卡

**识别信号**
- 需要 O(1) 查找某个值是否存在
- 统计频率 / 计数
- 「两数之和」类：找 target - x
- 需要记录「上次出现位置」

**Python 常用操作**

```python
# 计数
from collections import Counter
cnt = Counter(nums)          # {元素: 频率}
cnt['a']                     # 不存在返回 0

# 默认值字典
from collections import defaultdict
d = defaultdict(int)         # 不存在的 key 默认为 0
d = defaultdict(list)        # 不存在的 key 默认为 []

# 普通 dict 安全访问
d.get(key, 0)                # 不存在返回 0
```

**复杂度**：时间 O(n)，空间 O(n)

---

## 完整入门

> 本专题开刷时填充。

---

## 经典题型（必刷）

| 题号 | 题目 | 难度 | 为什么经典 |
|------|------|------|-----------|
| 0001 | 两数之和 | Easy | 哈希表入门，「补数查找」模式 |
| 0049 | 字母异位词分组 | Medium | 排序后做 key，分组套路 |
| 0128 | 最长连续序列 | Medium | 用 set 实现 O(n) |
| 0560 | 和为 K 的子数组 | Medium | 前缀和 + 哈希表，高频组合 |
| 0146 | LRU 缓存 | Medium | 哈希表 + 双向链表，系统设计前置 |

---

## 题目列表

| 题号 | 题目 | 难度 | 关键词 |
|------|------|------|--------|
