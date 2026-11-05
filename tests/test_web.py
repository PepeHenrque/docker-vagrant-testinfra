
# Fase 6 - Testes automatizados com Testinfra

def test_apache_instalado(host):
    pacote = host.package("apache2")
    assert pacote.is_installed


def test_apache_ativo(host):
    servico = host.service("apache2")
    assert servico.is_running


def test_apache_habilitado(host):
    servico = host.service("apache2")
    assert servico.is_enabled


def test_porta_http(host):
    porta = host.socket("tcp://80")
    assert porta.is_listening


def test_pagina_inicial(host):
    pagina = host.file("/var/www/html/index.html")
    assert pagina.exists
    assert pagina.is_file


def test_conteudo_html(host):
    pagina = host.file("/var/www/html/index.html")
    assert "Grupo 9 - Testinfra Lab" in pagina.content_string
    assert "Servidor provisionado com Ansible" in pagina.content_string
