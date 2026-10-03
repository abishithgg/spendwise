# 💰 SpendWise – Personal Expense Management System

SpendWise is a Java-based personal expense management system designed to help users efficiently track their **income, expenses, budgets, and financial reports** in one place.

The project is developed using **Java Swing for the GUI**, **JDBC for database connectivity**, and **MySQL for data storage**.

## 🚀 Features

* 👤 User Management
* 💸 Add and manage expenses
* 💰 Record income
* 📊 Set and manage budgets
* 📈 Generate expense and income reports
* 🗂️ Categorize expenses such as Food, Travel, Shopping, Education, etc.
* 🗄️ Store data securely in a MySQL database
* 🖥️ User-friendly Java Swing interface

## 🛠️ Technologies Used

* **Java**
* **Java Swing**
* **JDBC**
* **MySQL**
* **IntelliJ IDEA**
* **MySQL Connector/J**

## 🏗️ Project Structure

```text
SpendWise/
│
├── src/
│   ├── model/
│   │   ├── User.java
│   │   ├── Expense.java
│   │   ├── Income.java
│   │   ├── Budget.java
│   │   └── ...
│   │
│   ├── dao/
│   │   ├── UserDAO.java
│   │   ├── ExpenseDAO.java
│   │   ├── IncomeDAO.java
│   │   └── BudgetDAO.java
│   │
│   └── gui/
│       ├── Dashboard.java
│       ├── AddExpense.java
│       ├── AddIncome.java
│       ├── Budget.java
│       ├── Report.java
│       └── ...
│
└── README.md
```

## 🗄️ Database

SpendWise uses **MySQL** as its database.

### Database Name

```text
SpendWiseDB
```

### Main Tables

* `Users`
* `Expenses`
* `Income`
* `Budget`

JDBC is used to establish communication between the Java application and MySQL database.

## ▶️ How to Run

1. Install **Java JDK**.
2. Install **MySQL Server**.
3. Create the database:

```sql
CREATE DATABASE SpendWiseDB;
```

4. Configure the MySQL username and password in the database connection class.
5. Add the **MySQL Connector/J** library to the project.
6. Open the project in **IntelliJ IDEA**.
7. Run the main GUI/application class.
8. Start managing your income, expenses, and budget through SpendWise.

## Demo Link

**Demo / Presentation:**
👉 [https://abishith.pythonanywhere.com/]


## 🎯 Objective

The main objective of SpendWise is to provide a simple and organized platform for managing personal finances while demonstrating practical implementation of:

* Object-Oriented Programming
* GUI Development
* Database Management
* JDBC Connectivity
* CRUD Operations

## 👨‍💻 Developed By

**Abishith Reddy**

**Project:** SpendWise – Personal Expense Management System
