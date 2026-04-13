import streamlit as st
from googleapiclient.discovery import build

# ---- CONFIG ----
API_KEY = "YOUR_API_KEY_HERE"

youtube = build("youtube", "v3", developerKey=API_KEY)

st.set_page_config(page_title="YouTube Channel Stats", layout="centered")

st.title("📊 YouTube Channel Stats Checker")

# ---- INPUT ----
channel_name = st.text_input("Enter YouTube Channel Name")

def get_channel_stats(name):
    search_response = youtube.search().list(
        q=name,
        part="snippet",
        type="channel",
        maxResults=1
    ).execute()

    if not search_response["items"]:
        return None

    channel_id = search_response["items"][0]["snippet"]["channelId"]

    channel_response = youtube.channels().list(
        part="snippet,statistics",
        id=channel_id
    ).execute()

    return channel_response["items"][0]

# ---- BUTTON ----
if st.button("Get Stats"):
    if channel_name:
        data = get_channel_stats(channel_name)

        if data:
            stats = data["statistics"]
            snippet = data["snippet"]

            st.subheader(snippet["title"])
            st.image(snippet["thumbnails"]["high"]["url"])

            st.write("**Subscribers:**", stats.get("subscriberCount", "Hidden"))
            st.write("**Total Views:**", stats["viewCount"])
            st.write("**Total Videos:**", stats["videoCount"])
        else:
            st.error("Channel not found!")
    else:
        st.warning("Enter a channel name first")
