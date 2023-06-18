from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_deve_listar_contas_a_pagar_e_receber():
    response = client.get('/contas-a-pagar-e-receber/contas')

    print(response.json())

    assert response.status_code == 200

    assert response.json() == [
        {'descricao': 'aluguel', 'id': 1, 'tipo': 'pagar', 'valor': 1000.5},
        {'descricao': 'estagio', 'id': 2, 'tipo': 'receber', 'valor': 1500.5}
    ]


def test_deve_criar_contas_a_pagar_e_receber():
    nova_conta = {
        'descricao': 'teste',
        'valor': 233.32,
        'tipo': 'teste',
    }

    response = client.post('/contas-a-pagar-e-receber/contas', json=nova_conta)

    assert response.status_code == 201
