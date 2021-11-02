def add_recipes(dictionnaire):
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    name = input("Entrez le nom de votre recette?\n")
    ingrediants = input("Entrez la liste d'ingrédiants de la recette, svp séparer les ingrédiants par une ,\n").split(",")
    dictionnaire[name] = ingrediants

def add_recipes_file(source):
    with open(source,"a") as file:
        file.write(input("Entrez le nom de votre recette?\n") + ":" + input("Entrez la liste d'ingrédiants de la recette, svp séparer les ingrédiants par une ,\n")+ "\n")

def reconstituerDict(source):
    result = {}
    with open(source,"r") as file:
        for a in file:
            ingredientlist = a.split(":")[1].replace("\n","").split(",")
            result[a.split(":")[0]] = ingredientlist
    return(result)
def print_recipe(ingredients: dict) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    name = input("Entrez le nom d'une recette?\n")

    if name in ingredients:
        print(ingredients[name])
    else:
        print("La recette demandée n'existe pas!")
        print(f"Les recettes existantes sont: {list(ingredients.keys())}")

print (reconstituerDict("recettesListe"))