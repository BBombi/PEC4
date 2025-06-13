# Readme

## Description:

This project loads and analyzes a dataset of reservoirs in Catalonia available at *Open Data Gencat*.

**Autor:** Borja Bombí 

## Project structure:

+ modules/        *Functional Python modules*
  - __init__.py
  - cleaning.py   *Data cleaning and renaming*
  - loader.py     *Data loading*
  - periods.py    *Drought detection*
  - smoothing.py  *Smooth the tendency curve*
  - timing.py     *Adjust time features*

+ test/
  - __init__.py
  - test_modules.py

+ img *Folder that will contain images of the charts (not necessary)*

+ screenchots/ *Folder that contains screenshots required by the PEC4*

+ main.py             *Main script (runs project steps)*
+ README.md           *This file*
+ requirements.txt    *Project dependencies*
+ setup.py            *Package configuration (optional)*

## Instalation:

### 1. Clone the repository

```bash
git clone https://github.com/bbombi/PEC4.git
cd embassaments_project
```


### 2. (Optional) Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate        # On macOS/Linux
venv\Scripts\activate           # On Windows
```


### 3.Install dependencies
```bash
pip install -r requirements.txt
```
Alternatively, using setup.py
```bash
pip install -e .
```

## Usage:
#### To run the code:
```bash
python main.py
```

#### Run a specific exercise
```bash
python main.py -ex 1   # -ex  1: Load dataset
python main.py -ex 2   # -ex  2: Clean and filter
python main.py -ex 3   # -ex  3: Time conversion and plotting
python main.py -ex 4   # -ex  4: Calculating an smooth tendency and plotting
python main.py -ex 5   # -ex  5: Calculating drought periods and plotting
```
*Please note*: Each exercise builds upon the previous one, so if you select a exercise bigger than the first one, we'll run all exercises from the first one up to the selected one.

## Code Style
To check for P8P compliance:
```bash
flake8 modules/
```

## Testing and testing coverage:
For testing, use:
```bash
pytest
```

For testing coverage, use:
```bash
coverage run -m pytest
```

And finally, to extract a report, use:
```bash
coverage report
```

## Dataset source:
Original dataset available at:

https://analisi.transparenciacatalunya.cat/Medi-Ambient/Quantitat-d-aigua-als-embassaments-de-les-Conques-/gn9e-3qhr
