from app import app

def test_pagina():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
<<<<<<< HEAD

#ares de testes
=======
>>>>>>> 570f3e0a5a25fcda837a59a94a4f15b15747b34f
