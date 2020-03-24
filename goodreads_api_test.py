import requests
key = "KB60qlcbONEWi3EFs9A"
isbns = "9781632168146"
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": key, "isbns": isbns})
print(res.json())