# test.py

from parse_to_json import parse_forecast
import json

def main():
    input_text = "FORECAST PM12 AT zona_norte IN 15 HOURS IF SUN > 10 AND HUMIDITY < 40"
    result = parse_forecast(input_text)
    print(json.dumps(result, indent=2))
   # with open("output_forecast.json", "w", encoding="utf-8") as f:
    # json.dump(result, f, indent=2)



if __name__ == "__main__":
    main()
