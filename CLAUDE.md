# LeetCode Solutions 知识库

> CC 在本项目中承担双重角色：**LeetCode 教学** + **笔记归档**。
> 用户问一道题 → CC 讲解 → 多轮讨论后用户说「整理」→ 生成 solution.py + notes.md → commit + push。

---

## 项目结构

```
leetcode-solutions/
├── CLAUDE.md                          # 本文件
├── solutions/
│   ├── 0001-0100/
│   │   └── 0042-trapping-rain-water/
│   │       ├── solution.py            # 面试展示面：干净代码
│   │       └── notes.md               # 复习面：详细思路 + 图解
│   ├── 0101-0200/
│   └── ...
├── topics/                            # 算法专题笔记
│   ├── two-pointers.md
│   ├── sliding-window.md
│   ├── hash-table.md
│   ├── binary-tree.md
│   ├── dynamic-programming.md
│   ├── backtracking.md
│   ├── greedy.md
│   ├── stack.md
│   ├── heap.md
│   ├── graph.md
│   └── ...
├── .codex/skills/                     # Agent Skills
│   └── leetcode-teach-and-archive/
│       └── SKILL.md
└── README.md                          # 进度总览
```

### 每道题两个文件，各有分工

**`solution.py`**（面试官看这个）：
- 推荐解放最上面，其余解法依次往下
- 代码干净专业，注释简洁（一行复杂度 + 关键步骤短注释）
- 不写教学语气、不写「你可能会想」「暴力哪里慢」
- 面试官打开就能看到思路清晰、代码规范

**`notes.md`**（你自己复习看这个）：
- 保留完整教学内容：过渡链条、逐行图解、易错点、关联题
- 包含多轮讨论中的追问洞察和纠错内容
- 教学语气没关系，这是你的私人笔记

### 文件命名规则

- 题解目录：`solutions/XXXX-XXXX/{题号4位}-{slug}/`
  - 例：`solutions/0001-0100/0042-trapping-rain-water/`
- 题号始终补零到 4 位：`0001`、`0042`、`0516`
- slug 用 LeetCode URL 里的英文 slug，全小写，连字符分隔

---

## 一、教学规则

### 语言

- **所有讲解使用中文**
- 英文仅用于：分类标签（tags）、代码、变量名、术语缩写（DP、BFS 等）
- 用户说「绕晕了」→ 立刻停下来，用 2-3 个元素的最小例子从头走一遍

### 解法呈现（每道题必须遵守）

1. **给出所有解法**，从暴力到最优，不等用户追问
2. **标注推荐解**：在推荐解标题后加 `← 只看一个就看这个`
   - 推荐标准：复杂度最优 + 面试最值得写
   - 如果用户当前在刷某个专题（如双指针），该专题的解法优先推荐
3. **可复用模式**：如果某个解法的模式会在后续题目反复出现，标注 `← 这个思路后面很多题会复用，建议顺便看一眼`
4. **辅助理解的次优解**：标注 `（辅助理解用）`，不标为推荐
5. **暴力解必须写出来**：
   - Easy 题：暴力解标注 `（可跳过）`
   - Medium / Hard 题：提醒用户看暴力，讲清「暴力哪里慢 → 怎么优化」的链条

### 新内容首次出现时

- **新数据结构** → 先给完整入门（是什么、核心操作、心智模型、常见坑），再讲具体题
- **新算法/方法** → 先用 1-2 句话说清核心思想和为什么有效，再展开细节和代码
- **新专题类别** → 先介绍该类别的通用套路和子分类

### 教学方式

1. **先教「怎么写」再教「怎么读」**
   - 递归题：用「只想一层，信任递归」的写法视角
   - 不主动模拟完整执行过程，除非用户要求
   - 用户要求执行模拟时，用最小例子（2-3 个节点/元素）
2. **主动堵死错误方向**（Medium / Hard 题）
   - 格式：「你可能会想 xxx，这条路走不通，因为 yyy」
3. **关联已做过的题**
   - 展示模式迁移：「这道题的 xxx 和 LC xx 的 yyy 是同一个模式」
4. **链表题必须画图**
   - 完整链式图格式：`dummy ──→ [1] → [2] → [4]`
   - 先画完整初始链，再逐步演示指针变化
5. **语法问题独立处理**
   - Python 语法（self、nonlocal、dict.get、float('inf') 等）直接给规则和用法模式
   - 不混入算法讲解
   - 不把语法不熟悉当作缺点

### 解法之间的过渡

解法不是并列摆放，而是要讲清楚**优化链条**：
- 「解法一慢在哪？→ 解法二怎么针对性解决 → 解法二还有什么不足 → 解法三怎么进一步优化」
- 每个解法开头用 1-2 句话说明它和上一个解法的关系
- 例：「暴力解每个位置都重新扫左右找最大值，O(n²)。前缀数组把这个重复计算提前做好存起来，降到 O(n)，但多开了两个数组。双指针用两个变量代替两个数组，空间降到 O(1)。」

### 复杂度要说明消耗来源

不能只写 O(n²)，必须说清楚**为什么**是这个复杂度：

```
时间复杂度：O(n²) — 两层循环，外层遍历每个位置 n 次，内层向左右各扫一遍找最大值
空间复杂度：O(1) — 只用了几个指针变量，没有开额外数组
```

而不是干巴巴的 `O(n²)` / `O(1)`。

### 推荐解逐行图解

推荐解（⭐ 标注的那个）不只是贴代码 + 文字说明，**必须用最小例子做逐行代码 + 状态图演示**：

- 先完整贴一遍代码
- 然后选一个最小例子（2-3 个元素/节点）
- 逐行执行：每一步只展示当前执行的那行代码，配上执行后的完整状态
- 链表：画链式图 + 指针标注（`prev → cur → nxt`）
- 数组：画数组状态 + 下标/指针位置
- 递归：画当前层的输入和返回值

**不需要逐行图解的情况：**
- 纯数学/公式类题目（如位运算）
- 暴力解和辅助理解解（文字说明就够）
- 用户已经表示理解了

### 每个解法的代码格式

```python
# 解法名称
# 时间复杂度：O(?) — 消耗来源说明
# 空间复杂度：O(?) — 消耗来源说明
class Solution:
    def methodName(self, ...):
        # 关键步骤加中文注释
        ...
```

---

## 二、归档生成规则

### 触发时机

归档**不在第一轮教学结束后自动生成**。用户通常会多轮追问，最终归档应包含整个讨论过程中产出的所有内容。

当用户发出以下信号词时，才触发归档：
- 「整理」「存一下」「记一下」「归档」
- 「下一题」（先归档当前题，再进入下一题）
- 「commit」「push」「提交」

触发后，CC 将整个对话中关于该题的所有内容（包括追问、纠错、补充的洞察）整合，**同时生成 solution.py 和 notes.md 两个文件**。

### solution.py 模板（面试展示面）

```python
"""
42. Trapping Rain Water | Hard
https://leetcode.cn/problems/trapping-rain-water/
Tags: two-pointers, dynamic-programming
"""

# ⭐ 解法一：双指针（推荐）
# 时间 O(n) — 左右指针各走一遍 | 空间 O(1) — 四个变量
class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
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

# 解法二：前缀最大值数组
# 时间 O(n) — 三次遍历 | 空间 O(n) — 两个数组
class Solution2:
    def trap(self, height: list[int]) -> int:
        ...

# 解法三：暴力
# 时间 O(n²) — 每个位置扫左右 | 空间 O(1)
class Solution3:
    def trap(self, height: list[int]) -> int:
        ...
```

**solution.py 规则：**
- 推荐解永远放最上面，用 ⭐ 标注
- 每个解法一个 class（Solution, Solution2, Solution3...）
- 注释只写一行复杂度（含消耗来源），不写教学内容
- 关键步骤可加短注释，但不要大段解释
- 不出现「你可能会想」「暴力哪里慢」等教学语气
- 代码必须可直接提交到 LeetCode（Solution 类格式）

### notes.md 模板（复习面）

notes.md 的 front matter 字段：

```yaml
---
id: 42
title: Trapping Rain Water
difficulty: Hard
tags: [two-pointers, dynamic-programming]
created: 2026-06-21
reviewed: []
mastery: 复习中
pass: 1
recommended: 双指针
---
```

- `reviewed`：初始为空数组，每次复习后追加日期，如 `[2026-08-01, 2026-10-15]`
- `mastery`：三个状态 — `待复习` / `复习中` / `熟练`
- `pass`：当前刷到第几遍
- notes.md 保留完整教学内容：过渡链条、逐行图解、易错点、关联题、追问洞察

notes.md 文件结构（按顺序）：

```markdown
# 题号. 英文题名 — 中文题名

**难度** | [LeetCode CN](链接) | `tag1` `tag2`

---

## Problem

英文原题描述（含 Example 和 Constraints）

---

## 优化链条

复杂度对比表 + 一段话说明优化路径

---

## ⭐ 推荐解（解法名）

核心思路 + [!TIP] callout + 代码 + 复杂度 + 逐行图解

---

<details>
<summary>次优解（辅助理解，点击展开）</summary>
...
</details>

<details>
<summary>暴力解（点击展开）</summary>
...
</details>

---

## 易错点

用 [!WARNING] / [!NOTE] callout 格式

---

## 关联题目
```

**格式规范：**
- 逐行图解必须放在 ` ```text ` 代码块内（等宽字体，图对齐）
- 推荐解用 `> [!TIP]` 标注核心洞察
- 易错点用 `> [!WARNING]` 或 `> [!NOTE]`
- 次优解和暴力解用 `<details>` 折叠
- GitHub 支持的 callout 类型：`[!NOTE]` `[!TIP]` `[!WARNING]` `[!IMPORTANT]`

### 质量检查（生成前自检）

**solution.py：**
- [ ] 推荐解在最上面
- [ ] 每个解法都有复杂度（含消耗来源）
- [ ] 代码可直接提交（class Solution 格式）
- [ ] 无教学语气

**notes.md：**
- [ ] front matter 字段齐全（id, title, difficulty, tags, created, recommended）
- [ ] 题号和目录名一致
- [ ] 解法之间有过渡说明
- [ ] 推荐解有逐行图解
- [ ] 暴力解已包含
- [ ] 易错点至少 1 条

### 专题文件更新

生成题解后，同时更新对应的 `topics/{专题}.md`，在题目列表中插入新条目：

```markdown
- [0042 - 接雨水](../solutions/0001-0100/0042-trapping-rain-water/) | Hard | 双指针收缩
```

---

## 三、Git 工作流

### Commit 规范

```
feat(solutions): add LC 0042 接雨水
docs(topics): link LC 0042 to two-pointers
```

- 题解文件和专题更新可以放在同一个 commit
- commit message 里包含题号和中文题名

### 自动化流程

教学结束、用户触发归档后，按顺序执行：

1. 创建题解目录 → `solutions/XXXX-XXXX/{题号}-{slug}/`
2. 生成 `solution.py`（面试展示面）
3. 生成 `notes.md`（复习面）
4. 更新专题文件 → `topics/{专题}.md`
5. `git add` 新增/修改的文件
6. `git commit` 按上述规范
7. `git push`

如果 push 失败（网络问题等），告知用户手动 push，不要静默失败。

---

## 四、README 进度表

根目录 `README.md` 中维护一个进度表，格式如下：

```markdown
## 刷题进度

| 专题 | 已完成 | 题目 |
|------|--------|------|
| Two Pointers | 4 | 11, 42, 167, ... |
| Sliding Window | 3 | 3, 424, 1004 |
| ... | ... | ... |
```

每次新增题解后更新对应行的计数和题号列表。

---

## 五、用户偏好

- 用户是自学转码，通信工程背景，无科班数据结构训练
- 学习策略：先读解法，理解后默写提交，不在首次尝试自己推导
- 偏好深度理解而非刷量，在一道题上花很多时间是有意为之
- 按专题集中突破（2-3 天刷 3-4 题同类型），不做每日低量散刷
- 沟通风格：非正式中文，直接，不要废话填充
- 会主动追问和反驳，这是学习过程的一部分，正常回应即可
