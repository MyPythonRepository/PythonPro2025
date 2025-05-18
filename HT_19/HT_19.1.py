# https://leetcode.com/problems/employee-bonus/description/
#
# Table: Employee
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | empId       | int     |
# | name        | varchar |
# | supervisor  | int     |
# | salary      | int     |
# +-------------+---------+
# empId is the column with unique values for this table.
# Each row of this table indicates the name
# and the ID of an employee in addition to their salary
# and the id of their manager.
#
# Table: Bonus
#
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | empId       | int  |
# | bonus       | int  |
# +-------------+------+
# empId is the column of unique values for this table.
# empId is a foreign key (reference column) to empId from the Employee table.
# Each row of this table contains the id of an employee and their respective bonus.
#
# Write a solution to report the name and bonus amount of each employee
# with a bonus less than 1000.
#
# Return the result table in any order.


import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:

    employee_with_bonus = pd.merge(employee, bonus, on="empId", how="left")

    employees_with_small_bonus = employee_with_bonus[
        (employee_with_bonus["bonus"] < 1000) | (employee_with_bonus["bonus"].isna())
    ]

    return employees_with_small_bonus[["name", "bonus"]]
