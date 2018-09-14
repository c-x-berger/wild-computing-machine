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

    if (type_ != "cast"):
        s_shape = shaper.create_spell_shape()
        print(s_shape)
        final_range = ""
        if (s_shape['shape']['type'] in ['cone', 'cylinder']):
            final_range = "Range: {!s} foot tall {}".format(
                s_shape['range'], s_shape['shape']['type'])
        else:
            final_range = "Range: {!s} foot {}".format(
                s_shape['range'], s_shape['shape']['type'])
        if ('radius' in s_shape['shape']):
            # d = 2r, dumbass
            final_range += ", {} feet across at the base".format(
                s_shape['shape']['radius'] * 2)
        if (s_shape['shape']['type'] != 'touch'):
            center = rand_center()
            final_range += ', centered on {}'.format(
                center) if s_shape['shape']['type'] != 'cone' else ', with its apex centered on {}'.format(center)
        print(final_range)
    else:
        print("Centered on " + rand_center())
