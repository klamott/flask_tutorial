from flaskr import create_app

app = create_app()


def test_index():

    tester = app.test_client()
    response = tester.get("/hello", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"