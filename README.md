# Cash Flow CLI

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)

A polished terminal-based personal finance tracker built with Python. Designed to be easy to use, reliable, and complete for managing daily cash flow.

## Project Overview

`CashFlow` is a Python CLI application for tracking income and expense entries with JSON persistence. Key workflows include:

- Add income and expense records
- View all transactions in a table
- Search entries by category or date
- Delete and update entries by ID
- Generate summary reports (total income/expenses/balance)

## Highlights

- Clean, colorized CLI interaction using `colorama`
- Data validation on date, amount, and category input
- Persistent store in `finance_data.json` for simplicity
- Modular code with service and storage separation

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

1. Fork repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit with descriptive message
4. Open a pull request for review

## License

MIT
