import urllib.parse
import random
import sys
import requests

def add_noise_to_url(url: str) -> str:
    parsed_url = urllib.parse.urlparse(url)
    query = urllib.parse.parse_qs(parsed_url.query)
    for key, value in query.items():
        # Add random byte noise to the value
        noise = bytes([random.randint(0, 255) for _ in range(3)])
        query[key] = [value[0] + noise.decode()]
    # Update the query string and return the modified URL
    new_query = urllib.parse.urlencode(query, doseq=True)
    return parsed_url._replace(query=new_query).geturl()
original_url = sys.argv[1]
noisy_url = add_noise_to_url(original_url)


r = requests.get(noisy_url)
print(r.text)

