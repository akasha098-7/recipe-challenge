from collections import defaultdict, deque

def findAllRecipes(recipes, ingredients, supplies):
    graph = defaultdict(list)
    indegree = {}

    for r, ing_list in zip(recipes, ingredients):
        indegree[r] = len(ing_list)
        for ing in ing_list:
            graph[ing].append(r)

    q = deque(supplies)
    result = []

    for r in recipes:
        if indegree[r] == 0:
            result.append(r)
            q.append(r)

    while q:
        item = q.popleft()
        for rec in graph.get(item, []):
            indegree[rec] -= 1
            if indegree[rec] == 0:
                result.append(rec)
                q.append(rec)

    return result

recipes = ["bread", "sandwich", "burger"]
ingredients = [["yeast", "flour"], ["bread", "ham"], ["sandwich", "patty"]]
supplies = ["yeast", "flour", "ham", "patty"]

print(findAllRecipes(recipes, ingredients, supplies))
