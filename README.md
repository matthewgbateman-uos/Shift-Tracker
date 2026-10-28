# Shift Tracker

A command-line Python app for tracking work shifts, working out pay, and keeping an eye on monthly bills.

I built this from scratch while learning Python, then refactored it step by step: tidying the code, splitting it into modules, moving settings into JSON files, and adding input validation and menus.

## Features

- **Pay calculation**: works out pay from a base hourly rate, including holiday pay, service charge and tax
- **Bills manager**: view, add and remove monthly bills, with a running total
- **Editable settings**: change the base rate, service charge range and tax rate from inside the app (no need to edit code)
- **Month reset**: start a fresh month from the menu
- **Input validation**: invalid entries are caught and you're asked again, instead of the program crashing
- **Saved data**: bills and settings are stored in JSON files, so they're kept between runs

## Project structure

```
Shift_Tracker/
├── Shift_Tracker.py   # Entry point: runs the main menu
├── shifts.py          # Shift-related functions
├── calculations.py    # Pay maths (base pay, holiday pay, service charge, tax)
├── bills.py           # Bills menu: view, add, remove
├── config.py          # Settings menu: edit config values
├── bills.json         # Your saved bills
└── config.json        # Your saved settings
```

## Requirements

- Python 3 <!-- TODO: add your exact version, e.g. 3.12 -->
- No extra packages: only Python's built-in modules (`json`, `os`) are used <!-- TODO: confirm -->

## Getting started

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/Shift_Tracker.git
   cd Shift_Tracker
   ```

2. Run the app:

   ```bash
   python Shift_Tracker.py
   ```

3. Pick an option from the menu by typing its number.

## Configuration

Settings live in `config.json`. You can edit them from the app's settings menu, or open the file directly.

| Setting     | What it means                         |
|-------------|---------------------------------------|
| `base_rate` | Your hourly pay rate                  |
| `min_sc`    | Lowest expected service charge        |
| `max_sc`    | Highest expected service charge       |
| `tax`       | Tax rate applied to your pay          |

<!-- TODO: add an example config.json with dummy values (not your real figures) -->

Bills live in `bills.json` and are managed from the bills menu.

## What I learned

- Splitting a single script into separate modules, and passing data between them with function parameters and return values
- Reading and writing JSON files with `json.load()` and `json.dump()`
- Building file paths that work on any computer with `os.path`
- Looping menus with `while True`
- Handling bad input with `try` / `except ValueError`

## Roadmap

- [ ] Turn it into a web app with Flask
- [ ] Add user accounts so more than one person can use it
- [ ] Host it online

## Author

Matt <!-- TODO: add GitHub / LinkedIn links -->
