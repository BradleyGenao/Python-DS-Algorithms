from collections import defaultdict, deque

def find_all_recipes(recipes, ingredients, supplies):
    indg_to_recipe = defaultdict(list)
    in_degrees = defaultdict(int)
    for index, recipe in enumerate(recipes):
        for ing in ingredients[index]:
            indg_to_recipe[ing].append(recipe)
            in_degrees[recipe] +=1
    queue = deque([supply for supply in supplies])
    while queue:
        curr_supp = queue.popleft()
        for neigh in indg_to_recipe[curr_supp]:
            in_degrees[neigh] -=1
            if in_degrees[neigh] == 0:
                queue.append(neigh)
    ans = []
    for rec in recipes:
        if in_degrees[rec] == 0:
            ans.append(rec)
    return ans

recipes1 = ["bread"] 
ingredients1 = [["yeast","flour"]] 
supplies1 = ["yeast","flour","corn"]

recipes2 = ["bread","sandwich"] 
ingredients2 = [["yeast","flour"],["bread","meat"]]
supplies2 = ["yeast","flour","meat"]

recipes3 = ["bread","sandwich","burger"]
ingredients3 = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies3 = ["yeast","flour","meat"]

print("Expected: [bread] Actual: {}".format(find_all_recipes(recipes1, ingredients1, supplies1)) )
print("Expected: [bread, sandwich] Actual: {}".format(find_all_recipes(recipes2, ingredients2, supplies2)) )
print("Expected: [bread,sandwich,burger] Actual: {}".format(find_all_recipes(recipes3, ingredients3, supplies3)) )
