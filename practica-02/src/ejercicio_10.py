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


def _calc_round_scores(rounds: Rounds) -> tuple[Rounds, Stats]:
    stats: Stats = {
        contestant: {
            "round_scores": [],
            "total_score": 0,
            "rounds_won": 0,
            "best_round": 0,
            "avg_score": 0,
        }
        for contestant in rounds[0]["scores"].keys()
    }

    for current_round in rounds:
        # Calcular el puntaje total de cada concursante en la ronda actual
        for contestant, scores in current_round["scores"].items():
            round_score: int = sum(scores.values())

            scores["total_score"] = round_score
            stats[contestant]["round_scores"].append(round_score)

        # Ordenar los concursantes por puntaje total en la ronda actual
        current_round["scores"] = dict(
            sorted(
                current_round["scores"].items(),
                key=lambda item: item[1]["total_score"],
                reverse=True,
            )
        )

        # Determinar el puntaje más alto en la ronda actual
        top_score: int = max(
            data["total_score"] for data in current_round["scores"].values()
        )

        # Identificar a los ganadores de la ronda actual (puede haber empates)
        winners: list[str] = [
            contestant
            for contestant, data in current_round["scores"].items()
            if data["total_score"] == top_score
        ]

        # Guardar el resultado de la ronda actual, incluyendo los ganadores y su puntaje
        current_round["result"] = {
            "winners": winners,
            "score": top_score,
        }

        # Actualizar las estadísticas de los concursantes ganadores de la ronda actual
        for winner in current_round["result"]["winners"]:
            stats[winner]["rounds_won"] += 1

    # Calcular total, mejor ronda y promedio de puntajes para cada concursante.
    for contestant, data in stats.items():
        data["total_score"] = sum(data["round_scores"])
        data["best_round"] = max(data["round_scores"])
        data["avg_score"] = data["total_score"] / len(data["round_scores"])

    # Ordenar las estadísticas de los concursantes por puntaje total
    stats = dict(
        sorted(
            stats.items(),
            key=lambda item: item[1]["total_score"],
            reverse=True,
        )
    )

    # Devolver rondas con puntajes totales y estadísticas de concursantes.
    return rounds, stats


def print_scores(rounds: Rounds) -> None:
    rounds, stats = _calc_round_scores(deepcopy(rounds))

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