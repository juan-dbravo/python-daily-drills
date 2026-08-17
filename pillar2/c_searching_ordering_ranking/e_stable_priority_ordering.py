"""
Drill 05 - Stable Priority Ordering

Each task is a dict with "name" and integer "priority". Write order_tasks(tasks)
returning new task references sorted by priority descending. Tasks tied on
priority must remain in their original order. Do not add an artificial tie key.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: use Python's stable sort intentionally and preserve meaningful order.
"""


def order_tasks(tasks: list[dict]) -> list[dict]:
    return sorted(
        tasks,
        key= lambda task: task["priority"],
        reverse=True
    )


# Time: O(n log n)
# Extra space: O(n)
# Sorting is the main cost, and Python's stable sorted() preserves the
# original order of tasks with equal priorities while returning a new list.