import pytest
from pillar2.c_searching_ordering_ranking.a_linear_search import linear_search
from pillar2.c_searching_ordering_ranking.b_binary_search import binary_search
from pillar2.c_searching_ordering_ranking.c_manual_min_max import min_max
from pillar2.c_searching_ordering_ranking.d_compound_key_sorting import (
    sort_scores)
from pillar2.c_searching_ordering_ranking.e_stable_priority_ordering import (
    order_tasks,
)


def test_linear_search_returns_first_occurrence():
    assert linear_search([2, 4, 6, 8, 6], 6) == 2


def test_linear_search_returns_expected_for_absent_target():
    assert linear_search([2, 4, 6, 8, 6], 5) == -1


def test_linear_search_returns_minus_one_for_empty_list():
    assert linear_search([], 6) == -1


# Test for b_binary_search.py


def test_binary_search_returns_minus_one_for_not_present_target():
    items = [0, 1, 2, 7, 23, 34, 45]
    target = 56
    assert binary_search(items, target) == -1


def test_binary_search_finds_first_item():
    items = [0, 1, 2, 7, 23, 34, 45]
    assert binary_search(items, 0) == 0


def test_binary_search_finds_middle_item():
    items = [0, 1, 2, 7, 23, 34, 45]
    assert binary_search(items, 7) == 3


def test_binary_search_finds_one_occurrence_when_duplicates_exist():
    items = [1, 2, 2, 2, 3]
    result = binary_search(items, 2)

    assert result in (1, 2, 3)
    assert items[result] == 2


def test_binary_search_works_with_negative_numbers():
    items = [-20, -10, -3, 0, 8]
    assert binary_search(items, -10) == 1


# Test for drill c_manual_min_max.py


def test_min_max_raises_value_error_for_empty_list():
    numbers = []
    with pytest.raises(ValueError, match= "numbers cannot be empty"):
        min_max(numbers)


def test_min_max_returns_expected():
    numbers = [0, 1, -2, 7, 23, 34, -45]
    assert min_max(numbers) == (-45, 34)


def test_min_max_with_single_number():
    assert min_max([5]) == (5, 5)


# Test for drill d_compound_key_sorting.py


def test_sort_scores_uses_score_then_name():
    scores = {"Zoe": 8, "amy": 10, "Bob": 10}
    result = sort_scores(scores)
    assert result == [("amy", 10), ("Bob", 10), ("Zoe", 8)]


def test_sort_scores_does_not_mutate_input():
    scores = {"Zoe": 8, "amy": 10, "Bob": 10}
    original = scores.copy()
    sort_scores(scores)
    assert scores == original


def test_sort_scores_orders_scores_descending():
    scores = {"amy": 5, "andrew": 20, "alex": 0}
    result = sort_scores(scores)
    assert result == [("andrew", 20), ("amy", 5), ("alex", 0)]


def test_sort_scores_breaks_score_ties_by_name():
    scores = {"Zoe": 8, "amy": 10, "Bob": 10}
    result = sort_scores(scores)
    assert result == [("amy", 10), ("Bob", 10), ("Zoe", 8)]


# Test for drill e_stable_priority_ordering.py


def test_order_tasks_sorts_by_priority_descending():
    tasks = [
        {"name": "low", "priority": 1},
        {"name": "high", "priority": 5},
        {"name": "medium", "priority": 3},
    ]

    result = order_tasks(tasks)

    assert [task["name"] for task in result] == ["high", "medium", "low"]


def test_order_tasks_preserves_order_of_equal_priorities():
    tasks = [
        {"name": "first", "priority": 2},
        {"name": "high", "priority": 5},
        {"name": "second", "priority": 2},
    ]

    result = order_tasks(tasks)

    assert [task["name"] for task in result] == ["high", "first", "second"]


def test_order_tasks_returns_new_list_with_same_task_objects():
    first = {"name": "first", "priority": 1}
    second = {"name": "second", "priority": 2}
    tasks = [first, second]

    result = order_tasks(tasks)

    assert result is not tasks
    assert result == [second, first]
    assert result[0] is second
    assert result[1] is first