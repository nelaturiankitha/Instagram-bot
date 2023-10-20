from selenium import webdriver
import time
import matplotlib.pyplot as plt

# Initialize the web driver (use the appropriate driver for your browser)
driver = webdriver.Chrome()

# Login to Instagram (replace with your credentials)
username = "YourUsername"
password = "YourPassword"

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(2)

# Fill in username and password and click the login button
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(5)

# Search for 'mealprep' and navigate to a related profile
search_query = "mealprep"
driver.get(f"https://www.instagram.com/explore/tags/{search_query}/")
time.sleep(5)

# Collect data
likes = []
comments = []

# Scroll through a few posts to load more data
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Extract data from posts (adjust the CSS selectors as needed)
post_elements = driver.find_elements_by_css_selector("div.v1Nh3.kIKUG._bz0w")
for post in post_elements:
    post.click()
    time.sleep(2)

    try:
        like_count = driver.find_element_by_css_selector("div.Nm9Fw span").text
        likes.append(int(like_count.replace(',', '')))
    except:
        likes.append(0)

    try:
        comment_count = driver.find_element_by_css_selector("button._6CZji span").text
        comments.append(int(comment_count.replace(',', '')))
    except:
        comments.append(0)

    driver.find_element_by_css_selector("div.Igw0E button.wpO6b").click()
    time.sleep(1)

# Close the browser
driver.quit()

# Data analysis and visualization
plt.figure(figsize=(10, 5))
plt.plot(likes, label="Likes", marker='o')
plt.plot(comments, label="Comments", marker='o')
plt.title("Likes and Comments on Meal Prep Posts")
plt.xlabel("Post Number")
plt.ylabel("Count")
plt.legend()
plt.grid(True)
plt.show()
