import pytest
from src.sub import sub_func


@pytest.mark.parametrize(
    ["text", "expected"],  # 변수명을 목록형태로 지정
    [
        pytest.param(
            "test1",
            "sub_func: test1",
            id="test1",  # 위에서 지정한 순서대로 변수지정
        ),
        pytest.param("test2", "sub_func: test2", id="test2"),
    ],
)
def test_sub_func(text: str, expected: str) -> None:
    """sub_func테스트
    parametrize를 사용하여 하나의 로직으로 여러 개의 테스트 케이스를 정의할 수 있음
    """
    assert sub_func(text) == expected
