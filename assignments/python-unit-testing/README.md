# 📘 Assignment: Python Unit Testing

## 🎯 Objective

Learn to write and run Python unit tests with the built-in `unittest` module. Test the provided `shipping.py` function without changing its implementation.

## 📝 Tasks

### 🛠️ Write Your First Test

#### Description
Create `test_shipping.py` beside `shipping.py`. Import `calculate_shipping` and write a `unittest.TestCase` class to check a typical package weight.

#### Requirements
Completed program should:

- Use `unittest` and a test method whose name starts with `test_`
- Assert that `calculate_shipping(2)` returns `9`
- Run successfully with `python3 -m unittest discover -v` from the assignment directory

### 🛠️ Cover More Valid Weights

#### Description
Add tests for other positive weights so that the shipping rule is checked at more than one point.

#### Requirements
Completed program should:

- Assert that `calculate_shipping(1)` returns `7`
- Assert that `calculate_shipping(0.5)` returns `6`
- Keep each test independent so it can run on its own

### 🛠️ Test Invalid Weights

#### Description
Verify that the function rejects weights that are not positive.

#### Requirements
Completed program should:

- Use `assertRaises(ValueError)` to check a weight of `0`
- Use `assertRaises(ValueError)` to check a negative weight
- Run the full test suite and confirm all tests pass