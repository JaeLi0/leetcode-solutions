# Binary Tree 二叉树

---

## ⚡ 速查卡

**识别信号**
- 题目给的是 TreeNode 结构
- 需要遍历 / 计算树的属性（高度、直径、路径和）
- 判断对称 / 相同 / 子树关系

**核心模板**

```python
# DFS 递归（最常用）
def dfs(node):
    if not node:
        return 基础值
    left = dfs(node.left)
    right = dfs(node.right)
    return 当前层的计算结果

# BFS 层序遍历
from collections import deque
queue = deque([root])
while queue:
    node = queue.popleft()
    # 处理 node
    if node.left:  queue.append(node.left)
    if node.right: queue.append(node.right)
```

**写法视角**：只想当前层做什么，信任递归处理子树，不要脑内模拟全过程。

---

## 完整入门

> 本专题开刷时填充。

---

## 经典题型（必刷）

| 题号 | 题目 | 难度 | 为什么经典 |
|------|------|------|-----------|
| 0104 | 二叉树最大深度 | Easy | DFS 入门，最基础的后序遍历 |
| 0226 | 翻转二叉树 | Easy | 递归思维入门，「只想一层」的典型 |
| 0543 | 二叉树的直径 | Easy | 后序遍历 + 全局变量，高频模式 |
| 0102 | 二叉树层序遍历 | Medium | BFS 模板题 |
| 0124 | 二叉树最大路径和 | Hard | 后序遍历，路径跨根节点的处理 |
| 0236 | 二叉树最近公共祖先 | Medium | 分类讨论 + 后序，面试高频 |

---

## 题目列表

| 题号 | 题目 | 难度 | 关键词 |
|------|------|------|--------|
