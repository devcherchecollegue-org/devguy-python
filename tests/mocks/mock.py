from typing import Any


class Mock:
    class MockData:
        def __init__(self, return_value: Any = None, raises: Any = None):
            self.return_values = return_value
            self.raises = raises

        def returns(self) -> Any:
            if self.raises:
                raise self.raises
            return self.return_values


    class UnexpectedMethod(Exception):
        def __init__(self, method: str = "undefined"):
            self.message = f'Method {method} was not expected'


    class UnexpectedArguments(Exception):
        def __init__(self, method: str = "undefined", **kwargs):
            self.message = f'Method {method} did not expected to be called with {kwargs}'


    __returns = {}

    @classmethod
    def on(cls, method: str, return_value: Any = None, raises: Any = None, **kwargs):
        """
        Set return or raises value for provided methods
        """
        if method not in cls.__returns:
            cls.__returns[method] = []

        cls.__returns[method].append((kwargs, cls.MockData(return_value, raises)))

    @classmethod
    def reset(cls):
        """
        Reset mock data to avoid border effects
        """
        cls.__returns = {}

    @classmethod
    def __mocked_data(cls, method: str, kwargs: dict) -> MockData:
        if method not in cls.__returns:
            raise cls.UnexpectedMethod(method)

        known_mocks = cls.__returns[method]

        for key, data in known_mocks:
            if key == kwargs:
                return data

        raise cls.UnexpectedMethod(method)

    @classmethod
    def returns(cls, method: str, **kwargs) -> Any:
        data = cls.__mocked_data(method, kwargs)
        return data.returns()
