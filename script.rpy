# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Marea", color="#5274a2")
define c = Character("Caspian")
define y = Character("You")
define n = Character("Narrator")
define cm = Character("Caspian and Marea")

# The game starts here.

label start:
    play music "music.mp3" loop
    "You and Caspian are meeting at the docks to hang out like they do every weekend."

    scene dock

    y "Oh boy, I can't wait to see my best friend!"
    y "Who is also a mermaid!"

    n "You walk up to the dock. Orange hair peeks out from the end of the dock."
    n "You walk over to see your fishy friend smiling at you."

    show caspian happy at right
    c "Hey buddy! How are you?" #happy 
    y "Good. My Marine Biochemistry professor is terrible at teaching though, I can hardly hear them because they mumble."
    c "Aw, that's rough buddy. Sucks to suck." #neutral
    c "Hey... why did the professor write on the window?"
    y "Why?"
    show caspian happy at right
    c "Because they wanted their lesson to be clear!" #happy
    n "..."
    y "Hilarious."
    y "Anyways, you said last time that you wanted to show me something. What is it?"
    show caspian happy at right
    c "Oh yeah! You know how my father campaigns against humans, saying they’re all fish hungry lunatics?" #happy 
    y "Yeah?"
    c "I decided that I will prove him wrong by showing humans and mermaids CAN have good relationships!" 
    y "Man, you have daddy issues."
    show caspian mad at right
    c "Shut upppp!" #angry
    n "Caspian sighs."
    show caspian sad at right
    c "will you help me with this?" # sad
    y "You know me, I’ll help you anytime, anywhere."
    c "Thank you thank you! That being said, lean down real quick!"
    y "Ok…"
    n "As you lean down, Caspian drags you into the water, and through the blurry water you see him peck your nose, and now your vision is completely clear." 
    scene underwater 
    show caspian neutral at center
    y "What happened?"
    c "teehee I gave you a life bubble, it took me a really long time to learn how to do it!"
    n "As you look around you realize that you are in fact underwater with a bubble around your head. Neat!"
    c "Anyways, there’s someone I want you to meet! This is Marea!"
    show marea neutral at left 
    show caspian neutral at right
    n "A buff shark mermaid swims up to you. An air of cockiness surrounds her."
    y "Uh, hi! I'm-"
    show marea happy at left
    m  "‘Sup nerd, heard you like books and stuff." #happy
    show marea neutral at left
    y "Yes I do! It’s always been my dream to learn more about the ocean!"
    m "That’s… cool I guess."
    m "I like wrestling alligators!"
    m "So… as a human, do you… y’know… have a thing called “tea parties?”" #confused
    y "…Tea parties? I mean, yes, I guess." 
    m "SO you really mean you just sit around, drinking crushed up leaves?!"
    show marea happy at left
    m "Well guess I can’t say much, I got three seaweed smoking girlfriends..." #happy
    y "Wow... by the way..."

    hide marea
    hide caspian
    menu: 
        "Do sharks really bite people?":
            jump goodc
        
        "You have really cool hair!":
            jump goodm

label goodc:
    show marea mad at left
    m "You know humans don't look that tasty." #angry
    m "ESPECIALLY you."
    show caspian happy at right
    c "BWAHAHAHAHAHA!" # happy
    jump back

label goodm:
    show marea happy at left
    m "Thanks, I cut it myself!" # happy
    jump back

label back: 
    show marea neutral at left
    m "Seeing a human is really interesting, never thought you’d be so stubby." #neutral
    n "You frown."
    m "Nono not in a…!"#sad
    m "I meant it in a cute way." #sad
    show marea neutral at left
    m "Anyways, Caspian are you going to your game later this week?" #neutral
    show caspian happy at right
    c "Of course, you know I’d never give up water polo." #happy
    m "And both of you should come to my competition tomorrow, I can bench 225 EASY." #happy
    c "You know, you always know how to “raise” the bar!"
    show marea confused at left
    m "Yeah, that’s how weight lifting works..?" #confused
    c "…never mind! Teehee."
    n "As the water gets darker and darker you realize you should head home."
    y "Hey I should head out, but see you guys tomorrow?"
    c "Of course!"
    m "See you then."

    # DAY 2
    scene black 
    n "Bright and early in the morning you arrive to head to Marea’s weight lifting competition. You now see orange and blue hair sticking out the water."
    scene dock
    n "As you approach you now have two smiling faces looking at you."
    show marea happy at left
    m "Bend over!" #happy
    y "Whoa!"
    m "You know what I mean!"
    n "As you bend over, you get dragged down by two sets of hands and once again receive a smooch on the nose."
    scene underwater
    y "You know, if you keep kissing me, I’ll fall for you."
    show caspian happy at right
    c "Guess you’ll need a bandaid!" #happy
    show marea neutral at left
    m "Ugh, stop flirting already and watch how big my muscles are!"
    n "Marea grabs you and Caspian, dragging you to a gym. When you arrive a bunch of mermaids stare at you, confused and some scared of you. But most just glance at Marea as their worries lessen."

    scene gym
    show marea neutral at left
    show caspian neutral at right
    m "Are you ready to see the best lifting of your life?" 
    c "The best lifting I’ve seen is when Mr. SquarePants lifted his rating by showing his humble beginnings as a fry cook!"
    y "That seems familiar…"
    show caspian mad at right
    c "My dad hates him, but that’s only because Mr. SquarePants can run a better campaign than him." #angry
    c "I am SO tired of hearing my dad complain about such a wholesome politician."
    m "Those are so hard to come across these days…"
    n "These underwater politics are very hard for you to follow, so you just sit and listen to Caspian and Marea talk of the prosperity of SpongeBob SquarePants's political career." 
    n "Another mermaid calls out to Marea that it's her turn to compete."
    show marea happy at left
    m "That’s me! Wish me luck!" # happy
    n "As Marea swims up to the podium to lift, you can feel Caspian is tense. You turn to him and he most certainly has no poker face." 
    n "He makes eye contact with you and immediately tells you what’s on his mind."
    show caspian sad at right
    c "Do you think we can really prove my dad wrong?" # sad

    hide marea
    hide caspian
    menu: 
        "Of course! We can overcome everything!":
            jump encourage
        "Yeah, let's just focus on Marea's competition.":
            jump dismissive

label encourage:
    show caspian flustered at center
    c "Thank you.. You always know what to say to make me feel better..." #flustered
    jump gym

label dismissive:
    show caspian neutral at center
    c "You're right. That's such a future problem!" # neutral
    jump gym

label gym:
    n "Later, Marea returns from her podium, bringing over a first place medal."
    m "Did you see how much I lifted? I even did my personal best! 230!" #flustered
    show caspian happy at right
    c "You did so good!" # happy
    m "Thank you so much!" # happy
    show caspian neutral at right
    c "Hey, have you ever used a magnifying glass?"
    m "No, why?" #confused
    c "So you can focus on your gains!"
    show marea confused at left
    m " ??? No, I use a calendar for that." # confused
    c   "Nevermind! Teehee." 
    m "...Okay..."
    y "Anyways, it’s getting late and I can kinda tell that my presence is a… bit of a bother." 
    y "I should head back. Can you show me the way to the dock?" 
    c "Of course!"
    scene underwater
    n "As you three head back, you can feel tensions melt as you get further away from the other mermaids."
    n "You tell Caspian and Marea goodnight, and head home for the night." 

    scene black 
    n "The next day, you go back to the dock."
    scene dock
    n "As you approach, you see Marea and Caspian sitting on the dock talking. They seem to get quiet when you arrive."
    n "They both smile and wave at you."
    y "So, what's the plan for today?"
    n "They both smile and outstretch their hands. When you take them, they once again drag you into your watery grave of love."
    scene underwater 
    show caspian neutral at right
    show marea neutral at left
    n "With another peck, you are able to see and breathe again."
    show caspian happy at right
    c "We actually both have different errands to run today. I have to go to the store to get candy and a new ball for water polo!" # happy
    m "And I need to get seaweed for my three seaweed smoking girlfriends!" # happy

    hide caspian
    hide marea

    menu:
        "Go with Caspian":
            jump caspianend

        "Go with Marea":
            jump mareaend

label caspianend:
    show caspian happy at right
    c "Alright let’s go!" # happy
    m "I’ll see you guys later!" # happy
    scene store
    show caspian neutral at center
    c "Have you ever had Swedish Fish?"
    y "Yeah, like... above water..."
    show caspian confused at right
    c "Wait, where is it?" #confused
    y "Where is what?"
    show caspian sad at right
    c "I lost my wallet…" # sad
    y "That's okay, I’ll pay for it."
    show caspian neutral at right
    c "Do you have any sea dollars?" #neutral
    n "You do not have any sea dollars."
    y "...No..."
    c "Aww, I can’t believe I lost my wallet."
    y  "Well, do you remember a while ago how I told you about shoplifting?"
    c "I get your implication, hold on."
    n "As you stand watch, Caspian shoves Swedish Fish into your pocket, which turns out to just be actual fish."
    n "They try to swim out but you get a good grasp." 
    c "Alright, you leave first. I’ll join in a few minutes." 
    n "You leave the store without any questions and a few minutes later you meet up with Caspian." 
    c "I’m so glad that worked!" #happy
    n "As Caspian eats the Swedish fish, you mention to eat them on the beach instead."
    show caspian flustered at right
    c "That sounds wonderful!" #flustered
    scene beach 
    show caspian neutral at center
    n "As you both swim up to the beach, he eats his Swedish Fish."
    c "You know, you’re really special to me, right? I'd really like to do this again. Can we?" 
    y "Of course, you’re special to me too. Let's do this again!"

    scene beach
    show handholding at center
    pause 5.0 
    
    jump end
    
label mareaend:
    show marea happy at left
    show caspian neutral at right 
    m "Awesome, let's go!" # happy
    show caspian happy at right
    c "I'll see you guys later!" # happy
    hide caspian
    show marea neutral at left
    m "The store is this way."
    n "As you two head towards the dispensary, Marea seems to be texting her girlfriends on her shell phone."
    scene store
    show marea neutral at center
    n "Heading into the store, Marea buys the seaweed cookies as requested. You both head out."
    scene underwater
    show marea neutral at center
    m "Hey, do you want to try some?"
    hide marea
    menu: 
        "Try the seaweed":
            jump tryweed
        "Don't try the seaweed":
            jump noweed
    
label tryweed:
    y "Sure, why not?"
    n "You try the seaweed cookie. It is, in fact, just a cookie made out of seaweed."
    jump idk

label noweed:
    show marea neutral at center
    m "No problem!"
    jump idk

label idk:
    show marea neutral at left
    m "I got some more snacks, too. Would you like some?"
    n "She is holding up a large handful of some sort of plant. It doesn't look appetizing. You decline it."
    m "Suit yourself! I wonder what surface snacks are like." # neutral
    y "How about we go to the beach to try some?"
    show marea happy at left
    m "Sure!" #happy
    scene beach
    show marea neutral at center
    m "Wow, this is so pretty."
    m "Y'know, I was told the surface was full of garbage."
    y "That's not wrong, necessarily..."
    show marea happy at left
    m "Trust me when I say you're not garbage." # happy
    y "Thank you. You're not, uh, garbage either..."
    show marea flustered at left
    m "Thank you..." # flustered

    scene beach
    show handholding at center
    pause 5.0
    jump end

label end:
    return 
