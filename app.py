import streamlit as st
import json
import requests

def display_word_cloud_and_sentiments(data):
    # Display word cloud
    st.header("Word Cloud")
    word_cloud_data = data.get("word_cloud_data", [])
    for entry in word_cloud_data:
        phrase = entry["phrase"]
        # Create an expander for each word
        with st.expander(phrase):
            display_unique_sentiments(entry)

def display_unique_sentiments(entry):
    # Display unique sentiments for the selected word
    sentiments_set = set()  # Set to store unique sentiments
    mentions = entry.get("mentions", [])
    for mention in mentions:
        sentiment = (mention['date'], mention['text'])  # Use a tuple to represent each sentiment
        if sentiment not in sentiments_set:
            st.write(f"Date: {mention['date']}")
            st.write(f"Text: {mention['text']}")
            st.write("-----")
            sentiments_set.add(sentiment)

def main():
    st.title("Word Cloud and Sentiments")

    # Fetch JSON data from URL
    url = 'https://blackpantherprotection.com/streamlit/wordcloud_data.json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        display_word_cloud_and_sentiments(data)
    else:
        st.error("Failed to fetch data from the provided URL.")

if __name__ == "__main__":
    main()
