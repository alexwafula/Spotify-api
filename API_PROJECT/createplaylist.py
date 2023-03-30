import requests


SPOTIFY_CREATE_PLAYLIST_URL = 'https://api.spotify.com/v1/users/wafs/pLaylists'
ACCESS_TOKEN =  'BQBcFa8h17up5YaIIhgfwWbbDpmpeHJ6OY4-PZGMSBPA-zg7zGwZn1AhcfnTiDXth0_yFPvgum_UxUhYBo7W2tcCmcFlIgZA0C2k4BQN0YLtN7QMwkVUOWPE0b-D_295v-gBQ_S3-qQtxJXQt2rSq-_LdfosFotWK0V4sCHAznqGlOi-6MtfJSVco93ynMausGHusLz1hUkBLDfEL91MgBncjBnnvEIz6cskDwkPIWt0rxOIgAiSorjPJT_T0RW-D8NyOf4lf3uT6YT94DvQHahrCE3ClqPEabxPjOIht6bWS1TgrB9-f266wrtKL-zW_zq4Y-Riu-MRaFbpf5uxLeoFPJ-tpduPxgKbm7J8HFMvq6Y'



def create_playlist_on_spotify(name, public):

    response = requests.post(
      SPOTIFY_CREATE_PLAYLIST_URL,
      headers={
          "Authorization": f"Bearer {ACCESS_TOKEN}"

        },

        json={

            "name" : name,
            "public": public

        }


    )

    json_resp = response. json()

    return json_resp


def main():
    playlist = create_playlist_on_spotify(
        name="Top 5!",
        public=False
    )

    print(f"Playlist: {playlist}")

if __name__ == '__main__':
    main()


