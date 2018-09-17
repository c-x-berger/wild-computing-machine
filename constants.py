DAMAGE_TYPES = ['acid', 'bludgeoning', 'cold', 'fire', 'force', 'lightning', 'necrotic', 'piercing', 'poison', 'psychic', 'radiant', 'slashing', 'thunder']
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
        'live': True,
        'size': 'small' 
    },
    'wolf': {
        'animate': True,
        'live': True,
        'size':  'medium',
    }
}
