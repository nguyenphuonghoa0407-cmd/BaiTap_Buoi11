import requests

response = requests.get("https://api.github.com/repos/python/cpython")
if response.status_code == 200:
    data = response.json()
    print("Tên repository:", data["full_name"])
    print("Số sao (stars):", data["stargazers_count"])
    print("Ngôn ngữ chính:", data["language"])
else:
    print("Lỗi kết nối API:", response.status_code)