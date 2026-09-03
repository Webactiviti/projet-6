from typing import Literal, Self
from pydantic import BaseModel, ConfigDict, Field, model_validator

class BuildingInput(BaseModel):
    # Gestion date
    DataYear: int = Field(
        ...,
        ge=2016,
        le=2026,
        description="Année de collecte de la donnée",
        examples=[2016],
    )
    BuildingAge: int = Field(
        ...,
        ge=0,
        le=200,
        description="Âge du bâtiment en années",
        examples=[35],
    )

    # CATÉGORIES
    BuildingType: str = Field(
        ...,
        description="Type de bâtiment",
        examples=["NonResidential"],
    )
    PrimaryPropertyType: str = Field(
        ...,
        description="Usage principal",
        examples=["Hotel"],
    )
    LargestPropertyUseType: str = Field(
        ...,
        description="Usage occupant la plus grande surface",
        examples=["Hotel"],
    )

    # GÉOLOCALISATION (Bornes sur la ville de Seattle)
    Latitude: float = Field(
        ...,
        ge=47.4,
        le=47.8,
        description="Latitude (Zone Seattle)",
        examples=[47.6062],
    )
    Longitude: float = Field(
        ...,
        ge=-122.5,
        le=-122.1,
        description="Longitude (Zone Seattle)",
        examples=[-122.3321],
    )

    # STRUCTURE ET SURFACES
    NumberofBuildings: float = Field(
        ...,
        ge=1,
        le=100,
        description="Nombre de bâtiments sur le site",
        examples=[1.0],
    )
    PropertyGFATotal: int = Field(
        ...,
        gt=0,
        le=10000000,
        description="Surface totale en sqft (> 0)",
        examples=[90000],
    )
    PropertyGFAParking: int = Field(
        ...,
        ge=0,
        description="Surface dédiée au parking en sqft",
        examples=[15000],
    )
    mean_GFA_per_floor: float = Field(
        ...,
        gt=0,
        description="Surface moyenne par étage en sqft",
        examples=[18000.0],
    )
    Number_of_Use_Types: int = Field(
        ...,
        ge=1,
        le=20,
        description="Nombre de types d'utilisations différentes",
        examples=[2],
    )

    # SCORES & INDICATEURS DE DONNÉES MANQUANTES
    ENERGYSTARScore: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Score Energy Star (0 à 100)",
        examples=[75.0],
    )
    ENERGYSTARScoreIsMissing: Literal[0, 1] = Field(
        ...,
        description="Flag indiquant si le score était manquant à l'origine (0 ou 1)",
        examples=[0],
    )

    # RATIOS ÉNERGÉTIQUES (0.0 à 1.0)
    Ratio_Electricity: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Proportion d'électricité (entre 0 et 1)",
        examples=[0.65],
    )
    Ratio_Steam: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Proportion de vapeur/gaz (entre 0 et 1)",
        examples=[0.35],
    )

    # VALIDATIONS LOGIQUES
    @model_validator(mode="after")
    def validate_surfaces_and_ratios(self) -> Self:
        # 1. Cohérence géométrique
        if self.PropertyGFAParking >= self.PropertyGFATotal:
            raise ValueError(
                f"La surface de parking ({self.PropertyGFAParking} sqft) "
                f"ne peut pas dépasser la surface totale ({self.PropertyGFATotal} sqft)."
            )

        # 2. Cohérence énergétique
        total_ratio = self.Ratio_Electricity + self.Ratio_Steam
        if total_ratio > 1.05:
            raise ValueError(
                f"La somme des ratios d'énergie ({total_ratio:.2f}) "
                "ne peut pas être supérieure à 1.0."
            )

        return self


    # CONFIGURATION JSON PAR DÉFAUT DANS SWAGGER UI :
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
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
                "mean_GFA_per_floor": 18742.66,
                "Number_of_Use_Types": 1,
                "ENERGYSTARScore": 95.0,
                "ENERGYSTARScoreIsMissing": 0,
                "Ratio_Electricity": 0.6086186356674146,
                "Ratio_Steam": 0.0,
            }
        }
    )
