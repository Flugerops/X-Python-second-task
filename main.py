def fix_ingredients(ingredients:list) -> list[str]:
    if not isinstance(ingredients, list):
        raise TypeError("ingredients must be list")
    if not all(isinstance(item, str) for item in ingredients):
        raise TypeError("All elements must be str")
    for item in ingredients:
        if not item.casefold().startswith("z"):
            ingredients[ingredients.index(item)] = item[::-1]
    return ingredients


if __name__ == "__main__":
    print(fix_ingredients(["sugar", "zmilk", "retaW", "salt", "honey"]))