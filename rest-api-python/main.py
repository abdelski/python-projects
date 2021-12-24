import requests
import pprint
import pandas as pd

api_key = "61a867ed341f789c69219866a4e81d35"
api_key_v4 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MWE4NjdlZDM0MWY3ODljNjkyMTk4NjZhNGU4MWQzNSIsInN1YiI6IjYxYWNkNzRkMDdhODA4MDA1ZmMxZTEyZiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.fGKE4_Apw0Xf9tTK8K8d1hwARAENll4JPe-2NmzP7L4"
"""
GET ->GRAB DATA
POST -> ADD/UPDATE DATA
PATCH 
PUT 
DELETE
"""


"""
endpoint 
GET
get/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=61a867ed341f789c69219866a4e81d35 
"""

# # version 3
#
# movie_id = 500
# api_version = 3
# api_base_url = f"https://api.themoviedb.org/{api_version}"
# endpoint_path = f"/movie/{movie_id}"
# endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
#
# r = requests.get(endpoint)  # json={"api_key": api_key})
# print(r.status_code)
# print(r.text)
#
# # version 4
#
# movie_id = 500
# api_version = 4
# api_base_url = f"https://api.themoviedb.org/{api_version}"
# endpoint_path = f"/movie/{movie_id}"
# endpoint = f"{api_base_url}{endpoint_path}"
# headers = {
#     'Authorization': f'Bearer {api_key_v4}',
#     'Content-Type': 'application/json;charset=utf-8'
# }
# r = requests.get(endpoint, headers=headers)
# print(r.status_code)
# print(r.text)

# version 3 search


movie_id = 500
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
search_query = "The Matrix"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"

r = requests.get(endpoint)
print(r.status_code)
movie_ids = set()
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    print(results[0].keys())
    for result in results:
        _id = result['id']
        titles = result['title']
        movie_ids.add(_id)

output = 'movies.csv'
movie_data = []
for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200, 299):
        data = r.json()
        movie_data.append(data)
df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=False)
