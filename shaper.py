import random

compass = {
    "N": "North",
    "S": "South",
    "E": "East",
    "W": "West",
    "L": "along your line-of-sight"
}
directions = {
    'cone': compass,
    'cylinder': {'U': 'Pointed upwards', **compass}
}


def get_range() -> int:
    return random.choice(range(0, 60, 5))


def get_shape() -> dict:
    shape = {}
    shape['type'] = random.choice(['sphere', 'cube', 'cylinder', 'cone'])
    if shape['type'] in ['cone', 'cylinder']:
        shape['radius'] = random.choice(range(5, 20, 5))
    return shape


def create_spell_shape() -> dict:
    range_ = get_range()
    if range_ is 0:
        return {'range': range_, 'shape': {'type': 'touch'}}
    else:
        s = {}
        s['shape'] = get_shape()
        s['range'] = range_
        return s
