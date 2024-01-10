# This file is generated by the BAML compiler.
# Do not edit this file directly.
# Instead, edit the BAML files and recompile.

# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off

from ..types.classes.cls_detailedsentiment import DetailedSentiment
from typing import Protocol, runtime_checkable


import typing

import pytest
from contextlib import contextmanager
from unittest import mock

ImplName = typing.Literal["version1"]

T = typing.TypeVar("T", bound=typing.Callable[..., typing.Any])
CLS = typing.TypeVar("CLS", bound=type)


IGetDetailedSentimentOutput = DetailedSentiment

@runtime_checkable
class IGetDetailedSentiment(Protocol):
    """
    This is the interface for a function.

    Args:
        arg: str

    Returns:
        DetailedSentiment
    """

    async def __call__(self, arg: str, /) -> DetailedSentiment:
        ...


class BAMLGetDetailedSentimentImpl:
    async def run(self, arg: str, /) -> DetailedSentiment:
        ...

class IBAMLGetDetailedSentiment:
    def register_impl(
        self, name: ImplName
    ) -> typing.Callable[[IGetDetailedSentiment], IGetDetailedSentiment]:
        ...

    async def __call__(self, arg: str, /) -> DetailedSentiment:
        ...

    def get_impl(self, name: ImplName) -> BAMLGetDetailedSentimentImpl:
        ...

    @contextmanager
    def mock(self) -> typing.Generator[mock.AsyncMock, None, None]:
        """
        Utility for mocking the GetDetailedSentimentInterface.

        Usage:
            ```python
            # All implementations are mocked.

            async def test_logic() -> None:
                with baml.GetDetailedSentiment.mock() as mocked:
                    mocked.return_value = ...
                    result = await GetDetailedSentimentImpl(...)
                    assert mocked.called
            ```
        """
        ...

    @typing.overload
    def test(self, test_function: T) -> T:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the GetDetailedSentimentInterface.

        Args:
            test_function : T
                The test function to be decorated.

        Usage:
            ```python
            # All implementations will be tested.

            @baml.GetDetailedSentiment.test
            async def test_logic(GetDetailedSentimentImpl: IGetDetailedSentiment) -> None:
                result = await GetDetailedSentimentImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, *, exclude_impl: typing.Iterable[ImplName]) -> pytest.MarkDecorator:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the GetDetailedSentimentInterface.

        Args:
            exclude_impl : Iterable[ImplName]
                The names of the implementations to exclude from testing.

        Usage:
            ```python
            # All implementations except "version1" will be tested.

            @baml.GetDetailedSentiment.test(exclude_impl=["version1"])
            async def test_logic(GetDetailedSentimentImpl: IGetDetailedSentiment) -> None:
                result = await GetDetailedSentimentImpl(...)
            ```
        """
        ...

    @typing.overload
    def test(self, test_class: typing.Type[CLS]) -> typing.Type[CLS]:
        """
        Provides a pytest.mark.parametrize decorator to facilitate testing different implementations of
        the GetDetailedSentimentInterface.

        Args:
            test_class : Type[CLS]
                The test class to be decorated.

        Usage:
        ```python
        # All implementations will be tested in every test method.

        @baml.GetDetailedSentiment.test
        class TestClass:
            def test_a(self, GetDetailedSentimentImpl: IGetDetailedSentiment) -> None:
                ...
            def test_b(self, GetDetailedSentimentImpl: IGetDetailedSentiment) -> None:
                ...
        ```
        """
        ...

BAMLGetDetailedSentiment: IBAMLGetDetailedSentiment