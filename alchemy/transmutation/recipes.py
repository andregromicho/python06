# relativa
from ..potions import strength_potion
# absoluta
from alchemy.potions import create_air, create_fire


def lead_to_gold() -> str:
    return (
        "Recipe transmuting Lead to Gold: brew "
        f"'{create_air()}' and '{strength_potion()}' "
        f"mixed with '{create_fire()}'"
    )
