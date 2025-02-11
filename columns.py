from enum import Enum


class ColumnNames(str,Enum):
    Patient_Id = 'Patient Id'
    Age = 'Age'
    Gender = 'Gender'
    Air_Pollution = 'Air Pollution'
    Alcohol_Use = 'Alcohol use'
    Dust_Allergy = 'Dust Allergy'
    Occupational_Hazards = 'OccuPational Hazards'
    Genetic_Risk = 'Genetic Risk'
    Chronic_Lung_Disease = 'chronic Lung Disease'
    Balanced_Diet = 'Balanced Diet'
    Obesity = 'Obesity'
    Smoking = 'Smoking'
    Passive_Smoker = 'Passive Smoker'
    Chest_Pain = 'Chest Pain'
    Coughing_of_Blood = 'Coughing of Blood'
    Fatigue = 'Fatigue'
    Weight_Loss = 'Weight Loss'
    Shortness_of_Breath = 'Shortness of Breath'
    Wheezing = 'Wheezing'
    Swallowing_Difficulty = 'Swallowing Difficulty'
    Clubbing_of_Finger_Nails = 'Clubbing of Finger Nails'
    Frequent_Cold = 'Frequent Cold'
    Dry_Cough = 'Dry Cough'
    Snoring = 'Snoring'
    Level = 'Level'
