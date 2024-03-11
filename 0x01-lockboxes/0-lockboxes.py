#!/bin/bash/python3
"""interview question"""


def canUnlockAll(boxes):
    """unloack function"""
    n = len(boxes)
    visited = set()
    stack = [0]

    while stack:
        box = stack.pop()
        visited.add(box)

        for key in boxes[box]:
            if key < n and key not in visited:
                stack.append(key)

    return len(visited) == n
