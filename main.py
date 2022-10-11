# def tri_personnalise(e):
#     return len(e)


pizzas = ["4 fromages", "végétarienne", "hawai", "calzone"]


def affichez(collection, num=-1):
    # collection.sort(reverse=True, key=tri_personnalise)
    c = collection
    if num != -1:
        c = collection[0:num]
    nb_pizzas = len(c)
    if nb_pizzas == 0:
        print("AUCUNE PIZZA")
    else:
        print(f"------- LISTE DES PIZZAS ({nb_pizzas}) -------")
        for i in (c):
            print(i)
        print()
        print(f"Première pizza: {c[0]}")
        print(f"Dernière pizza: {c[-1]}")


# vide = ()


def user_add_pizza(collection):
    p = input("Pizza à ajouter: ")
    if p.lower() in collection:
        print("ERREUR: cette pizza existe")
    else:
        collection.append(p)
    """# pizza_existe(collection, p)
    if pizza_existe(collection, p):
        print("ERREUR: cette pizza existe")
    else:
        collection.append(p)"""


"""def pizza_existe(collection, p):
    # if p in collection:
    #     print("ERREUR: la pizza existe déja")
    #     quit()
    # else:
    #     collection.append(p)
    for i in collection:
        if i == p:
            return True
    return False"""


user_add_pizza(pizzas)
affichez(pizzas)


# lower() -> minuscules
# upper() -> majuscules
