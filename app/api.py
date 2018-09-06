from flask import Flask, jsonify, request
from resources import *
APP = Flask(__name__)
APP.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@APP.route('/orders', methods=['GET'])
def get_orders():
    '''
    Gets all the orders
    '''
    if not isinstance(orders, list):
        raise TypeError('Orders seem to be broken')
    elif not orders:
        return 'No new orders!'
    else:
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

if __name__ == '__main__':
    APP.run(debug=True)
