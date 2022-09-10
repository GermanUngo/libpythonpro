from libpythonpro_ger.spam.main import EnviadorDeSpam
from libpythonpro_ger.spam.enviador_de_email import Enviador


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'germanungo2gmail.com',
        'Curso DevPro',
        'Confira meus projetos no GitHub'
    )