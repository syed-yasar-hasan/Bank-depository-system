## Bank Depository System

This project is a simple command-line banking system implemented in Python. It provides two versions:

1. **main.py**: A procedural (function-based) implementation.
2. **mainby_oops.py**: An object-oriented implementation using classes.

---

### Features

- Create Savings, Current, or Fixed Deposit accounts
- Deposit, withdraw, and transfer money (except for Fixed Deposit accounts)
- Check account balance and view transaction history
- User authentication with password
- Minimum balance enforcement

---

## File Descriptions

### main.py (Procedural Version)

- Uses functions and dictionaries to manage user data and transactions.
- Supports account creation, login, deposit, withdrawal, transfer, and transaction history.
- All user data is stored in-memory (no database).
- Menu-driven interface for user interaction.

**How to run:**
```bash
python main.py
```

---

### mainby_oops.py (Object-Oriented Version)

- Uses `BankAccount` and `BankingSystem` classes for better structure and encapsulation.
- Each user is represented as a `BankAccount` object.
- All features from the procedural version are available, with improved code organization.
- Menu-driven interface for account management and transactions.

**How to run:**
```bash
python mainby_oops.py
```

---

## Requirements

- Python 3.x
- No external libraries required

---

## Usage

1. Run either `main.py` or `mainby_oops.py`.
2. Follow the on-screen prompts to create an account, login, and perform banking operations.
3. All data is lost when the program exits (no persistent storage).

---

## Notes

- This project is for educational/demo purposes and does not implement real security or persistent storage.
- Passwords are stored in plain text and are only for demonstration.

---

## Author

**Syed Yasar Hasan**

- Email: syedyasar580@gmail.com
- LinkedIn: [syed-yasar-hasan](https://www.linkedin.com/in/syed-yasar-hasan-a74562321)
- GitHub: [syed-yasar-hasan](https://github.com/syed-yasar-hasan)
