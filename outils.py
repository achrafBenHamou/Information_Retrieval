#!/usr/bin/env python
# -*- coding: utf-8 -*-


#lib
import os
from  nltk.stem.snowball import FrenchStemmer

import string


DOSSIERDOCUMENTS=""
MOTSOUTILS = ["a", "Ã ", "Ã¢", "abord", "afin", "ah", "ai", "aie", "ainsi", "allaient", "allo", "allÃ´", "allons", "aprÃ¨s", "assez", "attendu", "au", "aucun", "aucune", "aujourd", "aujourd'hui", "auquel", "aura", "auront", "aussi", "autre", "autres", "aux", "auxquelles", "auxquels", "avaient", "avais", "avait", "avant", "avec", "avoir", "ayant", "b", "bah", "beaucoup", "bien", "bigre", "boum", "bravo", "brrr", "c", "Ã§a", "car", "ce", "ceci", "cela", "celle", "celle-ci", "celle-lÃ ", "celles", "celles-ci", "celles-lÃ ", "celui", "celui-ci", "celui-lÃ ", "cent", "cependant", "certain", "certaine", "certaines", "certains", "certes", "ces", "cet", "cette", "ceux", "ceux-ci", "ceux-lÃ ", "chacun", "chaque", "cher", "chÃ¨re", "chÃ¨res", "chers", "chez", "chiche", "chut", "ci", "cinq", "cinquantaine", "cinquante", "cinquantiÃ¨me", "cinquiÃ¨me", "clac", "clic", "combien", "comme", "comment", "compris", "concernant", "contre", "couic", "crac", "d", "da", "dans", "de", "debout", "dedans", "dehors", "delÃ ", "depuis", "derriÃ¨re", "des", "dÃ¨s", "dÃ©sormais", "desquelles", "desquels", "dessous", "dessus", "deux", "deuxiÃ¨me", "deuxiÃ¨mement", "devant", "devers", "devra", "diffÃ©rent", "diffÃ©rente", "diffÃ©rentes", "diffÃ©rents", "dire", "divers", "diverse", "diverses", "dix", "dix-huit", "dixiÃ¨me", "dix-neuf", "dix-sept", "doit", "doivent", "donc", "dont", "douze", "douziÃ¨me", "dring", "du", "duquel", "durant", "e", "effet", "eh", "elle", "elle-mÃªme", "elles", "elles-mÃªmes", "en", "encore", "entre", "envers", "environ", "es", "Ã¨s", "est", "et", "etant", "Ã©taient", "Ã©tais", "Ã©tait", "Ã©tant", "etc", "Ã©tÃ©", "etre", "Ãªtre", "eu", "euh", "eux", "eux-mÃªmes", "exceptÃ©", "f", "faÃ§on", "fais", "faisaient", "faisant", "fait", "feront", "fi", "flac", "floc", "font", "g", "gens", "h", "ha", "hÃ©", "hein", "hÃ©las", "hem", "hep", "hi", "ho", "holÃ ", "hop", "hormis", "hors", "hou", "houp", "hue", "hui", "huit", "huitiÃ¨me", "hum", "hurrah", "i", "il", "ils", "importe", "j", "je", "jusqu", "jusque", "k", "l", "la", "lÃ ", "laquelle", "las", "le", "lequel", "les", "lÃ¨s", "lesquelles", "lesquels", "leur", "leurs", "longtemps", "lorsque", "lui", "lui-mÃªme", "m", "ma", "maint", "mais", "malgrÃ©", "me", "mÃªme", "mÃªmes", "merci", "mes", "mien", "mienne", "miennes", "miens", "mille", "mince", "moi", "moi-mÃªme", "moins", "mon", "moyennant", "n", "na", "ne", "nÃ©anmoins", "neuf", "neuviÃ¨me", "ni", "nombreuses", "nombreux", "non", "nos", "notre", "nÃ´tre", "nÃ´tres", "nous", "nous-mÃªmes", "nul", "o", "o|", "Ã´", "oh", "ohÃ©", "olÃ©", "ollÃ©", "on", "ont", "onze", "onziÃ¨me", "ore", "ou", "oÃ¹", "ouf", "ouias", "oust", "ouste", "outre", "p", "paf", "pan", "par", "parmi", "partant", "particulier", "particuliÃ¨re", "particuliÃ¨rement", "pas", "passÃ©", "pendant", "personne", "peu", "peut", "peuvent", "peux", "pff", "pfft", "pfut", "pif", "plein", "plouf", "plus", "plusieurs", "plutÃ´t", "pouah", "pour", "pourquoi", "premier", "premiÃ¨re", "premiÃ¨rement", "prÃ¨s", "proche", "psitt", "puisque", "q", "qu", "quand", "quant", "quanta", "quant-Ã -soi", "quarante", "quatorze", "quatre", "quatre-vingt", "quatriÃ¨me", "quatriÃ¨mement", "que", "quel", "quelconque", "quelle", "quelles", "quelque", "quelques", "quelqu'un", "quels", "qui", "quiconque", "quinze", "quoi", "quoique", "r", "revoici", "revoilÃ ", "rien", "s", "sa", "sacrebleu", "sans", "sapristi", "sauf", "se", "seize", "selon", "sept", "septiÃ¨me", "sera", "seront", "ses", "si", "sien", "sienne", "siennes", "siens", "sinon", "six", "sixiÃ¨me", "soi", "soi-mÃªme", "soit", "soixante", "son", "sont", "sous", "stop", "suis", "suivant", "sur", "surtout", "t", "ta", "tac", "tant", "te", "tÃ©", "tel", "telle", "tellement", "telles", "tels", "tenant", "tes", "tic", "tien", "tienne", "tiennes", "tiens", "toc", "toi", "toi-mÃªme", "ton", "touchant", "toujours", "tous", "tout", "toute", "toutes", "treize", "trente", "trÃ¨s", "trois", "troisiÃ¨me", "troisiÃ¨mement", "trop", "tsoin", "tsouin", "tu", "u", "un", "une", "unes", "uns", "v", "va", "vais", "vas", "vÃ©", "vers", "via", "vif", "vifs", "vingt", "vivat", "vive", "vives", "vlan", "voici", "voilÃ ", "vont", "vos", "votre", "vÃ´tre", "vÃ´tres", "vous", "vous-mÃªmes", "vu", "w", "x", "y", "z", "zut"]

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
    stemmer = FrenchStemmer()
    racine = stemmer.stem(mot)
    return racine