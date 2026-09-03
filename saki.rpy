label saki_plot:
    show food saki with Dissolve(.5)
    "A decoração deles é muito fofa, principalmente as estrelinhas."
    hide food saki with Dissolve(.5)
    "Você começa a comer seus donuts."
    "São ótimos! A massa é fofa e a cobertura é doce na medida certa. Dá vontade de pedir mais."
    "Enquanto come, você escuta uma batida vindo de uma mesa perto da sua."

    scene bg saki1
    with Dissolve(.5)

    "Você olha na direção do barulho e vê uma moça com orelhas de gato. Ela leva a mão à testa."
    "???""{i}Ai{/i}... Hmph, cochilei de novo..."
    "Parece que ela bateu a cabeça na mesa."
    "Tem um livro no chão perto dela. Você está quase certo de que caiu quando ela bateu a cabeça."
    "???""Huh?"
    "???""!—"
    "Ah, ela notou você encarando."

    default samean =+ 0
    
menu:
    "Segurar uma risada":
        $ samean += 1
        jump escolha_2_1
    "Entregar o livro para ela":
        $ salove += 1
        jump escolha_2_2

return