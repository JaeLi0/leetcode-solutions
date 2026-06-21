# LeetCode Solutions

A personal LeetCode knowledge base — not a dump of accepted code, but a structured, searchable record of *how* each problem is solved and *why* the approach works. Built around an AI-driven workflow that turns each problem discussion into a permanent note.

---

## Features

- **Persistent knowledge base** — Conversations with AI don't disappear after the session. Most people solve a problem with AI's help, close the tab, and remember nothing the second time around. Here, every discussion is archived into a structured note with reasoning chains, diagrams, and key insights — a reference you can actually review months later.
- **Agent-powered archiving** — A custom Claude Code Agent Skill handles the busywork: generating the note from the discussion, updating the topic index, and committing. The thinking stays manual; the bookkeeping is automated.
- **Topic-based navigation** — Problems are indexed by algorithm in `topics/`, each broken down into sub-patterns with reusable templates. Find problems by *technique*, not just by number.
- **Spaced-repetition tracking** — Each note carries front matter (`pass`, `reviewed`, `mastery`) to track how many times a problem has been revisited and how well it's understood.

---

## Workflow

```
Discuss a problem in Claude Code
        │
        ▼
Trigger the archiving step ("整理")
        │
        ▼
Agent Skill generates the note  →  updates the topic index  →  commits & pushes
```

Solving stays a manual, deliberate process. Once a problem is understood, a single trigger turns the whole discussion into a clean note, links it into the relevant topic page, and pushes it — no copy-pasting, no formatting by hand.

---

## Topics

Indexes live in `topics/`. Each page covers the core idea, sub-patterns with template code, and a list of solved problems linking back to their notes.

| Topic | Index |
|-------|-------|
| Two Pointers | [topics/two-pointers.md](topics/two-pointers.md) |
| Sliding Window | [topics/sliding-window.md](topics/sliding-window.md) |
| Hash Table | [topics/hash-table.md](topics/hash-table.md) |
| Binary Tree | [topics/binary-tree.md](topics/binary-tree.md) |
| Dynamic Programming | [topics/dynamic-programming.md](topics/dynamic-programming.md) |
| Backtracking | [topics/backtracking.md](topics/backtracking.md) |
| Greedy | [topics/greedy.md](topics/greedy.md) |
| Stack | [topics/stack.md](topics/stack.md) |
| Heap | [topics/heap.md](topics/heap.md) |
| Graph | [topics/graph.md](topics/graph.md) |

---

## Directory Structure

```
leetcode-solutions/
├── solutions/                  # problem notes, 100 per folder
│   └── 0001-0100/
│       └── 0042-trapping-rain-water/
│           └── solution.md     # full write-up for one problem
├── topics/                     # algorithm indexes (entry point for browsing by technique)
│   └── two-pointers.md
├── SKILL.md                    # Agent Skill definition (the archiving workflow)
└── CLAUDE.md                   # project rules for Claude Code
```

Two entry points: browse by **number** under `solutions/`, or by **technique** under `topics/`. The two link to each other, so a topic page is the index and the solution notes are the content.

---

## About the Notes

Each `solution.md` is the heart of this repo — written for review, not just storage. A note contains:

- The full problem statement and constraints
- An **optimization chain**: brute force → better → optimal, with a short explanation of *why* each step improves on the last
- The recommended solution walked through **line by line on a minimal example**, with state diagrams
- Sub-optimal and brute-force solutions kept in collapsible sections for reference
- Common pitfalls and links to related problems

The notes are written in Chinese (my working language for studying); code, tags, and structure are language-agnostic. The goal is simple: open a note six months later and immediately re-derive the solution without starting from scratch.
