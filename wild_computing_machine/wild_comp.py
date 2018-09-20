from . import common, constants, effector, shaper
import random

compass = {
    "N": "north",
    "S": "south",
    "E": "east",
    "W": "west",
    "L": "along your line-of-sight"
}
directions = {
    'cone': compass,
    'cylinder': {'U': 'pointed upwards', **compass}
}


def rand_center() -> str:
    if random.uniform(0, 1) > 0.75:
        dist = random.choice(['nearest', 'furthest'])
        type_ = random.choices(['creature', 'tree', 'rock', 'doorway'], [
                               0.6, 0.15, 0.15, 0.1])
        return "the {} {} that you can see".format(dist, type_[0])
    return "you"


def get_spell_string() -> str:
    effect = effector.random_resolve()
    shape = shaper.create_spell_shape()
    fin = "You...\n"
    # generate shape selector and str
    shape_txt = ""
    if (shape['shape']['type'] in ['cone', 'cylinder']):
        key, direct = random.choice(
            list(directions[shape['shape']['type']].items()))
        shape_txt = "{} foot long {}, {} feet across at the base, directed {}, ".format(
            shape['range'], shape['shape']['type'], shape['shape']['radius'] * 2, direct)
        center = "you" if key == 'L' else rand_center()
        shape_txt += "with its apex on {}".format(center) if shape['shape']['type'] == 'cone' else "with its base centered on {}".format(center)
    elif ('sphere' in shape['shape']['type']):
        shape_txt = "{}, with a diameter of {} feet, ".format(
            shape['shape']['type'], shape['range'])
        shape_txt += "centered on {}".format(rand_center())
    else:
        shape_txt = "{} foot {}, centered on {}".format(
            shape['range'], shape['shape']['type'], rand_center())

    suffix = constants.YOU_SUFF_TYPE[effect['type']]
    if (effect['type'] == 'damage'):
        fin += suffix.format(effect['amount'], effect['d_type'])
        if (shape['shape']['type'] != 'touch'):
            fin += " to all creatures in a {}".format(shape_txt)
        else:
            fin += " to the next creature you touch"
    elif (effect['type'] == 'transform' or effect['type'] == 'resize'):
        select = "all creatures in a {}".format(
            shape_txt) if shape['shape']['type'] != 'touch' else "the next creature you touch"
        if (effect['type'] == 'transform'):
            fin += suffix.format(select,
                                 common.plural(effect['transform_type']))
            fin += " for {} minutes, or until reduced to 0 HP/destroyed".format(
                effect['duration'])
        elif (effect['type'] == 'resize'):
            fin += suffix.format(
                select, 'grow', effect['amount'])
            if (effect['duration'] is not 0):
                fin += " for {} minutes".format(effect['duration'])
    elif (effect['type'] == 'create'):
        # create ignores shape
        fin += suffix.format(effect['amount'], effect['create_type'])
        fin += " in any shape, centered on " + rand_center()
    return fin


if __name__ == '__main__':
    print(get_spell_string())
