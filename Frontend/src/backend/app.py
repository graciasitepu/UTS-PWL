from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import json

# Inisialisasi data produk
products = [
    {
        "id": 1,
        "name": "Product 1",
        "price": 10.0,
        "stock": 100,
        "img": "product1.jpg"
    },
    {
        "id": 2,
        "name": "Product 2",
        "price": 20.0,
        "stock": 50,
        "img": "product2.jpg"
    }
]

# Route untuk mendapatkan daftar produk
def get_products(request):
    return Response(json.dumps(products))

# Route untuk menambahkan produk
def add_product(request):
    data = json.loads(request.body)
    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"],
        "stock": data["stock"],
        "img": data["img"]
    }
    products.append(new_product)
    return Response(json.dumps(new_product))

# Konfigurasi aplikasi Pyramid
with Configurator() as config:
    config.add_route('get_products', '/get_products')
    config.add_view(get_products, route_name='get_products', renderer='json')

    config.add_route('add_product', '/add_product')
    config.add_view(add_product, route_name='add_product', renderer='json', request_method='POST')

    app = config.make_wsgi_app()

# Buat server WSGI
if __name__ == '__main__':
    server = make_server('0.0.0.0', 8000, app)
    print('Pyramid backend berjalan di http://0.0.0.0:8000')
    server.serve_forever()
