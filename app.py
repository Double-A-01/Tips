import streamlit as st
import pandas as pd
import json
import subprocess
import os
from glob import glob
from datetime import datetime

st.title("🏇 UK Horse Racing Tips – Today")
st.info("Running racecards scraper...")

try:
    result = subprocess.run(
        ["python3", "rpscrape/scripts/racecards.py"],
        capture_output=True, text=True, check=True
    )
    st.success("Scraper ran successfully")
    st.code(result.stdout)
except subprocess.CalledProcessError as e:
    st.error("Scraper failed")
    st.code(e.stderr)
    st.stop()

# Show what's inside the folder
st.write("Files in scripts folder:", os.listdir("rpscrape/scripts"))

try:
    latest = sorted(glob("rpscrape/scripts/racecards-*.json"))[-1]
    with open(latest, "r") as f:
        data = json.load(f)
except:
    st.warning("No racecards file found")
    st.stop()

tips = []
for meeting in data.get("meetings", []):
    if meeting.get("region") != "gb":
        continue
    for race in meeting.get("races", []):
        for runner in race.get("runners", []):
            score = 0
            if runner.get("form", [9])[0] <= 3: score += 1
            if runner.get("trainer_strike", 0) >= 0.10: score += 1
            if race.get("going", "").lower() in runner.get("going", "").lower(): score += 1
            if runner.get("or", 99) <= 3: score += 1
            if score >= 2:
                tips.append({
                    "course": meeting["course"],
                    "time": race["time"],
                    "name": runner["name"],
                    "trainer": runner["trainer"],
                    "jockey": runner["jockey"],
                    "odds": runner["odds"],
                    "score": score
                })

if tips:
    st.dataframe(pd.DataFrame(tips))
else:
    st.warning("No tips found for today.")