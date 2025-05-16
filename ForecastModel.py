#Se corre en main.py
#Árbol de Sintaxis Abstracta (AST).
#flujo final compilador
import numpy as np

def weather_forecast(tree):
    """
    {
        "type": "ForecastStatement",
        "pollutant": "PM25",
        "location": "zona_norte",
        "duration_hours": 2,
        "conditions": [
            {
            "metric": "WIND",
            "comparator": ">",
            "value": 10
            },
            {
            "metric": "HUMIDITY",
            "comparator": "<",
            "value": 40
            }
        ]
    }
    """

    forecast = np.random.randint(0, 100)
    # Simulate a forecast value for the pollutant
    forecast_text = f"""The forecast for {str(tree["pollutant"])} in zona_norte in 2 hours is {forecast} micrograms per cubic meter."""
    return forecast_text