import random
import shaper

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


def rand_center() -> str:
    if random.uniform(0, 1) > 0.75:
        dist = random.choice(['nearest', 'furthest'])
        type_ = random.choices(['creature', 'tree', 'rock', 'doorway'], [
                               0.6, 0.15, 0.15, 0.1])
        return "the {} {} that you can see".format(dist, type_[0])
    return "you"


if __name__ == '__main__':
    e_types = ["transform", "cast", "shape", "damage"]
    type_ = random.choice(e_types)
    print("Effect type: " + type_)
    print(shaper.create_spell_shape() if type_ != 'cast' else '')
