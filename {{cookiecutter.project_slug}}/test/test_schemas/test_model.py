import pytest
from pydantic import ValidationError

from {{cookiecutter.project_slug}}.schemas.model import DiffRequest, SumRequest


@pytest.mark.parametrize(
    "data, model_cls",
    [
        ({"a": 10, "b": 20}, SumRequest),
        ({"a": 5, "b": 15}, SumRequest),
        ({"a": 0, "b": 0}, SumRequest),
    ],
)
def test_valid_input(data, model_cls):
    assert model_cls(**data)


@pytest.mark.parametrize(
    "data, model_cls",
    [
        ({"a": 10}, SumRequest),
        ({"b": 20}, SumRequest),
        ({"a": "invalid", "b": 20}, SumRequest),
        ({"a": 10, "b": "invalid"}, SumRequest),
    ],
)
def test_invalid_input(data, model_cls):
    with pytest.raises(ValidationError):
        model_cls(**data)


@pytest.mark.parametrize(
    "data, model_cls",
    [
        ({"a": 10, "b": 5}, DiffRequest),
        ({"a": 5, "b": 15}, DiffRequest),
        ({"a": 0, "b": 0}, DiffRequest),
    ],
)
def test_valid_diff_request(data, model_cls):
    assert model_cls(**data)


@pytest.mark.parametrize(
    "data, model_cls",
    [
        ({"a": 10}, DiffRequest),
        ({"b": 20}, DiffRequest),
        ({"a": "invalid", "b": 20}, DiffRequest),
        ({"a": 10, "b": "invalid"}, DiffRequest),
    ],
)
def test_invalid_diff_request(data, model_cls):
    with pytest.raises(ValidationError):
        model_cls(**data)
