# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define m = Character("Marea")
define c = Character("Caspian")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show marea neutral at right
    show caspian neutral at left 

    # These display lines of dialogue.

    "Narrator Test"
    m "Test 1" 
    c "Test 2"

    menu: 

        "This is a menu test..."

        "Response to Caspian": 
            jump caspian_response 

        "Response to Marea":
            jump marea_response 
        

label marea_response: 
            "I responded to Marea."

            m "Yippee!"

            jump back


    
label caspian_response: 
        "I responded to Caspian."

        c "Yippee!"

        jump back

label back: 
        "We're back from the menu. "


    # This ends the game.

return
