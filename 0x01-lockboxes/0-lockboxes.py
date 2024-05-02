#!/usr/bin/python3
"""
A python method that determines if all boxes can be opened
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked by using the keys in the first box
    """
    seen = set()
    unseen = [0]

    while len(unseen) > 0:
        present = unseen.pop()

        if not present or present >= len(boxes) or present < 0:
            continue

        seen.add(present)

        for key in boxes[present]:
            if key in seen:
                continue
            unseen.append(key)

    return len(seen) == len(boxes)
