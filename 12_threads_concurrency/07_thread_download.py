import threading
import requests
import time

def download(url):
    print(f"Starting to Downloading {url}")
    response = requests.get(url)
    print(f" finished Downloaded {url} in {len(response.content)} bytes")

urls = [
   "https://httpbin.org/image/jpeg",
   "https://httpbin.org/image/png",
   "https://httpbin.org/image/svg", 
]

start = time.time()
threads = []

for url in urls:
    thread = threading.Thread(target=download, args=(url,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

end = time.time()
print(f"Time taken: {end - start:.2f}")