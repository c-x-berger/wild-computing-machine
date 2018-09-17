import common
import constants
import random

e_types = ['damage', 'resize', 'transform', 'create']


def random_type() -> str:
    return random.choice(e_types)


def random_resolve(type_: str = None) -> dict:
    r = {}
    if type_ is None:
        type_ = random_type()
    r['type'] = type_
    if type_ == 'damage':
        # pick random amount, type
        r['amount'] = common.roll_ndn([1, random.choice([4, 6, 8, 10, 20])])
        r['d_type'] = random.choice(constants.DAMAGE_TYPES)
    elif type_ == 'resize':
        # random growing/shrinking, optional duration
        r['amount'] = common.roll_ndn([1, 12]) * random.choice([-1, 1])
        r['duration'] = 0 if random.uniform(0, 1) <= 0.25 else common.roll_ndn([3, 4])
    elif type_ == 'transform':
        # random shape, duration
        r['duration'] = common.roll_ndn([3, 4])
        key, value = random.choice(list(constants.TRANSFORM_SHAPES.items()))
        r['transform_type'] = key
        r['transform_properties'] = value
    elif type_ == 'create':
        # random amount, random thing
        r['amount'] = common.roll_ndn([1, 20])
        r['create_type'] = random.choice(['water', 'mud', 'dirt'])
    return r
