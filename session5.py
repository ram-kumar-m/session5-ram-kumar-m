import time
import math


def time_it(fn, *args, repetitons=1, **kwargs):
    if callable(fn):
        start = time.perf_counter()
        out = fn(*args, **kwargs)
        for _ in range(repetitons-1):
            fn(*args, **kwargs)

        duration = round(time.perf_counter() - start, 10)

        return out, duration
    else:
        raise TypeError(f'{fn} must be a callbale function')


def squared_power_list(num, start=0, end=5):

    if not isinstance(num, (int, float)):
        raise ValueError('Number must be an integer or a float')
    elif not isinstance(start, int) and isinstance(end, int):
        raise ValueError('Starting and Ending numbers must be integers')
    elif abs(num) > 100:
        raise ValueError('Base is too large')
    elif abs(start) > 40 or abs(end)-abs(start) > 40:
        raise ValueError('Powers are too big')
    else:
        vals = [num**i for i in range(int(start), int(end)+1)]
        print(*vals,)
        return vals


def polygon_area(len_side, sides):
    '''
    Area is calculated with using the formula
    sides(len_side^2)/4tan(pi/sides)
    '''
    if sides >= 3 and sides <= 6 and isinstance(sides, int) and len_side >= 0:
        b = math.tan(math.pi / sides)
        area = (len_side ** 2) * sides / (4 * b)
        print(
            f'Polygon Area with {sides} sides of length {len_side} = {area:.4f}')
        return area
    elif len_side < 0:
        raise ValueError('Side length cannot be negative')
    elif not isinstance(sides, int):
        raise ValueError('Number of sides must be an integer')
    elif sides > 2 or sides < 7:
        raise ValueError('Number of sides must be between 3 and 6')
    else:
        raise NotImplementedError


def temp_converter(val, temp_given_in):
    temp_given_in = temp_given_in.upper()
    if temp_given_in not in set(['F', 'C', 'K']):
        raise ValueError('given unit is not in (f, c , k)')

    elif temp_given_in == 'C' and val < -273.15:
        raise ValueError('Invalid Centigrade Range')

    elif temp_given_in == 'F' and val < -459.67:
        raise ValueError('Invalid Farenheit Range')

    elif temp_given_in == 'K' and val < 0:
        raise ValueError('You cannot go below absolute Zero')

    else:
        conv_table = {
            'F': lambda x: f'{(x-32)*5/9} in C or {(x-32)*5/9+273.15} in K',
            'C': lambda x: f'{x*(9/5)+32} in F or {x+273.15} in K',
            'K': lambda x: f'{x-273.15} in C or {(x-273.15)*(9/5)+32} in F'
        }
        out = f"{val} in {temp_given_in} = {conv_table.get(temp_given_in)(val)}"
        print(out)
        return conv_table.get(temp_given_in)(val)


def speed_converter(speed, dist, time):

    dist_table = {"km": 1, 'm': 1000, "ft": 3280.84,
                  "yrd": 1093.61, "mile": 0.621371}
    time_table = {"ms": 1/(3.6 * 10**6), "s": 1/3600,
                  "min": 1/60, "hr": 1, "day": 24}

    if speed < 0:
        raise ValueError('Speed cannot be negative')

    elif dist not in dist_table:
        raise ValueError(f'Distance unit must be one of {*dist_table.keys(),}')
    elif time not in time_table:
        raise ValueError(f'Time unit must be one of {*time_table.keys(),}')

    else:
        conv_speed = speed*dist_table.get(dist)*time_table.get(time)
        print(f'Speed, {speed}kmph = {round(conv_speed, 10)}{dist}/{time}')
        return conv_speed
