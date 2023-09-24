from pandas import pandas as pd
import pynsee
from pynsee.macrodata.get_series import get_series
from pynsee.utils.init_conn import init_conn
import joblib
def GetData():
    init_conn(insee_key="qVEgZrQLRUAK9YL1zrWJigwaPNoa", insee_secret="fXzRKDIN0RnGQRx6laam9zbqMc8a")

    dataGDP = get_series("001690224")
    dataGDP = pd.DataFrame(dataGDP)
    dataGDP = dataGDP.rename(mapper=dataGDP["DATE"])
    GDP = pd.DataFrame(dataGDP["OBS_VALUE"]/1000)
    dataCTB = get_series("001694183")
    dataCTB = pd.DataFrame(dataCTB)
    dataCTB = dataCTB.rename(mapper=dataCTB["DATE"])
    CTB = pd.DataFrame(dataCTB["OBS_VALUE"]/1000)
    data_merge0 = pd.merge(GDP, CTB, left_index=True, right_index=True)
    data_merge0.columns = ["GDP", "CTB"]

    dataDebt = pd.DataFrame(get_series('010596744'))
    dataExpenses = pd.DataFrame(get_series('010588331'))
    dataDebt = dataDebt.rename(mapper=dataDebt["DATE"])
    Debt = pd.DataFrame(dataDebt["OBS_VALUE"])
    dataExpenses= dataExpenses.rename(mapper=dataExpenses["DATE"])
    Expenses = pd.DataFrame(dataExpenses["OBS_VALUE"]/1000)
    data_merge = pd.merge(Expenses, Debt, left_index=True, right_index=True)
    data_merge.columns = ["Public expenses", "Public debt"]
    df_Merge = pd.merge(data_merge0, data_merge, left_index=True, right_index=True)

    dataUnemployment = get_series("001688526")
    dataUnemployment = pd.DataFrame(dataUnemployment)
    dataUnemployment = dataUnemployment.rename(mapper=dataUnemployment["DATE"])
    Unemployment = pd.DataFrame(dataUnemployment.iloc[:, 2])
    dataInflation = get_series('001761313')
    dataInflation = pd.DataFrame(dataInflation)
    dataInflation = dataInflation.rename(mapper=dataInflation["DATE"])
    Inflation = pd.DataFrame(dataInflation["OBS_VALUE"])
    Inflation = Inflation.rename(mapper=dataInflation["DATE"])
    data_merge2 = pd.merge(Inflation, Unemployment, left_index=True, right_index=True)
    data_merge2.columns = ["Inflation", "Unemployment"]

    df_MergeFin = pd.merge(df_Merge, data_merge2, left_index=True, right_index=True)

    return df_MergeFin
def get_cached_data():
    try:
        # Charger les données à partir du cache s'il existe
        df = joblib.load("data_cache.pkl")
        print("Utilisation des données en cache.")
    except FileNotFoundError:
        # Si le cache n'existe pas, extraire les données de l'API et les mettre en cache
        df = GetData()
        joblib.dump(df, "data_cache.pkl")
        print("Données extraites de l'API et mises en cache.")

    return df