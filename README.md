# Cash Flow CLI

A lightweight personal finance manager that runs in the terminal.

## Project Overview

`CashFlow` is a Python CLI application for tracking income and expenses. It stores transaction records in `finance_data.json` and supports:

- Add income and expenses
- List all transactions
- Search by category or date
- Delete transactions by ID
- Update transactions by ID
- Summary report (total income, total expenses, balance)

## Architecture

- `main.py`: application entry point.
- `CLI_UI.py`: command line menu and interaction.
- `Features.py`: business logic for transaction operations.
- `Finance_Service.py`: service layer for CRUD operations and summary calculations.
- `Storage.py`: JSON file persistence.
- `utils.py`: input validation and helpers.
- `finance_data.json`: data store (auto-created/updated by app).

## Installation

1. Clone repository

```bash
git clone https://github.com/Yeahyea187/CashFlow.git
cd CashFlow
```

2. Create and activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\Activate.ps1 # Windows PowerShell
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the app:

```bash
python main.py
```

Menu choices:

- `1`: Add income
- `2`: Add expense
- `3`: View all transactions
- `4`: Search transactions by category/date
- `5`: Delete transaction by ID
- `6`: Update transaction by ID
- `7`: View summary report
- `0`: Exit

## Data Format

Transactions are saved in `finance_data.json` with fields:

- `id` (int)
- `category` (string)
- `amount` (float)
- `date` (DD-MM-YYYY string)
- `type`: `income` or `expense`

## Validation

- category: >2 characters, letters/spaces only.
- amount: positive number.
- date: `DD-MM-YYYY` or empty for today.

## Git

`.gitignore` includes:

```
__pycache__/
.venv/
```

## Developer

Md. Yeahyea Jam

## Contribution

1. Fork repo
2. Create topic branch
3. Commit changes
4. Open PR

## License

MIT (or your preferred license)
