from flask import Flask, jsonify
from webargs import fields
from webargs.flaskparser import use_kwargs
from database_handler import execute_query


app = Flask(__name__)


# http://localhost:5000/sales?country=Germany
@app.route("/sales")
@use_kwargs(
    {
        "country": fields.Str(missing=None)
    },
    location="query"
)
def get_sales(country):

    query = """
        SELECT BillingCountry, SUM(UnitPrice * Quantity) as TotalSales
        FROM invoices
        JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
    """

    if country:
        query += " WHERE BillingCountry = ? GROUP BY BillingCountry"
        records = execute_query(query, (country,))
    else:
        query += " GROUP BY BillingCountry"
        records = execute_query(query)

    sales_data = [{"country": row[0], "total_sales": row[1]} for row in records]

    return jsonify(sales_data)


if __name__ == '__main__':
    app.run(
        'localhost', debug=True
    )
