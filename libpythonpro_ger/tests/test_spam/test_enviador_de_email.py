from libpythonpro_ger.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

def test_remetente():
    enviador = Enviador()
    enviador.enviar(
        'germanungo@gmail.com',
    'sissiventurin@gmail.com',
    'Curso DevPro',
    'Link do GitHub com Projetos Python')