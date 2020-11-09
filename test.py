import os

Documents_Folder = "./XML_Coll_MWI_withSem/coll/"
for filename in os.listdir(Documents_Folder):
    print("Traitement du fichier " + filename)

    # ouverture du fichier
    with open(Documents_Folder+ filename, encoding="utf8") as f:
        filecontent = f.read()
        print(filecontent)


