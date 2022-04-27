
import requests
from pprint import pprint



class YaUploader:
    def __init__(self, token, file_path: str, file: str):
        self.token = token
        self.file_path = file_path
        self.file = file

    def get_headers(self):
        return {'Content-type': 'application/json','Authorization': 'OAuth {}'.format(self.token)}

    def upload(self):
        """Метод загруджает файлы по списку file_list на яндекс диск"""

        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": self.file_path, "overwrite": "true"}
        response_upload = requests.get(upload_url, headers=headers, params=params)
        res = response_upload.json().get("href", "")
        response_url = requests.put(res, data=open(self.file, 'rb'))
        response_url.raise_for_status()
        if response_url.status_code == 201:
            print("Success")


if __name__ == '__main__':

    token = ''
    file_path = "homework/AndPetrov.docx"
    file = 'c:\\AndPetrov.docx'
    uploader = YaUploader(token, file_path, file)
    uploader.upload()