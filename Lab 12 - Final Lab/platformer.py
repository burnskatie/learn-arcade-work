"""
Scroll around a large screen.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_scrolling
"""

import random
import arcade
import math

SPRITE_SCALING = 0.3

SPRITE_SCALING_FLY = 0.1

SPRITE_SCALING_BIRD = 0.3

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 1500
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 5

FLY_COUNT = 100

BIRD_COUNT = 10


class MenuView(arcade.View):
    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BLUE)

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Welcome to The Froggy Picnic",
                         DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2 + 100,
                         arcade.color.WHITE, font_size=30, anchor_x="center")

        arcade.draw_text("Use arrow keys to move and jump",
                        DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2 + 20,
                        arcade.color.WHITE, font_size=30, anchor_x="center")

        arcade.draw_text("Eat 50 flys to win the game!",
                         DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2 - 20,
                         arcade.color.WHITE, font_size=30, anchor_x="center")

        arcade.draw_text("CLICK TO START",
                         DEFAULT_SCREEN_WIDTH / 2, DEFAULT_SCREEN_HEIGHT / 2 - 100,
                         arcade.color.WHITE, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)


class Fly(arcade.Sprite):
    def reset_pos(self):
        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(DEFAULT_SCREEN_HEIGHT + 20,
                                         DEFAULT_SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(DEFAULT_SCREEN_WIDTH)

    def update(self):
        # Move the coin
        self.center_y -= 1

        # See if the coin has fallen off the bottom of the screen.
        # If so, reset it.
        if self.top < 0:
            self.reset_pos()


class Bird(arcade.Sprite):
    def __init__(self, filename, sprite_scaling):

        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def reset_pos(self):
        # Reset the coin to a random spot above the screen
        self.center_y = random.randrange(DEFAULT_SCREEN_HEIGHT + 20,
                                         DEFAULT_SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(DEFAULT_SCREEN_WIDTH)

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > DEFAULT_SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > DEFAULT_SCREEN_HEIGHT:
            self.change_y *= -1

        # Move the coin
        self.center_y -= 1

        if self.top < 0:
            self.reset_pos()


class GameView(arcade.View):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        super().__init__()

        self.lose_sound = arcade.load_sound("arcade_resources_sounds_error4.wav")

        self.win_sound = arcade.load_sound("arcade_resources_sounds_coin1.wav")

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.fly_list = None
        self.bird_list = None
        self.done = False

        # Set up the player
        self.player_sprite = None
        self.score = 0
        self.lives = 3

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        game_view = MenuView()
        self.window.show_view(game_view)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.fly_list = arcade.SpriteList()
        self.bird_list = arcade.SpriteList()

        # Set up the player https://api.arcade.academy/en/latest/resources.html
        self.player_sprite = arcade.Sprite("frog_move.png",
                                           scale=0.3)
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        map_name = "test.json"
        self.title_map = arcade.load_tilemap(map_name, scaling=SPRITE_SCALING)
        self.wall_list = self.title_map.sprite_lists["Walls"]

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list,
                                                             gravity_constant=0.5)

        # Set the background color
        if self.title_map.background_color:
            arcade.set_background_color(self.title_map.background_color)

        for i in range(FLY_COUNT):

            # Create the coin instance
            # Coin image from kenney.nl
            fly = Fly("fly.png", SPRITE_SCALING_FLY)

            # Position the coin
            fly.center_x = random.randrange(DEFAULT_SCREEN_WIDTH)
            fly.center_y = random.randrange(DEFAULT_SCREEN_HEIGHT)

            # Add the coin to the lists
            self.fly_list.append(fly)

        for i in range(BIRD_COUNT):

            # Bird image from toppng.com
            bird = Bird("eagle.png", SPRITE_SCALING_BIRD / 3)

            # Position the center of the circle the eagle will orbit
            bird.circle_center_x = random.randrange(DEFAULT_SCREEN_WIDTH)
            bird.circle_center_y = random.randrange(DEFAULT_SCREEN_HEIGHT)
            bird.change_x = random.randrange(-5, 4)
            bird.change_y = random.randrange(-5, 4)

            self.bird_list.append(bird)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.fly_list.draw()
        self.bird_list.draw()

        output = f"Score: {self.score}"
        arcade.draw_text(output, 5, 10, arcade.color.BLACK, 10)

        if len(self.fly_list) == 50:
            arcade.draw_text("YOU WIN!", 100, 500, arcade.color.WHITE, 50)

        output = f"Lives: {self.lives}"
        arcade.draw_text(output, 5, 25, arcade.color.BLACK, 10)

        if len(self.bird_list) == 0:
            arcade.draw_text("GAME OVER", 75, 500, arcade.color.WHITE, 50)

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()

        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.bird_list) == 0:
            arcade.draw_text("GAME OVER", 300, 300, arcade.color.WHITE, 25)

        # Draw the GUI
        arcade.draw_rectangle_filled(self.window.width // 2,
                                     20,
                                     self.window.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        arcade.draw_text(text, 10, 10, arcade.color.BLACK_BEAN, 20)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = 20
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

        self.fly_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.fly_list)

        for fly in hit_list:
            fly.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.win_sound)

        self.bird_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.bird_list)

        for bird in hit_list:
            bird.remove_from_sprite_lists()
            self.lives -= 1
            arcade.play_sound(self.lose_sound)

        if self.lives <= 0:
            self.done = True
            for bird in self.bird_list:
                bird.remove_from_sprite_lists()

        if self.lives <= 0:
            self.done = True
            for fly in self.fly_list:
                fly.remove_from_sprite_lists()

        if self.lives > 0:
            self.physics_engine.update()
            self.player_sprite.update_animation(delta_time)
            self.fly_list.update()

    def scroll_to_player(self):

        position = self.player_sprite.center_x - self.window.width / 2, \
            self.player_sprite.center_y - self.window.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    window = arcade.Window(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
