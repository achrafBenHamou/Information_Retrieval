#!/usr/bin/env python
# -*- coding: utf-8 -*-

import indexer, monindex, outils, math

def welcome(user):
    """
    Affichage d'accueil du moteur
    :param user:
    :return: None
    """
    print("=======================================================================")
    print()
    print("Bienvenue {}".format(user))
    print()
    print("Ce moteur de recherche indexe {} documents. ".format(indexer.NBDOCS))
    print()

def saisie_requete():
    """
    Lecture d'une requÃªte
    :return: la requÃªte
    """
    requete = input("Saisissez votre requÃªte, * pour arrÃªter : ")
    return requete

def pretraitement_requete(requete):
    """
    Effectue le prÃ©-traitement de la requÃªte (tokenization, stopword removal, stemming
    Renvoie le vecteur requÃªte
    :param requete:
    :return: vecteur requÃªte
    """
    liste_mots_requete = indexer.filtreMots(outils.string2list(requete))

    # suppression des mots outils
    liste = indexer.filtreMotsOutils(liste_mots_requete)
    print("sans mots outils : " + str(liste))
    # stemming
    dicoStem = {}
    for mot in liste:
        rac = outils.mot2racine(mot)
        if rac in dicoStem.keys():
            dicoStem[rac] += 1
        else:
            dicoStem[rac] = 1
    return dicoStem

def normeVecteur(vecteur):
    """
    calcule la norme d'un vecteur (donnÃ© sous la forme d'un dictionnaire)
    """
    norme = 0
    # calcule la somme des poids au carrÃ©
    for (t, w) in vecteur.items():
        norme += w**2
    # renvoie la racine carrÃ©e
    return math.sqrt(norme)

def calculeSimilarites(index, vecteurrequete):
    """
    Pour un document donnÃ© et une requÃªte donnÃ©e, sous forme de vecteurs, calcule le cosinus et le renvoie
    """
    ldocs_cosinus = {}

    # parcours des racines de la requÃªte
    for stem in vecteurrequete:
        if stem in index.keys():
            # parcours des documents contenant cette racine
            for doc in index[stem]:
                if doc in ldocs_cosinus.keys() and doc !='df':
                    ldocs_cosinus[doc] += vecteurrequete[stem] * index[stem][doc]
                elif doc !='df':
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
        if ldocs_cosinus[doc]>max[1] and doc not in doc_exclus:
            max = (doc, ldocs_cosinus[doc])
    return max


def affiche_resultat(ldocs_cosinus, n):
    """
    Gestion de l'affichage des n documents les plus pertinents
    """
    if ldocs_cosinus=={}:
        print("Il n'y a aucun rÃ©sultat pertinent pour cette requÃªte. ")
    else:
        # s'il y a moins de n documents pertinents
        if (len(ldocs_cosinus)<n):
            n = len(ldocs_cosinus)

        nbdocs = 0
        topn = {}

        print("Les {} documents les plus pertinents sont : ".format(n))
        exclus = []

        # boucle visant Ã  trouver les n documents les plus pertinents
        for i in range(1, n+1):
            max_doc = max_dicodoc(ldocs_cosinus, exclus)
            exclus.append(max_doc[0])
            print("{}) Document {} - score {}".format(i, max_doc[0], max_doc[1]))
        print()



# prog principal
welcome("Lorraine")
index = monindex.MON_INDEX

marequete = saisie_requete()
while marequete != '*':
    vecteur_req = pretraitement_requete(marequete)
    affiche_resultat(calculeSimilarites(index, vecteur_req), 5)

    marequete = saisie_requete()
