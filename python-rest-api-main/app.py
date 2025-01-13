from gc import is_finalized

from flask import Flask, request, jsonify

from eshop.data_access.product_repo import Product, get_all

from eshop.data_access.product_repo import get_by_id, save

products = []
app =Flask(__name__)



@app.route('/products', methods=["POST"])
def create_product():
    product_json = request.get_json()
    product = Product(product_json["id"], product_json["name"], product_json["price"])
    save(product)
    return jsonify({"response": "success"})


@app.route("/products")
def get_products():
    product = get_all()
    return jsonify(product)



@app.route("/product/<id>")
def get_product_by_id(id):
    product = get_by_id(id)
    if product is None:
        return jsonify({"error": f"Product with id {id} not found"}), 404
    return jsonify(product.to_dict())


if __name__ == ("__main__"):
    app.run(debug=True)

