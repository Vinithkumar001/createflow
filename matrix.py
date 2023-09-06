name: Count Zeros in Matrix

on:
  push:
    branches:
      - main  # Adjust this branch name as needed

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.8  # You can choose your desired Python version

    - name: Install dependencies
      run: pip install -r requirements.txt  # If you have any requirements

    - name: Run Python script
      run: python matrix.py  # Replace with the actual filename of your script

    - name: Display result
      run: |
        zeros_count=$(python -c "from your_script import count_zeros; matrix = [[1, 0, 2], [0, 3, 4], [5, 0, 6]]; print(count_zeros(matrix))")
        echo "Number of zeros in the matrix: $zeros_count"
