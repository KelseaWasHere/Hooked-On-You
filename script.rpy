# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Marea")
define c = Character("Caspian")
define y = Character("You")

# The game starts here.

label start:

    "You and Caspian are meeting at the docks to hang out like they do every weekend."

    scene dock

    y "Oh boy, I can't wait to see my best friend!"
    y "Who is also a mermaid!"

    "You walk up to the dock. Orange hair peeks out from the end of the dock."
    "You walk over to see your fishy friend smiling at you."

    show c at left 

    c "Hey buddy! How are you?" #happy 
    y "Good. My Marine Biochemistry professor is terrible at teaching though, I can hardly hear them because they mumble."
    c "Aw, that's rough buddy. Sucks to suck." #neutral
    c "Hey... why did the professor write on the window?"
    y "Why?"
    c "Because they wanted their lesson to be clear!" #happy
    "..."
    y "Hilarious."
    y "Anyways, you said last time that you wanted to show me something. What is it?"
    c "Oh yeah! You know how my father campaigns against humans, saying they’re all fish hungry lunatics?" #happy 
    y "Yeah?"
    c "I decided that I will prove him wrong by showing humans and mermaids CAN have good relationships!" 
    y "Man, you have daddy issues."
    c "Shut upppp!" #angry
    "Caspian sighs."
    c "will you help me with this?" # sad
    y "You know me, I’ll help you anytime, anywhere."
    c "Thank you thank you! That being said, lean down real quick!"
    y "Ok…"
    "As you lean down, Caspian drags you into the water, and through the blurry water you see him peck your nose, and now your vision is completely clear." 
    scene underwater 
    show c at center
    y "What happened?"
    c "teehee I gave you a life bubble, it took me a really long time to learn how to do it!"
    "As you look around you realize that you are in fact underwater with a bubble around your head. Neat!"
    c "Anyways, there’s someone I want you to meet! This is Marea!"
    show m at left 
    show c at right
    "A buff shark mermaid swims up to you. An air of cockiness surrounds her."
    y "Uh, hi! I'm-"
    m  "‘Sup nerd, heard you like books and stuff." #happy
    y "Yes I do! It’s always been my dream to learn more about the ocean!"
    m "That’s… cool I guess."
    m "I like wrestling alligators!"
    m "So… as a human, do you… y’know… have a thing called “tea parties?”" #confused
    y "…Tea parties? I mean, yes, I guess." 
    m "SO you really mean you just sit around, drinking crushed up leaves?!"
    m "Well guess I can’t say much, I got three seaweed smoking girlfriends..." #happy
    y "Wow... by the way..."

    menu: 
        "Do sharks really bite people?":
            jump goodc
        
        "You have really cool hair!":
            jump goodm

label goodc:
    m "You know humans don't look that tasty." #angry
    m "ESPECIALLY you."
    c "BWAHAHAHAHAHA!" # happy
    jump back

label goodm:
    m "Thanks, I cut it myself!" # happy
    jump back

label back: 
    m "Seeing a human is really interesting, never thought you’d be so stubby." #neutral
    "You frown."
    m "Nono not in a…!"#sad
    m "I meant it in a cute way." #sad
    m "Anyways, Caspian are you going to your game later this week?" #neutral
    c "Of course, you know I’d never give up water polo." #happy
    m "And both of you should come to my competition tomorrow, I can bench 225 EASY." #happy
    c "You know, you always know how to “raise” the bar!"
    m "Yeah, that’s how weight lifting works..?" #confused
    c "…never mind! Teehee."
    "As the water gets darker and darker you realize you should head home."
    y "Hey I should head out, but see you guys tomorrow?"
    c "Of course!"
    m "See you then."

    
    
    
    return
