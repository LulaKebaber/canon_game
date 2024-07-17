from .game_object import GameObject

class TargetWidget(GameObject):
    def __init__(self, target_info, pos, **kwargs):
        """Initializes the target widget properties."""
        target_info['name'] = 'target'
        super(TargetWidget, self).__init__(target_info, pos, **kwargs)