import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        yandex_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        get_request = requests.get(yandex_url, headers={'Authorization': token}, params={'path': file_path})
        upload_url = get_request.json()['href']
        with open(file_path, 'rb') as file_obj:
            requests.put(upload_url, files={"file": file_obj})


if __name__ == '__main__':
    path_to_file = 'test.txt'
    token = #Сюда надо вписать Токен
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
