def test_max_difference():
    """
    To test the max_difference function in the list_module
    """
    try:
        import pytest
        from list_module.list_thing import ListThing
        from custom_list_error import EmptyError, InfinityError
    except ImportError as e:
        print("Necessary imports failed: {}".format(e))
        return
    test_object = ListThing([])
    test_data = ([0, -3, -1, 10], [1, 3, 2, 5], [-1.5, -9, -3, -7, -1])
    test_answers = (11, 3, 7.5)
    for test, ans in zip(test_data, test_answers):
        test_object.the_list = test
        test_object.max_difference()
        assert test_object.max_diff == ans
    test_type_fails = [5, 'abc', {1: 4}]
    for type_fail in test_type_fails:
        with pytest.raises(TypeError):
            test_object.the_list = type_fail
    infinity_fails = (['-inf', 5], ['-inf', 5], [float('-inf'), 5],
                      [float('-inf'), 5])
    for test in infinity_fails:
        with pytest.raises(InfinityError):
            test_object.the_list = infinity_fail
            test_object.max_difference()
    test_value_fails = (['s', 8], [1.0, {6: 'a'}], [8, None])
    for test in test_value_fails:
        test_object.the_list = test
        test_object.max_difference()
        assert test_object.max_difference is None
