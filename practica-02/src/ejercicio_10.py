rounds = [
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


def _calc_round_scores(rounds):
    def sort_by_total_score(item):
        return item[1]["total_score"]

    stats = {
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
        for contestant, scores in current_round["scores"].items():
            round_score = sum(scores.values())

            scores["total_score"] = round_score
            stats[contestant]["round_scores"].append(round_score)

        current_round["scores"] = dict(
            sorted(
                current_round["scores"].items(),
                key=sort_by_total_score,
                reverse=True,
            )
        )

        top_score = max(
            data["total_score"]
            for data in current_round["scores"].values()
        )
        
        current_round["result"] = {
            "winners":  [
                contestant
                for contestant, data in current_round["scores"].items()
                if data["total_score"] == top_score
            ],
            "score": top_score,
        }

        for winner in current_round["result"]["winners"]:
            stats[winner]["rounds_won"] += 1

    for contestant, data in stats.items():
        data["total_score"] = sum(data["round_scores"])
        data["best_round"] = max(data["round_scores"])
        data["avg_score"] = data["total_score"] / len(data["round_scores"])

    stats = dict(
        sorted(
            stats.items(),
            key=sort_by_total_score,
            reverse=True,
        )
    )

    return rounds, stats


def print_scores(rounds):
    rounds, stats = _calc_round_scores(rounds[:])

    for i, current_round in enumerate(rounds):
        last_score = None
        position = 1

        print(f"Ronda {i+1}: {current_round['theme']}")
        for contestant, scores in current_round["scores"].items():
            score = scores["total_score"]

            print(f" {position:>2}º: " if score != last_score else " " * 6, end="")
            print(f"{contestant} ({score} pts)")

            if score != last_score:
                position += 1
            last_score = score
        print()

    print("Tabla de posiciones final:")

    print(
        f"{'Cocinero':<14} "
        f"{'Puntaje':<9} "
        f"{'Rondas ganadas':<16} "
        f"{'Mejor ronda':<13} "
        f"{'Promedio'}"
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