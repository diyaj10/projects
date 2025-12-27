import requests
query = input("What do you want to know?\n")
api = "094b51fb41da45dcb7ab6dcfaf30f054"
url =f"https://newsapi.org/v2/everything?q={query}&from=2025-11-27&sortBy=publishedAt&apiKey={api}"

r = requests.get(url)
data = r.json()
articles = data['articles']
print(f"\nHere's all the related news regarding {query}\n")
for article in articles:

    print("Title: "+ article["title"]) 
    print("Content: " + article["content"])
    print("URL: "+ article["url"])
    print("\n***********************\n")
