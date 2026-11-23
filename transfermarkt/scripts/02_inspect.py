from pathlib import Path
import pandas as pd

# Paths are built from the script's own location, so it works from anywhere
ROOT = Path(__file__).resolve().parent.parent   # the transfermarkt folder
RAW = ROOT / "data" / "raw"
REPORT = ROOT / "logs" / "inspection_report.txt"

lines = []

def out(text=""):
    """Print on screen AND keep a copy for the report file."""
    print(text)
    lines.append(str(text))

# Part 1: generic inspection of every CSV file
for f in sorted(RAW.glob("*.csv")):
    df = pd.read_csv(f)
    out(f"\n===== {f.name} =====")
    out(f"Rows: {len(df):,} | Columns: {df.shape[1]}")
    out(f"Columns: {df.columns.tolist()}")
    out("Share of missing values (top 10 columns):")
    out(df.isna().mean().sort_values(ascending=False).head(10).round(3))

    # Any column with "date" in its name: show the range
    for col in [c for c in df.columns if "date" in c.lower()]:
        d = pd.to_datetime(df[col], errors="coerce")
        out(f"Date range of '{col}': {d.min()} -> {d.max()}")

# Part 2: valuation points per player (adjust names if your files differ)
val_file = RAW / "player_valuations.csv"
if val_file.exists():
    vals = pd.read_csv(val_file, parse_dates=["date"])
    out("\n===== Valuation points per player =====")
    out(vals.groupby("player_id").size().describe())

REPORT.write_text("\n".join(lines), encoding="utf-8")
print(f"\nReport saved to {REPORT}")