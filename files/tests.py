import json
from pathlib import Path
from django.test import TestCase, Client
from .models import File

BASE_DIR = Path(__file__).resolve().parent.parent

class FilesTest(TestCase):
    def generate_file(self):
        try:
            file = open('test.txt', 'w')
            file.write("Test file")
        finally:
            file.close()

        return file

    def setUp(self):
        self.client = Client()
        items = [
            {"file": "/file.txt", "uploaded_at": "2024-02-17T00:45:27.505768+03:00", "processed": False},
            {"file": "/file.jpg", "uploaded_at": "2024-02-17T00:45:27.505768+03:00", "processed": True},
            {"file": "/file.png", "uploaded_at": "2024-02-17T00:45:27.505768+03:00", "processed": False},
        ]
        for item in items:
            File.objects.create(**item)

    def test_all_files(self):
        response = self.client.get('/api/v1/files/files/')
        self.assertEqual(response.status_code, 200)
        items = json.loads(response.content)
        self.assertEqual(len(items), 3)
        self.assertEqual(items[0]['file'], '/media/file.txt')

    def test_one_file(self):
        response = self.client.get('/api/v1/files/files/2/')
        self.assertEqual(response.status_code, 200)
        item = json.loads(response.content)
        self.assertEqual(item['file'], '/media/file.jpg')

    def test_all_files_pagination(self):
        response = self.client.get('/api/v1/files/paginated_files/?limit=10')
        self.assertEqual(response.status_code, 200)

    
    def test_file_upload(self):
        file = self.generate_file()
        file = open(file.name, "r")
        print(file.name)

        post_data = {'file': file}

        response = self.client.post('/api/v1/files/upload/', post_data)
        self.assertEqual(response.status_code, 201)