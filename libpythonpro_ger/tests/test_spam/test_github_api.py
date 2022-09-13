from unittest.mock import Mock

import pytest

from libpythonpro_ger import github_api

@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/105610168?v=4'
    resp_mock.json.return_value = {
        'login': 'GermanUngo', 'id': 105610168,
        'node_id': 'U_kgDOBkt7uA', 'avatar_url': url, }
    get_mock = mocker.patch('libpythonpro_ger.github_api.requests.get')
    get_mock.return_value=resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('GermanUngo')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('GermanUngo')
    assert 'https://avatars.githubusercontent.com/u/105610168?v=4' == url