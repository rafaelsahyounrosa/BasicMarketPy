from typing import List, Dict
from time import sleep

from models.products import Product
from utils.helper import format_float_str_currency

products: List[Product] = []
cart: List[Dict[Product, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('='.center(100, "="))
    print(' Welcome! '.center(100, "="))
    print(" Rafael's Market ".center(100, '='))
    print('='.center(100, "="))

    print('Select one of the followings options bellow: ')
    print('1 - Register a product')
    print('2 - List a product')
    print('3 - Buy a product')
    print('4 - View cart')
    print('5 - Close order')
    print('6 - Exit system')

    option: int = int(input('Inform the option: \n'))

    if option == 1:
        register_product()
    elif option == 2:
        list_products()
    elif option == 3:
        buy_products()
    elif option == 4:
        view_cart()
    elif option == 5:
        close_order()
    elif option == 6:
        print('Thank you! See you soon :P')
        sleep(2)
        exit(0)
    else:
        print('Sorry, this is not a valid option. Please choose it again.')
        sleep(1)
        menu()


def register_product() -> None:
    print('Product registration\n')
    name: str = input("Please inform the product's name: ")
    price: float = float(input("Please inform the product's price: "))

    product: Product = Product(name, price)

    products.append(product)

    print(f'{product.name.title()} registered with success!')
    sleep(2)
    menu()


def list_products() -> None:
    if len(products) > 0:
        print('Products list\n')
        for product in products:
            print(f'- {product}\n')
            sleep(1)
    else:
        print('No products registered yet.')
    sleep(2)
    menu()


def buy_products() -> None:
    if len(products) > 0:
        print('Inform the ID of the product that you want to buy: ')
        print('='.center(100, '='))
        print('Available Products'.center(100, '='))
        for product in products:
            print(product)
            print('-'.center(100, '-'))
            sleep(1)
        product_id: int = int(input())

        product: Product = take_product_by_code(product_id)

        if product:
            if len(cart) > 0:
                cart_check: bool = False
                for item in cart:
                    amount: int = item.get(product)
                    if amount:
                        item[product] = amount + 1
                        print(f'Now you have {amount + 1} unity(s) of {product.name} in your cart.')
                        cart_check = True
                        sleep(2)
                        menu()
                if not cart_check:
                    prod = {product: 1}
                    cart.append(prod)
                    print(f'{product.name.title()} added to cart.')
                    sleep(2)
                    menu()

            else:
                item = {product: 1}
                cart.append(item)
                print(f'{product.name.title()} added to cart.')
                sleep(2)
                menu()
        else:
            print(f'The product with the {product_id} id was not found.')
            sleep(2)
            menu()

    else:
        print('No products to sell yet')
    sleep(2)
    menu()


def view_cart() -> None:
    if len(cart) > 0:
        print('Products in cart: ')

        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Amount: {data[1]}\n')
                sleep(1)
    else:
        print('You have 0 products in your cart.')
    sleep(2)
    menu()


def close_order() -> None:
    if len(cart) > 0:
        total_value: float = 0

        print('Products in cart')
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f'Amount: {data[1]}')
                total_value += data[0].price * data[1]
                print('\n')
                sleep(1)
        print(f'Your bills is: {format_float_str_currency(total_value)}')
        print('Thank you for your custom. See you on next time.')
        cart.clear()
        sleep(5)
    else:
        print('The cart is empty.')
    sleep(2)
    menu()


def take_product_by_code(product_id: int) -> Product:
    p: Product = None

    for product in products:
        if product.product_id == product_id:
            p = product
    return p


if __name__ == '__main__':
    main()
