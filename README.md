<div align="center">

# Wordle

**One of my first personal projects.** A statistical dive into Wordle strategy — built for fun in 2022, revisited in 2025.

[![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)](https://www.python.org)
[![Flask](https://img.shields.io/badge/Flask-black?logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?logo=jupyter&logoColor=white)](https://jupyter.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-black.svg)](LICENSE)

</div>

<br />

<table>
<tr>
<td width="50%"><img src="docs/screenshots/complete-found-in-distribution.png" alt="Letter distribution across all Wordle answers" /></td>
<td width="50%"><img src="docs/screenshots/line-graph-possibilities-remaining.png" alt="Possibilities remaining after each guess" /></td>
</tr>
<tr>
<td width="50%"><img src="docs/screenshots/adjusted-found-in-distribution.png" alt="Adjusted letter-found distribution" /></td>
<td width="50%"><img src="docs/screenshots/record-daily-wordle-bar-graph.png" alt="Personal record: me vs. computer vs. tie" /></td>
</tr>
</table>

## History

Built in **2022**, not long after Wordle took off, out of curiosity about whether letter-frequency stats could out-guess intuition. Revisited briefly in **2025** to rerun the analysis with more data. It predates the habits — dependency pinning, tests, a structured layout — I'd reach for on something built today. This repo is cleaned of accumulated cruft (duplicate binaries, stale reruns, cache files) but deliberately not modernized: it's kept as a snapshot of early work, not a demonstration of current practice.

## How it works

- `all wordles.ipynb` — main analysis notebook: possibilities remaining per guess, letter/word distribution stats, generates the charts above and the interactive `complete_found_in_distribution.html` export.
- `Best Guess Individual.ipynb` — analysis of the best individual opening guesses.
- `wordle.py` — minimal Flask app that serves the results: `home.html` links to `letters.html`, which serves the generated distribution chart.

## What's here

- **Data** — `Wordle.csv`, `guesses.json`, `remaining.json` (cached inputs/outputs of the analysis), `5-letter-words` (candidate word list).
- **Charts** — `docs/screenshots/` holds the exported chart images; `complete_found_in_distribution.html` is the interactive Plotly version.
- **`Record.txt`** — a personal scoreboard (me vs. computer vs. tie) from playing against the model's suggestions.

## Getting started

```bash
pip install -r requirements.txt
python wordle.py
```

Then visit `http://localhost:5000`. To rerun the analysis itself, open the notebooks in Jupyter (or any notebook-capable editor).

## License

[MIT](LICENSE) © Jack Van Zeeland
