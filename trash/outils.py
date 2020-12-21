#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re

XmlFilesFolder = "./XML_Coll_MWI_withSem/coll/"
stop_words=set(stopwords.words("english"))

###Fonctions ajoute par achraf
def doc_preprocessing(doc):
    # tout en miniscule
    doc=doc.lower()
    ## Replace line break to single space
    doc = re.sub(r"\n", " ", doc)
    ##Remove hyperlinks
    doc=re.sub(r"https?://.*[\s]*","",doc)
    ## Remove numbers and characters
    doc=re.sub(r"[^a-z ]*","",doc)
    ## Replace multiple spaces by single space
    doc=re.sub(r"[\s]+"," ",doc)
    return doc

#we can change between stemmer and limmatization
def TextTowords(text):
    listeOfWords = word_tokenize(text)
    list_stem_words=[]
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    for word in listeOfWords:
        #from nltk.stem import PorterStemmer
        #stemmer = PorterStemmer()
        #word = stemmer.stem(word)
        word = lemmatizer.lemmatize(word)
        if(word not in stop_words):
            list_stem_words.append(word)
    return list_stem_words


def loadXmlFile(filename):
    #read XML file
    with open(XmlFilesFolder+filename) as f:
        return f.read()

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

