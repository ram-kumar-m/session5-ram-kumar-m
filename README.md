# Assignment 5

## Major Functions
<br/>

### __time_it__
This function is an attempt to manually write a `timeit` which comes inbuilt with Python.
It takes a function as the first positional argument, along with the arguments/keyword arguments for this function as its `args` and `kwargs` along with a keyword parameter called repetitions which includes the number repetions to compute the avg. time.
It returns a tuple with the orginal function output and the average time taken rounded to 10 decimals.

### __squared_power_list__

This function returns a list of powers of a base including the start and end integers till which the powers are computed.
This function takes a base which can be `int` or `float` and start and end parameters which default to 0 and 5. 

### __polygon_area__

This function uses the formula:
>Area of Regular Polygon = sides(len_side^2)/4tan(pi/sides)

This function takes the lenght of a side and number of sides are their positional arguments respectively.
>Do note  It computes only for non negative sides and polygons from traingles to hexagons.

### __temp_converter__
This function takes a value and the unit of the value (`c,f,k`) ie. Celcius, Farenheit and Kelvin respectively  as its positional arguments.

It then converts them and returns the other two corresponding units.
>Note that it ensures temperatures can't go below Absolute Zero (`0 degree Kelvin`)

### __speed_converter__
This functon converts KMPH (km/hr) into any of the coresponding units of speed where the distnace can be one of (km, m, ft, yrd, mile) 
and the time can be one of (ms, s, min, hr, day)

>It takes kmph value, dist unit, time unit as its postional arguments. where dist and time arguments are the char values mentioned above.


## Test Cases (Pytest)
>The names of the tests are so that `'test_'` prefix is added to the function it tests, suffied by the what the test does.

### test_timeit_for_uncallable_func
Tests the main time_it function to make sure the passed function is callable.

### test_print_func
Uses the created functio time_it to find abg. time as well as look at the stdout to ensure the print fuction prints correctly.

### test_squared_power_list
Uses a random integer to test the `squared_power_list` function and to check its output.

### test_squared_power_list_invalid_base
Checks if an invalid base raises an `ValueError` to the `squared_power_list` function.

### test_squared_power_list_invalid_powers
Checks if very large powers raise an `ValueError` for the `squared_power_list` function.

### test_squared_power_list_very_large_base
Checks if very large base will raise an `ValueError` for the `squared_power_list` function.

### test_squared_power_list_power_range_too_large
Checks if a very large range between the input ranges will raise an `ValueError` for the `squared_power_list` function.

### test_polygon_area
Checks if the area calculated using the `polygon_area` function is accurate.

### test_polygon_area_neg_side
Checks if a negative side value to the `polygon_area` function will raise an `ValueError`

### test_polygon_area_non_integer_side
Tests if an non integer value given to the number of sides parameter raises an `ValueError`.

### test_polygon_area_invalid_side_range
Tests if number of sides lies in the range `[3,6]` raises an `ValueError`.

### test_temp_converter_test_invalid_unit
Tests if an invalid unit i.e something other than `k`,`c`,`f` will raise an `ValueError`.

### test_temp_converter_test_invalid_range_c
Tests if the given centigrade input isn't below Absolute Zero.

### test_temp_converter_test_invalid_range_f
Tests if the given farenheit input isn't below Absolute Zero.

### test_temp_converter_test_invalid_range_k
Tests if the given kelvin input isn't below Absolute Zero.

### test_temp_converter_test_c
Tests if the Centigrade to Kelvin and Farenheight Conversion is accurate using the boiling of water as ref.

### test_temp_converter_test_f
Tests if the Farenheit to Kelvin and Centigrade Conversion is accurate using the boiling of water as ref.

### test_temp_converter_test_k
Tests if the Kelvin to Centigrade and Farenheight Conversion is accurate using the boiling of water as ref.

### test_speed_converter_invalid_dist_unit
Tests the `speed_converter` function for invalid distance units. ie something other than `km, m, ft, yrd, mile` raises an `ValueError`.

### test_speed_converter_invalid_time_unit
Tests the `speed_converter` function for invalid time units. ie something other than `ms, s, min, hr, day ` raises an `ValueError`.

### test_speed_converter_neg_speed
Tests if a negative speed input raises an `ValueError`.

### test_speed_converter_into_mps
Tests KMPH to meter/sec conversion.

### test_speed_converter_into_mpm
Tests KMPH to meter/min conversion.

### test_readme_exists
   Checks if there is a README.md file in the same folder.

### test_readme_contents
   Checks if the README.md file has alteast 500 words.

### test_readme_proper_description
   Checks if the required functions are present in the README.md file.

### test_readme_file_for_formatting
   Checks if there are adequete headings present in the README.md file.

### test_indentations
   Checks if proper indentations are present throughout the python file.
   using the rule of 4 spaces equals 1 Tab.

### test_function_name_had_cap_letter
   Checks if any one the functions have capital letters used in their names, which breaks the PEP8 conventions.
