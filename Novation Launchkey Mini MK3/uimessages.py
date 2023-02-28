### UI Messages
import variables as var
import ui
uimixer = {
    "Stop": "Ready to arm mixer tracks!",
    "Solo": "Ready to solo mixer tracks!",
    "Mute": "Ready to mute mixer tracks!",
    ""    : "Special mixer controls disabled!"
}

uichanrack = {
    "Stop" : "Ready to step-sequence the selected channel! ",
    "Solo" : "Ready to solo channels!",
    "Mute" : "Ready to mute channels!",
    ""     : "Special Channel rack controls disabled"
}

def SceneMsg(scenesel, mode):
    if scenesel == var.SCENE_SEL:
        for x,y in var.scmodes.items():
                if x == mode:
                    if scenesel == "Mixer":
                        for a,b in uimixer.items():
                            if y == a:
                                ui.setHintMsg(b)
                    if scenesel == "Channel rack":
                        for a,b in uichanrack.items():
                            if y == a:
                                ui.setHintMsg(b)
