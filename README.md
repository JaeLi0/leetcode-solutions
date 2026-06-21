# LeetCode Solutions

个人 LeetCode 算法知识库。

配合 Claude Code 实现教学 + 归档一体化：在终端里讨论题目，讲完说「整理」，自动生成代码 + 笔记并 push。

## 特性

- **教学即归档**：CC 中讨论完题目，触发归档后自动生成文件并 push
- **代码与笔记分离**：`solution.py` 面向面试官（干净代码），`notes.md` 面向自己（详细思路 + 图解）
- **多解法对比**：每题保留暴力 → 最优的完整优化链条，标注推荐解
- **专题串联**：`topics/` 目录按算法专题组织，题目之间交叉链接

## 目录结构

```
├── solutions/              # 题解，按题号分段
│   └── 0001-0100/
│       └── 0042-trapping-rain-water/
│           ├── solution.py     # 面试展示：干净代码
│           └── notes.md        # 自己复习：详细笔记
├── topics/                 # 算法专题笔记
└── .codex/skills/          # CC Agent Skills
```

## 刷题进度

| 专题 | 已完成 | 题目 |
|------|--------|------|
| [Two Pointers](topics/two-pointers.md) | 3 | [11](), [42](solutions/0001-0100/0042-trapping-rain-water/), [167]() |
| Sliding Window | 3 | [3](), [424](), [1004]() |
| Hash Table | 0 | |
| Binary Tree | 0 | |
| Dynamic Programming | 0 | |
| Backtracking | 0 | |
| Greedy | 0 | |
| Stack | 0 | |
| Heap | 0 | |
| Graph | 0 | |

## 使用方式

在项目目录下打开 Claude Code，直接说：

```
讲一下 LC 42 接雨水
```

CC 会完成教学 → 生成笔记 → 归档 → commit + push 的完整流程。
