"""
Drill 06 - Leaderboard Ranking

Each event has "player" and integer "points". Write leaderboard(events) that
normalizes players to lowercase, aggregates their points, and returns
(player, total) pairs by total descending then player ascending.

Empty input returns []. Target complexity: O(n + k log k), k unique players.

Complexity: O(n + k log k) time, where n is the number of events and k unique players.
Worst-case time: O(n log n) when every event belongs to a unique player.
Extra space: O(k), or O(n) in the worst case.

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

# Time: O(n + k log k), where n is the number of events and k is the number of unique players.
# Worst-case time: O(n log n) when every player is unique.
# Space: O(k), or O(n) in the worst case.