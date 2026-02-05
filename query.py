def search(query, start_date=None, end_date=None):
    results = base_search(query)

    if start_date and end_date:
        results = [
            item for item in results
            if start_date <= item.created_at <= end_date
        ]

    return results
