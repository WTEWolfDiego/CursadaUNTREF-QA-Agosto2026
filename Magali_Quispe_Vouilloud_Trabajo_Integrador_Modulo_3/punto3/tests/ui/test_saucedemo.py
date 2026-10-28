from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_caso1_ordenar_por_precio(driver):
    LoginPage(driver).login()
    inventario = InventoryPage(driver)
    assert inventario.esta_cargada()

    inventario.ordenar_por("Price (low to high)")

    precios = inventario.obtener_precios()
    assert precios == sorted(precios)


def test_caso2_errores_en_checkout(driver):
    LoginPage(driver).login()
    inventario = InventoryPage(driver)

    nombres_esperados = inventario.obtener_nombres()
    cantidad = inventario.agregar_todos()
    assert inventario.cantidad_en_badge() == cantidad

    inventario.ir_al_carrito()
    carrito = CartPage(driver)
    assert carrito.esta_cargada()
    assert sorted(carrito.obtener_nombres()) == sorted(nombres_esperados)

    carrito.ir_al_checkout()
    checkout = CheckoutPage(driver)
    checkout.ingresar_nombre("Juan")
    checkout.continuar()
    assert checkout.obtener_error() == "Error: Last Name is required"

    checkout.ingresar_apellido("Pérez")
    checkout.continuar()
    assert checkout.obtener_error() == "Error: Postal Code is required"


def test_caso3_compra_completa(driver):
    LoginPage(driver).login()
    inventario = InventoryPage(driver)

    inventario.agregar_productos(1)
    inventario.ir_al_carrito()
    carrito = CartPage(driver)
    carrito.remover_primero()

    assert carrito.cantidad_items() == 0
    assert not carrito.tiene_badge()

    carrito.continuar_comprando()
    nombres_agregados = inventario.agregar_productos(2)

    inventario.ir_al_carrito()
    assert sorted(carrito.obtener_nombres()) == sorted(nombres_agregados)

    carrito.ir_al_checkout()
    checkout = CheckoutPage(driver)
    checkout.completar_datos("Juan", "Pérez", "1744")
    checkout.finalizar()

    assert checkout.obtener_mensaje_final() == "Thank you for your order!"
