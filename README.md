# LeetCode Solutions

个人 LeetCode 算法知识库，配合 Claude Code 实现教学 + 归档一体化。

在终端里讨论题目，讲完说「整理」，自动生成代码 + 笔记并 push。

---

## 特性

- **教学即归档**：CC 中讨论完题目，一句「整理」自动生成文件并 push
- **代码与笔记分离**：`solution.py` 面向面试官（干净代码），`notes.md` 面向自己（详细思路 + 图解）
- **多解法对比**：每题保留暴力 → 最优的完整优化链条，标注推荐解
- **专题串联**：`topics/` 目录按算法专题组织，题目之间交叉链接

---

## 算法专题

| 专题 | 进度 | 完成 / 计划 |
|------|------|-------------|
| [Two Pointers 双指针](topics/two-pointers.md) | `████░░░░░░` | 3 / 15 |
| [Sliding Window 滑动窗口](topics/sliding-window.md) | `░░░░░░░░░░` | 0 / 10 |
| [Hash Table 哈希表](topics/hash-table.md) | `░░░░░░░░░░` | 0 / 10 |
| [Binary Tree 二叉树](topics/binary-tree.md) | `░░░░░░░░░░` | 0 / 15 |
| [Dynamic Programming 动规](topics/dynamic-programming.md) | `░░░░░░░░░░` | 0 / 20 |
| [Backtracking 回溯](topics/backtracking.md) | `░░░░░░░░░░` | 0 / 10 |
| [Greedy 贪心](topics/greedy.md) | `░░░░░░░░░░` | 0 / 10 |
| [Stack 栈](topics/stack.md) | `░░░░░░░░░░` | 0 / 8 |
| [Heap 堆](topics/heap.md) | `░░░░░░░░░░` | 0 / 8 |
| [Graph 图](topics/graph.md) | `░░░░░░░░░░` | 0 / 12 |

> 每道题的掌握程度和复习记录在各题的 `notes.md` front matter 中维护。

---

## 目录结构

```
├── solutions/              # 题解，按题号分段
│   └── 0001-0100/
│       └── 0042-trapping-rain-water/
│           ├── solution.py     # 面试展示：干净代码
│           └── notes.md        # 自己复习：详细笔记
└── topics/                 # 算法专题笔记
```

---

## 使用方式

在项目目录下打开 Claude Code，直接说：

```
讲一下 LC 42 接雨水
```

CC 完成：教学 → 生成笔记 → 归档 → commit + push。
