from antlr4 import *
from ForecastLexer import ForecastLexer
from ForecastParser import ForecastParser
from parse_to_json import parse_forecast
from ForecastModel import weather_forecast

input_text = "FORECAST PM25 AT zona_norte IN 2 HOURS IF WIND > 10 AND HUMIDITY < 40"
tree = parse_forecast(input_text)
forecast_text = weather_forecast(tree)
print(forecast_text)