from unittest.mock import Mock


my_mock = Mock()
my_mock.__str__ = Mock(return_value='Mocking')
print(str(my_mock))