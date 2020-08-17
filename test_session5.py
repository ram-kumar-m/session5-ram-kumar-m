import session5 as main
import pytest
import random
import os
import inspect
import re
import math
import timeit


README_CONTENT_CHECK_FOR = [
    'time_it',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
    ]

CHECK_FOR_THINGS_NOT_ALLOWED = []


def test_timeit_for_uncallable_func():
    x = 0
    with pytest.raises(TypeError):
        main.time_it(x)


def test_print_func(capsys):
    main.time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitons=6)
    expected_print_out = '1-2-3 ***\n'*6
    out, err = capsys.readouterr()
    assert out == expected_print_out and err == '', f'When you print the bible, atleast do it right!'

# def test_time_it_vs_timeit():
#     our_timeit_time = main.time_it(print, 1, 2, 3, sep='-', end= ' ***', repetitons=6)
#     stmt = '''print( 1, 2, 3, sep='-', end=' ***')'''
#     inbuit_method_time = timeit.timeit(stmt,number=6)
#     assert math.isclose(inbuit_method_time, our_timeit_time) == True


def test_squared_power_list():
    num = random.randint(-100, 100)
    start = random.randint(-10, 40)
    end = start + 20
    assert main.time_it(main.squared_power_list, num, start=start, end=end, repetitons=1)[0] == \
        [num**i for i in range(start, end+1)]


def test_squared_power_list_invalid_base():
    with pytest.raises(ValueError):
        main.squared_power_list('1', 1, 0)


def test_squared_power_list_invalid_powers():
    start = random.uniform(40, 100)
    end = start+10
    with pytest.raises(ValueError):
        main.squared_power_list(5, start, end)


def test_squared_power_list_very_large_base():
    num = random.randint(110, 1000)
    with pytest.raises(ValueError):
        main.squared_power_list(num, 1, 0)


def test_squared_power_list_power_range_too_large():
    start = random.randint(0, 40)
    end = start+45
    print(start, end)
    with pytest.raises(ValueError):
        main.squared_power_list(2, start, end)


def test_polygon_area():
    sides = random.randint(3, 6)
    len_side = random.randint(0, 1000)
    assert main.polygon_area(len_side, sides) == (
        len_side ** 2) * sides / (4 * math.tan(math.pi / sides))


def test_polygon_area_neg_side():
    with pytest.raises(ValueError):
        main.polygon_area(random.randint(-100, -1), 10)


def test_polygon_area_non_integer_side():
    with pytest.raises(ValueError):
        main.polygon_area(10, float(10))


def test_polygon_area_invalid_side_range():
    with pytest.raises(ValueError):
        main.polygon_area(random.randint(-100, 1), 10)
        main.polygon_area(random.randint(8, 100), 10)


def test_temp_converter_test_invalid_unit():
    with pytest.raises(ValueError):
        main.temp_converter(random.randint(0, 100), 'a')


def test_temp_converter_test_invalid_range_c():
    with pytest.raises(ValueError):
        main.temp_converter(random.randint(-273.15, -500), 'c')


def test_temp_converter_test_invalid_range_f():
    with pytest.raises(ValueError):
        main.temp_converter(random.randint(-460, -500), 'f')


def test_temp_converter_test_invalid_range_k():
    with pytest.raises(ValueError):
        main.temp_converter(random.randint(0, -500), 'k')


def test_temp_converter_test_c():
    assert main.temp_converter(100, 'c') == '212.0 in F or 373.15 in K'


def test_temp_converter_test_f():
    assert main.temp_converter(212, 'f') == '100.0 in C or 373.15 in K'


def test_temp_converter_test_k():
    assert main.temp_converter(373.15, 'k') == '100.0 in C or 212.0 in F'


def test_speed_converter_invalid_dist_unit():
    with pytest.raises(ValueError):
        main.speed_converter(10, 'k', 's')


def test_speed_converter_invalid_time_unit():
    with pytest.raises(ValueError):
        main.speed_converter(10, 'km', 'ss')


def test_speed_converter_neg_speed():
    with pytest.raises(ValueError):
        main.speed_converter(-10, 'km', 's')


def test_speed_converter_into_mps():
    assert main.speed_converter(18, 'm', 's') == 5


def test_speed_converter_into_mpm():
    assert main.speed_converter(18, 'm', 'min') == 5*60


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(main)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(
            r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(main, inspect.isfunction)
    for function in functions:
        assert len(re.findall(
            '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
