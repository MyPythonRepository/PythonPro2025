# SELECT customers.City, COUNT(invoice_items.InvoiceId) AS PurchaseCount
# FROM invoice_items
# JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId
# JOIN customers ON invoices.CustomerId = customers.CustomerId
# JOIN tracks ON invoice_items.TrackId = tracks.TrackId
# JOIN genres ON tracks.GenreId = genres.GenreId
# WHERE genres.Name = 'Jazz'
# GROUP BY customers.City
# ORDER BY PurchaseCount DESC;
