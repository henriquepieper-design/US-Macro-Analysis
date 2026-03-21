# US Macroeconomic Analysis
An analysis of US macroeconomic indicators from 1970 to the present, using data from Federal Reserve Economic Data (FRED) API. This project covers business cycle decomposition, inflation dynamics, and the historical relationship between unemployment and inflation and the misery index.
---
## Overview
This project investigates four core macroeconomic series:
- **Real GDP** - quarterly output of the US economy
- **Unemployment Rate** - monthly share of the labor force without work
- **CPI** - Consumer Price Index, used as a proxy for inflation
- **Federal Funds Rate** - the benchmark interest rate set by the Federal Reserve

Using these series, the analysis explores business cycles, the Phillips Curve, and the Misery Index across more than five decades of US economic history.
---
## Project Structure
```
us-macro-analysis/
├── data/
│   ├── raw/                  # raw data from FRED API
│   └── processed/            # cleaned and transformed data
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_business_cycles.ipynb
│   ├── 04_phillips_curve.ipynb
│   └── 05_misery_index.ipynb
├── src/
│   ├── data_loader.py
│   
├── outputs/
│   └── figures/
├── .gitignore
├── README.md
└── requirements.txt
```
---
## Notebooks 
| Notebook | Description |
|---|---|
| `01_data_collection` | Fetches and saves raw data from the FRED API |
| `02_exploratory_analysis` | Time series visualization with NBER recession shading |
| `03_business_cycles` | HP filter decomposition of Real GDP into trend and cycle |
| `04_phillips_curve` | OLS regression of unemployment vs inflation by decade |
| `05_misery_index` | Misery Index construction and historical analysis |

---

## Key Findings
- The **HP filter** (λ=1600) successfully decomposes Real GDP into a long-run trend and a cyclical component, with negative cycle values aligning closely with NBER recession periods.
- The **Phillips Curve** relationship varies significantly by decade. The classic negative trade-off between unemployment and inflation is strongest in the 2000s (R²=0.50), while the 1970s and 1980s show no significant relationship, consistent with supply-side inflation shocks dominating those periods.
- The **Misery Index** peaked at 21.9 in 1980 during the Volcker disinflation period — substantially higher than the COVID-19 peak — reflecting the prolonged combination of high inflation and rising unemployment in that era.
## Setup

**1. Clone the repository**
```bash
git clone https://github.com/your-username/us-macro-analysis.git
cd us-macro-analysis
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up your FRED API key**

Get a free API key at https://fred.stlouisfed.org/docs/api/api_key.html

Create a `.env` file in the root directory:
```
FRED_API_KEY=your_key_here
```

**4. Run the notebooks in order**

Start with `01_data_collection.ipynb` to fetch and save the data, then proceed through the remaining notebooks.

---

## Dependencies

- `pandas` — data manipulation
- `numpy` — numerical operations
- `fredapi` — FRED API client
- `statsmodels` — econometric models and HP filter
- `plotly` — interactive visualizations
- `scipy` — OLS regression
- `python-dotenv` — environment variable management

---

## Data Source

All data sourced from the [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/), Federal Reserve Bank of St. Louis.

| Series ID | Description | Frequency |
|---|---|---|
| GDPC1 | Real Gross Domestic Product | Quarterly |
| UNRATE | Unemployment Rate | Monthly |
| CPIAUCSL | Consumer Price Index | Monthly |
| FEDFUNDS | Federal Funds Rate | Monthly |
| USREC | NBER Recession Indicator | Monthly |

---

## Author

**Henrique Rosso Pieper**
[GitHub](https://github.com/henriquepieper-design) · [Email](mailto:henriquepieper@gmail.com)

