from starlette.testclient import TestClient
from app import app


def test_index_page():
	client = TestClient(app)
	res = client.get("/")
