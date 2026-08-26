# Wordle

A personal project analyzing Wordle strategy — word-frequency and letter-distribution
statistics across past Wordle answers — plus a tiny Flask app for viewing the results.

## What's here

**Analysis (Jupyter notebooks)**
- `all wordles.ipynb` — main analysis: possibilities remaining per guess, letter/word
  distribution stats, generates the PNG charts and `complete_found_in_distribution.html`.
- `Best Guess Individual.ipynb` — analysis of best individual guesses.

**Data**
- `Wordle.csv`, `guesses.json`, `remaining.json` — cached data used/produced by the notebooks.
- `5-letter-words` — raw word list (five-letter words) used as guess/answer candidates.
- `Record.txt` — personal scoreboard (me vs. computer vs. tie) from playing against the model.

**Charts**
- `*.png` — exported chart images from the notebooks (distribution plots, possibilities
  remaining per guess, etc.).
- `complete_found_in_distribution.html` — self-contained interactive Plotly chart export.

**Web app**
- `wordle.py` — minimal Flask app serving `home.html`, which links to `letters.html`
  (served from `complete_found_in_distribution.html`).
- `home.html` — static landing page.

## Running the app

No dependency lockfile exists yet; install what's imported:

```bash
pip install flask pandas matplotlib
python wordle.py
```

Then visit `http://localhost:5000`.
