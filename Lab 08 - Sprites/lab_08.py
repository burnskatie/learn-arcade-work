import random
import arcade
import math


SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Saw(arcade.Sprite):

    def __init__(self, filename, sprite_scaling):
        """ Constructor. """
        # Call the parent class (Sprite) constructor
        super().__init__(filename, sprite_scaling)

        self.change_x = 0
        self.change_y = 0

    def update(self):

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y

        # If we are out-of-bounds, then 'bounce'
        if self.left < 0:
            self.change_x *= -1

        if self.right > SCREEN_WIDTH:
            self.change_x *= -1

        if self.bottom < 0:
            self.change_y *= -1

        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1


class Key(arcade.Sprite):

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

        self.circle_angle += self.circle_speed

        # Move the coin
        self.center_x += self.change_x
        self.center_y += self.change_y


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        self.lose_sound = arcade.load_sound("arcade_resources_sounds_lose2.wav")

        self.win_sound = arcade.load_sound("arcade_resources_sounds_coin3.wav")

        super().__init__(width, height)

        # Sprite lists
        self.player_list = None
        self.key_list = None
        self.saw_list = None

        # Set up the player
        self.score = 0
        self.player_sprite = None

    def start_new_game(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.key_list = arcade.SpriteList()
        self.saw_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        self.player_sprite = arcade.Sprite("robot_fall.png", SPRITE_SCALING)
        self.player_sprite.center_x = 60
        self.player_sprite.center_y = 80
        self.player_list.append(self.player_sprite)

        for i in range(50):

            key = Key("keyYellow.png", SPRITE_SCALING / 3)

            key.circle_center_x = random.randrange(SCREEN_WIDTH)
            key.circle_center_y = random.randrange(SCREEN_HEIGHT)

            # Random radius from 10 to 200
            key.circle_radius = random.randrange(10, 200)

            # Random start angle from 0 to 2pi
            key.circle_angle = random.random() * 2 * math.pi

            self.key_list.append(key)

        for i in range(20):

            saw = Saw("sawHalf.png", SPRITE_SCALING / 3)

            saw.center_x = random.randrange(SCREEN_WIDTH)
            saw.center_y = random.randrange(SCREEN_HEIGHT)
            saw.change_x = random.randrange(-5, 4)
            saw.change_y = random.randrange(-5, 4)

            self.saw_list.append(saw)

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        # Set the background color
        arcade.set_background_color(arcade.color.RED_ORANGE)

    def on_draw(self):

        arcade.start_render()

        # Draw all the sprites
        self.saw_list.draw()
        self.key_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.key_list) == 0:
            arcade.draw_text("GAME OVER", 300, 300, arcade.color.WHITE, 25)

    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.key_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        """ Movement and game logic """
        if len(self.key_list) > 0:
            self.key_list.update()
            self.saw_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.key_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for key in hit_list:
            self.score += 1
            arcade.play_sound(self.win_sound)
            key.remove_from_sprite_lists()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                        self.saw_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for key in hit_list:
            self.score -= 3
            arcade.play_sound(self.lose_sound)
            key.remove_from_sprite_lists()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.start_new_game()
    arcade.run()


if __name__ == "__main__":
    main()