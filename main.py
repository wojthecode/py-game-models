import init_django_orm  # noqa: F401
import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as json_input:
        players = json.load(json_input)

    for nickname, player in players.items():

        race = Race.objects.get_or_create(
            name=player["race"]["name"],
            defaults={"description": player["race"]["description"]}
        )

        for skill in player["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults={
                    "bonus": skill["bonus"],
                    "race": race[0]
                }
            )

        guild = Guild.objects.get_or_create(
            name=player["guild"]["name"],
            defaults={
                "description": player["guild"]["description"]
                if player["guild"]["description"] else None
            }
        ) if player["guild"] else None

        Player.objects.create(
            nickname=nickname,
            email=player["email"],
            bio=player["bio"],
            race=race[0],
            guild=guild[0] if guild else None
        )


if __name__ == "__main__":
    main()
