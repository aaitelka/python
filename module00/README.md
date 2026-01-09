# 🌱 Growing Code - Python Fundamentals Through Garden Data

A project that teaches fundamental Python programming concepts through community garden scenarios. Each exercise builds upon the previous one, introducing new concepts in a practical and engaging way.

## 📚 Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [What You'll Learn](#what-youll-learn)
- [Getting Started](#getting-started)
- [Exercises](#exercises)
- [Testing Your Code](#testing-your-code)
- [Requirements](#requirements)

## 🎯 Project Overview

**Growing Code** introduces Python fundamentals through hands-on exercises based on community garden data. You'll work with practical scenarios that teach core programming concepts while contributing to sustainable community initiatives.

**Key Focus Areas:**
- Python syntax and semantics
- Expressions and variables
- Functions and control flow
- Data structures and type annotations

## 📁 Project Structure

```
growing-code/
├── README.md
├── main.py                              # Test runner (helper tool)
├── ex0/
│   └── ft_hello_garden.py              # Exercise 0: Hello Garden
├── ex1/
│   └── ft_plot_area.py                 # Exercise 1: Garden Plot Area
├── ex2/
│   └── ft_harvest_total.py             # Exercise 2: Harvest Total
├── ex3/
│   └── ft_plant_age.py                 # Exercise 3: Plant Age Check
├── ex4/
│   └── ft_water_reminder.py            # Exercise 4: Water Reminder
├── ex5/
│   ├── ft_count_harvest_iterative.py   # Exercise 5a: Count to Harvest (Iteration)
│   └── ft_count_harvest_recursive.py   # Exercise 5b: Count to Harvest (Recursion)
├── ex6/
│   └── ft_garden_summary.py            # Exercise 6: Garden Summary
└── ex7/
    └── ft_seed_inventory.py            # Exercise 7: Seed Inventory with Type Annotations
```

## 🎓 What You'll Learn

### Exercise 0: Hello Garden (`ft_hello_garden`)
**Concepts:** Functions, Print statements, Basic output

Your first Python function! Learn to create a simple function that displays a welcome message.

**Key Takeaways:**
- How to define a function with `def`
- Using `print()` to display messages
- Basic function structure and syntax

**Example Output:**
```python
>>> ft_hello_garden()
Hello, Garden Community!
```

---

### Exercise 1: Garden Plot Area (`ft_plot_area`)
**Concepts:** Variables, User input, Arithmetic operations, Type conversion

Calculate the area of a rectangular garden plot by getting user input and performing calculations.

**Key Takeaways:**
- Getting user input with `input()`
- Converting strings to integers with `int()`
- Storing values in variables
- Performing arithmetic operations (multiplication)
- Displaying calculated results

**Example Output:**
```python
>>> ft_plot_area()
Enter length: 5
Enter width: 3
Plot area: 15
```

---

### Exercise 2: Harvest Total (`ft_harvest_total`)
**Concepts:** Multiple inputs, Addition operations, Sequential processing

Calculate the total weight of vegetables harvested over multiple days.

**Key Takeaways:**
- Working with multiple input values
- Adding numbers together
- Storing intermediate results
- Displaying formatted output

**Example Output:**
```python
>>> ft_harvest_total()
Day 1 harvest: 5
Day 2 harvest: 8
Day 3 harvest: 3
Total harvest: 16
```

---

### Exercise 3: Plant Age Check (`ft_plant_age`)
**Concepts:** Conditional statements, If-else logic, Comparison operators

Check if a plant is ready to harvest based on its age using conditional logic.

**Key Takeaways:**
- Using `if-else` statements
- Comparison operators (`>`, `<=`)
- Making decisions in code based on conditions
- Control flow fundamentals

**Example Output:**
```python
>>> ft_plant_age()
Enter plant age in days: 75
Plant is ready to harvest!

>>> ft_plant_age()
Enter plant age in days: 45
Plant needs more time to grow.
```

---

### Exercise 4: Water Reminder (`ft_water_reminder`)
**Concepts:** Conditional logic, Threshold checking, Decision making

Determine if plants need water based on the number of days since last watering.

**Key Takeaways:**
- Boolean conditions and comparisons
- Using thresholds for decision making
- Conditional output based on criteria
- Practical application of if-else statements

**Example Output:**
```python
>>> ft_water_reminder()
Days since last watering: 4
Water the plants!

>>> ft_water_reminder()
Days since last watering: 1
Plants are fine
```

---

### Exercise 5: Count to Harvest (`ft_count_harvest_iterative` & `ft_count_harvest_recursive`)
**Concepts:** Loops (iteration), Recursion, Repetition, range()

Count days until harvest using two different approaches: iteration and recursion.

**Key Takeaways:**
- **Iterative approach:** Using `for` loops with `range()`
- **Recursive approach:** Functions calling themselves
- Understanding loop mechanics
- Base cases in recursion
- Two different solutions to the same problem
- When to use iteration vs recursion

**Example Output:**
```python
>>> ft_count_harvest_iterative()
Days until harvest: 5
Day 1
Day 2
Day 3
Day 4
Day 5
Harvest time!

>>> ft_count_harvest_recursive()
Days until harvest: 5
Day 1
Day 2
Day 3
Day 4
Day 5
Harvest time!
```

---

### Exercise 6: Garden Summary (`ft_garden_summary`)
**Concepts:** String concatenation, Multiple inputs, Formatted output

Create a summary report combining multiple pieces of information about a garden.

**Key Takeaways:**
- Combining different types of data
- Building formatted output
- Working with multiple input values
- Creating structured information displays

**Example Output:**
```python
>>> ft_garden_summary()
Enter garden name: Community Garden
Enter number of plants: 25
Garden: Community Garden
Plants: 25
Status: Growing well!
```

---

### Exercise 7: Seed Inventory with Type Annotations (`ft_seed_inventory`)
**Concepts:** Type hints, Function parameters, Type annotations, Pattern matching

Manage seed inventory with type-safe functions, using proper type annotations and parameter handling.

**Key Takeaways:**
- Function parameters and arguments
- Type hints for parameters (`: str`, `: int`)
- Return type annotations (`-> None`)
- String methods for capitalization
- Conditional logic for different unit types
- Writing self-documenting code

**Function Signature:**
```python
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
```

**Example Output:**
```python
>>> ft_seed_inventory("tomato", 15, "packets")
Tomato seeds: 15 packets available

>>> ft_seed_inventory("carrot", 8, "grams")
Carrot seeds: 8 grams total

>>> ft_seed_inventory("lettuce", 12, "area")
Lettuce seeds: covers 12 square meters

>>> ft_seed_inventory("basil", 5, "unknown")
Basil seeds: Unknown unit type
```

**Supported Units:**
- `"packets"` → "X packets available"
- `"grams"` → "X grams total"
- `"area"` → "covers X square meters"
- Any other unit → "Unknown unit type"

**Note:** The seed type is automatically capitalized (e.g., "tomato" becomes "Tomato") using Python's `.title()` string method.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher (required for modern Python features)
- A text editor or IDE (VS Code, Vim, PyCharm, etc.)
- Git for version control
- flake8 (for code style checking)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/aaitelka/python.git
cd python/module00
```

2. Verify Python installation:
```bash
python3 --version
```

3. Install flake8 for code style checking:
```bash
pip install flake8
# or
pip3 install flake8
```

4. Start with Exercise 0 and work your way through sequentially.

## 🧪 Testing Your Code

### Using the Test Runner (Helper Tool)

The project includes a convenient test runner (`main.py`) that helps you test your exercises easily.

#### Run the Interactive Menu:
```bash
python3 main.py
```

You'll see a menu like this:
```
🌱 Welcome to Growing Code! 🌱
This helper will test your exercises for you.

Which exercise would you like to test?

0 - ft_hello_garden     (Say hello to the garden community)
1 - ft_plot_area        (Calculate garden plot area)
2 - ft_harvest_total    (Add up harvest weights)
3 - ft_plant_age        (Check if plant is ready)
4 - ft_water_reminder   (Check if plants need water)
5 - ft_count_harvest    (Count days to harvest)
6 - ft_garden_summary   (Display garden info)
7 - ft_seed_inventory   (Seed inventory with type hints)
a - test all exercises

Enter your choice:
```

#### Testing Options:

**Test a specific exercise:**
```bash
python3 main.py
# Then enter the number (0-7)
```

**Test all exercises at once:**
```bash
python3 main.py
# Then type: a
```

### Manual Testing

You can also test each exercise manually using Python's interactive mode:

```python
# Example: Testing exercise 1
python3
>>> from ex1.ft_plot_area import ft_plot_area
>>> ft_plot_area()
Enter length: 5
Enter width: 3
Plot area: 15
```

Or run directly from the exercise folder:

```bash
cd ex1
python3 -c "from ft_plot_area import ft_plot_area; ft_plot_area()"
```

### Code Style Checking with flake8

All code must pass flake8 style checks. Run flake8 on your exercises:

```bash
# Check a specific exercise
flake8 ex0/ft_hello_garden.py

# Check all exercises
flake8 ex*/

# Check everything including main.py
flake8 .
```

**Common flake8 checks:**
- Line length (max 79 characters)
- Proper indentation (4 spaces)
- Blank lines between functions
- No trailing whitespace
- Proper import formatting

**Example of fixing flake8 errors:**
```bash
# Run flake8
flake8 ex1/ft_plot_area.py

# If you see errors like:
# ex1/ft_plot_area.py:1:1: E302 expected 2 blank lines, found 1

# Fix by adding proper spacing in your code
```

## 📋 Requirements

### General Instructions

- Your functions must be written in Python 3.10+
- Your code must respect the flake8 linter standards
- Each exercise must be in its own file within its designated folder (ex0/, ex1/, etc.)
- Each file should contain **only the requested function**
- Function names must match exactly what is requested
- **Important:** Write only functions, not main programs. Do not include `if __name__ == "__main__":` blocks
- You don't need to handle input validation or error cases unless explicitly mentioned
- For negative numbers or invalid inputs, the behavior is undefined

### Submission

- Turn in your assignment in your Git repository
- Only the work inside your repository will be evaluated
- You need to return only the files requested by the subject
- Double-check file names and folder structure
- During evaluation, you may be asked to explain your code, trace through execution, or modify your solutions

### Before Submission Checklist

- [ ] All exercises are in their correct folders (ex0/, ex1/, etc.)
- [ ] Each file contains only the requested function
- [ ] All functions run without errors
- [ ] Code passes flake8 style checks (no errors)
- [ ] Function names match exactly as specified
- [ ] Test runner (`main.py`) works correctly for all exercises
- [ ] No trailing whitespace or unnecessary blank lines
- [ ] Git repository is clean and well-organized
- [ ] You can explain every line of code you wrote

## 📖 Additional Resources

### Python Documentation
- [Official Python Tutorial](https://docs.python.org/3/tutorial/)
- [PEP 8 - Style Guide](https://peps.python.org/pep-0008/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [flake8 Documentation](https://flake8.pycqa.org/)

### Code Quality Tools
- **flake8**: Style guide enforcement (required)
- **black**: Auto-formatter (optional, for consistent formatting)
- **pylint**: Additional code analysis (optional)

## 🎯 Learning Path

**Progressive Difficulty - How to Approach:**

1. **Start with Exercise 0** - Build confidence with basics
2. **Work sequentially through exercises** - Each builds on previous knowledge
3. **Don't skip ahead** - Concepts are designed to compound
4. **Read the subject carefully** - Understand what's being asked
5. **Test frequently** - Use the helper tool to verify your solutions
6. **Experiment** - Try different inputs and see what happens
7. **Review with peers** - Discuss solutions and approaches
8. **Understand deeply** - Be able to explain every line during evaluation

## 🏆 Skills Developed

By completing this project, you will have learned:
- ✅ Python syntax and fundamentals
- ✅ Functions and function design
- ✅ Variables and data types
- ✅ User input and output
- ✅ Control flow (conditionals and loops)
- ✅ Recursion vs iteration
- ✅ String manipulation
- ✅ Type hints and code documentation
- ✅ Debugging and testing
- ✅ Code style and best practices (PEP 8, flake8)

## 💡 Tips for Success

- **Read the subject carefully** - Each exercise has specific requirements
- **Test your code** - Use the helper tool frequently
- **Keep it simple** - Don't overcomplicate solutions
- **Follow the rules** - Only write functions, not main programs
- **Use flake8** - Check your code style before submission
- **Understand your code** - You'll need to explain it during evaluation
- **Ask for help** - Collaborate with peers when stuck

---

**Happy Coding! 🌱**

*"The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie*

Remember: Programming is like gardening - it requires patience, practice, and nurturing. Start small, grow steadily, and enjoy the process!
