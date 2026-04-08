from service import get_hello_message

def test_get_hello_message_returns_dict_with_message():
    result = get_hello_message()
    assert result == {"message": "Hello, world!"}
