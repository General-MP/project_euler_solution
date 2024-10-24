
# Project Euler Solutions

This repository contains solutions to the 903 problems from [Project Euler](https://projecteuler.net/).  
Each problem includes multiple approaches, mathematical proofs, and tests to ensure correctness.

## Project Overview

The goal of this project is to solve **all 970 problems** from **Project Euler** using **Python**.  
For each problem, the project provides:

- **Multiple approaches**: Explore both brute force and optimized solutions.
- **Mathematical proofs**: Validate solutions with formal reasoning using LaTeX.
- **Unit tests and property-based tests**: Ensure the correctness and robustness of solutions.
- **Jupyter notebooks**: Explore solutions interactively and document thought processes.

This project also follows **best practices in software development** by:
- Ensuring code quality through **Python-TA linting**.
- Automating tests using **GitHub Actions**.
- Using **version control** with Git and GitHub.

This project is created by **Phonlakrit Tiraratn (MP)**,  
a first-year student pursuing a **double major in Computer Science and Economics**.

---

## **Folder Structure**

```
project_euler_solution/
│
├── utils/
│   ├── __init__.py
│   └── performance_test.py
│
├── euler_{problem_number}_{problem_name}/
│   ├── notebook_{problem_number}_{problem_name}.ipynb            # Jupyter notebook for exploration
│   ├── proof_{problem_number}_{problem_name}.tex                 # LaTeX proof of the solution
│   ├── proof_{problem_number}_{problem_name}.pdf                 # Compiled PDF of the LaTeX proof
│   ├── solution_{problem_number}_{problem_name}_approach_1.py    # Mathematical (Analytical) Solution
│   ├── solution_{problem_number}_{problem_name}_approach_2.py    # Idiomatic Python Solution
│   ├── solution_{problem_number}_{problem_name}_approach_2.py    # Imperitive Python Solution
│   ├── test_solution_{problem_number}_{problem_name}.py          # Unit tests
│   ├── property_test_solution_{problem_number}_{problem_name}.py # Property-based tests
│
├── README.md                # Overview and instructions
├── CREDITS.md               # Acknowledgments and credits
├── requirements.txt         # List of dependencies
├── .gitignore               # Files and directories to ignore in Git
├── CHANGELOG.md             # Track project changes over time
├── LICENSE                  # MIT License for the project
└── tree.txt                 # Directory structure of the project

```

---

## **Getting Started**

### **Prerequisites**

- **Python**: Make sure **Python 3.8+** is installed on your system.
- **Dependencies**: Install the required libraries using:

```bash
pip install -r requirements.txt
```

---

## **Running the Solutions**

### **Run a Specific Solution**

You can run any solution directly from the command line. For example:

```bash
python problem_001_multiples_of_3_or_5/solution_001_multiples_of_3_or_5_approach_1.py
```

### **Run Unit Tests**

Ensure that the code passes all unit tests:

```bash
pytest problem_001_multiples_of_3_or_5/test_problem_001_multiples_of_3_or_5.py
```

### **Run Property-Based Tests**

Validate the solution with property-based tests:

```bash
pytest problem_001_multiples_of_3_or_5/property_test_problem_001_multiples_of_3_or_5.py
```

---

## **Credits**

This project was created by **Phonlakrit Tiraratn (MP)**,  
a first-year student pursuing a **double major in Computer Science and Economics**.

MP aims to solve **all 970 Project Euler problems** using multiple approaches and best practices in software development.

For a complete list of tools, libraries, and acknowledgments, see the [CREDITS.md](CREDITS.md) file.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Acknowledgments**

- **Project Euler**: For providing these stimulating mathematical problems.
- **GitHub Actions**: For automating tests and maintaining code quality.
- **pytest**: For comprehensive unit testing.
- **Hypothesis**: For property-based testing of solutions.
- **LaTeX**: For generating mathematical proofs.

---

## **How to Contribute**

Although this is a personal project, if you encounter any errors or have suggestions for improvement,  
feel free to submit a **pull request** or open an **issue** on GitHub.