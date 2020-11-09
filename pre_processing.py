import os

from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import re
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC, NuSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier


def doc_preprocessing(docs):
    list_docs_words = []
    for doc in docs:
        list_doc_words = []
        doc = doc.lower()
        ##Remove userName
        doc = re.sub(r"@[a-z0-9_-]*", "", doc)
        ##Remove hyperlinks
        doc = re.sub(r"https?://.*[\s]*", "", doc)
        ## Remove numbers and characters
        doc = re.sub(r"[^a-z ]*", "", doc)
        ## Replace multiple spaces by single space
        doc = re.sub(r"[\s]+", " ", doc)
        ##Word Tokenization
        doc_words = word_tokenize(doc)
        for word in doc_words:
            if (word not in stop_words):
                word = stemmer.stem(word)
                list_doc_words.append(word)
        ## join : from list of words to string
        list_docs_words.append(" ".join(list_doc_words))
    return list_docs_words

#Documents_Folder
Documents_Folder = "./XML_Coll_MWI_withSem/coll/"
nb_docs = len(os.listdir(Documents_Folder))
print("Nombre des documetns : ",nb_docs)

def loadFile(filename):
    """
    Lit un fichier et le renvoie sous forme de chaine unicode (tout en minuscule)
    """
    with open(Documents_Folder+filename) as f:
        result = f.read()
    return result.lower()

nb_docs = len(os.listdir(Documents_Folder))
print("Nombre des documetns : ",nb_docs)
print(loadFile("612.xml"))


stemmer = PorterStemmer()
stop_words = set(stopwords.words("english"))
#tweet_pos = twitter_samples.strings('positive_tweets.json')
#tweet_neg = twitter_samples.strings('negative_tweets.json')
#print(len(tweet_neg))
#print(len(tweet_pos))

# 1- Preprocessing
list_docs_words = doc_preprocessing(Documents_Folder)


# 2- Vectorization (Bag-of-Words (BoW) model)
# Convert a collection of text documents to a matrix of token counts
countvectorizer = CountVectorizer()
countvector = countvectorizer.fit(list_docs_words)
countvector = countvectorizer.transform(list_docs_words)

print(countvector)
"""
#2.2 Word Frequencies with TfidfVectorizer
#Convert a collection of raw documents to a matrix of TF-IDF features.
tfidfvectorizer=TfidfVectorizer()
tfidfvector=tfidfvectorizer.fit(list_all_tweets)
tfidfvector=tfidfvectorizer.transform(list_all_tweets)
#print(tfidfvector)


# 3 Classification
X = countvector
Y = ["Pos" for i in range(5000)] + ["Neg" for i in range(5000)]
labelEncoder = LabelEncoder()
Y = labelEncoder.fit(Y).transform(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=100, shuffle="true")

##Classifiers:
# from sklearn.naive_bayes import  MultinomialNB
# MultinomialNB
clfMultinomialNB = MultinomialNB()
modelMultinomialNB = clfMultinomialNB.fit(X_train, Y_train)
Y_predict = modelMultinomialNB.predict(X_test)
print("*******Classification avec MultinomialNB*******")
evaluation(Y_test, Y_predict)


"""
