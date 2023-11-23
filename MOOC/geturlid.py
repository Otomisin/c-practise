import argparse
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_video_id(api_key, video_url):
    # Parse video ID from the URL
    video_id = video_url.split("v=")[1]

    # Build the YouTube Data API service
    youtube = build("youtube", "v3", developerKey=api_key)

    try:
        # Make API request to get video details
        response = youtube.videos().list(part="snippet", id=video_id).execute()

        # Extract video title
        video_title = response["items"][0]["snippet"]["title"]

        print(f"Video Title: {video_title}")
        print(f"Video ID: {video_id}")

    except HttpError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get YouTube Video ID")
    parser.add_argument("--api_key", required=True, help="Your YouTube Data API key")
    parser.add_argument("--video_url", required=True, help="URL of the YouTube video")

    args = parser.parse_args()

    get_video_id(args.api_key, args.video_url)
