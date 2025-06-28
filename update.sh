#!/bin/bash

# DEFAUT VALUES
# programming language - python
# competetive platform - codeforces

# INPUT BLOCK
echo "Enter Problem Name"
read problem_name

echo "Enter Problem Web Link"
read problem_link

echo "Enter Commit Message"
read commit_message
echo ""


# VARIABLE BLOCK
code_path="./codeForces/python/$problem_name.py"


# EXECUTION BLOCK
cp run.py $code_path

echo "| $problem_name | [[$problem_link][$problem_name]] | [[$code_path][Python]] |" | tee -a README.org

git add .

git commit -m "$commit_message"

git push origin main
