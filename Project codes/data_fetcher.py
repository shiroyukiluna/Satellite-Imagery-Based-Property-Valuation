# Imports

from asyncio import futures
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import requests
import pandas as pd
from time import sleep


# Configuration

MAPBOX_TOKEN = "pk.eyJ1Ijoic2lnaHR5MDciLCJhIjoiY21qaWRlczJrMGwwYzNmc2x3NTV0MXA2MyJ9.C2-ykOD9lUzEX17cX6rYMw"
ZOOM = 18
IMAGE_SIZE = "224x224"
STYLE = "satellite-v9"

BASE_URL = f"https://api.mapbox.com/styles/v1/mapbox/{STYLE}/static"


# Image fetch function

def fetch_image(row, output_dir):
    image_path = os.path.join(output_dir, f"{row['id']}.png")

    # Skip if already exists
    if os.path.exists(image_path) and os.path.getsize(image_path) > 0:
        return "skipped"

    url = f"{BASE_URL}/{row['long']},{row['lat']},{ZOOM},0,0/{IMAGE_SIZE}"
    params = {"access_token": MAPBOX_TOKEN}

    try:
        r = requests.get(url, params=params, timeout=10)
        if r.status_code == 200:
            with open(image_path, "wb") as f:
                f.write(r.content)
            return "downloaded"
        else:
            return "failed"
    except Exception:
        return "error"


# Parallel download function

def download_images_fast(df, output_dir, max_workers=8):
    os.makedirs(output_dir, exist_ok=True)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(fetch_image, row, output_dir)
            for _, row in df.iterrows()
        ]

        for future in as_completed(futures):
            pass  # we don't need per-image logs


# Run it

if __name__ == "__main__":
    train = pd.read_excel("data/train1.xlsx")
    test  = pd.read_excel("data/test2.xlsx")

    download_images_fast(train, "images/train", max_workers=8)
    download_images_fast(test,  "images/test",  max_workers=8)

    print("Download complete")


