#!/usr/bin/env python
# -*- coding: utf-8 -*-cmd
#lib
import os
from  nltk.stem.snowball import FrenchStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
import string
import codecs
import math
import outils

#constantes
#Documents Folder path
Documents_Folder = "./XML_Coll_MWI_withSem/coll/"

#nb of documents
nb_docs = len(os.listdir(Documents_Folder))
print("Nombre des documetns : ",nb_docs)


#Les fonctions

def tokenize_plus(listetokens):
    """
    Traite les chaines non tokenizÃ©es avec apostrophe
    """
    for token in listetokens:
        if ("'" in token):
            listetokens.remove(token)
            listetokens += token.split("'")
        if ("â€™" in token):
            listetokens.remove(token)
            listetokens += token.split("â€™")
        if ("/" in token):
            listetokens.remove(token)
            listetokens += token.split("/")
    return listetokens

#enlever les caracteres specieux pour le mot
def nettoieMot(mot):
    """
    EnlÃ¨ve les caractÃ¨res spÃ©ciaux
    """
    i=0
    for c in mot:
        if c in u"Â«Â»Å‚.â”œ":
            mot = mot[:i]+mot[i+1:]
    return mot

#input list of words
def filtreMots(liste):
    """
    Prend une liste de tokens en entree, et supprime les elements qui ne sont pas des mots (ponctuation etc.)
    """
    listeResultat = [] # liste dans laquelle on va recopier les mots
    for elem in liste:
        if outils.contientLettres(elem): #on garde tout ce qui contient une lettre
            listeResultat.append(elem)
    return listeResultat

def filtreMotsOutils(liste):
    """
    Prend en entree une liste de mots et en filtre les mots outils
    """
    listeResultat = []# liste dans laquelle on va recopier les mots
    for mot in liste:
        if mot not in outils.MOTSOUTILS: #on garde tout ce qui n'est pas un mot outil
            listeResultat.append(mot)
    return listeResultat


#list of words to dictionary with frequency
def liste2dicionary(liste):
    """
    Lit une liste de racines et renvoie le dictionnaire correspondant (mot -> frequence of word)
    """
    dicionary = {} #initialisation du nouveau dictionnaire
    for mot in liste: # parcours des mots de la liste
        if mot in dicionary.keys(): # si le mot est dÃ©jÃ  une clÃ© du dictionnaire on incrÃ©mente sa frÃ©quence
            dicionary[mot] += 1
        else: # sinon on l'ajoute comme nouvelle clÃ©
            dicionary[mot] = 1
    return dicionary

def docs2dicionaryDoc():
    """
    traitement des fichiers contenus dans Documents_Folder et convertit le corpus en dicionary doc -> stem -> freq
    """
    
    # initialisation du dictionnaire
    dicionaryDocs = {}
    #les documents de fichier text

    ## code ajoute par Achraf
    Documents_txt = "./Text_Only_Ascii_Coll_MWI_NoSem/Text_Only_Ascii_Coll_MWI_NoSem"
    # parcours des fichiers du repertoire documents folder, a  l'aide de la fonction listdir du module os

    # ouverture du fichier
    with open(Documents_txt, encoding="utf8") as f:
        filecontent = f.read()

    """ les listes d'indice de doc, docno"""
    A = outils.cherche_occurrences(filecontent, "<docno>")
    B = outils.cherche_occurrences(filecontent, "</docno>")
    C = outils.cherche_occurrences(filecontent, "</doc>")
    DocsList = outils.getListIDs(filecontent, A, B)
    for i in range (0,len(A)):
    #for filename in os.listdir(Documents_Folder):
        filename = DocsList[i]
        print("processing of file : "+DocsList[i])
        doc_content = outils.getTextByIndices(filecontent, A[i] + 8 + len(DocsList[i]), C[i])

        #decoupage en mots ## word breakdown
        liste = filtreMots(word_tokenize(doc_content))

        #suppression des mots outils
        liste = filtreMotsOutils(liste)
        print("sans mots outils : "+str(liste))
        #stemming
        listeStem = []
        for mot in liste:
            listeStem.append(outils.mot2racine(mot))
        print("apres stemming : "+str(listeStem))
        #construction du dictionnaire mot --> frÃ©quence et ajout dans dicionary final
        dicionaryDocs[filename] = liste2dicionary(listeStem)

    return dicionaryDocs

def dicionaryDoc2dicionaryStem(dicionaryDoc):
    """
    prend en entrÃ©e la sortie de docs2dicionaryDoc (dicionary doc -> stem -> frÃ©q) et le transforme en fichier inverse : stem -> doc -> freq
    """
    dicionaryStem = {} # initialisation du dictionnaire
    for (file, dicionaryFile) in dicionaryDoc.items(): # parcours des documents
        for stem in dicionaryFile: # parcours des racines
            if stem in dicionaryStem.keys():
                #si le stem st dÃ©jÃ  dans le dicionary rÃ©sultat on ajoute sa frÃ©quence pour le document file
                dicionaryStem[stem][file] = dicionaryFile[stem]
            else:
                # sinon on crÃ©e un nouveau dictionnaire qu'on ajoute pour ce stem, puis on ajoute au dictionnaire le doc et la frÃ©quence
                dicionaryStem[stem] = {}
                dicionaryStem[stem][file] = dicionaryFile[stem]
    return dicionaryStem

def calculeSomme(dicionaryStem):
    """
    calcule la somme des frÃ©quence du terme dont le dicionary des frÃ©quences est passÃ© en paramÃ¨tre
    """
    df = 0
    for (doc, freq) in dicionaryStem.items(): # pour chaque document, somme les tf
        if freq!=0:
            df += 1
    return df


def calculeDFdicionary(dicionaryStem):
    """
    prend en entrÃ©e le dicionary stem et calcule le DF de chaque stem et le stocke dans le dicionary Ã  l'indice "df"
    """
    for stem in dicionaryStem:
        dicionaryStem[stem]["df"] = len(dicionaryStem[stem])
    return dicionaryStem


def calculenormalizedTFIDFdicionary(dicionaryStem):
    """
    calcule le tf idf normalisÃ© de chaque stem/doc
    """
    normdocs = {}
    for stem in dicionaryStem:  # pour chaque stem
        df = dicionaryStem[stem]["df"]
        for doc in dicionaryStem[stem]:  # pour chaque document
            if doc != "df":
                dicionaryStem[stem][doc] *= math.log10(float(nb_docs) / float(df))  # on change la valeur du tf par le tf idf
                if doc in normdocs.keys():
                    normdocs[doc] += (dicionaryStem[stem][doc])**2
                else:
                    normdocs[doc] = (dicionaryStem[stem][doc]) ** 2

    # finalise normalisation
    for stem in dicionaryStem:
        for doc in dicionaryStem[stem]:
            if doc != "df":
                dicionaryStem[stem][doc] = dicionaryStem[stem][doc]/math.sqrt(normdocs[doc])


    return dicionaryStem


def calculeTFIDFdicionary(dicionaryStem, dicionaryDoc):
    """
    calcule le tf idf de chaque stem/doc
    """

    for stem in dicionaryStem: # pour chaque stem
        df = dicionaryStem[stem]["df"]
        for doc in dicionaryStem[stem]: # pour chaque document
            if doc!="df":

                dicionaryStem[stem][doc] *= math.log10(float(nb_docs)/float(df)) # on change la valeur du tf par le tf idf
    return dicionaryStem



def genereIndex(tf):
    """
    Generee l index des documents situees dans le repertoire Documents_Folder, avec les tf.idf si tf est vrai, les frÃ©quences sinon
    """
    print("---------------------------")
    print("Construction de l'index... ")
    print("---------------------------")
    if tf:
        return calculenormalizedTFIDFdicionary(calculeDFdicionary(dicionaryDoc2dicionaryStem(docs2dicionaryDoc())))
    else:
        return dicionaryDoc2dicionaryStem(docs2dicionaryDoc())
    print("-------------------------------------------------")

def exportdicionary(index, filename):
    """
    Exporte le dicionary sous forme d'un fichier  racine doc:freq (freq ou tf selon le dicionary input)
    """
    fd = open(filename, 'w') # ouverture du fichier rÃ©sultat
    for (stem, dicionaryStem) in index.items(): # parcours de l'index
        fd.write(stem+"\t") # affichage du terme
        for (doc, val) in dicionaryStem.items(): # affichage des docs:poids pour chaque terme
            fd.write(doc+":"+str(val)+"\t")
        fd.write("\n") # retour Ã  la ligne aprÃ¨s chaque terme
    fd.close() # fermeture du fichier




if __name__ == "__main__":
    # module de test - mettez ici le code a  executer
    d = genereIndex(True)
    print(d)
    exportdicionary(d, "monindex.txt")
