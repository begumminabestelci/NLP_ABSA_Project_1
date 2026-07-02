from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from langdetect import detect
import time
import random
import json

# Set up Selenium with Service
driver_path = "/Users/busedikici/Downloads/chromedriver-mac-arm64/chromedriver"
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Open YouTube video
video_url = "https://www.youtube.com/watch?v=X9hKRIQ3uxc"
driver.get(video_url)
time.sleep(5)

# Scroll to load comments
for _ in range(20):  # Adjust scrolling depth
    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(2)

# Extract comments
comments = []
comment_elements = driver.find_elements(By.CSS_SELECTOR, "#content-text")

for element in comment_elements:
    try:
        text = element.text
        # Detect language of the comment
        if detect(text) == "en":
            comments.append(text)
    except Exception as e:
        # Skip if language detection fails
        print(f"Error detecting language for comment: {element.text}")

# Randomly select 300 English comments
random_comments = random.sample(comments, min(300, len(comments)))

# Save comments to JSON
output_file = "youtube_comments_english.json"
with open(output_file, "w", encoding="utf-8") as file:
    json.dump(random_comments, file, ensure_ascii=False, indent=4)

print(f"Saved {len(random_comments)} English comments to {output_file}")

# Close the browser
driver.quit()
