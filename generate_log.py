import requests
from lib.generate_log import generate_log

def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return {}

if __name__ == "__main__":
    post = fetch_data()
    post_title = post.get("title", "No title found")
    print("Fetched Post Title:", post_title)

    log_data = [
        "User logged in",
        f"Fetched post title: {post_title}",
        "Report exported"
    ]
    generate_log(log_data)
