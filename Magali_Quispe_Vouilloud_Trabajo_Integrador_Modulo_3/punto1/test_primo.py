from primo import es_primo


def test_numero_primo():
    assert es_primo(7) is True


def test_numero_no_primo():
    assert es_primo(10) is False


def test_uno_no_es_primo():
    assert es_primo(1) is False
