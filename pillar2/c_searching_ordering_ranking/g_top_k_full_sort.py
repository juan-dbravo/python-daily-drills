"""
Drill 07 - Top-K by Full Sort

Write top_k_items(counts, k) returning up to k (item, count) pairs ordered by
count descending then item ascending. Return [] when k <= 0. Do not mutate the
input and use a full sorted result followed by slicing.

Target complexity: O(n log n) time and O(n) auxiliary space.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: understand the simple baseline before optimizing selection.
"""


def top_k_items(counts: dict[str, int], k: int) -> list[tuple[str, int]]:
    result = []

    if k <= 0:
        return result
    
    result = list(counts.items())
    result.sort(key=lambda pair: (-pair[1], pair[0]))

    return result[0:k]


# Time: O(n log n) because all n dictionary items are fully sorted.
# Extra space: O(n) because the items are copied into a new list before sorting.


