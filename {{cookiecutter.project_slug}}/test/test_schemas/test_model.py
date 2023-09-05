import pytest
from pydantic import ValidationError
from {{cookiecutter.project_slug}}.schemas.model import SumRequest, DiffRequest


@pytest.mark.parametrize("data, model_cls", [
    ({"a": 10, "b": 20}, SumRequest),
    ({"a": 5, "b": 15}, SumRequest),
    ({"a": 0, "b": 0}, SumRequest),
])
def test_valid_input(data, model_cls):
    assert model_cls(**data)

@pytest.mark.parametrize("data, model_cls", [
    ({"a": 10}, SumRequest),  # Missing 'b' field
    ({"b": 20}, SumRequest),  # Missing 'a' field
    ({"a": "invalid", "b": 20}, SumRequest),  # Invalid data type for 'a'
    ({"a": 10, "b": "invalid"}, SumRequest),  # Invalid data type for 'b'
])
def test_invalid_input(data, model_cls):
    with pytest.raises(ValidationError):
        model_cls(**data)

@pytest.mark.parametrize("data, model_cls", [
    ({"a": 10, "b": 5}, DiffRequest),
    ({"a": 5, "b": 15}, DiffRequest),
    ({"a": 0, "b": 0}, DiffRequest),
])
def test_valid_diff_request(data, model_cls):
    assert model_cls(**data)

@pytest.mark.parametrize("data, model_cls", [
    ({"a": 10}, DiffRequest),  # Missing 'b' field
    ({"b": 20}, DiffRequest),  # Missing 'a' field
    ({"a": "invalid", "b": 20}, DiffRequest),  # Invalid data type for 'a'
    ({"a": 10, "b": "invalid"}, DiffRequest),  # Invalid data type for 'b'
])
def test_invalid_diff_request(data, model_cls):
    with pytest.raises(ValidationError):
        model_cls(**data)
