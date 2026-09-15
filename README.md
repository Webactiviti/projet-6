# Projet : Anticipez les besoins en consommation d'un bâtiment

## contenu du repository

* Un notebook de nettoyage et l'exploration des données et de construction de variables

* Entraîner différentes familles de modèles de machine learning

* utilisation de BenToML et de Pydantic

* Mise en service sur le cloud sur une base  Docker

## exemple de format du JSON 
```text
{
  "input_data": {
    "DataYear": 2016,
    "BuildingAge": 55,
    "BuildingType": "SPS-District K-12",
    "PrimaryPropertyType": "K-12 School",
    "LargestPropertyUseType": "K-12 School",
    "Latitude": 47.54576,
    "Longitude": -122.26853,
    "NumberofBuildings": 1.0,
    "PropertyGFATotal": 56228,
    "PropertyGFAParking": 0,
    "mean_GFA_per_floor": 18742,
    "Number_of_Use_Types": 1,
    "ENERGYSTARScoreIsMissing": 0
  }
}
```
* liste des commandes bentoml

Affichage du bentoml et models

uv run bentoml models list

uv run bentoml  list

* Construction du bentoml

 importer le model dans le projet

uv run bentoml models export seattle_co2  ./models/seattle_co2



uv run bentoml build



uv run bentoml containerize seattle_building_service

et ensuite 

docker run --rm -p 3000:3000 seattle_building_service:(TAG)

Lancer BenToML en local

uv run bentoml serve service:SeattleBuildingService --reload


* autres commandes

Respecter l'ordre des commandes  si vous voulez supprimer

uv run bentoml  delete seattle_building_service:(TAG)

uv run bentoml models  delete seattle_co2:(TAG)

* ordre d'utilisation des notebooks

AnalyseExploiratoire.ipynb

analyse_ml.ipynb

bentoml_prediction.ipynb ( créer le bentoml avant l'utilisation')

* afficher le ou les docker et supression

sudo docker images "seattle_building_service"

sudo docker rmi -f $(docker images "seattle_building_service" )

## 📂 Structure du Répertoire

```text
projet_6/
├── AnalyseExploiratoire.ipynb                      # Script d'analyse du fichier CSV 
├── analyse_ml.ipynb                                # Script d'analyse ML
├── docker-compose.yml                              # Orchestration des conteneurs 
├── Dockerfile                                      # Configuration du conteneur pour le cloud render.com
├── service.py                                      # Script service BenToML
├── bentofile.yaml                                  # Script 
├── bentoml_prediction.ipynb                        # Script ML
├── pyproject.toml                                  # Gestion des dépendances Python (uv)
├── data                                            # répertoire des données 
|    └── 2016_Building_Energy_Benchmarking.csv      # fichier data de Seattle
|    └── projet6_analyse.csv                        # fichier analysé
|    └── dico_seattle_2016.xlsx                     # dictionnaire de données
|    └── building_sample.json                       # exemple de fichier JSON pour le ML sue le cloud
|    └── projet6_estimation.csv                     # fichier extrait des data quand estimé
├── models                                          # répertoire des models ML 
|    └── seattle_co2.bentoModel                     # fichier du model ML
└── README.md                                       # Documentation du projet
```
