from starlette.testclient import TestClient
from bs4 import BeautifulSoup
from app import app
import unittest


class MyTestCase(unittest.TestCase):
	def test_index_page_status_code(self):
		client = TestClient(app)
		response = client.get("/")
		self.assertEqual(200, response.status_code)

	def test_index_page_response(self):
		client = TestClient(app)
		response = client.get("/")
		content = bytes.decode(response.content)
		html = BeautifulSoup(content)
		title = html.select_one('title').text
		print(title)
		self.assertEqual("Expected Title", title)



if __name__ == '__main__':
	unittest.main()
