
# 🐍 Python Practical Works (Travaux Pratiques)

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python%203-blue.svg" alt="Language">
  <img src="https://img.shields.io/badge/Topics-OOP%20%7C%20Files%20%7C%20Exceptions-green.svg" alt="Topics">
  <img src="https://img.shields.io/badge/Status-Educational-orange.svg" alt="Status">
</p>


## 📖 Overview
This repository contains a comprehensive collection of Python exercises and practical works (Travaux Pratiques), ranging from basic syntax to advanced Object-Oriented Programming (OOP), file handling, and error management.

The projects are structured progressively to cover key software engineering concepts in Python.

---

## 📂 Project Structure

The repository is organized into six main modules, each focusing on a specific domain of Python programming:

| Module | Topic | Key Concepts |
| :--- | :--- | :--- |
| **`TravauxPratiques1/`** | 🏗️ **Basics** | Lists, Dictionaries, Sets, Lambda functions, `*args`. |
| **`TravauxPratiques2/`** | 🧱 **OOP Basics** | Classes, Inheritance, Polymorphism, Method Overriding. |
| **`TravauxPratiques3/`** | 🔐 **Encapsulation & Abstraction** | Abstract Base Classes (`ABC`), `@property`, Setters/Getters. |
| **`TravauxPratiques4/`** | 🧬 **Advanced OOP** | **Multiple Inheritance**, Method Resolution Order (MRO). |
| **`TravauxPratiques5/`** | 💾 **File Handling** | Reading/Writing Text, **CSV**, **JSON**, `shutil`, `os` modules. |
| **`TravauxPratiques6/`** | ⚠️ **Exceptions & Testing** | `try/except/finally`, Custom Exceptions, Logging, **Unittest**. |

---

## 📝 Detailed Content

### 🔹 TP 1: Python Fundamentals
Introduction to Python data structures and functional programming tools.
* **Key Exercises:**
    * `ex6.py`: Usage of **Lambda** functions.
    * `ex8.py`: Handling variable arguments with `*args`.
    * `ex10.py`: Merging dictionaries efficiently.

### 🔹 TP 2: Object-Oriented Programming (Introduction)
Building classes to model real-world entities.
* **Key Exercises:**
    * `Exercice3.py`: A `CompteBancaire` class with deposit/withdraw logic.
    * `Exercice5.py`: Polymorphism demonstration with `Animal`, `Chien`, and `Chat`.
    * `Exercice7.py`: A `Bibliotheque` system to manage a collection of books.

### 🔹 TP 3: Advanced OOP Concepts
Focuses on robust code design using encapsulation and abstraction.
* **Key Exercises:**
    * `Exercice1.py` & `3.py`: Using `ABC` and `@abstractmethod` to define geometric shapes.
    * `Exercice2.py` & `4.py`: protecting attributes using **Properties** (`@property`, `@setter`).
    * `Exercice6.py`: A Shopping Cart system (`Panier`, `Commande`, `Produit`) with total calculation.

### 🔹 TP 4: Multiple Inheritance
Explores complex inheritance structures.
* **`Exercice.py`**: A `Voiture` and `Moto` class inheriting from both `Vehicule` (brand info) and `Moteur` (power info) simultaneously.

### 🔹 TP 5: File Manipulation & Persistence
Reading and writing data in various formats.
* **Key Exercises:**
    * `Exercice4.py`: Managing contacts using the **CSV** module.
    * `Exercice5.py`: Serializing objects to **JSON**.
    * `Exercice7.py`: File operations (copy/move) using `shutil` and `os`.
    * `Exercice10.py`: A complete CLI menu for adding/searching/deleting contacts in a CSV file.

### 🔹 TP 6: Error Handling & Unit Testing
Writing robust and testable code.
* **Key Exercises:**
    * `EX1.py` & `EX6.py`: Handling `ZeroDivisionError` safely.
    * `EX4.py`: Creating a custom exception `NegativeAgeError`.
    * `EX7.py`: Logging errors to a file (`error.log`) instead of crashing.
    * **`EX8.py`**: Unit testing the other modules using Python's `unittest` framework.

---

## 🚀 How to Run
Ensure you have Python installed. You can run any specific exercise file directly from the terminal.

```bash
# Clone the repository
git clone [https://github.com/medbaihich/TravauxPratiques_python.git](https://github.com/medbaihich/TravauxPratiques_python.git)

# Navigate to a specific TP folder (e.g., TP5)
cd TravauxPratiques_python/TravauxPratiques5

# Run a script (e.g., the Contact Management System)
python Exercice10.py

```

### Running Tests

To run the unit tests provided in TP6:

```bash
cd TravauxPratiques6
python EX8.py

```

---

## 👤 Author

**Mohamed Baihich**
*Computer Engineering & Embedded Systems Student*
