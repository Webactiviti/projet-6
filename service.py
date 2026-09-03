import bentoml
import numpy as np
import pandas as pd

# Import du schéma Pydantic
from BuildingInput import BuildingInput

# Force la résolution complète du schéma Pydantic pour BentoML
BuildingInput.model_rebuild()


@bentoml.service(
    name="seattle_building_service",
    resources={"cpu": "200m", "memory": "512Mi"},
)
class SeattleBuildingService:

    def __init__(self):
        # Chargement automatique de la dernière version du modèle depuis le store BentoML
        self.model = bentoml.sklearn.load_model("seattle_co2:latest")

    @bentoml.api()
    def predict(self, input_data: BuildingInput) -> dict:
        # Convertit l'objet Pydantic directement en DataFrame Pandas à 1 ligne
        df_input = pd.DataFrame([input_data.model_dump()])

        # Prédiction (modèle entraîné en log1p)
        pred_log = self.model.predict(df_input)

        # Reconversion réelle
        predictions = float(np.expm1(pred_log)[0])

        return {"prediction_tCO2": round(predictions, 2)}