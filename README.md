# ISM3232 Midterm: Copper Kettle Coffee Roasters

- **Name:** Sharath Srinivasan
- **Version:** ZETA
- **Date:**10/25/2026

## What This Program Does
This program analyzes the buyers in main.py and their shipment of coffee by the bag. It follows the rules in business_rules.py to determine things like cost, discounts, fees, pallets and prepayments, and then allows for summary statements to be output. It gives Cooper Kettle Coffee the ability to see who their biggest and largest customers are, and the impact their partnership has on business.
## Business Rules
The business has 6 rules. 
1. The cost of the beans is the bag price times the amount of bags
2. There are various discounts depending on number of bags ordered. 80 and above is 14%, 20-79 is 9%, and there is no discount for orders under 20 bags.
3. If a cafe is a partner, they get an extra discount of 4%, provided they order more than 20 bags. The extra applies to the discounts set by rule 2.
4. If the order is less than $250, there is a $35 shipping fee.
5. If the order is more than $1500, there needs to be a prepayment.
6. If the order is $700 or more, and there is 60 or more bags, that shipment requires a frieght pallet.
## How to Run
```
python3 -m venv .venv && source .venv/bin/activate
pip install pytest ruff && pip freeze > requirements.txt
echo '.venv/' > .gitignore && echo '__pycache__/' >> .gitignore

```

```
python3 main.py
```

## How to Test
```
pytest -v
ruff format .
ruff check .
```
I wrote 26 tests to test edge cases and make sure the outputs match

## Files in This Repository

.
├── README.md  - README file for documentation and understanding of what is in the project
├── business_rules.py - rules for main.py to follow based on the 6 business rules. Functions for each element of the project created
├── commands.md - All the commands used in the making of the project.
├── main.py - The data being tested and printing of summary stats based on business rules
├── requirements.txt - libraries required for this project, being pytest and ruff
└── tests - Folder containing all the tests we are running
    └── test_business_rules.py - all 26 tests for pytest


## AI Use Statement

I did not use AI on this exam.