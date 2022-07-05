from pprint import pprint

recipe_book = "recipe_book.txt"

def catalog_recipe(book):
    with open(book, 'r', encoding = 'utf-8') as catalog_rec:
        dict_recipe = {}
        for line in catalog_rec:
            recipe_name = line
            ingredients_recipe = []
            dict_ingredients = {}
            number_of_ingredients = catalog_rec.readline()
            for ingredients in range(int(number_of_ingredients)):
                ingredients = catalog_rec.readline()
                ingredients_list = list(ingredients.split("|"))
                dict_ingredients = { "ingredient_name" : ingredients_list[0],
                                     "quantity": ingredients_list[1],
                                     "measure": ingredients_list[2].strip()}
                ingredients_recipe.append(dict_ingredients)
            dict_recipe[recipe_name.strip()] = ingredients_recipe
            catalog_rec.readline()
    return dict_recipe

cook_book = catalog_recipe(recipe_book)
pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):

    list_ingredient = {}
    list_item = {}
    for food in dishes:
        if food  in cook_book.keys():
            for ingredient in cook_book[food]:
                component = list(ingredient.values())
                list_item = { f"{component[0]}": {"quantity": (int(component[1])*person_count), "measure": component[2]}}
                if component[0] in list(list_ingredient.keys()):
                    for product, quantity in list_item.items():
                        for quant, element in quantity.items():
                            if quant == 'quantity':
                                for key_quantity, recorded_quantity in list_ingredient[component[0]].items():
                                    if key_quantity == 'quantity':
                                        recorded_quantity += element
                                        list_item = { f"{component[0]}": {"quantity": recorded_quantity, "measure": component[2]}}
                                        list_ingredient.update(list_item)
                else:
                    list_ingredient.update(list_item)
        else:
            print(f"Рецепта {food}нет в книге")
    return list_ingredient

pprint((get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)))
