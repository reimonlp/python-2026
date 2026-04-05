from copy import deepcopy
from typing import Final, TypedDict, TypeAlias


ContestantRoundData: TypeAlias = dict[str, int]


class RoundData(TypedDict):
    theme: str
    scores: dict[str, ContestantRoundData]


Rounds: TypeAlias = list[RoundData]


class ContestantStats(TypedDict):
    total_score: int
    rounds_won: int
    rounds_played: int
    best_round: int
    avg_score: float


Stats: TypeAlias = dict[str, ContestantStats]


rounds: Final[Rounds] = [
    {
        "theme": "Entrada",
        "scores": {
            "Valentina": {"judge_1": 8, "judge_2": 7, "judge_3": 9},
            "Mateo": {"judge_1": 7, "judge_2": 8, "judge_3": 7},
            "Camila": {"judge_1": 9, "judge_2": 9, "judge_3": 8},
            "Santiago": {"judge_1": 6, "judge_2": 7, "judge_3": 6},
            "Lucía": {"judge_1": 8, "judge_2": 8, "judge_3": 8},
        },
    },
    {
        "theme": "Plato principal",
        "scores": {
            "Valentina": {"judge_1": 9, "judge_2": 9, "judge_3": 8},
            "Mateo": {"judge_1": 8, "judge_2": 7, "judge_3": 9},
            "Camila": {"judge_1": 7, "judge_2": 6, "judge_3": 7},
            "Santiago": {"judge_1": 9, "judge_2": 8, "judge_3": 8},
            "Lucía": {"judge_1": 7, "judge_2": 8, "judge_3": 7},
        },
    },
    {
        "theme": "Postre",
        "scores": {
            "Valentina": {"judge_1": 7, "judge_2": 8, "judge_3": 7},
            "Mateo": {"judge_1": 9, "judge_2": 9, "judge_3": 8},
            "Camila": {"judge_1": 8, "judge_2": 7, "judge_3": 9},
            "Santiago": {"judge_1": 7, "judge_2": 7, "judge_3": 6},
            "Lucía": {"judge_1": 9, "judge_2": 9, "judge_3": 9},
        },
    },
    {
        "theme": "Cocina internacional",
        "scores": {
            "Valentina": {"judge_1": 8, "judge_2": 9, "judge_3": 9},
            "Mateo": {"judge_1": 7, "judge_2": 6, "judge_3": 7},
            "Camila": {"judge_1": 9, "judge_2": 8, "judge_3": 8},
            "Santiago": {"judge_1": 8, "judge_2": 9, "judge_3": 7},
            "Lucía": {"judge_1": 7, "judge_2": 7, "judge_3": 8},
        },
    },
    {
        "theme": "Final libre",
        "scores": {
            "Valentina": {"judge_1": 9, "judge_2": 8, "judge_3": 9},
            "Mateo": {"judge_1": 8, "judge_2": 9, "judge_3": 8},
            "Camila": {"judge_1": 7, "judge_2": 7, "judge_3": 7},
            "Santiago": {"judge_1": 9, "judge_2": 9, "judge_3": 9},
            "Lucía": {"judge_1": 8, "judge_2": 8, "judge_3": 7},
        },
    },
]


def _new_contestant_stats() -> ContestantStats:
    """Crea una estructura de estadísticas iniciales para un concursante."""
    return {
        "total_score": 0,
        "rounds_won": 0,
        "rounds_played": 0,
        "best_round": 0,
        "avg_score": 0.0,
    }


def _aggregate_stats(stats: Stats) -> Stats:
    """Resume puntajes acumulados, calcula totales y ordena por ranking final."""
    for contestant in stats.values():
        if contestant["rounds_played"] == 0:
            continue

        contestant["avg_score"] = (
            contestant["total_score"] / contestant["rounds_played"]
        )

    stats = dict(
        sorted(
            stats.items(),
            key=lambda item: item[1]["total_score"],
            reverse=True,
        )
    )
    return stats


def _process_round(current_round: RoundData, stats: Stats) -> None:
    """Procesa una ronda y actualiza puntajes, orden y ganadores."""
    round_scores = current_round["scores"]

    if not round_scores:
        return

    for contestant, judge_scores in round_scores.items():
        if contestant not in stats:
            stats[contestant] = _new_contestant_stats()
        stats_row = stats[contestant]

        total_score = sum(judge_scores.values())
        current_round["scores"][contestant]["total_score"] = total_score
        judge_scores["total_score"] = total_score

        stats_row["total_score"] += total_score

        stats_row["rounds_played"] += 1

        stats_row["best_round"] = max(stats_row["best_round"], total_score)

    sorted_scores = sorted(
        round_scores.items(),
        key=lambda item: item[1]["total_score"],
        reverse=True,
    )

    round_scores.clear()
    round_scores.update(sorted_scores)

    top_score = sorted_scores[0][1]["total_score"]

    winners = [
        contestant
        for contestant, scores in round_scores.items()
        if scores["total_score"] == top_score
    ]

    for winner in winners:
        stats[winner]["rounds_won"] += 1


def _calc_rounds_scores(rounds: Rounds) -> tuple[Rounds, Stats]:
    """Procesa todas las rondas y devuelve rondas actualizadas con estadísticas."""
    stats: Stats = {}

    for current_round in rounds:
        _process_round(current_round, stats)

    stats = _aggregate_stats(stats)

    return rounds, stats


def print_scores(rounds: Rounds) -> None:
    """Imprime el resumen por ronda y la tabla final de posiciones."""
    rounds_processed, stats = _calc_rounds_scores(deepcopy(rounds))

    for round_index, current_round in enumerate(rounds_processed, start=1):
        print(f"Ronda {round_index}: {current_round['theme']}")

        previous_score: int | None = None
        position = 1

        for contestant, scores in current_round["scores"].items():
            score = scores["total_score"]

            prefix = (f"{position:>3}º: ", " " * 6)[score == previous_score]
            print(f"{prefix}{contestant} ({score} pts)")

            if score != previous_score:
                position += 1
            previous_score = score

        print()

    print("\nTabla de posiciones final:\n")

    header = (
        f"{'Rondas':>30}{'Mejor':>8}\n"
        f"Cocinero{'Puntaje':>13}{'ganadas':>9}{'ronda':>8}{'Promedio':>10}"
    )
    chars_in_header = len(header.splitlines()[1])

    print(header)
    print("-" * chars_in_header)

    for contestant, data in stats.items():
        print(
            f"{contestant:<13}"
            f"{data['total_score']:^10}"
            f"{data['rounds_won']:^9}"
            f"{data['best_round']:^9}"
            f"{data['avg_score']:^8.1f}"
        )

    print("-" * chars_in_header)


if __name__ == "__main__":
    print_scores(rounds)