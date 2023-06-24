from starlette.testclient import TestClient

from main import app
from server.models.usuario_model import UsuarioModel
from server.repository.database_repository import get_db

client = TestClient(app)

def test_get_all_usuarios():
    _db = next(get_db())

    response = client.get('/usuarios/usuarios')

    print(response)

    data = _db.query(UsuarioModel).all()

    assert response.json()[0]['id'] == data[0].id
    assert response.json()[0]['nome'] == data[0].nome
    assert response.json()[0]['numero'] == data[0].numero
    assert response.json()[0]['salario'] == data[0].salario
    assert response.json()[0]['email'] == data[0].email
    assert response.json()[0]['senha'] == data[0].senha

    assert response.status_code == 200

def test_get_user_by_id():
    _db = next(get_db())

    response = client.get('/usuarios/usuarios/9')

    print(response)

    data = _db.query(UsuarioModel).filter_by(id=9).first()

    assert response.json()['id'] == data.id
    assert response.json()['nome'] == data.nome
    assert response.json()['numero'] == data.numero
    assert response.json()['salario'] == data.salario
    assert response.json()['email'] == data.email
    assert response.json()['senha'] == data.senha

    assert response.status_code == 200

def test_create_and_delete_user():
    _db = next(get_db())

    novo_usuario = {
        'nome': 'teste',
        'numero': 123456789,
        'salario': 1000.00,
        'email': 'qwerty@gmail.com',
        'senha': '123456'
    }

    response = client.post('/usuarios/usuarios', json=novo_usuario)

    id_usuario = response.json()['id']

    data = _db.query(UsuarioModel).filter_by(id=id_usuario).first()

    assert response.json()['id'] == data.id
    assert response.json()['nome'] == data.nome
    assert response.json()['numero'] == data.numero
    assert response.json()['salario'] == data.salario
    assert response.json()['email'] == data.email
    assert response.json()['senha'] == data.senha

    assert response.status_code == 201

    response = client.delete(f'/usuarios/usuarios/{id_usuario}')

    assert response.status_code == 204
