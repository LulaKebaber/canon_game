from .game_object import GameObject

class ObstacleWidget(GameObject):
    def __init__(self, obstacle_info, pos, **kwargs):
        """Initializes the obstacle widget properties."""
        obstacle_info['name'] = 'obstacle'
        super(ObstacleWidget, self).__init__(obstacle_info, pos, **kwargs)