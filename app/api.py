from flask import Flask, jsonify, request
from .resources import resources
APP = Flask(__name__)
APP.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


@APP.route('/orders/<int:order_id>', methods=['PUT'])
def update_status(order_id):
    '''
    Update the status of a particular order
    '''
    data = request.get_json()
    status = data.get('status')
    if not any(i.get('order_id') == order_id for i in resources.orders):
        return 'Order does not exist', 404
    for i in resources.orders:
        if i.get('order_id') == order_id:
            i['order_status'] = status
    return jsonify(resources.orders)


if __name__ == '__main__':
    APP.run(debug=True)
