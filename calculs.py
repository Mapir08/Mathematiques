from random import randint, choice


def choix_add_sous():
    choix = choice([addition_pose(), soustraction_pose()])
    return choix


def choix_chrono():
    choix = choice([addition_pose(), soustraction_pose(), table_multiplication(randint(1, 9))])
    return choix


def addition_pose():
    valeur_a = randint(1, 999)
    valeur_b = randint(1, 999)
    resultat = valeur_a + valeur_b
    signe = "+"
    return resultat, valeur_a, valeur_b, signe


def soustraction_pose():
    valeur_a = randint(1, 999)
    valeur_b = randint(1, 999)
    if valeur_a < valeur_b:
        valeur_a, valeur_b = valeur_b, valeur_a
    resultat = valeur_a - valeur_b
    signe = "-"
    return resultat, valeur_a, valeur_b, signe


def multiplication(val_b=None):
    valeur_a = randint(1, 99)
    if val_b:
        valeur_b = val_b
    else:
        valeur_b = randint(1, 9)
    resultat = valeur_a * valeur_b
    signe = "x"
    return resultat, valeur_a, valeur_b, signe


def table_multiplication(val_b):
    valeur_a = randint(1, 10)
    valeur_b = val_b
    resultat = valeur_a * valeur_b
    signe = "x"
    return resultat, valeur_a, valeur_b, signe
