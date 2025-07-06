import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
from datetime import date
from utils.going import get_surface
from utils.header import RandomHeader
from utils.lxml_funcs import find

# Simulate a successful scrape (simplified)
data = {
    "meetings": [
        {
            "region": "gb",
            "course": "Sandown",
            "races": [
                {
                    "time": "14:00",
                    "going": "Good to Soft",
                    "runners": [
                        {
                            "name": "Lightning Bolt",
                            "trainer": "Jane Smith",
                            "jockey": "Tom Hardy",
                            "form": [2],
                            "trainer_strike": 0.15,
                            "going": "Good to Soft",
                            "or": 2,
                            "odds": "4/1"
                        },
                        {
                            "name": "Slow Runner",
                            "trainer": "Joe Bloggs",
                            "jockey": "Bob Rider",
                            "form": [5],
                            "trainer_strike": 0.08,
                            "going": "Good",
                            "or": 6,
                            "odds": "12/1"
                        }
                    ]
                }
            ]
        }
    ]
}

# Save mock JSON to expected path
output_path = os.path.join(os.path.dirname(__file__), f"racecards-{date.today()}.json")
with open(output_path, "w") as f:
    json.dump(data, f)

print(f"✅ Racecards JSON saved to {output_path}")