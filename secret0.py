
import requests
import pandas as pd
from io import StringIO


def decode_secret_message(url):
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    tables = pd.read_html(StringIO(response.text))

    if not tables:
        print("No table found!")
        return

    data = tables[0]
    data.columns = data.iloc[0]
    data = data.iloc[1:].reset_index(drop=True)

    # Remove extra spaces from column names
    data.columns = [
        str(col).strip().lower() for col in data.columns
    ]

    print("Column names:", data.columns.tolist())
    print("First rows:")
    print(data.head())

    # Identify columns by their actual names
    x_col = None
    y_col = None
    char_col = None

    for col in data.columns:
        name = str(col).lower()

        if name == "x" or "x-coordinate" in name or "x coordinate" in name:
            x_col = col
        elif name == "y" or "y-coordinate" in name or "y coordinate" in name:
            y_col = col
        elif any(word in name for word in ["character", "char", "unicode"]):
            char_col = col

    # If the column names are unclear, show them instead of crashing
    if x_col is None or y_col is None or char_col is None:
        print("\nColumn names do not match the expected format.")
        print("Send me the Column names and First rows shown above.")
        return

    points = []

    for _, row in data.iterrows():
        try:
            x = int(row[x_col])
            y = int(row[y_col])
            char = str(row[char_col])

            if char.lower() != "nan":
                points.append((x, y, char))
        except (ValueError, TypeError):
            continue

    if not points:
        print("No valid points found.")
        return

    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)
    min_y = min(p[1] for p in points)
    max_y = max(p[1] for p in points)

    grid = [
        [" "] * (max_x - min_x + 1)
        for _ in range(max_y - min_y + 1)
    ]

    for x, y, char in points:
        grid[max_y - y][x - min_x] = char

    print("\nDecoded secret message:\n")

    for row in grid:
        print("".join(row))


url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"

try:
    decode_secret_message(url)
except requests.RequestException as error:
    print("Download error:", error)