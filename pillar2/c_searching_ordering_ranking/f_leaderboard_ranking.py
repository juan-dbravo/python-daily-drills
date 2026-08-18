"""
Drill 06 - Leaderboard Ranking

Each event has "player" and integer "points". Write leaderboard(events) that
normalizes players to lowercase, aggregates their points, and returns
(player, total) pairs by total descending then player ascending.

Empty input returns []. Target complexity: O(n + k log k), k unique players.

Complexity check:
State the worst-case time and extra-space Big-O. In one sentence, explain the
main cost and why your chosen data structure or pattern fits the problem.

Thinking goal: separate aggregation from ranking and specify deterministic ties.
"""


def leaderboard(events: list[dict]) -> list[tuple[str, int]]:
    totals = {}

    for event in events:
        player = event["player"].strip().lower()
        points = event["points"]

        totals[player] = totals.get(player, 0) + points

    result = list(totals.items())
    result.sort(key=lambda pair: (-pair[1], pair[0]))

    return result



events = [
    {"player": "Matthew", "points": 10},
    {"player": "Mary", "points": 15},
    {"player": "MATTHEW", "points": 8},
    {"player": "John", "points": 12},
    {"player": "mary", "points": 5},
    {"player": "Peter", "points": 7},
]


print(leaderboard(events))