import pytest

def test_get_report_service(client, create_orders, report_uri):
    
    response = client.get(report_uri)
    pytest.assume(response.status.startswith('200'))
    
    report_response = response.json

    assert type(report_response['popular_ingredient'][0]) == str
    assert type(report_response['popular_ingredient'][1]) == int
    assert type(report_response['wealthy_month'][0]) == str
    assert type(report_response['wealthy_month'][1]) == float
    assert len(report_response['top_customers']) == 3
