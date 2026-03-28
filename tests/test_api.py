import requests
import pytest

@pytest.fixture
def respuesta_usuarios():
    return requests.get("https://jsonplaceholder.typicode.com/users")

@pytest.fixture
def respuesta_post():
    return requests.get("https://jsonplaceholder.typicode.com/posts/1")

def test_lista_usuarios_status_ok(respuesta_usuarios):
    assert respuesta_usuarios.status_code == 200

def test_lista_usuarios_no_esta_vacia(respuesta_usuarios):
    usuarios = respuesta_usuarios.json()
    assert len(usuarios) > 0

def test_post_tiene_titulo(respuesta_post):
    posts = respuesta_post.json()
    assert "title" in posts

def test_usuario_inexistente():
    respuesta = requests.get("https://jsonplaceholder.typicode.com/users/9999")
    assert respuesta.status_code == 404

def test_crear_usuario():
    nuevo_usuario = {"name": "Santiago", "email": "santiago@email.com", "username": "santi"}
    respuesta = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=nuevo_usuario
    )
    datos = respuesta.json()
    assert respuesta.status_code == 201
    assert datos["name"] == "Santiago"

def test_actualizar_usuario():
    mod_usuario = {"name": "Santiago Updated", "email": "updated@email.com", "username": "santi"}
    respuesta = requests.put(
        "https://jsonplaceholder.typicode.com/users/1",
        json=mod_usuario
    )
    datos = respuesta.json()
    assert respuesta.status_code == 200
    assert datos["name"] == "Santiago Updated"

def test_eliminar_usuario():
    respuesta = requests.delete("https://jsonplaceholder.typicode.com/users/1")
    assert respuesta.status_code == 200