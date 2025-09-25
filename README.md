# README — Sentiment vs Trader Performance (Submission Package)

**Short project summary**

We explored the relationship between Bitcoin market sentiment (Fear/Greed index) and trader performance using Hyperliquid historical trades. Deliverables include cleaned data, aggregated features, EDA and analysis notebooks, event-study and Granger causality outputs, a detailed final report, a slide deck, and a small Streamlit demo.

---

## What we DID (high level)
- Cleaned and normalized the Hyperliquid trade data (timestamps, sizes, sides, PnL flags).
- Cleaned the Fear/Greed sentiment series and normalized the numeric index to [-1,1].
- Aggregated trades to daily, per-account metrics (daily PnL, num trades, win rate, avg size, leverage where available).
- Performed EDA: distributions, skewness, top accounts, rolling correlations.
- Performed event studies around extreme-sentiment days ([-3,+3]) at market and account levels.
- Ran Granger-causality tests (market-level and per-account samples) to study lead/lag relationships.
- Produced a detailed multi-page PDF report and an 8-slide presentation.

---

## Where to find things (exact paths)
All files live in the folder: `submission_package/`

Key files:

- `trades_clean.csv` — cleaned & normalized Hyperliquid trades
- `sentiment_clean.csv` — cleaned Fear/Greed index (numeric + labels)
- `daily_account_agg.csv` — per-account, per-day aggregates
- `daily_overall_agg.csv` — market-level daily aggregates
- `merged_daily_sentiment.csv` — merged daily market metrics + sentiment

Event-study outputs:
- `event_study_market_low.csv`, `event_study_market_high.csv`
- `event_study_account_low.csv`, `event_study_account_high.csv`
- `event_study_market_low.png`, `event_study_market_high.png`, `event_study_account_low.png`, `event_study_account_high.png`

Causality & tests:
- `granger_full_summary.json` — ADF & Granger p-values (market & account sampling)
- `granger_account_summary.csv` — account-level Granger summary

Notebooks & code:
- `1_eda.ipynb`
- `2_features_and_aggregation.ipynb`
- `3_analysis.ipynb`
- `streamlit_app.py` — starter demo

Reports & presentation:
- `final_report_detailed.pdf` — detailed final report (multi-page)
- `presentation.pdf` — 8-slide deck

Helper files:
- `requirements.txt`
- `README.md` (you are reading)

---

## How to run (repro steps)
> Recommended: run from the parent directory of `submission_package/` so the notebooks will find the files using the shipped relative paths.

1. **Create & activate virtual environment**

```bash
python -m venv venv
source venv/bin/activate    # macOS / Linux
# venv\Scripts\activate    # Windows
```

2. **Install dependencies**

```bash
pip install -r submission_package/requirements.txt
# (optional) pillow is useful for embedding images: pip install pillow
```

3. **Open Jupyter and run notebooks**

```bash
jupyter notebook
# Open and run (in order):
# submission_package/1_eda.ipynb
# submission_package/2_features_and_aggregation.ipynb
# submission_package/3_analysis.ipynb
```

4. **Run the demo Streamlit app** (optional)

```bash
streamlit run submission_package/streamlit_app.py
```

5. **Re-generate the detailed PDF** (if needed)
- The file `final_report_detailed.pdf` is provided. If you want to re-run the script that produced it, open the relevant notebook cell that generates the PDF (see `1_eda.ipynb`) and execute.

---

## Useful quick commands
- Show first rows of cleaned trades:

```bash
python - <<'PY'
import pandas as pd
print(pd.read_csv('submission_package/trades_clean.csv').head())
PY
```

- Inspect event-study CSVs:

```bash
python - <<'PY'
import pandas as pd
print(pd.read_csv('submission_package/event_study_market_low.csv'))
PY
```

---

## What to look for (review checklist)
Use this checklist when reviewing results:

1. **Data integrity**
   - Confirm timestamp correctness: check `trades_clean.csv` max/min `time`. There are future-dated records (2025-12-04) — validate whether these are intended.
   - Check `closedPnL` distribution: heavy skew exists (median = 0; mean > median).

2. **EDA & distributions**
   - Look in `final_report_detailed.pdf` pages for histograms and percentiles (1%,5%,25%,50%,75%,95%,99%).
   - Top accounts by total PnL: verify if a small number of accounts dominate returns.

3. **Event study**
   - Inspect `event_study_market_*.csv` and `event_study_account_*.csv` and corresponding PNGs. Does the mean/CI behavior around t=0 match expectations? Check alternative windows (e.g., [-1,+1] or [-7,+7]) in the notebooks.

4. **Causality**
   - Check `granger_full_summary.json`: note that market→sentiment shows small p-values across many lags; sentiment→market has weaker p-values. This suggests the index is reactive.

5. **Repro & robustness**
   - Re-run panel regressions (not included by default) with BTC returns and realized volatility as controls to confirm whether sentiment adds incremental predictive power.

---

## How we organized the analysis (short overview for reviewers)
- **Cleaning & aggregation**: single-pass cleaning pipeline saved cleaned CSVs. Aggregations to daily by account implemented in `2_features_and_aggregation.ipynb`.
- **EDA**: `1_eda.ipynb` contains data quality checks, distributions, and initial charts (market PnL timeseries, histograms).
- **Analysis**: `3_analysis.ipynb` contains example regressions, event-study code, and Granger causality calls used to produce `granger_full_summary.json`.
- **Deliverables**: `final_report_detailed.pdf` contains consolidated results and interpretation. `presentation.pdf` contains an 8-slide executive deck.

---

## Known issues & caveats (important for reviewer to note)
- **Future-dated timestamps**: max trade date is after the system date used for analysis; these may be placeholders or erroneous. Reviewer should confirm with data provider.
- **Skew & outliers**: a few trades drive most PnL. Interpret mean-based aggregates cautiously.
- **No BTC price included**: causal/regression claims should include BTC returns & realized volatility. We provided places in notebooks to merge such data (you must supply `btc_daily.csv` if desired).
- **Stationarity & sample size**: Granger tests require enough post-differencing observations; some account-level tests were skipped for being too short.

---

## Recommended reviewer workflow (step-by-step)
1. Inspect `submission_package/trades_clean.csv` and `sentiment_clean.csv` for obvious anomalies (timestamps, NaNs). Check counts and unique accounts.
2. Open `final_report_detailed.pdf` for the 1–2 minute executive read (contains the main figures & takeaways).
3. Open `1_eda.ipynb` and run cells to reproduce histograms and the market PnL timeseries.
4. Run the event-study cell in `3_analysis.ipynb` (adjust window/quantile if desired) and inspect CSV output + PNGs.
5. Open `granger_full_summary.json` to review ADF decisions and Granger p-values. Run additional lags if you prefer.
6. (Optional) Add BTC daily returns and re-run panel regressions as described in the notebooks.

---

## Contact / who to ask
If you need additional tests, deeper econometric models, or a dashboard, contact the project owner (uploader) or request me (assistant) to run the chosen analyses. I can produce panel FE regressions, predictive models, clustering, or a Streamlit dashboard on demand.

---

Thank you for reviewing this submission package — the code & notebooks are intentionally modular so you can reproduce, extend, and audit each step. Good luck!
