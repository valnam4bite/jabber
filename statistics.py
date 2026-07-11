from importer import group_by_source


def show_statistics(albums):

    print("-" * 40)

    print(f"Albums: {len(albums)}")

    artists = {
        album.artist
        for album in albums
    }

    print(f"Artists: {len(artists)}")

    average = (
        sum(album.rating for album in albums)
        / len(albums)
    )

    print(f"Average Rating: {average:.1f}")

    print("\nAlbums by Source:")

    grouped = group_by_source(albums)

    for source, items in grouped.items():
        print(f"{source}: {len(items)}")
