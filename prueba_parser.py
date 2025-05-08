# test.py

import sys
import json
from parse_to_json import parse_forecast

def main():
    if len(sys.argv) < 2:
        print("Uso: python test.py 'TEXTO_DEL_FORECAST'")
        sys.exit(1)

    input_text = sys.argv[1]
    result = parse_forecast(input_text)

    print(json.dumps(result, indent=2))

    with open("output_forecast.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
