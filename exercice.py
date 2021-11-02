#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici
def tripleEspace(a:str):
    result = ""
    for l in a:
        if l == " ":
            result += "   "
        else:
            result += l
    return result

def tripleEspaceFile(source:str):
    sourceText = []
    with open(source,"r") as file:
        for l in file:
            sourceText.append(str(l))
    with open(source,"w") as file:
        for l in sourceText:
            file.write(tripleEspace(l))

notesToLettres = {
    (0,20):" F",
    (21,30):" E",
    (31,40):" D",
    (41,60):" C",
    (61, 80): " B",
    (81, 90): " A",
    (91, 100): " A*",

}
def gradation(n:int,table):
    print(n)
    toCheck = list(table.keys())
    lettre = ""
    for a in toCheck:
        if a[0]<=n<=a[1]:
            lettre = table[a]
            break
    return(str(n) + lettre)

def gradationFile(source:str,table):
    sourceText = []
    with open(source,"r") as file:
        for a in file:
            sourceText.append(int(a))
    print(sourceText)
    with open("source"+" mentions","w") as file:
        for a in sourceText:
            file.write(gradation(a, table))
            file.write("\n")


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    pass