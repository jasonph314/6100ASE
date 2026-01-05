import requests

def main():
    artwork = input("Artwork: ")
    artworks = get_artworks(query=artwork, limit=3)
    for artwork in artworks:
        print(f"*{artwork}")

def get_artworks(query, limit):
    try:
        response = requests.get(
                "https://api.artic.edu./api/v1/artworks/search",
                {"q": query,"l": limit}
                )
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        return

    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")

main ()
