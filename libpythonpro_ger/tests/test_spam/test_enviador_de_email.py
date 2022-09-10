import pytest

from libpythonpro_ger.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['germanungo@gmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'sissiventurin@gmail.com',
        'Curso DevPro',
        'Link do GitHub com Projetos Python')

    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['germanungogmail.com', '']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'sissiventurin@gmail.com',
            'Curso DevPro',
            'Link do GitHub com Projetos Python')
