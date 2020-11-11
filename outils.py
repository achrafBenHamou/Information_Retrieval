#!/usr/bin/env python
# -*- coding: utf-8 -*-


#lib

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string


DOSSIERDOCUMENTS=""
MOTSOUTILS = stopwords.words('english')
def loadFile(filename):
    """
    Lit un fichier et le renvoie sous forme de chaine unicode (tout en minuscule)
    """
    with open(DOSSIERDOCUMENTS+filename) as f:
        result = f.read()
    return result.lower()


def contientLettres(chaine):
    for c in chaine:
        if c in string.ascii_lowercase:
            return True
    return False

def mot2racine(mot):
    stemmer = PorterStemmer()
    racine = stemmer.stem(mot)
    return racine


# outils ajoute par achraf

def isprefixe(filecontent,mot,i):
    """Vérifie si mot a une occurrence dans texte en position i"""
    B = True
    j = 0
    while (j < len(mot)) and B:
        if filecontent[i+j] != mot[j]:
            B = False
        j +=1
    return B

def getTextByIndices (file,indice_debut,indice_fin):
    """ get text a partie de l'indice de debut jusqu'a indice fin"""
    Text = ""
    for k in range (indice_debut+7,indice_fin):
        Text=Text+file[k]
    return Text

def cherche_occurrences(texte, mot):
    """Donne la liste de toutes les occurrences de mot dans texte"""
    occ = [] # liste des occurrences
    for i in range(len(texte)-len(mot)+1):
        if isprefixe(texte,mot,i):
            occ.append(i)
    return occ

def getListIDs(filecontent,A,B):
    listofIDs=[]
    for i in range (0,len(A)) :
        listofIDs.append(getTextByIndices(filecontent,A[i], B[i]))
    return listofIDs

