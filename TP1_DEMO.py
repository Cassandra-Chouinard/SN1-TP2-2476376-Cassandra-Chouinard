import pandas as pd # J'importe pandas.
import matplotlib.pyplot as plt # J'importe matpolib pour faire les graphiques.
df = pd.read_csv('C:/Users/2476396/Downloads/vdq-arbrerepertorie.csv')  # J'introduit le fichier csv dans le projet
# python.

# QUESTIONS
# Question 1:
# Quelles sont les variables présentes dans le jeu de données?
def variables_presentes(df):    # Cette fonction montre le nom des colonnes du fichier.
    return(df.head(0))  # La fonction retourne le nom des colonnes du fichier.
print("Variables présentes :", variables_presentes(df)) # J'imprime les variables présentes.
print("")   # Je laisse un espace pour faciliter la lecture des réponses.

# Question 2:
# Combien y a-t-il d'enregistrements (lignes) dans le jeu de donnée?
def nbr_enregistrements(df):    # Cette fonction montre la longueur d'une ligne du fichier.
    desc_df = df.describe() # Cette ligne créé un tableau avec le nombre d'éléments, la moyenne, l'écart type, le
    # minimum, le maximum, et les quartiles de toutes les colonnes contenant des numéros.
    longueur = desc_df.loc["count", "ID"]   # Cette variable correcspond au nombre d'élément de la colonne "ID" du
    # tableau créé à la ligne précédente. Ajouter "ID" permet de n'avoir qu'un seul nombre plutôt que plusieurs pour
    # chaques colonnes du tableau, j'aurais pu utiliser "DIAMETRE", "LONGITUDE" OU "ALTITUDE" à la place.
    return(longueur)    # La fonction retourne la longueur d'une ligne du fichier.
print("Nombre d'enregistrement :", nbr_enregistrements(df)) # J'imprime le nombre d'enregistrement.
print("")

# Question 3:
# Combien y a-t-il d'espèces d'arbres différentes?
def nbr_especes(df):    # Cette fonction montre le nombre d'espèces d'arbres différentes.
    df_especes = df["NOM_FRANCAIS"].unique()    # Je créé une nouvelle liste ne contenant que les noms en français des
    # arbres, où chaque nom n'apparait qu'une seule fois.
    return(len(df_especes)) # La fonction retourne le nombre d'espèces d'arbres différents de notre dernière liste.
print("Nombre d'espèces d'arbres différentes :", nbr_especes(df))   # J'imprime le nombre d'espèces d'arbres différents.
print("")

# Question 4:
# Quels noms d'espèces d'arbres (en français) font moins de 20 caractères?
def noms_moins_20car(df):   # Cette fonction montre le nom des espèces d'arbre qui contiennent moins de 20 lettres.
    df_enleve_plus_20car = df[df["NOM_FRANCAIS"].str.len() < 20]    # Je fais une nouvelle liste qui exclus tous les nom
    # d'arbres qui ont ou dépassent 20 lettres.
    df_moins_20car = df_enleve_plus_20car["NOM_FRANCAIS"].unique()  # Chaque espèce ne s'affiche qu'une seule fois.
    return(df_moins_20car)  # La fonction retourne le nom de toutes les espèces d'arbres qui ont un nom qui contient
    # moins de 20 lettres.
print("Nom des espèces qui contiennent moins de 20 caractères :",noms_moins_20car(df))  # J'imprime le nom des espèces
# qui contiennent moins de 20 caractères.
print("")

# Question 5:
# De quelle espèce est l'arbre avec le tronc le plus gros?
def espece_arbre_plus_grand(df):    # Cette fonction affiche le nom de l'espèce d'arbre ayant le plus gros tronc.
    df_nom_diametre = df[["NOM_FRANCAIS", "DIAMETRE"]]  # Je créé une nouvelle liste qui ne contient que le nom et le
    # diamètre de l'arbre.
    df_plus_grand = df_nom_diametre.sort_values(by="DIAMETRE", ascending=False) # Je place l'arbre ayant le plus gros
    # tronc en haut de la liste.
    df_nom = df_plus_grand["NOM_FRANCAIS"]  # Je créé une nouvelle liste où j'enlève la valeur du diamètre de cette
    # liste, car on ne s'intéresse qu'à son espèce.
    return(df_nom.head(1))  # La fonction retourne le premier élément de ma dernière liste.
print("Espèce de l'arbre ayant le plus gros tronc :", espece_arbre_plus_grand(df))  # J'imprime le nom de l'espèce ayant
# le plus gros tronc.
print("")

# Question 6:
# Quel est le diamètre moyen du tronc des feuillus dans la ville de Québec? Des conifères?
def moyenne_tronc(df, type_arbre):  # Cette fonction affiche lla moyenne du diamètre des troncs d'un type d'arbre en
    # particulier.
    df_type = df[df["TYPE_ARBRE"] == type_arbre]    # Je créé une nouvelle liste ne gardant que les lignes ayant un
    # arbre du type spécifique que je recherche.
    desc_type = df_type.describe()  # Cette ligne créé un tableau avec le nombre d'éléments, la moyenne, l'écart type,
    # le minimum, le maximum, et les quartiles de toutes les colonnes contenant des numéros.
    moyenne_type = desc_type.loc["mean", "DIAMETRE"]    # Cette variable correcspond au à la moyenne des éléments de la
    # colonne "DIAMETRE" du tableau créé à la ligne précédente. Ici, nous cherchons vraiement la moyenne du diamètre,
    # donc "DIAMETRE" n'est pas interchangeable.
    return(moyenne_type)    # La fonction retourne la moyenne de diamètre des troncs d'un type d'arbre spécifique.
print("Diamètre moyen du tronc des feuillus :", round(moyenne_tronc(df, "Feuillu"), 1))   # J'imprime le diamètre moyen
# du tronc pour les arbres de types feuillus.
print("Diamètre moyen du tronc des conifères :", round(moyenne_tronc(df, "Conifère"), 1)) # J'imprime le diamètre moyen
# du tronc pour les arbres de types conifères...
print("")

# GRAPHIQUES
# Graphique 1:
df_enleve_plus_5car = df[df["NOM_FRANCAIS"].str.len() <= 5]
df_moins_5car = df_enleve_plus_5car["NOM_FRANCAIS"].sort_values().unique()

nbr_moins_5car = df_enleve_plus_5car["NOM_FRANCAIS"].value_counts().sort_index() #***
'''
plt.bar(df_moins_5car, nbr_moins_5car)

plt.xticks(rotation=45, ha='right')
plt.title("Nombre d'arbres répertoriés pour les 10 espèces d'arbres \n aux noms les plus courts (<= 5 caractères)") 
plt.xlabel("")
plt.ylabel("Nombre d'arbres répertoriés")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.show()

# Graphique 2:
df_enleve_plus_5car.boxplot(column="DIAMETRE", by="NOM_FRANCAIS")
plt.title("Diamètre du tronc des 10 espèces d'arbres \n aux noms les plus courts (<= 5 caractères)")
plt.suptitle("")  # Supprimer le titre autogénéré apparaisant en haut de notre titre (il indique le regroupement 
# réalisé)
plt.xlabel("Espèce d'arbre")
plt.ylabel("Diamètre (cm)")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.show()

# Graphique 3:
df_feuillu = df[df["TYPE_ARBRE"] == "Feuillu"]
df_conifere = df[df["TYPE_ARBRE"] == "Conifère"]

plt.scatter(df_feuillu["LONGITUDE"], df_feuillu["LATITUDE"], s=0.01, alpha=0.5) # s = taille des points
plt.scatter(df_conifere["LONGITUDE"], df_conifere["LATITUDE"], s=0.01, alpha=0.5) # s = taille des points
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Localisation et type des arbres répertoriés à la Ville de Québec")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.legend(title="Type d'arbre", markerscale=50, labels=['Feuillu', 'Conifère'])
plt.show()
'''
# Graphique 4:
df_parc_gerard_marchand = df[df["NOM_TOPOGRAPHIE"] == "Parc de la Chaudière"]
df_conifere = df[df["TYPE_ARBRE"] == "Conifère"]

plt.scatter(df_parc_gerard_marchand["LONGITUDE"], df_parc_gerard_marchand["LATITUDE"], s=0.01, alpha=0.5) # s = taille des points
plt.scatter(df_conifere["LONGITUDE"], df_conifere["LATITUDE"], s=0.01, alpha=0.5) # s = taille des points
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Localisation et type des arbres répertoriés à la Ville de Québec")
plt.grid(axis='both', linestyle='--', linewidth=0.5)
plt.legend(title="Type d'arbre", markerscale=50, labels=['Feuillu', 'Conifère'])
plt.show()