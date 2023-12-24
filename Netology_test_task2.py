import requests


class YandexDiskAPIClient:
    API_BASE_URL = 'https://cloud-api.yandex.net'

    def __init__(self, token):
        self.headers = {'Authorization': token}

    def creating_folder(self, folder_name):
        self.folder_name = folder_name
        url_for_creating_folder = self.API_BASE_URL + '/v1/disk/resources'
        params = {'path': self.folder_name}
        response = requests.put(url_for_creating_folder, params=params, headers=self.headers)
        return response

    def get_info(self):
        url_for_get_info = self.API_BASE_URL + '/v1/disk/resources'
        params = {'path': self.folder_name}
        response = requests.get(url_for_get_info, params=params, headers=self.headers)
        return response


TOKEN_YANDEX = '********************************************'

if __name__ == '__main__':
    yandex_disk_client = YandexDiskAPIClient(TOKEN_YANDEX)
    response = yandex_disk_client.creating_folder('Test_Homework')
    print(response.status_code)
    response = yandex_disk_client.get_info()
    print(response.json())
