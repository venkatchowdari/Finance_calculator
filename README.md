# Finance Calculator

A Python-based financial calculator that helps users track their monthly and yearly finances including salary, taxes, and expenses.

## Features

- Calculate monthly and yearly net income
- Account for tax deductions
- Track monthly expenses including:
  - Gym membership
  - Rent
  - Food
- Support for different currency symbols
- Error handling for invalid inputs

## Usage

There are three versions of the calculator:

1. [main.py](main.py) - Basic version with salary and tax calculations
2. [main_c.py](main_c.py) - Extended version with expense tracking
3. [main_errorless.py](main_errorless.py) - Full version with error handling

### Running the Program

```bash
python main_errorless.py
```

### Input Requirements

The program will ask for:
- Monthly salary (number)
- Tax rate percentage (number)
- Monthly gym membership cost (number)
- Monthly rent (number)
- Food expenses (number)
- Currency symbol

### Example Output

```
-----------------------------------------------------------

Monthly income: $5000.00
Monthly Expense: $2000.00
Monthly Net income: $2600.00
Yearly Salary: $60000.00
Yearly Tax Rate: $4800.00
Your per year income: $24000.00
Yearly Net income: $31200.00

-----------------------------------------------------------
```

## Error Handling

The `main_errorless.py` version includes error handling for:
- Invalid numeric inputs
- Type conversion errors

## Requirements

- Python 3.x

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request