def test_input_length():
    user_input = input()
    expected_length_max_value = 14
    actual_length = len(user_input)
    assert actual_length <= expected_length_max_value, f"Input length is {actual_length}, expected maximum value is {expected_length_max_value}"