label fat2:
    if check==False and persistent.checkpoint_8 != None:
        "Where do you want to start?"
        menu:
            "From the beginning of the chapter":
                $ dr=Player('fat2')
                $ check=True
                jump fat2
            "From automatic checkpoint_":
                $ renpy.jump(persistent.checkpoint_8)
    else:
        $ dr=Player('fat2')
label fat2_1:
    u5 "Help!!!"
    Inner "What the ..."
    u5 "I am thristy!! please water!"
    Inner "She looks very weak and sick!"
    #Pulse screen
    Inner "The pulse is very weak"
label fat2_q1:
    $ dr.current('fat2_q1')
    "Why do you think the patient complains of being thristy, with a weak pulse and fast pulse?"

    menu:
        "Because she tried to kill herself":
            "There is no enough evidence to assess that!"
            $ dr.life_loss()
        "Because volume of fluids is reduced":
            $ dr.current('fat2_2')
        "There is no enough information to assess that!":
            "There is enough data to assess that!"
            $ dr.life_loss()
label fat2_2:
    Inner "That poor woman barely speaks!"
    Bont "Alice come quick!"
    Alice "Yes, Dr Bont,\nWhat are your orders?"
    menu:
        "Give a warm cup of tea to that woman":
            Alice "That poor woman is barely able to speak, I don't think she is able to drink\nThis is nonsense"
            $ dr.life_loss()
        "Open an intravenous line in her right arm! QUICK":

            $ dr.current('fat2_3')
        "Give a her a can of soda!":
            Alice "That poor woman is barely able to speak, I don't think she is able to drink\nThis is nonsense"
            $ dr.life_loss() 
label fatal2_3:
    Alice "Done! which medication show I pass?"
    menu:
        "1 liter of Saline solution within 15 min":
            $ dr.current('fat2_3')
            
        "1 liter of Saline solution within 1 hour":
            Alice "This poor woman is dehydrated! It's too slow"
            $ dr.life_loss() 
        "1 liter of Saline solution within 8 hours":
            Alice "This poor woman is dehydrated! It's too slow"
            $ dr.life_loss() 
label fat2_3:
    Alice "Immediately!"
    Inner "Why is this woman so dehydrated?"
    Inner "There are no visible wounds, her skin is dry ..."
    Bont "Excuse me do you have diarrhea?"
    u5 "No, I am hungry!! I'm thirsty!!!"
    Inner 'Did she say {color=#ffff00}hungry{/color}?\nthat gives me a clue'
    Bont "Alice, put a urinary sound to the patient, quick"
    Alice "Done.... but"
    Bont "What happened?"
    Alice "I just put and the urine bag is full..."
    Bont "What? change the bag!"
    Alice "Done, but the bag is full again"
    $persistent.Slow_Girl=True
    return
