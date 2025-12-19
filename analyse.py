import pandas as pd # J'importe pandas.
import matplotlib.pyplot as plt # J'importe matpolib pour faire les graphiques.
df = pd.read_csv('C:/Users/2476396/Downloads/vdq-arbrerepertorie.csv')  # J'introduis le fichier csv dans le projet
# python.

# QUESTIONS
# Question 1:
# Quelles sont les variables présentes dans le jeu de données?
def variables_presentes(df):    # Cette fonction montre le nom des colonnes du fichier.
    return(df.head(0))  # La fonction retourne le nom des colonnes du fichier.
print("Variables présentes :", variables_presentes(df)) # J'imprime les variables présentes.
print("")   # Je laisse un espace pour faciliter la lecture des réponses.

# Question 2:
# Combien y a-t-il d'enregistrements (lignes) dans le jeu de données?
def nbr_enregistrements(df):    # Cette fonction montre la longueur d'une ligne du fichier.
    desc_df = df.describe() # Cette ligne créée un tableau avec le nombre d'éléments, la moyenne, l'écart type, le
    # minimum, le maximum, et les quartiles de toutes les colonnes contenant des numéros.
    longueur = desc_df.loc["count", "ID"]   # Cette variable correspond au nombre d'éléments de la colonne "ID" du
    # tableau créé à la ligne précédente. Ajouter "ID" permet de n'avoir qu'un seul nombre plutôt que plusieurs pour
    # chaque colonne du tableau, j'aurais pu utiliser "DIAMETRE", "LONGITUDE" OU "ALTITUDE" à la place.
    return(longueur)    # La fonction retourne la longueur d'une ligne du fichier.
print("Nombre d'enregistrement :", nbr_enregistrements(df)) # J'imprime le nombre d'enregistrements.
print("")

# Question 3:
# Combien y a-t-il d'espèces d'arbres différents?
def nbr_especes(df):    # Cette fonction montre le nombre d'espèces d'arbres différentes.
    df_especes = df["NOM_FRANCAIS"].unique()    # Je crée une nouvelle liste ne contenant que les noms en français des
    # arbres, où chaque nom n'apparait qu'une seule fois.
    return(len(df_especes)) # La fonction retourne le nombre d'espèces d'arbres différents de notre dernière liste.
print("Nombre d'espèces d'arbres différentes :", nbr_especes(df))   # J'imprime le nombre d'espèces d'arbres différents.
print("")

# Question 4:
# Quels noms d'espèces d'arbres (en français) font moins de 20 caractères?
def noms_moins_20car(df):   # Cette fonction montre le nom des espèces d'arbre qui contiennent moins de 20 lettres.
    df_enleve_plus_20car = df[df["NOM_FRANCAIS"].str.len() < 20]    # Je fais une nouvelle liste qui exclu tous les
    # noms d'arbres qui ont ou dépassent 20 lettres.
    df_moins_20car = df_enleve_plus_20car["NOM_FRANCAIS"].unique()  # Chaque espèce ne s'affiche qu'une seule fois.
    return(df_moins_20car)  # La fonction retourne le nom de toutes les espèces d'arbres qui ont un nom qui contient
    # moins de 20 lettres.
print("Nom des espèces qui contiennent moins de 20 caractères :",noms_moins_20car(df))  # J'imprime le nom des espèces
# qui contiennent moins de 20 caractères.
print("")

# Question 5:
# De quelle espèce est l'arbre avec le tronc le plus gros?
def espece_arbre_plus_grand(df):    # Cette fonction affiche le nom de l'espèce d'arbre ayant le plus gros tronc.
    df_nom_diametre = df[["NOM_FRANCAIS", "DIAMETRE"]]  # Je crée une nouvelle liste qui ne contient que le nom et le
    # diamètre de l'arbre.
    df_plus_grand = df_nom_diametre.sort_values(by="DIAMETRE", ascending=False) # Je place l'arbre ayant le plus gros
    # tronc en haut de la liste.
    df_nom = df_plus_grand["NOM_FRANCAIS"]  # Je crée une nouvelle liste où j'enlève la valeur du diamètre de cette
    # liste, car on ne s'intéresse qu'à son espèce.
    return(df_nom.head(1))  # La fonction retourne le premier élément de ma dernière liste.
print("Espèce de l'arbre ayant le plus gros tronc :", espece_arbre_plus_grand(df))  # J'imprime le nom de l'espèce ayant
# le plus gros tronc.
print("")

# Question 6:
# Quel est le diamètre moyen du tronc des feuillus dans la ville de Québec? Des conifères?
def moyenne_tronc(df, type_arbre):  # Cette fonction affiche lla moyenne du diamètre des troncs d'un type d'arbre en
    # particulier.
    df_type = df[df["TYPE_ARBRE"] == type_arbre]    # Je crée une nouvelle liste ne gardant que les lignes ayant un
    # arbre du type spécifique que je recherche.
    desc_type = df_type.describe()  # Cette ligne créée un tableau avec le nombre d'éléments, la moyenne, l'écart type,
    # le minimum, le maximum, et les quartiles de toutes les colonnes contenant des numéros.
    moyenne_type = desc_type.loc["mean", "DIAMETRE"]    # Cette variable correspond à la moyenne des éléments de la
    # colonne "DIAMETRE" du tableau créé à la ligne précédente. Ici, nous cherchons vraiment la moyenne du diamètre,
    # donc "DIAMETRE" n'est pas interchangeable.
    return(moyenne_type)    # La fonction retourne la moyenne de diamètre des troncs d'un type d'arbre spécifique.
print("Diamètre moyen du tronc des feuillus :", round(moyenne_tronc(df, "Feuillu"), 1))   # J'imprime le
# diamètre moyen du tronc pour les arbres de types feuillus.
print("Diamètre moyen du tronc des conifères :", round(moyenne_tronc(df, "Conifère"), 1)) # J'imprime le
# diamètre moyen du tronc pour les arbres de types conifères...
print("")

# GRAPHIQUES
# Graphique 1:
df_enleve_plus_5car = df[df["NOM_FRANCAIS"].str.len() <= 5] # Je crée une nouvelle liste qui contient seulement les
# espèces d'arbres dont les noms en français ne dépasse pas 5 caractères.
df_moins_5car = df_enleve_plus_5car["NOM_FRANCAIS"].sort_values().unique() # Je garde le nom des arbres avec des noms de
# moins de 5 caractères pour qu'ils n'apparaissent qu'une seule fois par type d'arbre et je les mets en ordre
# alphabétique.

nbr_moins_5car = df_enleve_plus_5car.groupby("NOM_FRANCAIS").size().sort_index()    # J'affiche le nombre d'arbres de
# chaque espèce d'arbres. J'organise les données selon l'ordre de la liste df_moins_5car, soit en ordre alphabétique,
# pour que les données fonctionnent ensemble.

def graphique_1():  # Je définis la fonction qui montrera le premier graphique.
    plt.bar(df_moins_5car, nbr_moins_5car)  # Je fais un graphique de diagramme à bar vertical avec le nombre
    # d'espèce d'arbre en y et leurs noms en x.

    plt.xticks(rotation=45, ha='right') # Je tourne le nom des arbres à 45 degrés.
    plt.title("Nombre d'arbres répertoriés pour les 10 espèces d'arbres \n aux noms les plus courts (<= 5 caractères)")
    # Voici le titre du graphique. \n permet de diviser le titre en deux pour qu'il rentre dans le graphique.
    plt.xlabel("")  # Voici le titre de l'axe des x. Ici, il n'y en a pas.
    plt.ylabel("Nombre d'arbres répertoriés")   # Voici le titre de l'axe des y.
    plt.grid(axis='y', linestyle='--', linewidth=0.5)   # J'active le grid mais seulement pour l'axe des y.
    plt.savefig("Graphique 1")  # Je sauvegarde l'image générée.
graphique_1()   # J'appelle la fonction du graphique 1.

# Graphique 2:
def graphique_2():  # Voici la fonction du deuxième graphique.
    df_enleve_plus_5car.boxplot(column="DIAMETRE", by="NOM_FRANCAIS")   # Je fais un graphique de type boxplot avec le
    # diamètre des arbres en cm sur l'axe des y et le nom des espèces d'arbres en x.
    plt.title("Diamètre du tronc des 10 espèces d'arbres \n aux noms les plus courts (<= 5 caractères)")    # Voici le
    # titre du graphique.
    plt.suptitle("")  # Supprimer le titre autogénéré apparaissant en haut de notre titre (il indique le regroupement
    # réalisé)
    plt.xlabel("Espèce d'arbre")    # Voici le titre de l'axe des x.
    plt.xticks(rotation=45, ha='right') # Je tourne le nom des arbres à 45 degrés.
    plt.ylabel("Diamètre (cm)") # Voici le titre de l'axe des y.
    plt.grid(False) # J'enlève le grid de l'axe des x, parce que la fonction boxplot active automatiquement le grid des
    # 2 axes.
    plt.grid(axis='y', linestyle='--', linewidth=0.5)   # Je remets manuellement le grid, mais seulement pour l'axe des
    # y.
    plt.savefig("Graphique 2")  # Je sauvegarde l'image générée.
graphique_2()   # J'appelle la fonction du graphique 2.

# Graphique 3:
def graphique_3():  # Voici la fonction pour le troisième graphique.
    plt.figure()    # Sans ceci, le graphique 3 affichera un boxplot au lieu d'un nuage de point. Il sert à séparer
    # chaque graphique, à les rendre distincts l'un de l'autre.
    df_feuillu = df[df["TYPE_ARBRE"] == "Feuillu"]  # Je fais une nouvelle liste ne contenant que les arbres de types
    # feuillus.
    df_conifere = df[df["TYPE_ARBRE"] == "Conifère"]    # Je fais une nouvelle liste ne contenant que les arbres de
    # types conifères.

    plt.scatter(df_feuillu["LONGITUDE"], df_feuillu["LATITUDE"], s=0.01, alpha=0.5) # s = taille des points
    plt.scatter(df_conifere["LONGITUDE"], df_conifere["LATITUDE"], s=0.01, alpha=0.5) # s = taille des points
    plt.xlabel("Longitude") # Voici le titre de l'axe des x.
    plt.ylabel("Latitude")  # Voici le titre de l'axe des y.
    plt.title("Localisation et type des arbres répertoriés à la Ville de Québec")   # Voici le titre du graphique.
    plt.grid(axis='both', linestyle='--', linewidth=0.5)    # J'active le grid pour les deux axes cette fois.
    plt.legend(title="Type d'arbre", markerscale=50, labels=['Feuillu', 'Conifère'])    # Je configure le nom de chaque
    # couleur dans la légende.
    plt.savefig("Graphique 3")  # Je sauvegarde l'image générée.
graphique_3()   # J'appelle la fonction du graphique 3.

# Graphique 4:
def graphique_4():  # Voici la fonction pour le quatrième graphique.
    plt.figure()    # Sans ceci, le graphique 3 affichera un boxplot au lieu d'un nuage de point. Il sert à séparer
    # chaque graphique, à les rendre distincts l'un de l'autre.
    df_parc_chaudiere = df[df["NOM_TOPOGRAPHIE"] == "Parc de la Chaudière"] # Je crée une nouvelle liste ne contenant
    # que les arbres du parc de la Chaudière.
    df_espece = (df_parc_chaudiere["NOM_FRANCAIS"].unique())    # Je crée une nouvelle liste avec le nom de chaque
    # espèce d'arbres dans le parc de la Chaudière. Chaque nom n'apparait qu'une fois.

    for espece in df_espece:    # Je crée une boucle qui se répètera pour chaque espèce d'arbre dans le parc de la
        # Chaudière.
        df_parc_chaudiere_espece = df_parc_chaudiere[df_parc_chaudiere["NOM_FRANCAIS"] == espece]   # J'isole tous les
        # arbres dont l'espèce correspond à celle de la dernière liste que j'ai créé, et ce, pour chaque espèce de la
        # liste, un après l'autre.
        plt.scatter(df_parc_chaudiere_espece["LONGITUDE"], df_parc_chaudiere_espece["LATITUDE"], s=50, alpha=1,
        label=espece) # s = taille des points

    plt.xlabel("Longitude") # Voici le titre de l'axe des x.
    plt.ylabel("Latitude")  # Voici le titre de l'axe des y.
    plt.title("Localisation et espèces des arbres répertoriés dans le Parc de la Chaudière")    # Voici le titre du
    # graphique.
    plt.legend(title="Type d'arbre", loc='lower left', prop={'size': 6}, title_fontsize=7, markerscale=0.6)     # J'ai
    # créé la légende selon ce qui nous est demandé dans le site du cours.
    plt.grid(axis='both', linestyle='--', linewidth=0.5)    # J'affiche le grid pour chacune des axes.
    plt.savefig("Graphique 4")  # Je sauvegarde l'image générée.
graphique_4()   # J'appelle la fonction du graphique 4.