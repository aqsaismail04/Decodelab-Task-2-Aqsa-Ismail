# Decodelabs-Task-2-Aqsa-Ismail

![DecodeLabs](https://img.shields.io/badge/DecodeLabs-Intern%202026-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A Python command-line Expense Tracker that accumulates expenses in real-time and displays the final total spent.

---

## 📌 Overview

Built as **Task 2** of my **DecodeLabs Internship (Batch 2026)**.

DecodeLabs is a virtual internship program focused on building real-world Python skills through practical projects. This task focused on **data accumulation** — how financial software stores, updates, and processes numerical data continuously.

Enter your expenses one by one, and the program keeps a running total. Type `done` when finished to see your **Final Total Spent**.

---

## 🚀 Features

- 💸 Add multiple expense amounts one by one
- 🔄 Shows running total after each entry
- 🛡️ Handles invalid input gracefully (no crash on wrong data)
- 🔢 Accumulator pattern — total updates in real-time
- ✅ Clean exit with final total on typing `done`

---

## 💻 Output

```
====================================
       EXPENSE TRACKER APP
====================================
Type 'done' to see your total expense
------------------------------------

Enter expense amount (or 'done' to finish): 100
✓ Expense added! Running Total: 100.00

Enter expense amount (or 'done' to finish): 50
✓ Expense added! Running Total: 150.00

Enter expense amount (or 'done' to finish): 20
✓ Expense added! Running Total: 170.00

Enter expense amount (or 'done' to finish): done

====================================
   FINAL TOTAL SPENT: 170.00
====================================
Thank you for using Expense Tracker!
```

---

## ⚙️ How to Run

> Make sure Python 3 is installed on your system.

```bash
git clone https://github.com/aqsaismail04/Decodelabs-Task-2-Aqsa-Ismail.git
cd Decodelabs-Task-2-Aqsa-Ismail
python main.py
```

---

## 📂 Project Structure

```
Decodelabs-Task-2-Aqsa-Ismail/
│
├── main.py        # Main application file
└── README.md
```

---

## 🧠 Concepts Practiced

- Accumulator Pattern (`total += expense`)
- While Loop with Sentinel Value (`done` to exit)
- Type Conversion (`float()` for decimal amounts)
- Exception Handling (`try/except ValueError`)
- Formatted Output (`:.2f` for 2 decimal places)

---

## 💡 What I Learned

During this internship task, I gained hands-on experience with:

- How real financial software processes and accumulates data in real-time
- The importance of initializing accumulators **outside** the loop
- Defensive coding — catching `ValueError` so invalid input doesn't crash the program
- Using sentinel values (`done`) to gracefully exit a continuous loop
- The difference between storing data as a string vs converting it to a number (`int` vs `float`)

---

## 👩‍💻 Author

**Aqsa Ismail**
CS Student @ University of Central Punjab, Lahore
🔗 [GitHub](https://github.com/aqsaismail04) | [LinkedIn](https://linkedin.com/in/aqsaismail04)
