#Commands typed to complete midterm
#Organization: Cooper Kettle Coffee Roasters
#Name: Sharath Srinivasan

# Terminal Record: Cooper Kettle Coffee Roasters

## 1. Building the project

```
pwd
/home/sharath/ism3232
MSI% mkdir ism3232-midterm
MSI% pwd
/home/sharath/ism3232
MSI% cd ~/ism3232/ism3232-midterm
MSI% python3 -m venv .venv && source .venv/bin/activate
(.venv) MSI% pip install pytest ruff && pip freeze > requirements.txt
Collecting pytest
  Using cached pytest-9.1.1-py3-none-any.whl.metadata (7.6 kB)
Collecting ruff
  Downloading ruff-0.17.2-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (20 kB)
Collecting iniconfig>=1.0.1 (from pytest)
  Using cached iniconfig-2.3.1-py3-none-any.whl.metadata (2.8 kB)
Collecting packaging>=22 (from pytest)
  Using cached packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pluggy<2,>=1.5 (from pytest)
  Downloading pluggy-1.7.0-py3-none-any.whl.metadata (5.0 kB)
Collecting pygments>=2.7.2 (from pytest)
  Using cached pygments-2.21.0-py3-none-any.whl.metadata (2.5 kB)
Using cached pytest-9.1.1-py3-none-any.whl (386 kB)
Downloading pluggy-1.7.0-py3-none-any.whl (27 kB)
Downloading ruff-0.17.2-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (10.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.5/10.5 MB 49.3 MB/s eta 0:00:00
Using cached iniconfig-2.3.1-py3-none-any.whl (7.6 kB)
Using cached packaging-26.3-py3-none-any.whl (129 kB)
Using cached pygments-2.21.0-py3-none-any.whl (1.3 MB)
Installing collected packages: ruff, pygments, pluggy, packaging, iniconfig, pytest
Successfully installed iniconfig-2.3.1 packaging-26.3 pluggy-1.7.0 pygments-2.21.0 pytest-9.1.1 ruff-0.17.2
(.venv) MSI% echo '.venv/' > .gitignore && echo '__pycache__/' >> .gitignore
(.venv) MSI% touch business_rules.py main.py
(.venv) MSI% mkdir -p tests && touch tests/__init__.py tests/test_business_rules.py
(.venv) MSI% tree -L 3
.
├── business_rules.py
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_business_rules.py

2 directories, 5 files
(.venv) MSI% pwd
/home/sharath/ism3232/ism3232-midterm
(.venv) MSI% touch commands.md README.md
(.venv) MSI% tree -L 3
.
├── README.md
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_business_rules.py
MSI% git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: will change to "main" in Git 3.0. To configure the initial branch name
hint: to use in all of your new repositories, which will suppress this warning,
hint: call:
hint:
hint:   git config --global init.defaultBranch <name>
hint:
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint:
hint:   git branch -m <name>
hint:
hint: Disable this message with "git config set advice.defaultBranchName false"
Initialized empty Git repository in /home/sharath/ism3232/ism3232-midterm/.git/
(.venv) MSI% git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        README.md
        business_rules.py
        commands.md
        main.py
        requirements.txt
        tests/

nothing added to commit but untracked files present (use "git add" to track)
(.venv) MSI% git remote set-url origin git@github.com:ShaSrinivasan/ism3232-midterm.git
error: No such remote 'origin'
(.venv) MSI% git branch -M main
(.venv) MSI% git remote set-url origin git@github.com:ShaSrinivasan/ism3232-midterm.git
error: No such remote 'origin'
(.venv) MSI% git remote set-url origin git@github.com:ShaSrinivasan/ism3232-midterm.git
error: No such remote 'origin'
(.venv) MSI% git fetch origin
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(.venv) MSI% git add .
(.venv) MSI% git commit -m 'intial tree setup'
[main (root-commit) 69fa6bf] intial tree setup
 8 files changed, 8 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 business_rules.py
 create mode 100644 commands.md
 create mode 100644 main.py
 create mode 100644 requirements.txt
 create mode 100644 tests/__init__.py
 create mode 100644 tests/test_business_rules.py
(.venv) MSI% git remote set-url origin git@github.com:ShaSrinivasan/ism3232-midterm.git
error: No such remote 'origin'
(.venv) MSI% git push -u origin main
fatal: 'origin' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
(.venv) MSI% git status
On branch main
nothing to commit, working tree clean
(.venv) MSI% git remote add origin  git@github.com:ShaSrinivasan/ism3232-midterm.git
(.venv) MSI% git push -u origin main
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 562 bytes | 562.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To github.com:ShaSrinivasan/ism3232-midterm.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```


## 2. The virtual environment
```
(.venv) MSI% which python3
```
```
/home/sharath/ism3232/ism3232-midterm/.venv/bin/python3
```
After the directory name (ism3232-midterm), the .venv shows that the virtual environment is active. venv stands for virtual environment


## 3. The project structure
```
(.venv) MSI% tree -L 2

```

.
├── README.md
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 8 files
```
The gitignore folder is not on the computer but it is in the repository. It is hidden


## 4. Every function and test
```
business_rules.py
```
```
6:def calculate_bean_cost(bag_price: float, bags: int) -> float:
12:def get_bulk_discount(bags: int, partner: bool = False) -> float:
26:def calculate_shipment_total(bag_price: float, bags: int, partner: bool = False) -> float:
38:def requires_prepayment(total: float) -> bool:
46:def needs_pallet(bags: int, total: float) -> bool:
53:def total_shipped(shipments: list) -> float:
61:def largest_shipment(shipments: list) -> str:
75:def format_shipment_line(buyer: str, total: float, prepayment: bool, pallet: bool) -> str:

tests/test_business_rules.py
7:def test_calculate_bean_cost():
12:def test_get_bulk_discount():
19:def test_calculate_shipment_total():
29:def test_requires_prepayment():
34:def test_needs_pallet():
40:def test_total_shipped():
44:def test_largest_shipment():
48:def test_format_shipment_line():

```
Business rules defines 8 functions, and tests/test_business_rules defines 8 tests


## 5. Which files print
```
MSI% rg -l 'print'
```
```
main.py
```
Only main.py prints, because business_rules.py is meant to set the rules only. By not having any prints, we keep the files separate, with one having the rules, and the other being the main testing file.


## 6. The commit history

```
(.venv) MSI% git log --oneline
ae6e7c4 (HEAD -> main, origin/main) Fixed test statements to pass pytest as well as fixing computation errors in business rules
808d6d1 updated test for business rules
6942c49 Fixed small errors in main and business rules to adjust main output to match perfectly
d4598d6 Added name and organization comment for business rules and main, and begun work on pytest
f256d46 Fixed Largest Shipment function in business_rules to complete main.py
fbeaf29 Base of main.py and format shiptment line print
cbf6e2a Business rules function 8
8af516d Edited comments for functions, and fixed functions 3-5 and added funciton 7
6d521a4 Business rules functions 5 and 6
28d17f8 Business rules 3-5
6ba3e7b Business rules 1 and 2
69fa6bf intial tree setup
```
Currently there are 12 commits.