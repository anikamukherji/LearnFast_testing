def test_min_max_list():
    """
    Tests the min_max_list function
    """
    try:
        import pytest
        from list_module.list_thing import ListThing
        from custom_list_error import EmptyError, InfinityError
    except ImportError as e:
        print("Necessary imports failed: {}".format(e))
        return
    test_object = ListThing([])
    test_data = ([0, -3, -1.2, 10], [1, 3, 2, 5], [-3/2, -9, -3, -7, -1])
    test_answers = ((-3, 10), (1, 5), (-9, -1))
    for test, ans in zip(test_data, test_answers):
        test_object.the_list = test
        test_object.min_max_list()
        assert test_object.min_max == ans
    test_type_fails = [5, 'abc', {1: 4}]
    for type_fail in test_type_fails:
        with pytest.raises(TypeError):
            test_object.the_list = type_fail
    infinity_fails = (['-inf', 5], ['-inf', 5], [float('-inf'), 5],
                      [float('-inf'), 5])
    for test in infinity_fails:
        with pytest.raises(InfinityError):
            test_object.the_list = infinity_fail
            test_object.min_max_list()
    test_value_fails = (['s', 8], [1.0, {6: 'a'}], [8, None])
    for test in test_value_fails:
        test_object.the_list = test
        test_object.min_max_list()
        assert test_object.min_max == (None, None)
