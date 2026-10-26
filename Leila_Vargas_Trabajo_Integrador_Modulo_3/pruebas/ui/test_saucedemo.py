from paginas.catalogo import Catalogo
from paginas.carrito import Carrito
from paginas.checkout import Checkout


def test_caso1_orden_por_precio_ascendente(sesion_iniciada):
    catalogo = Catalogo(sesion_iniciada)
    assert catalogo.titulo_es("Products")

    catalogo.ordenar("Price (low to high)")

    assert catalogo.criterio_actual() == "Price (low to high)"
    precios = catalogo.lista_precios()
    assert precios, "La pagina no muestra productos"
    assert all(precios[i] <= precios[i + 1] for i in range(len(precios) - 1)), (
        f"Los precios no quedaron de menor a mayor: {precios}"
    )


def test_caso2_campos_obligatorios_en_checkout(sesion_iniciada):
    catalogo = Catalogo(sesion_iniciada)
    assert catalogo.titulo_es("Products")
    todos = catalogo.lista_productos()

    catalogo.agregar_todo()
    assert catalogo.carrito_tiene(len(todos))

    catalogo.abrir_carrito()
    carrito = Carrito(sesion_iniciada)
    assert carrito.titulo_es("Your Cart")
    assert set(carrito.productos()) == set(todos)

    carrito.ir_a_checkout()
    checkout = Checkout(sesion_iniciada)
    assert checkout.titulo_es("Checkout: Your Information")

    checkout.completar(nombre="Leila")
    checkout.continuar()
    assert checkout.mensaje_error() == "Error: Last Name is required"

    checkout.completar(apellido="Vargas")
    checkout.continuar()
    assert checkout.mensaje_error() == "Error: Postal Code is required"


def test_caso3_quitar_producto_y_comprar(sesion_iniciada):
    catalogo = Catalogo(sesion_iniciada)
    assert catalogo.titulo_es("Products")

    catalogo.agregar("Sauce Labs Fleece Jacket")
    catalogo.abrir_carrito()

    carrito = Carrito(sesion_iniciada)
    assert carrito.titulo_es("Your Cart")
    carrito.quitar("Sauce Labs Fleece Jacket")
    assert carrito.productos() == []
    assert carrito.carrito_tiene(0)

    carrito.seguir_comprando()
    assert catalogo.titulo_es("Products")

    elegidos = ["Sauce Labs Onesie", "Sauce Labs Backpack"]
    for producto in elegidos:
        catalogo.agregar(producto)
    assert catalogo.carrito_tiene(len(elegidos))

    catalogo.abrir_carrito()
    assert set(carrito.productos()) == set(elegidos)

    carrito.ir_a_checkout()
    checkout = Checkout(sesion_iniciada)
    checkout.completar(nombre="Leila", apellido="Vargas", codigo_postal="1406")
    checkout.continuar()
    assert checkout.titulo_es("Checkout: Overview")

    checkout.finalizar()
    assert checkout.titulo_es("Checkout: Complete!")
    assert checkout.mensaje_final() == "Thank you for your order!"
