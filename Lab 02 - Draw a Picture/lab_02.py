"""
Lab 2: Sunrise Drawing
"""
import arcade

arcade.open_window(800, 600, "Dog Drawing")

arcade.set_background_color(arcade.csscolor.DARK_ORANGE)

arcade.start_render()

# Draw Dog

arcade.draw_ellipse_filled(650, 200, 50, 100, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(500, 200, 50, 100, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(530, 300, 400, 200, arcade.csscolor.SADDLE_BROWN)

arcade.draw_circle_filled(350, 380, 100, arcade.csscolor.SIENNA)

# Dog Collar
arcade.draw_arc_outline(150, 400, 400, 600, arcade.csscolor.DARK_RED, 45, 90, 45, -90)

# Legs Front
arcade.draw_ellipse_filled(250, 410, 50, 120, arcade.csscolor.SIENNA, 45)
arcade.draw_ellipse_filled(450, 410, 50, 120, arcade.csscolor.SIENNA, 135)

# Eyes
arcade.draw_circle_filled(320, 395, 20, arcade.csscolor.WHITE)
arcade.draw_circle_filled(385, 395, 20, arcade.csscolor.WHITE)
arcade.draw_circle_filled(320, 395, 10, arcade.csscolor.BLACK)
arcade.draw_circle_filled(385, 395, 10, arcade.csscolor.BLACK)

# Tongue
arcade.draw_ellipse_filled(350, 300, 50, 70, arcade.csscolor.LIGHT_PINK)
arcade.draw_rectangle_filled(350, 300, 3, 70, arcade.csscolor.BLACK)

# Nose
arcade.draw_ellipse_filled(350, 340, 50, 40, arcade.csscolor.BLACK)
arcade.draw_circle_filled(340, 340, 4, arcade.csscolor.DARK_GRAY)
arcade.draw_circle_filled(360, 340, 4, arcade.csscolor.DARK_GRAY)

# Dog Tag
arcade.draw_rectangle_filled(370, 240, 50, 50, arcade.csscolor.YELLOW)

# Legs Back
arcade.draw_ellipse_filled(630, 200, 50, 100, arcade.csscolor.SADDLE_BROWN)
arcade.draw_ellipse_filled(480, 200, 50, 100, arcade.csscolor.SADDLE_BROWN)

# Tail
arcade.draw_arc_outline(450, 400, 400, 600, arcade.csscolor.SADDLE_BROWN, 45, 90, 45, -90)

# Bone
arcade.draw_rectangle_filled(180, 250, 170, 30, arcade.csscolor.GHOST_WHITE, 45)
arcade.draw_circle_filled(110, 290, 25, arcade.csscolor.GHOST_WHITE)
arcade.draw_circle_filled(150, 320, 25, arcade.csscolor.GHOST_WHITE)
arcade.draw_circle_filled(215, 175, 25, arcade.csscolor.GHOST_WHITE)
arcade.draw_circle_filled(250, 205, 25, arcade.csscolor.GHOST_WHITE)

arcade.finish_render()

arcade.run()



