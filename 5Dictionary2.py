import random

keys = ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]

characterA = {}

for key in keys:
    characterA[key] = random.randint(1, 20)

for (key, item) in characterA.items():
    print(key + ":", item)