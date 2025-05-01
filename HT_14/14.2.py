# https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
# 181. Employees Earning More Than Their Managers
# Table: Employee
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | salary      | int     |
# | managerId   | int     |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID of an employee, their name,
# salary, and the ID of their manager.
# Write a solution to find the employees who earn more than their managers.
# Return the result table in any order.


import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(employee, left_on="managerId", right_on="id", suffixes=("", "_manager"))

    result = merged[merged["salary"] > merged["salary_manager"]]

    return result[["name"]].rename(columns={"name": "Employee"})
