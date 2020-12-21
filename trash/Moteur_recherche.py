#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from trash import outils

groupe_name = "AbouAchrafAmineAli"

def saisie_requete():
    """
    Lecture d'une requÃªte
    :return: la requÃªte
    """
    requete = input("Saisissez votre requete, * pour arreter : ")
    return requete


def pretraitement_requete(requete):
    """
    Effectue le pre-traitement de la requete (tokenization, stopword removal, stemming
    Renvoie le vecteur requÃªte
    :param requete:
    :return: vecteur requete
    """
    processed_text = outils.doc_preprocessing(requete)
    liste = outils.TextTowords(processed_text)
    dicoStem = {}
    for mot in liste:
        if mot in dicoStem.keys():
            dicoStem[mot] += 1
        else:
            dicoStem[mot] = 1
    return dicoStem


def normeVecteur(vecteur):
    """
    calcule la norme d'un vecteur (donne sous la forme d'un dictionnaire)
    """
    norme = 0
    # calcule la somme des poids au carre
    for (t, w) in vecteur.items():
        norme += w ** 2
    # renvoie la racine carre
    return math.sqrt(norme)


def calculeSimilarites(index, vecteurrequete):
    """
    Pour un document donnÃ© et une requete donnee, sous forme de vecteurs, calcule le cosinus et le renvoie
    """
    ldocs_cosinus = {}

    # parcours des racines de la requete
    for stem in vecteurrequete:
        if stem in index.keys():
            # parcours des documents contenant cette racine
            for doc in index[stem]:
                if doc in ldocs_cosinus.keys() and doc != 'df':
                    ldocs_cosinus[doc] += vecteurrequete[stem] * index[stem][doc]
                elif doc != 'df':
                    ldocs_cosinus[doc] = vecteurrequete[stem] * index[stem][doc]
    # calcul cosinus : produit scalaire / norme req
    for doc in ldocs_cosinus:
        ldocs_cosinus[doc] /= normeVecteur(vecteurrequete)
    return ldocs_cosinus


def max_dicodoc(ldocs_cosinus, doc_exclus):
    """
    Renvoie le couple (doc, cos) dont le cosinus est le maximum
    """
    max = ("", -1)
    for doc in ldocs_cosinus.keys():
        if ldocs_cosinus[doc] > max[1] and doc not in doc_exclus:
            max = (doc, ldocs_cosinus[doc])
    return max


def affiche_resultat(ldocs_cosinus, n):
    """
    Gestion de l'affichage des n documents les plus pertinents
    """
    if ldocs_cosinus == {}:
        print("Il n'y a aucun resultat pertinent pour cette requete. ")
    else:
        # s'il y a moins de n documents pertinents
        if len(ldocs_cosinus) < n:
            n = len(ldocs_cosinus)

        nbdocs = 0
        topn = {}
        exclus = []

        # boucle visant Ã  trouver les n documents les plus pertinents
        for i in range(1, n + 1):
            max_doc = max_dicodoc(ldocs_cosinus, exclus)
            exclus.append(max_doc[0])
            print("{}) Document {} - score {}\n".format(i, max_doc[0], max_doc[1]))
        print()


# Abou
def read_request_file():
    file = open("./data/request.txt", "r")
    lines = file.readlines()
    return lines


def put_result_file(ldocs_cosinus, n, req):
    output_file = open("./data/runs/" + "AbouAchrafAmineAli_01_01_btc_articles.txt", "a")
    if ldocs_cosinus == {}:
        print("Il n'y a aucun resultat pertinent pour cette requete. ")
    else:
        if len(ldocs_cosinus) < n:
            n = len(ldocs_cosinus)

        nbdocs = 0
        topn = {}

        exclus = []
        for i in range(1, n + 1):
            max_doc = max_dicodoc(ldocs_cosinus, exclus)
            exclus.append(max_doc[0])
            output_file.write("{} {} {} {} {} {} {}\n"
                              .format(req, "Q0", max_doc[0], i, max_doc[1], groupe_name, "/article[1]"))


if __name__ == "__main__":
    index = mon_index.MON_INDEX
    myrequest = read_request_file()
    for item in myrequest:
        request_preprocess = pretraitement_requete(item.split(":")[1].rstrip("\n"))
        put_result_file(calculeSimilarites(index, request_preprocess), 1500, item.split(":")[0])