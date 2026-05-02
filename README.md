# 💸 SpendWise — Personal Expense Tracker

A full-stack personal finance web app built with **Python (Flask)**, **SQLite**, **HTML**, and **CSS**.  
Track your daily expenses, monitor budgets, manage wallets, and visualize your spending — all in one place.

---

## 🚀 Features

- ➕ **Add & delete expenses** with category, wallet type, date, and notes
- 📊 **Dashboard** with live spending stats for the week and month
- 🗂️ **Multiple wallets** — Cash, Card, and UPI tracked separately
- 🎯 **Budget & savings goals** with real-time alerts when you overspend
- 🔍 **Search & filter** your expense history by name, category, or wallet
- 📈 **Charts & graphs** — category breakdown, budget vs spent, 6-month trend
- 🔁 **Recurring expenses** — mark fixed costs like rent or subscriptions
- 👤 **Profile page** — set your name, income, and photo
- 🌙 **Dark / Light mode** toggle with preference saved automatically
- 💬 **Daily motivational money quote** shown on every visit
- 🔔 **Budget alert notifications** — popup warning at 80% and 100% of budget
- 💾 **Persistent data** stored locally using SQLite — no internet required

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| Database | SQLite (via Python's built-in `sqlite3`) |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Charts | Chart.js (CDN) |
| Fonts | Google Fonts — Syne + DM Sans |

---

## 📁 Project Structure
---

## ⚙️ Getting Started

### Prerequisites

- Python 3.7 or above
- pip (comes with Python)

### Step 1 — Download the project

```bash
git clone https://github.com/kanchanrwt007/expense-tracker.git
cd expense-tracker
```

Or simply download the ZIP and extract it.

### Step 2 — Install Flask

Open your terminal or VS Code terminal and run:

```bash
pip install flask
```

### Step 3 — Run the app

```bash
python app.py
```

### Step 4 — Open in your browser

The SQLite database (`expenses.db`) is created automatically on the very first run. No extra configuration needed.

---

## 🧭 How to Use

| Step | What to do |
|---|---|
| 1 | Go to **Goals** and set your monthly budget and savings target |
| 2 | Go to **Add Expense** and log what you spend with category and wallet |
| 3 | Visit the **Dashboard** to see real-time totals, charts, and goal status |
| 4 | Use **History** to search, filter by category or wallet, and delete entries |
| 5 | Check **Analytics** for your 6-month trend and recurring vs one-time split |
| 6 | Set up your **Profile** with your name, monthly income, and photo |
| 7 | Use **Wallets** to see how much you spent via Cash, Card, and UPI |

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/expenses` | Get all expenses — supports `?search=`, `?category=`, `?wallet=` |
| POST | `/api/expenses` | Add a new expense |
| DELETE | `/api/expenses/<id>` | Delete a specific expense by ID |
| GET | `/api/stats` | Monthly and weekly totals, category and wallet breakdown |
| POST | `/api/goals` | Save or update budget and savings goals |
| GET | `/api/trend` | 6-month spending data for the trend chart |
| GET | `/api/profile` | Get saved profile info |
| POST | `/api/profile` | Update name, income, and photo |

---

## 📸 Screenshots

> Add your own screenshots once the app is running. Take a screenshot of each page and save them inside a `screenshots/` folder.

| Dashboard | Add Expense | History |
|---|---|---|
| ![dashboard](screenshots/dashboard.png) | ![add](screenshots/add.png) | ![history](screenshots/history.png) |

| Analytics | Wallets | Goals |
|---|---|---|
| ![analytics](screenshots/analytics.png) | ![wallets](screenshots/wallets.png) | ![goals](screenshots/goals.png) |

---

## 🔮 Future Plans

- [ ] Export all expenses to a CSV or PDF file
- [ ] Monthly spending summary sent by email
- [ ] Support for multiple currencies (USD, EUR, INR, etc.)
- [ ] Recurring expense auto-add every month
- [ ] Mobile-friendly PWA version
- [ ] Cloud sync so data is not lost if the file is deleted

---

## 🙋‍♂️ About This Project

This is a personal project built entirely from scratch as a way to learn full-stack web development using Python.

No frameworks like React or Django were used — just pure Flask on the backend, plain HTML and CSS on the frontend, and SQLite as the database. Every feature was planned, designed, and coded manually.

**Built by:** Kanchan Rawat 
**Location:** India  
**Stack:** Python · Flask · SQLite · HTML · CSS · JavaScript

---

## 📄 License

This project is free and open source under the [MIT License](LICENSE).  
Feel free to fork it, improve it, and make it your own.

---

> *"A budget is telling your money where to go instead of wondering where it went."*
