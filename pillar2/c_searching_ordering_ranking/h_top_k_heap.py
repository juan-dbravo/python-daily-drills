"""
Drill 08 - Top-K with a Heap

Write top_k_items_heap(counts, k) with heapq. Match Drill 07's exact ordering:
count descending then item ascending. Return [] when k <= 0 and do not mutate
counts. Avoid sorting every input item when k is much smaller than n.

Target complexity: O(n log k) selection plus O(k log k) final ordering.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: optimize only after preserving the original behavioral contract.
"""

from heapq import nsmallest

def top_k_items_heap(
    counts: dict[str, int], k: int
) -> list[tuple[str, int]]:
    if k <= 0:
        return []

    items = counts.items()
    print(items)

    return nsmallest(k, items, key=lambda pair: (-pair[1], pair[0]))
