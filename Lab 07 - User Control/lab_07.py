import arcade


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Cloud:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        x = self.position_x
        y = self.position_y

        arcade.draw_circle_filled(40 + x - 60, 190 + y - 200, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(70 + x - 60, 170 + y - 200, 20, arcade.color.WHITE)
        arcade.draw_circle_filled(90 + x - 60, 190 + y - 200, 25, arcade.color.WHITE)
        arcade.draw_circle_filled(70 + x - 60, 210 + y - 200, 20, arcade.color.WHITE)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class Flower:
    def __init__(self, position_x, position_y, radius, color):

        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):

        x = self.position_x
        y = self.position_y

        # Petals
        arcade.draw_circle_filled(260 + x - 275, y - 160 + 180, 20, arcade.color.PINK_PEARL)
        arcade.draw_circle_filled(270 + x - 275, y - 210 + 180, 20, arcade.color.PINK_PEARL)
        arcade.draw_circle_filled(250 + x - 275, y - 190 + 180, 20, arcade.color.PINK_PEARL)
        arcade.draw_circle_filled(295 + x - 275, y - 160 + 180, 20, arcade.color.PINK_PEARL)
        arcade.draw_circle_filled(300 + x - 275, y - 190 + 180, 20, arcade.color.PINK_PEARL)

        # Center of flower
        arcade.draw_circle_filled(275 + x - 275, y - 185 + 180, 15, arcade.color.YELLOW)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.laser_sound = arcade.load_sound("laser.wav")

        self.set_mouse_visible(False)

        self.flower = Flower(50, 50, 25, arcade.color.YELLOW)
        self.cloud = Cloud(50, 50, 0, 0, 15, arcade.color.WHITE)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        draw_background()
        self.flower.draw()
        self.cloud.draw()

    def on_mouse_motion(self, x, y, dx, dy):

        self.flower.position_x = x
        self.flower.position_y = y

    def on_mouse_press(self, x: float, y: float, button: int, modifiers):
        laser_sound = arcade.load_sound("laser.wav")
        arcade.play_sound(laser_sound)

        self.laser_sound = arcade.load_sound(":resources:Lab 07 - User Control/laser.wav")
        self.laser_sound_player = None

        if not self.laser_sound_player or not self.laser_sound_player:

            self.laser_sound_player = arcade.play_sound(self.laser_sound)

        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.laser_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.laser_sound)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.cloud.change_x = -5
        elif key == arcade.key.RIGHT:
            self.cloud.change_x = 5
        elif key == arcade.key.UP:
            self.cloud.change_y = 5
        elif key == arcade.key.DOWN:
            self.cloud.change_y = -5

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.cloud.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.cloud.change_y = 0

    def on_update(self, dt):
        self.cloud.update()


def draw_background():
    arcade.set_background_color(arcade.color.ORANGE)
    arcade.draw_lrtb_rectangle_filled(0, 800, 800 / 2, 0, arcade.color.DARK_TANGERINE)
    arcade.draw_lrtb_rectangle_filled(0, 800, 600 / 2, 0, arcade.color.YELLOW_ORANGE)
    arcade.draw_lrtb_rectangle_filled(0, 800, 400 / 2, 0, arcade.color.SAFFRON)
    arcade.draw_lrtb_rectangle_filled(0, 800, 200 / 2, 0, arcade.color.DARK_GREEN)


def draw_flower(x, y):

    # Petals
    arcade.draw_circle_filled(260 + x - 275, y - 160 + 180, 20, arcade.color.PINK_PEARL)
    arcade.draw_circle_filled(270 + x - 275, y - 210 + 180, 20, arcade.color.PINK_PEARL)
    arcade.draw_circle_filled(250 + x - 275, y - 190 + 180, 20, arcade.color.PINK_PEARL)
    arcade.draw_circle_filled(295 + x - 275, y - 160 + 180, 20, arcade.color.PINK_PEARL)
    arcade.draw_circle_filled(300 + x - 275, y - 190 + 180, 20, arcade.color.PINK_PEARL)

    # Center of flower
    arcade.draw_circle_filled(275 + x - 275, y - 185 + 180, 15, arcade.color.YELLOW)


def draw_clouds(x, y):
    """ Draw a cloud """
    # Clouds
    arcade.draw_circle_filled(40 + x - 60, 190 + y - 200, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(70 + x - 60, 170 + y - 200, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(90 + x - 60, 190 + y - 200, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(70 + x - 60, 210 + y - 200, 20, arcade.color.WHITE)


def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()
