import os
import json
import sqlite3
from dotenv import load_dotenv
from driver import Driver
from datetime import datetime, timedelta


start=datetime.now()
# Load environment variables and webdriver
load_dotenv()  # take environment variables from .env.
driver = Driver()

# Initialize database
con = sqlite3.connect("linkedin.db")
cur = con.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS post(
            id TEXT PRIMARY KEY DEFAULT (lower(hex(randomblob(4))) || '-' || lower(hex(randomblob(2))) || '-4' || substr(lower(hex(randomblob(2))),2) || '-a' || substr(lower(hex(randomblob(2))),2) || '-%' || lower(hex(randomblob(6)))),
            title VARCHAR(255) NOT NULL
            );
        """
)

# Sign in to LinkedIn Account defined in .env file
driver.get("https://www.linkedin.com/")
driver.find_element_by_id("session_key").send_keys(os.getenv("LINKEDIN_USER"))
driver.find_element_by_id("session_password").send_keys(os.getenv("LINKEDIN_PASS"))
driver.find_element_by_class_name("sign-in-form__submit-btn--full-width").click()

# Load all posts to list
# Scroll to last post
# Find new posts
# Add new posts to the list

input()
posts = driver.find_elements_by_class_name("update-components-text")


for post in posts:
    cur.execute("INSERT INTO post(title) VALUES("
                f"""'{post.text.replace("'", "").replace('"', "")}');"""
    )
    con.commit()
while True:
    new_posts = driver.find_elements_by_class_name("update-components-text")
    for new_post in new_posts:
        if new_post not in posts:
            cur.execute(
                "INSERT INTO post(title) VALUES("
                f"""'{new_post.text.replace("'", "").replace('"', "")}');""" 
            )
            con.commit()
            posts.append(new_post)
    print(f"Time eleapsed : {datetime.now()-start}")
    if datetime.now()-start > timedelta(seconds=60) :
        break
    driver.scroll_to_end_of_page()

# Serializing json
json_object = json.dumps([{"post":post.text}for post in posts], indent=4)

driver.quit()
