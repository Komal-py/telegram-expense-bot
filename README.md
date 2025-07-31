# 💰 Telegram Expense Tracker Bot

A simple Telegram bot to track trip expenses, set a budget, and show remaining balance after each transaction.

## 🚀 Features

- Set a trip budget using `/setbudget <amount>`
- Add expenses with `/add <description> <amount>`
- View summary of all expenses with `/summary`
- Runs 24/7 on Render (or any Python host)

## 📦 Commands

| Command         | Description                                |
|------------------|--------------------------------------------|
| `/start`         | Welcome message                            |
| `/setbudget 5000`| Set your trip budget                       |
| `/add food 200`  | Add an expense (description + amount)      |
| `/summary`       | Shows all added expenses + remaining balance|

## 🛠 How to Run Locally

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
