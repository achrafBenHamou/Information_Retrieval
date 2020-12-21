#!/usr/bin/env python
# -*- coding: utf-8 -*-cmd
# lib

import math
from trash import outils

Xml_Documents_Folder = "./XML_Coll_MWI_withSem/coll/"


# nb of documents
# nb_docs = len(os.listdir(Documents_Folder))
# print("Nombre des documents : ",nb_docs)
# Les fonctions
# enlever les caracteres specieux pour le word

# list of words to dictionary with frequency
def liste2dicionary(liste):
    # Lit une liste de racines et renvoie le dictionnaire correspondant (word -> frequence of word)
    dicionary = {}  # initialisation du nouveau dictionnaire
    for word in liste:  # parcours des words de la liste
        if word in dicionary.keys():  # si le word est deja  un key du dictionnaire on incremente sa frequence
            dicionary[word] += 1
        else:  # sinon on l'ajoute comme nouvelle key
            dicionary[word] = 1
    return dicionary


def docs2dicionaryDoc():
    """
    traitement des fichiers contenus dans Documents_Folder et convertit le corpus en dicionary doc -> stem -> freq
    """
    # initialisation du dictionnaire
    dicionaryDocs = {}
    # les documents de fichier text

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
    global nb_docs
    nb_docs = len(DocsList)
    for i in range(0, len(A)):
        # for filename in os.listdir(Documents_Folder):
        filename = DocsList[i]
        print("processing of file : " + DocsList[i])
        doc_content = outils.getTextByIndices(filecontent, A[i] + 8 + len(DocsList[i]), C[i])
        # print("document content before preprocessing")
        # print(doc_content)
        doc_processed_content = outils.doc_preprocessing(doc_content)
        print("document content after preprocessing")
        print(doc_processed_content)
        # decoupage en words ## word breakdown
        listeOfWords = outils.TextTowords(doc_processed_content)
        print("list after word_tokenize")
        print(listeOfWords)
        # construction du dictionnaire word --> frequence et ajout dans dicionary final
        dicionaryDocs[filename] = liste2dicionary(listeOfWords)

    return dicionaryDocs


def dicionaryDoc2dicionaryStem(dicionaryDoc):
    """
    prend en entrÃ©e la sortie de docs2dicionaryDoc (dicionary doc -> stem -> frÃ©q) et le transforme en fichier inverse : stem -> doc -> freq
    """
    dicionaryStem = {}  # initialisation du dictionnaire
    for (file, dicionaryFile) in dicionaryDoc.items():  # parcours des documents
        for stem in dicionaryFile:  # parcours des racines
            if stem in dicionaryStem.keys():
                # si le stem st deja  dans le dicionary resultat on ajoute sa frÃ©quence pour le document file
                dicionaryStem[stem][file] = dicionaryFile[stem]
            else:
                # sinon on cree un nouveau dictionnaire qu'on ajoute pour ce stem, puis on ajoute au dictionnaire le doc et la frÃ©quence
                dicionaryStem[stem] = {}
                dicionaryStem[stem][file] = dicionaryFile[stem]
    return dicionaryStem


def calculeSomme(dicionaryStem):
    """
    calcule la somme des frÃ©quence du terme dont le dicionary des frÃ©quences est passÃ© en paramÃ¨tre
    """
    df = 0
    for (doc, freq) in dicionaryStem.items():  # pour chaque document, somme les tf
        if freq != 0:
            df += 1
    return df


def calculeDFdicionary(dicionaryStem):
    """
    prend en entree le dicionary stem et calcule le DF de chaque stem et le stocke dans le dicionary Ã  l'indice "df"
    """
    for stem in dicionaryStem:
        dicionaryStem[stem]["df"] = len(dicionaryStem[stem])
    return dicionaryStem


def calculenormalizedTFIDFdicionary(dicionaryStem):
    """
    calcule le tf idf normalisee de chaque stem/doc
    """
    normdocs = {}
    for stem in dicionaryStem:  # pour chaque stem
        df = dicionaryStem[stem]["df"]
        for doc in dicionaryStem[stem]:  # pour chaque document
            if doc != "df":
                dicionaryStem[stem][doc] *= math.log10(
                    float(nb_docs) / float(df))  # on change la valeur du tf par le tf idf
                if doc in normdocs.keys():
                    normdocs[doc] += (dicionaryStem[stem][doc]) ** 2
                else:
                    normdocs[doc] = (dicionaryStem[stem][doc]) ** 2

    # finalise normalisation
    for stem in dicionaryStem:
        for doc in dicionaryStem[stem]:
            if doc != "df":
                dicionaryStem[stem][doc] = dicionaryStem[stem][doc] / math.sqrt(normdocs[doc])

    return dicionaryStem


def calculeTFIDFdicionary(dicionaryStem, dicionaryDoc):
    """
    calcule le tf idf de chaque stem/doc
    """

    for stem in dicionaryStem:  # pour chaque stem
        df = dicionaryStem[stem]["df"]
        for doc in dicionaryStem[stem]:  # pour chaque document
            if doc != "df":
                dicionaryStem[stem][doc] *= math.log10(
                    float(nb_docs) / float(df))  # on change la valeur du tf par le tf idf
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


if __name__ == "__main__":
    # module de test - mettez ici le code a  executer
    d = genereIndex(True)
    print(d)
    # ouverture du fichier resultat
    fd = open("mon_index.py", 'w')
    fd.write("MON_INDEX = " + str(d))
    print("index generated with succes at file mon_index.py")
