from web.routes import create_app

def test_create_app():
    app = create_app()
    client = app.test_client()
    response = client.post("/id_text", data={"user_text": "Straße gesperrt"})
    assert response.get_json()[0][0] == "Germany"