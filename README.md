# Servier drugs in clinicals trials and pubmed

## Description
Ce projet développe un pipeline de traitement de données en Python, conçu pour nettoyer, transformer et analyser les mentions de médicaments issues de publications scientifiques et d'essais cliniques. Il s'organise autour de plusieurs fichiers Python, décrits en détail dans les sections suivantes.

Les étapes du projet incluent :
1. **Data clean** : 
Appliquer un ensemble de traitement pour nettoyer et uniformiser la donnée :

    **1.1** Standardisation du format des dates: les dates dans les fichiers ont plusieurs format différents donc il faut standariser le format pour pouvoir les traiter.

    **1.2** Traitement des problèmes d'encodage : "\xc3\x28".

    **1.3** Suppression des espaces non nécéssaires.

2. **Data pipeline** : 
Élaboration d'un graphe reliant chaque médicament à ses mentions dans divers journaux, en incluant les dates et types de publication.

3. **Traitement ad-hoc** : 
Depuis le json produit par la data pipeline:

**•** Extraire le nom du journal qui mentionne le plus de médicaments différents.

**•** Pour un médicament donné, trouver l’ensemble des médicaments mentionnés par les mêmes
journaux.

## Structure du projet

Le dossier **sources** contient les fichiers de données JSON et CSV et le dossier **tests** contient les tests unitaires.
- **`Github CI`** : Lance un workflow de test lorsqu'un push ou un merge est effectué sur la branche test.
- **`clean.py`** : Contient les fonctions de cleansing citées dans la partie précédente.
- **`data_pipeline.py`** : Contient la partie de la génération du graphe de mentions.
- **`adhoc.py`** : Contient la partie des traitements ad-hoc.
- **`main.py`** : Le point d'entrée principal du projet qui orchestre l'appel des autres fichiers.
- **`requirements.txt`** : Contient les dépendances du projet, ici pandas.


## Installation des dépendances

- pandas

pip3 install -r requirements.txt

## Exécution du projet 

python3 main.py

Résultat de l'exécution ci dessous: 

![alt text](<Screenshot 2024-12-07 at 10.15.25.png>)


## Exécution des tests unitaires

python3 -m unittest discover -s tests

![alt text](<Screenshot 2024-12-07 at 10.16.41.png>)

## Amélioration

Points pour adapter le code à de grands volumes de données :

- **Deployement sur cloud** Déployer ce projet sur Google Cloud Platform pour bénéficier d'une meilleure performance en matière de stockage et d'exécution

- **Partitionnement des données**  si la donnée est énorme cela peut être utile de partitionner par date par exemple ou autre(s) colonne(s) pertinentes

- **Orchestration des pipeline** avec airflow ou dataflow, workflow pour organiser et automatiser l'éxécution les taches.

- **Parallélisation** du traitement de données avec des threads.

- **Monitoring et gestion des erreurs**  Utiliser des outils de logging et de monitoring pour surveiller les performances.

- **Intégration continue (CI)** Joue un rôle essentiel lors des étapes de push et de merge dans le processus de développement. Elle permet d'automatiser les tests et les vérifications sur le code nouvellement ajouté, garantissant ainsi sa qualité et sa conformité avec les normes du projet. 

## Partie SQL


**Première partie du test SQL**


SELECT date, SUM(prod_price*prod_qty) AS total 

FROM TRANSACTIONS

WHERE date BETWEEN '2019-01-01' AND '2019-12-31'

GROUP BY date

ORDER BY date ASC

**Seconde partie du test SQL**


SELECT

  tr.client_id,

  SUM(CASE WHEN pn.product_type = 'MEUBLE' THEN tr.prod_price * tr.prod_qty ELSE 0 END) AS ventes_meuble,

  SUM(CASE WHEN pn.product_type = 'DECO' THEN tr.prod_price * tr.prod_qty ELSE 0 END) AS ventes_deco

FROM 
  TRANSACTIONS tr
WHERE 
    date BETWEEN '2019/01/01' AND '2019/12/31'

JOIN 
  PRODUCT_NOMENCLATURE pn
ON 
  t.prod_id = pn.product_id
GROUP BY 
  t.client_id
