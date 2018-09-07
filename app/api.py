from flask import Flask, jsonify, request
from app import APP
from app.resources import orders


@APP.route('/orders', methods=['GET'])
def get_orders():
    '''
    Gets all the orders
    '''
    order_list = []
    for i in orders:
        order_list.append({'order_id': i['order_id'],
                           'order_content': i['order_content'],
                           'order_status': i['order_status']})
    return jsonify(order_list)


@APP.route('/orders/<int:order_id>', methods=['GET'])
def get_order_byid(order_id):
    '''
    Gets orders by a specific id
    '''
    if not any(i.get('order_id') == order_id for i in orders):
        return 'No such order exists', 404
    order = [i for i in orders if i.get('order_id') == order_id]
    return jsonify(order)


@APP.route('/orders', methods=['POST'])
def add_order():
    '''
    Adds an order to the list of orders
    '''
    data = request.get_json()
    order_id = data.get('order_id')
    order_content = data.get('order_content')
    user = data.get('user')
    order_status = data.get('order_status')
    if not any(i.get('order_id') == order_id for i in orders):
        orders.append({'order_id': order_id,
                       'order_content': order_content,
                       'user': user,
                       'order_status': order_status})
        return jsonify(orders)
    return 'Order already exists', 404

if __name__ == '__main__':
    APP.run(debug=True)
