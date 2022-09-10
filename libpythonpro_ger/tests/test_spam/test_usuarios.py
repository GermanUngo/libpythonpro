from libpythonpro_ger.spam.modelos import Usuario
from libpythonpro_ger.spam.db import Conexao


def test_salvar_usuario(sessao):
    usuario = Usuario(nome ='German')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='German'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

