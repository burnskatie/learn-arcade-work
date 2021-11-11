""" Sprite Sample Program """

import arcade

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 1024

MOVEMENT_SPEED = 5


class Coin(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        # Current angle in radians
        self.circle_angle = 0

        # How far away from the center to orbit, in pixels
        self.circle_radius = 0

        # How fast to orbit, in radians per frame
        self.circle_speed = 0.008

        # Set the center of the point we will orbit around
        self.circle_center_x = 0
        self.circle_center_y = 0

    def update(self):

        self.center_x = self.circle_radius * math.sin(self.circle_angle) \
            + self.circle_center_x
        self.center_y = self.circle_radius * math.cos(self.circle_angle) \
            + self.circle_center_y


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.coin_list = None

        # Set up the player
        self.player_sprite = None

        # This variable holds our simple "physics engine"
        self.physics_engine = None

        self.score = 0

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.DARK_BLUE)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList

        # Reset the score
        self.score = 0

        # Create the player
        self.player_sprite = arcade.Sprite("alienBlue_walk1.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 160
        self.player_sprite.center_y = 120
        self.player_list.append(self.player_sprite)

        # Manually create and position a box at 300, 200
        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 600
        wall.center_y = 150
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 650
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 150
        wall.center_y = 500
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 200
        wall.center_y = 900
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 400
        wall.center_y = 965
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 670
        wall.center_y = 450
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 670
        wall.center_y = 965
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 750
        wall.center_y = 650
        self.wall_list.append(wall)

        wall = arcade.Sprite("meteorGrey_big3.png", SPRITE_SCALING_BOX)
        wall.center_x = 200
        wall.center_y = 250
        self.wall_list.append(wall)

        # --- Left
        for x in range(128, 1024, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)
        # --- Bottom
        for y in range(0, 1024, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 90
            wall.center_y = y
            self.wall_list.append(wall)
        # --- Top
        for x in range(128, 1024, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1024
            self.wall_list.append(wall)
        # --- Bottom
        for y in range(0, 1024, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 1024
            wall.center_y = y
            self.wall_list.append(wall)

        # --- Place boxes inside a loop
        for x in range(173, 650, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 640
            self.wall_list.append(wall)

        for x in range(173, 832, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 320
            self.wall_list.append(wall)

        for x in range(173, 832, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 808
            self.wall_list.append(wall)


        for x in range(173, 300, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 720
            self.wall_list.append(wall)

        for x in range(250, 450, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 100
            self.wall_list.append(wall)

        for y in range(300, 200, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 550
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(173, 500, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 880
            wall.center_y = y
            self.wall_list.append(wall)

        for y in range(173, 500, 64):
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 810
            wall.center_y = y
            self.wall_list.append(wall)

        # --- Place walls with a list
        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("planetCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        # Create the physics engine. Give it a reference to the player, and
        # the walls we can't run into.
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def start_new_game(self):

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        for i in range(30):

            coin = Coin("star.png", SPRITE_SCALING_BOX / 3)

            coin.circle_center_x = random.randrange(SCREEN_WIDTH)
            coin.circle_center_y = random.randrange(SCREEN_HEIGHT)

            coin.circle_radius = random.randrange(10, 200)

            self.key_list.append(coin)

    def on_draw(self):
        arcade.start_render()

        # Select the scrolled camera for our sprites
        self.camera_for_sprites.use()

        # Draw the sprites
        self.wall_list.draw()
        self.player_list.draw()
        self.coin_list()

        # Select the (unscrolled) camera for our GUI
        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)


    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the window to the player.
        #
        # If CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        # Anything between 0 and 1 will have the camera move to the location with a smoother
        # pan.
        CAMERA_SPEED = 1
        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
