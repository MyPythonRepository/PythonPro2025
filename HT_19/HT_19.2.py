# https://leetcode.com/problems/customers-who-bought-all-products/description/
#
# 1045. Customers Who Bought All Products
#
# Table: Customer
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | customer_id | int     |
# | product_key | int     |
# +-------------+---------+
# This table may contain duplicates rows.
# customer_id is not NULL.
# product_key is a foreign key (reference column) to Product table.
#
# Table: Product
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | product_key | int     |
# +-------------+---------+
# product_key is the primary key (column with unique values) for this table.
#
# Write a solution to report the customer ids from the Customer table that
# bought all the products in the Product table.
#
# Return the result table in any order.


import pandas as pd


def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    all_products = product["product_key"].nunique()

    customer_product_count = (
        customer
        .drop_duplicates()
        .groupby("customer_id")["product_key"]
        .nunique()
        .reset_index()
    )

    result = customer_product_count[
        customer_product_count["product_key"] == all_products
        ][["customer_id"]]

    return result
