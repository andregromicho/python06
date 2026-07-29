import alchemy

print("=== Distillation 1 ===")
print("Using: 'import alchemy' structure to access potions")
print(
    "Testing strenght_potion: "
    f"{alchemy.potions.strength_potion()}"
)
print(
    "Testing heal alias: "
    f"{alchemy.heal()}"
)
