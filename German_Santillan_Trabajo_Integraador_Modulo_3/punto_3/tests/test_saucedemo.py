# UNTREF Universidad Nacional de Tres de Febrero
# Diplomatura en Control de Calidad de Software
# Trabajo integrador Módulo 3 - Punto 3
# Automatización de los tres casos de prueba de SauceDemo.
# Alumno: Germán Santillán.

# Importamos pytest para clasificar los tests y las clases reutilizables.
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


# Caso 1: Login y ordenamiento de precios de menor a mayor.
@pytest.mark.ui
@pytest.mark.caso1
def test_caso_1_ordenar_productos_precio_ascendente(driver):

    # Iniciamos sesión con el usuario estándar.
    LoginPage(driver).iniciar_sesion()
    inventario = InventoryPage(driver)

    # Ordenamos los productos por precio de menor a mayor.
    inventario.ordenar_por_precio_ascendente()

    # Obtenemos los precios en el orden visible y verificamos que no esté vacío.
    precios = inventario.obtener_precios()
    assert len(precios) > 0, "No se encontraron precios para validar."

    # Comparamos el orden real con una copia ordenada usando sorted().
    assert precios == sorted(precios), f"Los precios no están ordenados: {precios}"


# Caso 2: Agregar todos los productos y validar los errores del checkout.
@pytest.mark.ui
def test_caso_2_todos_los_productos_y_validaciones_checkout(driver):

    # Iniciamos sesión y obtenemos los nombres del catálogo.
    LoginPage(driver).iniciar_sesion()
    inventario = InventoryPage(driver)
    productos_esperados = inventario.agregar_todos_los_productos()

    # Abrimos el carrito y verificamos que estén todos los productos agregados.
    inventario.abrir_carrito()
    carrito = CartPage(driver)
    productos_en_carrito = carrito.obtener_nombres_productos()
    assert sorted(productos_en_carrito) == sorted(productos_esperados)

    # Ingresamos al checkout y completamos solamente el nombre.
    carrito.iniciar_checkout()
    checkout = CheckoutPage(driver)
    checkout.ingresar_nombre("German")
    checkout.continuar()

    # Validamos el mensaje exacto de apellido obligatorio.
    assert checkout.obtener_mensaje_error() == "Error: Last Name is required"

    # Completamos el apellido, volvemos a continuar y verificamos el código postal.
    checkout.ingresar_apellido("Santillan")
    checkout.continuar()
    assert checkout.obtener_mensaje_error() == "Error: Postal Code is required"


# Caso 3: Agregar y quitar productos, volver al catálogo y finalizar compra.
@pytest.mark.ui
def test_caso_3_quitar_producto_y_finalizar_compra(driver):

    # Iniciamos sesión y agregamos un producto al carrito.
    LoginPage(driver).iniciar_sesion()
    inventario = InventoryPage(driver)
    inventario.agregar_primeros_productos(1)
    inventario.abrir_carrito()

    # Quitamos el producto y validamos que el carrito quede vacío.
    carrito = CartPage(driver)
    carrito.quitar_primer_producto()
    assert len(carrito.obtener_nombres_productos()) == 0, "El carrito no está vacío."

    # Volvemos al catálogo y agregamos dos productos.
    carrito.continuar_comprando()
    productos_esperados = inventario.agregar_primeros_productos(2)
    inventario.abrir_carrito()

    # Validamos que exactamente los dos productos elegidos estén presentes.
    productos_en_carrito = carrito.obtener_nombres_productos()
    assert sorted(productos_en_carrito) == sorted(productos_esperados)

    # Completamos todos los datos necesarios para avanzar al resumen.
    carrito.iniciar_checkout()
    checkout = CheckoutPage(driver)
    checkout.ingresar_nombre("German")
    checkout.ingresar_apellido("Santillan")
    checkout.ingresar_codigo_postal("1000")
    checkout.continuar()

    # Finalizamos la compra y verificamos el mensaje de éxito.
    mensaje_final = checkout.finalizar_compra()
    assert mensaje_final == "Thank you for your order!"
