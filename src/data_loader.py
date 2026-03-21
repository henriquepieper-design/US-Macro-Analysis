import pandas as pd
import os 
from datetime import date
import fredapi as fred

FRED_SERIES = {
    "gdp_real": "GDPC1",#quarterly
    "unemployment": "UNRATE",#monthly
    "cpi": "CPIAUCSL",#monthly
    "fed_funds_rate": "FEDFUNDS",#monthly
}

def get_fred_client(api_key: str = None) -> fred:
    key = api_key or os.getenv("FRED_KEY_API")
    if not key:
        raise ValueError("FRED API key not found.",
                         "Set the FRED_KEY_API environment variable or pass it directly")
    return fred.Fred(api_key=key)

def fetch_series(fred: fred, series_id: str, start: str, end: str) -> pd.Series:
    return fred.get_series(series_id, observation_start=start, observation_end=end)

def load_macro_data(
    api_key: str = None,
    start: str = "1970-01-01",
    end: str = str(date.today()),
) -> pd.DataFrame:
    fred = get_fred_client(api_key)

    series = {}
    for name, series_id in FRED_SERIES.items():
        print(f"Fetching {name} ({series_id})...")
        series[name] = fetch_series(fred, series_id, start, end)

    df = pd.DataFrame(series)
    df.index.name = "date"
    return df


def save_raw(df: pd.DataFrame, path: str = "data/raw/macro_data.csv") -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path)
    print(f"Saved to {path}")
 