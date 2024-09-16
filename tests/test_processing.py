import pytest

from src.processing import filter_by_state, sort_by_date



@pytest.mark.parametrize(
    "fixture_name, state_val, expected_output",
    [
        ("list_transactions1", "EXECUTED", [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]),
        ("list_transactions2", "CANCELED", [
            {"id": 112233445, "state": "CANCELED", "date": "2021-01-30T18:35:29.512364"},
            {"id": 666555443, "state": "CANCELED", "date": "2018-09-12T21:30:00.241689"},
        ]),
        ("list_transactions_same_state", "CANCELED", [
        ]),
    ]
)
def test_filter_by_state(request, fixture_name, state_val, expected_output):
    input_list = request.getfixturevalue(fixture_name)
    assert filter_by_state(input_list, state_val) == expected_output


@pytest.mark.parametrize(
    "fixture_name, sort_order, expected_output",
    [
        ("list_transactions1", False, [
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        ]),
        ("list_transactions2", True, [
            {"id": 112233445, "state": "CANCELED", "date": "2021-01-30T18:35:29.512364"},
            {"id": 666555443, "state": "CANCELED", "date": "2018-09-12T21:30:00.241689"},
            {"id": 322211344, "state": "EXECUTED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 343455333, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]),
    ]
)
def test_sort_by_date(request, fixture_name, sort_order, expected_output):
    input_list = request.getfixturevalue(fixture_name)
    assert sort_by_date(input_list, sort_order) == expected_output


@pytest.mark.parametrize(
    "fixture_name, sort_order, expected_exception",
    [
        ("list_transactions_invalid_dates", True, ValueError)
    ]
)
def test_sort_by_date_invalid_formats(request, fixture_name, sort_order, expected_exception):
    input_list = request.getfixturevalue(fixture_name)
    with pytest.raises(expected_exception):
        sort_by_date(input_list, sort_order)