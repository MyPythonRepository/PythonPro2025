# SELECT BillingCountry, SUM(UnitPrice * Quantity) as TotalSales
# FROM invoices
# JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
# GROUP BY BillingCountry;

# SELECT
# tracks.TrackId,
# tracks.Name AS TrackName,
# albums.Title AS AlbumTitle,
# artists.Name AS ArtistName,
# genres.Name AS GenreName,
# tracks.Composer,
# tracks.Milliseconds AS Duration,
# tracks.Bytes AS Size,
# tracks.UnitPrice AS Price,
# media_types.Name AS MediaType,
#
# COUNT(DISTINCT invoice_items.InvoiceId) AS PurchasesCount,
# SUM(invoice_items.Quantity) AS TotalQuantitySold,
#
# GROUP_CONCAT(DISTINCT customers.FirstName || ' ' || customers.LastName) AS Customers,
# GROUP_CONCAT(DISTINCT playlists.Name) AS Playlists
#
# FROM tracks
# JOIN albums ON tracks.AlbumId = albums.AlbumId
# JOIN artists ON albums.ArtistId = artists.ArtistId
# JOIN genres ON tracks.GenreId = genres.GenreId
# JOIN media_types ON tracks.MediaTypeId = media_types.MediaTypeId
# LEFT JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
# LEFT JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
# LEFT JOIN customers ON invoices.CustomerId = customers.CustomerId
# LEFT JOIN playlist_track ON tracks.TrackId = playlist_track.TrackId
# LEFT JOIN playlists ON playlist_track.PlaylistId = playlists.PlaylistId
#
# GROUP BY tracks.TrackId, albums.AlbumId, artists.ArtistId, genres.GenreId, media_types.MediaTypeId
# ORDER BY tracks.TrackId;
