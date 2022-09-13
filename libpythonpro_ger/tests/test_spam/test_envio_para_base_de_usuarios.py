import pytest
from unittest.mock import Mock
from libpythonpro_ger.spam.modelos import Usuario
from libpythonpro_ger.spam.main import EnviadorDeSpam
from libpythonpro_ger.spam.enviador_de_email import Enviador


@pytest.mark.parametrize('usuarios', [[Usuario(nome='German', email='germanungo@gmail.com'),
                                       Usuario(nome='Sissi', email='sissiventurin@gmail.com')],
                                      [Usuario(nome='German', email='germanungo@gmail.com')]])
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'germanungo@gmail.com',
        'Curso DevPro',
        'Confira meus projetos no GitHub')
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='German', email='germanungo@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'sissiventurin@gmail.com',
        'Curso DevPro',
        'Confira meus projetos no GitHub')
    enviador.enviar.assert_called_once_with(
        'sissiventurin@gmail.com',
        'germanungo@gmail.com',
        'Curso DevPro',
        'Confira meus projetos no GitHub')
