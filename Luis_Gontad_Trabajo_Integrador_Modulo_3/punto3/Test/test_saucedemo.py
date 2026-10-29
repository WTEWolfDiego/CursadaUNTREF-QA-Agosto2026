# Diplomatura en Control de Calidad de Software - UNTREF
# Trabajo integrador Módulo 3
# Gontad Luis

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


# Caso 1: Login y ordenar precios de menor a mayor.
def test_caso_1(driver):
    login = LoginPage(driver)
    login.iniciar_sesion()

    inventario = InventoryPage(driver)
    
    inventario.ordenar_por("Price (low to high)")
    assert inventario.get_orden() == "Price (low to high)"

    precios = inventario.get_precios()
    assert precios == sorted(precios), f"Los precios no estan ordenados correctamente: {precios}"


# Caso 2: Login, agregar todos y validar checkout.
def test_caso_2(driver):
    login = LoginPage(driver)
    login.iniciar_sesion()

    inventario = InventoryPage(driver)


    productos = inventario.get_items()
    inventario.add_todos()
    assert inventario.get_cantidad_carrito() == len(productos)

    inventario.go_to_carrito()
    carrito = CartPage(driver)

    productos_en_carrito = carrito.get_nombres_producto()
    assert sorted(productos_en_carrito) == sorted(productos), (f"Error, los prodcutos no coinciden.\nProductos esperados: {productos}\nProductos en el carrito: {productos_en_carrito}")

    carrito.go_to_checkout()
    checkout = CheckoutPage(driver)

    checkout.ingresar_nombre("Luis")
    checkout.continuar()

    assert checkout.validar_campos() == "Error: Last Name is required"

    checkout.ingresar_apellido("Gontad")
    checkout.continuar()

    assert checkout.validar_campos() == "Error: Postal Code is required"

 
# Caso 3: Login, Agregar y quitar productos, volver y finalizar la compra.
def test_caso_3(driver):
    login = LoginPage(driver)
    login.iniciar_sesion()

    inventario = InventoryPage(driver)

    inventario.add_item("Sauce Labs Bike Light")
    assert inventario.get_cantidad_carrito() == 1

    inventario.go_to_carrito()
    carrito = CartPage(driver)

    carrito.remove_item("Sauce Labs Bike Light")

    assert carrito.get_nombres_producto() == [], "El carrito aún posee productos"
    assert carrito.get_cantidad_badge() == 0, "Cantidad en carrito es distinta de 0"

    carrito.click_seguir_comprando()

    productos = ["Sauce Labs Bolt T-Shirt", "Sauce Labs Backpack"]
    for producto in productos:
        inventario.add_item(producto)
    assert inventario.get_cantidad_carrito() == 2

    inventario.go_to_carrito()

    productos_en_carrito = carrito.get_nombres_producto()
    assert sorted(productos_en_carrito) == sorted(productos), (  f"Error, los prodcutos no coinciden.\nProductos esperados: {productos}\nProductos en el carrito: {productos_en_carrito}")

    carrito.go_to_checkout()
    checkout = CheckoutPage(driver)
    checkout.completar_campos("Luis", "Gontad", "1456")
    checkout.continuar()
    checkout.finalizar_compra()

    assert checkout.obtener_confirmacion() == "Thank you for your order!"