from flask import Flask, jsonify
from webargs import fields
from webargs.flaskparser import use_kwargs
from database_handler import execute_query

app = Flask(__name__)


# http://localhost:5000/stats_by_city?genre=Rock
# http://localhost:5000/stats_by_city?genre=Jazz
# http://localhost:5000/stats_by_city?genre=Metal
@app.route("/stats_by_city")
@use_kwargs(
    {
        "genre": fields.Str(required=True)
    },
    location="query"
)
def get_city_by_genre(genre):

    query = """
    SELECT customers.City, COUNT(invoice_items.InvoiceId) AS PurchaseCount
    FROM invoice_items
    JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
    JOIN customers ON invoices.CustomerId = customers.CustomerId
    JOIN tracks ON invoice_items.TrackId = tracks.TrackId
    JOIN genres ON tracks.GenreId = genres.GenreId
    """

    query_parameters = {}
    query_parameters["genres.Name"] = genre

    if query_parameters:
        query += " WHERE " + " AND ".join(f"{key}=?" for key in query_parameters)

    query += " GROUP BY customers.City ORDER BY PurchaseCount DESC;"

    records = execute_query(query, tuple(query_parameters.values()))

    if not records:
        return jsonify({"message": "No such genre"}), 404

    result = [{"city": row[0], "purchase_count": row[1]} for row in records]

    return jsonify(result)


if __name__ == '__main__':
    app.run(
        'localhost', debug=True
    )
