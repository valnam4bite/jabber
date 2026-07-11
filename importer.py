def group_by_source(albums):

    grouped = {}

    for album in albums:

        grouped.setdefault(
            album.source,
            []
        ).append(album)

    return grouped
