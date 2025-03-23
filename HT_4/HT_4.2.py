from flask import Flask, jsonify
from database_handler import execute_query


app = Flask(__name__)


@app.route("/tracks")
def get_all_info_about_track():

    query = """
    SELECT
        tracks.TrackId,
        tracks.Name AS TrackName,
        albums.Title AS AlbumTitle,
        artists.Name AS ArtistName,
        genres.Name AS GenreName,
        tracks.Composer,
        tracks.Milliseconds AS Duration,
        tracks.Bytes AS Size,
        tracks.UnitPrice AS Price,
        media_types.Name AS MediaType,

        COUNT(DISTINCT invoice_items.InvoiceId) AS PurchasesCount,
        SUM(invoice_items.Quantity) AS TotalQuantitySold,

        GROUP_CONCAT(DISTINCT customers.FirstName || ' ' || customers.LastName) AS Customers,
        GROUP_CONCAT(DISTINCT playlists.Name) AS Playlists

    FROM tracks
    JOIN albums ON tracks.AlbumId = albums.AlbumId
    JOIN artists ON albums.ArtistId = artists.ArtistId
    JOIN genres ON tracks.GenreId = genres.GenreId
    JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
    LEFT JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
    LEFT JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
    LEFT JOIN customers ON invoices.CustomerId = customers.CustomerId
    LEFT JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
    LEFT JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId

    GROUP BY tracks.TrackId, albums.AlbumId, artists.ArtistId, genres.GenreId, media_types.MediaTypeId
    ORDER BY tracks.TrackId;
    """

    records = execute_query(query)

    tracks_data = []
    for result in records:
        track_info = {
            "track_id": result[0],
            "track_name": result[1],
            "album_title": result[2],
            "artist_name": result[3],
            "genre_name": result[4],
            "composer": result[5],
            "duration_ms": result[6],
            "size_bytes": result[7],
            "price": result[8],
            "media_type": result[9],
            "purchases_count": result[10],
            "total_quantity_sold": result[11],
            "customers": result[12],
            "playlists": result[13]
        }
        tracks_data.append(track_info)

    return jsonify(tracks_data)


if __name__ == '__main__':
    app.run(
        'localhost', debug=True
    )
