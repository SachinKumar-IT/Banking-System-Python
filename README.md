# Banking-System-Python
A simple Python banking program that lets users create an account, check balance, deposit, and withdraw money. Runs in the terminal – ideal for learning basic Python functions and control flow.
# 🏦 Simple Banking System (Python Console App)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/status-Basic%20Demo-green)

## 📌 Overview
This is a minimal **banking system** written in Python. It runs in the terminal and allows a user to:
- Create an account (enters details – but data is not saved between runs).
- Check balance.
- Deposit money.
- Withdraw money (with insufficient balance check).
- Exit the program.

> **Note:** This is a **single-session, single-user** simulation. No database or file storage is used – data resets when the program ends.

## ✨ Features
- User-friendly menu system (1-5).
- Input validation for negative deposit/withdrawal amounts.
- Insufficient balance protection.
- Clear balance display in Indian Rupees (₹).

## 🛠️ How It Works (Code Logic)
1. The `main()` function initializes `balance = 0` and runs a `while` loop.
2. User chooses an option:
   - **1:** Calls `createAccount()` – asks for account number, name, branch code, mobile number (but doesn't store them permanently).
   - **2:** Displays current balance.
   - **3:** Calls `deposit()` – returns positive amount to add to balance.
   - **4:** Calls `withdraw(balance)` – checks if enough balance exists, then returns amount to subtract.
   - **5:** Exits the loop.
3. After exit, a thank you message appears.

## 🚀 How to Run
### Prerequisites
- Python 3.x installed on your system

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/SachinKumar-IT/Banking-System-Python.git
