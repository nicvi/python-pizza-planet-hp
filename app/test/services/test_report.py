import pytest

def test_get_report_service(client, create_orders, order_uri):
    response = client.get(order_uri)
    pytest.assume(response.status.startswith('200'))
    returned_clients = {order['_id']: order['client_name'] for order in response.json}
    returned_dates = {order['_id']: order['date'] for order in response.json}
    returned_ingredients = {order['_id']: order['detail'] for order in response.json}

    for order in create_orders:
        pytest.assume(order['client_name'] == returned_clients[order['_id']])
    
    for order in create_orders:
        pytest.assume(order['date'] == returned_dates[order['_id']])

    for order in create_orders:
        pytest.assume(order['detail'] == returned_ingredients[order['_id']])
