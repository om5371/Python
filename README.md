## 📋 Requirements Covered

### User Input

The program uses `input()` to collect:

* Name
* Age
* Height
* Favorite Number

### Output Display

The program uses `print()` to:

* Display welcome messages
* Show collected information
* Display the calculated birth year

### Variables and Data Types

The application stores data using:

* `str` for Name
* `int` for Age
* `float` for Height
* `int` for Favorite Number

### Type Casting

The program converts user input into appropriate data types:

```python
age = int(input("Please Enter your age: "))
height = float(input("Please Enter your height in meters: "))
```

### Operators Used

The subtraction operator (`-`) is used to calculate the birth year:

```python
birthday = currentyear - age
```

### Built-in Functions

The project demonstrates the use of:

```python
input()
print()
type()
id()
```

### Date and Time Module

The `datetime` module is used to obtain the current year:

```python
currentyear = datetime.now().year
```

### Birth Year Calculation

The user's approximate birth year is calculated using:

```python
birthday = currentyear - age
```

