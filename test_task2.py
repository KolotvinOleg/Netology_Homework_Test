import pytest
from Netology_test_task2 import YandexDiskAPIClient, TOKEN_YANDEX


class Test_create_folder:
    def setup(self):
        self.y = YandexDiskAPIClient(TOKEN_YANDEX)

    def teardown(self):
        self.y = None

    def test_create_folder_status_code(self):
        response = self.y.creating_folder('Netology_test')
        assert response.status_code == 201
        response = self.y.get_info()
        assert response.json()['name'] == 'Netology_test'
        assert response.json()['type'] == 'dir'