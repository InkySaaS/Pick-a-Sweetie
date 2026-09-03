screen cafemenu():
    fixed:
        style_prefix "navigation"

        add "bg menu pt"

        imagebutton auto "images/sprites/menu/tart_%s.png":
            xpos 334 
            ypos 186
            focus_mask True
            action [SetVariable("charlotte", True), Jump("routes")]

        imagebutton auto "images/sprites/menu/donut_%s.png":
            xpos 585
            ypos 754
            focus_mask True
            action [SetVariable("saki", True), Jump("routes")]

        imagebutton auto "images/sprites/menu/macaron_%s.png":
            xpos 991
            ypos 199
            focus_mask True
            action [SetVariable("amaya", True), Jump("routes")]

        imagebutton auto "images/sprites/menu/crepe_%s.png":
            xpos 1367
            ypos 711
            focus_mask True
            action [SetVariable("cath", True), Jump("routes")]

screen cafemenu_1():
    fixed:
        style_prefix "navigation"

        add "bg menu1 pt"

        imagebutton auto "images/sprites/menu/tart_%s.png":
            xpos 334 
            ypos 186
            focus_mask True
            action [SetVariable("charlotte", True), Jump("routes")]

        imagebutton auto "images/sprites/menu/donut_%s.png":
            xpos 585
            ypos 754
            focus_mask True
            action [SetVariable("saki", True), Jump("routes")]

        imagebutton auto "images/sprites/menu/macaron_%s.png":
            xpos 991
            ypos 199
            focus_mask True
            action [SetVariable("amaya", True), Jump("routes")]

        imagebutton auto "images/sprites/menu/crepe_%s.png":
            xpos 1367
            ypos 711
            focus_mask True
            action [SetVariable("cath", True), Jump("routes")]