recipes = {}
n = 0
one_recipe = []
with open('recipes.txt',encoding='utf-8') as f:
    for line in f:
        if line[:len(line)-1] != '':
            one_recipe.append(line[:len(line)-1])
        else:
            recipes[one_recipe[0]] = []
            for i in range(int(one_recipe[1])):
                recipes[one_recipe[0]].append({"ingredient_name": one_recipe[i+2].split(' | ')[0], "quantity": one_recipe[i+2].split(' | ')[1], "measure":one_recipe[i+2].split(' | ')[2]})
            one_recipe.clear()
        
def get_shop_list_by_dishes(dishes, person_count):
    d = {}
    for dish in dishes:
        for i in range(len(recipes[dish])):
            d[dish] = {"measure": recipes[dish][i]["measure"],"quantity": int(recipes[dish][i]["quantity"])*number}
            print(d[dish])

for name in recipes:
    print(name,':')
    for ingredient in recipes[name]:
        print("     ",ingredient)


print("Введите блюда через запятую, которые будем готовить")
food = input()
print("Введите кол-во гостей, для которых будет приготовлены блюда, которые вы ввели через запятую выше")
number = int(input())
get_shop_list_by_dishes(food.split(", "),number)


