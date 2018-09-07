from flask import Flask, jsonify, request
from app import APP
from app.resources import orders


@APP.route('/orders/<int:order_id>', methods=['PUT'])
def update_status(order_id):
    '''
    Update the status of a particular order
    '''
    data = request.get_json()
    status = data.get('order_status')
    if not any(i.get('order_id') == order_id for i in orders):
        return 'Order does not exist', 404
    for i in orders:
        if i.get('order_id') == order_id:
            i['order_status'] = status
    return jsonify(orders)


if __name__ == '__main__':
    APP.run(debug=True)
