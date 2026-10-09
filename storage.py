# Zakhire-ye natije. Hich input/print inja nist.
import json


def save_result(result, path="results.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)