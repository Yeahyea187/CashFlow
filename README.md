# 💸 Cash Flow CLI

A professional command-line application to manage your personal finances efficiently. Track income, expenses, and financial summaries with a clean interface and structured data storage.

---

## 🌟 Key Features

- 💰 **Income & Expense Tracking**
  Easily add and manage your daily financial transactions.

- 🧾 **Smart Categorization**
  Assign categories to transactions with default and custom options.

- 🔍 **Advanced Search**
  Search transactions by category, date, or ID.

- ✏️ **Update & Delete**
  Modify or remove transactions with dynamic ID handling.

- 📊 **Summary Report**
  View total income, total expenses, and net balance instantly.

- 🎨 **Enhanced CLI UI**
  Color-coded interface using colorama for better readability.

- 🧠 **Input Validation**
  Validates amount, date format, and category input.

- 🔁 **Dynamic ID Management**
  Automatically reorders IDs after deletion to maintain consistency.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Virtual environment (recommended)

---

### Installation

Clone the repository:

```bash
git clone https://github.com/your-username/CashFlowCLI.git
cd CashFlowCLI
```

---

### Set up virtual environment (Optional but Recommended)

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Run the application

```bash
python main.py
```

---

## 🛠️ Tech Stack

- Python – Core programming language
- Colorama – Terminal color formatting
- Tabulate – Table display for transactions
- JSON – Local data storage

---

## 🏗️ Project Structure

```
├── main.py              # Entry point
├── features.py          # Menu & feature handling
├── CLI_UI.py            # User interaction logic
├── Finance_Service.py   # Business logic layer
├── Storage.py           # JSON storage handler
├── model.py             # Transaction model
└── finance_data.json    # Data storage file
```

---

## 📜 Usage Guide

### ➕ Add Transaction

Choose option `1` or `2` to add income or expense.

- Press Enter to use default category or date
- Enter custom values if needed

---

### 🔍 Search Transactions

Find transactions by:

- Category
- Date
- ID

---

### ✏️ Update Transaction

- Select option `6`
- Leave fields blank to keep existing values

---

### 🗑️ Delete Transaction

- Select option `5`
- IDs will automatically reorder

---

### 📊 View Summary

- Option `7` shows:
  - Total Income
  - Total Expenses
  - Net Balance

---

## ⚠️ Notes

- Data is stored locally in `finance_data.json`
- Ensure the file is not corrupted or manually altered incorrectly
- Date format must follow: `DD-MM-YYYY`

---

## 💡 Future Improvements

- 📅 Monthly & yearly reports
- 📈 Graph visualization
- 🗂️ Category management system
- 🌐 Web or GUI version

---

## 👨‍💻 Author

Developed with ❤️ by Md. Yeahyea Jam
