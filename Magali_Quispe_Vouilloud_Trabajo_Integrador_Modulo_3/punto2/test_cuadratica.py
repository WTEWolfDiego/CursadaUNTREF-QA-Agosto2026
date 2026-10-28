import pytest

from cuadratica import resolver_cuadratica


def test_dos_soluciones():
    raices = resolver_cuadratica(1, -5, 6)
    assert len(raices) == 2
    assert sorted(raices) == [2, 3]


def test_una_solucion():
    raices = resolver_cuadratica(1, -4, 4)
    assert raices == [2]


def test_sin_solucion():
    raices = resolver_cuadratica(1, 1, 1)
    assert raices == []


def test_a_igual_a_cero():
    with pytest.raises(ValueError):
        resolver_cuadratica(0, 2, 1)
