from copy import deepcopy
from typing import NotRequired, TypedDict, TypeAlias


class RoundResult(TypedDict):
    winners: list[str]
    score: int


ContestantScore: TypeAlias = dict[str, int]


class RoundData(TypedDict):
    theme: str
    scores: dict[str, ContestantScore]
    result: NotRequired[RoundResult]


Rounds: TypeAlias = list[RoundData]


class ContestantStats(TypedDict):
    round_scores: list[int]
    total_score: int
    rounds_won: int
    best_round: int
    avg_score: float


Stats: TypeAlias = dict[str, ContestantStats]


rounds: Rounds = [
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


def _init_stats(rounds: Rounds) -> Stats:
    if not rounds:
        return {}

    stats: Stats = {
        contestant: _new_contestant_stats()
        for contestant in rounds[0]["scores"]
    }
    return stats


def _new_contestant_stats() -> ContestantStats:
    return {
        "round_scores": [],
        "total_score": 0,
        "rounds_won": 0,
        "best_round": 0,
        "avg_score": 0,
    }


def _finalize_stats(stats: Stats) -> Stats:
    for contestant in stats.values():
        num_rounds: int = len(contestant["round_scores"])

        if num_rounds == 0:
            continue

        contestant["total_score"] = sum(contestant["round_scores"])
        contestant["best_round"] = max(contestant["round_scores"])
        contestant["avg_score"] = contestant["total_score"] / num_rounds

    stats = dict(
        sorted(
            stats.items(),
            key=lambda item: item[1]["total_score"],
            reverse=True,
        )
    )
    return stats


def _process_round(current_round: RoundData, stats: Stats) -> None:
    """Calcula puntajes por ronda y actualiza estadísticas acumuladas."""
    round_scores = current_round["scores"]

    # si no hay puntajes para esta ronda, se asigna un resultado vacío y se retorna
    if not round_scores:
        current_round["result"] = {"winners": [], "score": 0}
        return

    # Calcula el puntaje total para cada concursante en la ronda actual y actualiza
    # las estadísticas acumuladas.
    for contestant, judge_scores in round_scores.items():
        contestant_stats = stats.setdefault(contestant, _new_contestant_stats())
        total_score: int = sum(judge_scores.values())

        judge_scores["total_score"] = total_score
        contestant_stats["round_scores"].append(total_score)

    # Ordena los concursantes por puntaje total en la ronda actual y determina el
    # ganador o ganadores.
    sorted_scores = sorted(
        round_scores.items(),
        key=lambda item: item[1]["total_score"],
        reverse=True,
    )

    # Actualiza los puntajes ordenados en la ronda actual para facilitar la impresión posterior.
    current_round["scores"] = dict(sorted_scores)

    # El puntaje más alto en la ronda actual es el del primer concursante en la lista ordenada.
    top_score: int = sorted_scores[0][1]["total_score"]

    # Determina los ganadores de la ronda actual, que son aquellos concursantes
    # cuyo puntaje total es igual al puntaje más alto.
    winners: list[str] = [
        contestant
        for contestant, data in sorted_scores
        if data["total_score"] == top_score
    ]

    # Guarda el resultado de la ronda actual, incluyendo los ganadores y el puntaje más alto.
    current_round["result"] = {"winners": winners, "score": top_score}

    # Actualiza las estadísticas acumuladas para los ganadores de la ronda actual.
    for winner in winners:
        stats[winner]["rounds_won"] += 1


def _calc_rounds_scores(rounds: Rounds) -> tuple[Rounds, Stats]:
    # Inicializa las estadísticas acumuladas para cada concursante.
    stats: Stats = _init_stats(rounds)

    # Procesa cada ronda
    for current_round in rounds:
        _process_round(current_round, stats)

    # Finaliza de calcular las estadísticas
    stats = _finalize_stats(stats)

    return rounds, stats


def print_scores(rounds: Rounds) -> None:

    # Calcula los puntajes por ronda y las estadísticas acumuladas para cada concursante.
    rounds, stats = _calc_rounds_scores(deepcopy(rounds))

    for i, current_round in enumerate(rounds, start=1):
        last_score = None
        position = 1

        print(f"Ronda {i}: {current_round['theme']}")

        # Imprimir los concursantes ordenados por puntaje total en la ronda actual
        for contestant, scores in current_round["scores"].items():
            score = scores["total_score"]

            # Imprimir posición solo si el puntaje cambia respecto al anterior.
            print(f" {position:>2}º: " if score != last_score else " " * 6, end="")

            # Imprimir el nombre del concursante y su puntaje total en la ronda actual
            print(f"{contestant} ({score} pts)")

            if score != last_score:
                position += 1
            last_score = score
        print()

    print("Tabla de posiciones final:")
    print(
        f"{'Cocinero':<14} {'Puntaje':<9} {'Rondas ganadas':<16} {'Mejor ronda':<13} Promedio"
    )
    print("-" * 62)
    for contestant, data in stats.items():
        print(
            f"{contestant:<14} "
            f"{data['total_score']:<9} "
            f"{data['rounds_won']:<16} "
            f"{data['best_round']:<13} "
            f"{data['avg_score']:.1f}"
        )
    print("-" * 62)


if __name__ == "__main__":
    print_scores(rounds)
