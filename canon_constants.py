
# The size of the field of the game, in pixels.
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

# The frame rate of the game, in frame/s.
FPS = 20

# Bullet and Bombshell projectiles parameter that affects the muzzle velocity range.
BULLET_MASS = SCREEN_WIDTH/2
BOMB_MASS  = SCREEN_WIDTH/3

# Bullet maximum muzzle velocity
BULLET_MAX_VEL = BULLET_MASS

# Bombshell maximum muzzle velocity
BOMB_MAX_VEL = BOMB_MASS

# Laser muzzle velocity (not controlled by the player)
LASER_VEL = SCREEN_WIDTH/1.5

# Bullet and Bombshell projectiles parameter that affects the (spherical) range of the damage.
BULLET_RADIUS = SCREEN_WIDTH/100
BOMB_RADIUS = SCREEN_WIDTH/50

# Laser projectiles parameter that affects the (cylindrical) range of the damage.
LASER_DIST = SCREEN_WIDTH/100

# Parameter of the Bombshell and Laser projectiles that represents the space travelled inside the obstacles.
BOMB_DRILL = SCREEN_WIDTH/50
LASER_IMPULSE = SCREEN_WIDTH/30
