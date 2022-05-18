from pprint import pprint
from urllib import response
import requests        


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net:443/v1/disk/resources"
        headers = {
            "Authorization": f"OAuth {token}"
            }

        file_path = (f"/{file_name}")

        res = requests.get(f"{url}/upload?path={file_path}", headers=headers).json()
        pprint(res)

        with open(path_to_file, "rb") as f:
            requests.put(res["href"], files={"file": f})

if __name__ == '__main__':
    file_name = "test.txt"
    path_to_file = (f"/home/fes/test/{file_name}")
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)