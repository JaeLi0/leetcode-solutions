# Graph 图

---

## ⚡ 速查卡

**识别信号**
- 题目有「节点」「边」「连通」「路径」
- 二维网格上的连通区域（岛屿问题）
- 依赖关系 / 拓扑排序（课程安排）
- 最短路径

**两大遍历模板**

```python
# DFS（递归）
visited = set()
def dfs(node):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor)

# BFS（最短路径用这个）
from collections import deque
queue = deque([start])
visited = {start}
steps = 0
while queue:
    for _ in range(len(queue)):    # 按层处理
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    steps += 1
```

**建图**：`graph = defaultdict(list)`，`graph[u].append(v)`

---

## 完整入门

> 本专题开刷时填充。

---

## 经典题型（必刷）

| 题号 | 题目 | 难度 | 为什么经典 |
|------|------|------|-----------|
| 0200 | 岛屿数量 | Medium | DFS/BFS 入门，网格图模板 |
| 0133 | 克隆图 | Medium | DFS + 哈希表，图的遍历 |
| 0207 | 课程表 | Medium | 拓扑排序入门，判断有无环 |
| 0210 | 课程表 II | Medium | 拓扑排序输出路径 |
| 0994 | 腐烂的橘子 | Medium | 多源 BFS，同时从多个起点扩散 |
| 0127 | 单词接龙 | Hard | BFS 求最短转换路径 |

---

## 题目列表

| 题号 | 题目 | 难度 | 关键词 |
|------|------|------|--------|
