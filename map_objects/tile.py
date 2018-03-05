class Tile:
    """A tile on a map. May or may not be blocked, may or may not block sight"""
    def __init__(self, blocked, block_sight=None):
        self.blocked = blocked

        #by default, a tile that is blocked blocks sight 
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight