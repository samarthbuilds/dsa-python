# DSA Practice in Python

This repository contains my implementations of **Data Structures and Algorithms using Python**.

The goal is to systematically practice core algorithmic patterns used in **software engineering interviews and real-world backend systems**.

Problems are mainly sourced from:

* LeetCode
* NeetCode roadmap
* Interview preparation sets

---

## What This Repository Shows

* Consistent DSA practice
* Understanding of core algorithmic patterns
* Clean Python implementations
* Organized problem categorization

Each solution includes:

* Approach explanation
* Time complexity
* Space complexity
* Clean and readable code

---

## Repository Structure

```
dsa-python
│
├── arrays
├── hashing
├── two_pointers
├── sliding_window
├── stack
├── linked_list
├── trees
├── graphs
└── dynamic_programming
```

Problems are grouped by **pattern / concept**, which reflects how algorithmic problem solving is actually learned.

---

## Example Implementation

```python
"""
Problem: Two Sum

Approach:
Use a hashmap to store numbers already seen.
For each number, check if the complement exists.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]

            seen[num] = i
```

---

## Current Focus

* Arrays and Hashing fundamentals
* Sliding Window patterns
* Tree and Graph traversal

The repository will grow as more problems and patterns are practiced.

---

## Purpose

This repository serves as a **public log of my algorithm practice and progress toward software engineering interviews**.

---

## Author

Samarth Singh
Computer Science Student
Interested in Backend Engineering and Systems
