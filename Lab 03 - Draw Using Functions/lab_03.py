import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_sky():
    """ Draw Sunrise """
    arcade.draw_lrtb_rectangle_filled(0, 800, 800 / 2, 0, arcade.color.DARK_TANGERINE)
    arcade.draw_lrtb_rectangle_filled(0, 800, 600 / 2, 0, arcade.color.YELLOW_ORANGE)
    arcade.draw_lrtb_rectangle_filled(0, 800, 400 / 2, 0, arcade.color.SAFFRON)
    arcade.draw_lrtb_rectangle_filled(0, 800, 200 / 2, 0, arcade.color.DARK_GREEN)


def draw_clouds(x, y):
    """ Draw a cloud """
    # Clouds
    arcade.draw_circle_filled(40 + x - 60, 190 + y - 200, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(70 + x - 60, 170 + y - 200, 20, arcade.color.WHITE)
    arcade.draw_circle_filled(90 + x - 60, 190 + y - 200, 25, arcade.color.WHITE)
    arcade.draw_circle_filled(70 + x - 60, 210 + y - 200, 20, arcade.color.WHITE)


def draw_petals(x, y):
    """ Draw Petals for Flower """
    # Stem of flower
    arcade.draw_rectangle_filled(290 + x - 275, y - 260 + 180, 230, 10, arcade.color.DARK_GREEN, 90)

    # Leaves for the flower
    arcade.draw_ellipse_filled(305 + x - 275, y - 240 + 180, 20, 40, arcade.color.DARK_GREEN, 45)
    arcade.draw_ellipse_filled(280 + x - 275, y - 260 + 180, 20, 40, arcade.color.DARK_GREEN, -45)

    # Petals
    arcade.draw_circle_filled(260 + x - 275, y - 160 + 180, 20, arcade.color.PINK_PEARL)
    arcade.draw_circle_filled(270 + x - 275, y - 210 + 180, 20, arcade.color.PINK_PEARL)
    arcade.draw_circle_filled(250 + x - 275, y - 190 + 180, 20, arcade.color.PINK_PEARL)
    arcade.draw_circle_filled(295 + x - 275, y - 160 + 180, 20, arcade.color.PINK_PEARL)
    arcade.draw_circle_filled(300 + x - 275, y - 190 + 180, 20, arcade.color.PINK_PEARL)

    # Center of flower
    arcade.draw_circle_filled(275 + x - 275, y - 185 + 180, 15, arcade.color.YELLOW)

def draw_moon(x,y):
    arcade.draw_circle_filled(x + 100, y + 300, 150, arcade.color.LIGHT_GRAY)


def main():
    arcade.open_window(800, 600, "Drawing with Functions")
    arcade.set_background_color(arcade.color.ORANGE)
    arcade.start_render()

    draw_sky()
    draw_clouds(230 + 60, 210 + 200)
    draw_clouds(390 + 60, 300 + 200)
    draw_clouds(600 + 60, 350 + 200)
    draw_clouds(20 + 60, 400 + 200)
    draw_clouds(200 + 60, 380 + 200)
    draw_clouds(60 + 60, 300 + 200)
    draw_clouds(630 + 60, 250 + 200)
    draw_petals(50, 200)
    draw_petals(700, 350)
    draw_petals(450, 200)
    draw_petals(110, 350)
    draw_petals(340, 310)
    draw_petals(520, 390)
    draw_petals(200, 270)
    draw_petals(250, 410)
    draw_moon(700, 230)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
