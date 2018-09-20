DAMAGE_TYPES = ['acid', 'bludgeoning', 'cold', 'fire', 'force', 'lightning',
                'necrotic', 'piercing', 'poison', 'psychic', 'radiant', 'slashing', 'thunder']
CONDITIONS = ['blinded', 'charmed', 'deafened', 'fatigued', 'frightened', 'incapacitated', 'invisible', 'paralyzed', 'petrified', 'poisoned', 'restrained', 'stunned', 'unconcious']
"""List of shapes for targeting."""
SPELL_SHAPES = ['cube', 'cone', 'cylinder', 'sphere', 'hemisphere']
"""List of things targets may transform into"""
TRANSFORM_SHAPES = {
    'plant': {
        'animate': False,
        'live': True,
        'size': 'tiny'
    },
    'sheep': {
        'animate': True,
        'live': True,
        'size': 'small'
    },
    'rock': {
        'animate': False,
        'live': False,
        'size': 'small'
    },
    'wolf': {
        'animate': True,
        'live': True,
        'size':  'medium',
    }
}
"""List of things to follow `You...` per effect type"""
YOU_SUFF_TYPE = {
    'damage': 'deal {} {} damage',
    'resize': 'cause {} to {} {} inches',
    'transform': 'transform {} into {} as if by True Polymorph',
    'create': 'create {} cubic feet of {}'
}
