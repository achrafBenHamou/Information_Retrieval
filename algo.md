doc_1 -> "salut tout le monde"
doc_2 -> "les vaccnaces"
doc_3 -> "les vaccnaces tout le onde"
doc_4 -> "les vaccnaces monde"
doc_5 -> "les vaccnaces dubai"

# step 1 parsing

```
dictionnary : {key -> value, key -> value}
dictionnary : { doc_1 -> "salut tout le monde",
                doc_2 -> "les vaccnaces",
                doc_3 -> "les vaccnaces tout le onde",
                doc_4 -> "les vaccnaces monde",
                doc_5 -> "les vaccnaces dubai"
}
```


# step 2 : building inverted index :
```
 dictionnary : {  salut -> [doc_1: tf(salut,doc_1)]
                    vaccnaces -> [doc_2:tf(vaccances,doc_2), doc_3: tf(vaccances,doc_3), doc_4: tf(vaccances,doc_4), doc_5:tf(vaccances,doc_5)]
                    monde -> [doc_1:tf(monde,doc_1), doc_3:tf(monde,doc_3), doc_4:tf(monde,doc_4)]
                 }

```
  


   query : "salut monde"
   mini step : tokenisation of query -> ["salut", "monde"]
   mini step : removes stop words ->  ["salut", "monde"]
  -> query_1 : ['salut', 'monde']


   f(x) = y

   score (query_1, doc_1) = score ("salut ", doc_1) + score("monde", doc_1)

   score (q, doc_i) = somme(score(w appartient q, doc_i))

   Ord par orde decroissant the les scores des doc_i : revient à classer par l'orde de pertinence.