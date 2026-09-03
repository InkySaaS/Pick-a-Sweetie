# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define cha = Character("Charlotte")
define sa = Character("Saki")
define cat = Character("Cath")
define am = Character("Amaya")

default saki = False
default amaya = False
default charlotte = False
default cath = False
default chalove = 0
default salove = 0
default catlove = 0
default amlove = 0

default persistent.final_chabest =+ 0
default persistent.final_chagood =+ 0
default persistent.final_chabad =+ 0

default persistent.final_sabest =+ 0
default persistent.final_sagood =+ 0
default persistent.final_sabad =+ 0

default persistent.final_catbest =+ 0
default persistent.final_catgood =+ 0
default persistent.final_catbad =+ 0

default persistent.final_ambest =+ 0
default persistent.final_amgood =+ 0
default persistent.final_ambad =+ 0

label start:
    stop music fadeout 1

    scene black
    with Dissolve(.5)

    if not player_name:
        $ player_name = "Hikari"

    define p= Character("[player_name]")

    "O dia tem sido bastante agradável até agora."
    "Tendo finalmente conseguido um tempo livre para si após tantos, você decide visitar um novo café no seu bairro."
    play sound "old-style-door-bell-101191.mp3"
    scene bg cafe
    play music "Idle Chatter.ogg" fadeout 1
    "Você escolhe um lugar perto da janela e se acomoda."
    show char smile talk
    with Dissolve(.5)
    "Pouco tempo depois, uma garçonete com asas de fada vem até você para anotar o pedido. Ela lembra vagamente alguém."

    $ dial = "Olá! Bem-vind"
    if player_pronouns == "ela/dela":
        $ dial += "a"
    else:
        $ dial += "o"
    $ dial += " ao Sweetie Bites Cafe. Gostaria de..."

    cha "[dial]"

    show char neutral
    cha "Espera... você me parece familiar."
    cha "Me diz, por acaso seu nome é [player_name]?"

    menu:
        "... Sim?":
            show char smile talk
            cha "Ah! Imaginei que fosse."
    "Ela dá uma risadinha, te observando por um instante a mais do que o necessário. Ao ver a confusão no seu rosto, ela decide se explicar."
    show char talk
    cha "Sou eu, a Charlotte! Já nos conhecemos antes."
    show char default
    cha "Mas podemos deixar isso para depois. Gostaria de fazer seu pedido agora?"

    menu:
        "Sim, só deixa eu dar uma olhadinha aqui.":
            "Você pega o cardápio que está à sua frente e folheia as páginas."

    window hide
    show screen cafemenu with Dissolve(.5)
    $ renpy.pause()
    
    scene bg card
    with Dissolve(.5)

label routes:
    
    hide screen cafemenu with Dissolve(.5)
    window show

    show char smile talk
    with Dissolve(.5)
    cha "Certinho, eu já volto!"
    hide char smile talk with Dissolve(.5)

    if saki == True:
        jump saki_plot
    elif amaya == True:
        jump amaya_plot
    elif charlotte == True:
        jump char_plot
    else:
        jump cath_plot

label char_plot:
    "Você começa a comer seu cheesecake."
    "É ótimo! O creme do cheesecake é doce e suave. A borda é crocante e amanteigada. Com certeza um trabalho incrível."
    p "Nossa, isso aqui tá muito bom!"
    show char smile
    with Dissolve(.5)
    cha "Fico feliz em ouvir isso!"

label cath_plot:
    #quero muito escrever o plot dela hehehe

return