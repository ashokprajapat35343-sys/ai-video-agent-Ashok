youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "Trending News Today",
            "description": "AI generated news"
        },
        "status": {
            "privacyStatus": "public"
        }
    },
    media_body=MediaFileUpload(
        "output/test_short.mp4"
    )
)
