import arcade, time


def man2(x):
    b = (0, 0, 0)
    arcade.open_window(600, 600, "Man")
    arcade.set_background_color(arcade.color.IVORY)
    arcade.start_render()

    # Stand for man + Head
    arcade.draw_line_strip([(100, 50), (200, 50), (150, 50), (150, 550), (350, 550), (350, 500)], line_width=4, color=b)

    while True:
        arcade.draw_circle_outline(350, 450, 50, color=b, border_width=4)
        if x == 5:
            arcade.finish_render()
            time.sleep(2)
            arcade.close_window()
            break

        # Body
        arcade.draw_line(350, 400, 350, 200, line_width=4, color=b)
        if x == 4:
            arcade.finish_render()
            time.sleep(2)
            arcade.close_window()
            break

        # Right arm
        arcade.draw_line(350, 300, 450, 375, line_width=4, color=b)
        if x == 3:
            arcade.finish_render()
            time.sleep(2)
            arcade.close_window()
            break

        # Left arm
        arcade.draw_line(350, 300, 250, 375, line_width=4, color=b)
        if x == 2:
            arcade.finish_render()
            time.sleep(2)
            arcade.close_window()
            break

        # Right leg
        arcade.draw_line(350, 200, 450, 100, line_width=4, color=b)
        if x == 1:
            arcade.finish_render()
            time.sleep(2)
            arcade.close_window()
            break

        # Left leg
        arcade.draw_line(350, 200, 250, 100, line_width=4, color=b)
        if x == 0:
            arcade.finish_render()
            time.sleep(4)
            arcade.close_window()
            break
