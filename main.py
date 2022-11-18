import Views
import visuals_For_Group
view = int(input("Which input do you want? 1/2 "))
if view == 1:
    Views.main()
elif view == 2:
    visuals_For_Group.main()


if __name__ == "__main__":
    """ Main function """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    start_view = StartMenu()
    window.show_view(start_view)
    arcade.run()