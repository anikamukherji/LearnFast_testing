def test_sum_list():
    """
    Tests the sum_list function of the list_module
    """
    try:
        import pytest
        from list_module import list_things 
        from list_modules import custom_list_error
    except ImportError as e:
        print("Necessary imports failed: {}".format(e))
        return
    test_object = ListThing()
    test_data = ([1, 1, 1, 1], [0, 0], [5, -1, -10], [-9, -4],
                 [1000, 2000, -1])
    test_answers = ([4, 0, -6, -13, 2999])
    for (example, ans) in zip(test_data, test_answers):
        test_object.the_list = example
        assert test_object.sum_list() == ans
    test_type_fails = ("BME", 590, 3.0)
    for type_fail in test_type_fails:
        assert sum_list(type_fail) is None
    with pytest.raises(EmptyError):
        test_object.the_list = []
        test_object.sum_list()
    with pytest.raises(InfinityError):
        sum_list([float('inf'), 2])
    with pytest.raises(InfinityError):
        sum_list([float('-inf'), 3.0])
