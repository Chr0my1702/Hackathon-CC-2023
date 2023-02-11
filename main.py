import threading
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from funcs import *

app = Ursina()
textures = {
    'sky': load_texture('assets/skybox.png'),
}
sounds = {
    'punch': Audio('assets/punch_sound', loop=False, autoplay=False),
}
block_pick = 1

window.fps_counter.enabled = True
window.exit_button.visible = False


NPC_Talk = Text(text="", enabled=False, background=True, origin=(
    0, -1), position=(0, 0), color=color.white, background_color=color.white)
agree = Button(text="ok!", parent=NPC_Talk,  enabled=False, size=(.3, .1))
disagree = Button(text="no", parent=NPC_Talk, enabled=False, size=(.3, .1))
agree.text_entity.size = 1
disagree.text_entity.size = 1


def update():
	global block_pick

	if held_keys['left mouse'] or held_keys['right mouse']:
		hand.active()
	else:
		hand.passive()

	if NPC_Talk.enabled == True:

		#lock player movement
		player.set_position((10, .25, 13))
		player.rotation = (0, 0, 0)

		if mouse.visible == False:
			current_position_player = player.position
			player.set_position((current_position_player.x,
			                    current_position_player.y, current_position_player.z))

			mouse.visible = True
			mouse.locked = False
	else:

		if mouse.visible == True:
			mouse.visible = False
			mouse.locked = True


class Voxel(Button):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block',
            origin_y=0.5,
            color=color.color(0, 0, random.uniform(0.9, 1)),
            scale=0.5)

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                sounds['punch'].play()
                #if block_pick == 1:
                #   voxel = Voxel(position=self.position +
                #                mouse.normal, texture=textures['g'])

            if key == 'right mouse down':
                sounds['punch'].play()
                destroy(self)


class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=textures['sky'],
            scale=150,
            double_sided=True)


class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            scale=0.2,
            rotation=Vec3(150, -10, 0),
            position=Vec2(0.4, -0.6))

    def active(self):
        self.position = Vec2(0.3, -0.5)

    def passive(self):
        self.position = Vec2(0.4, -0.6)


def npc_action():
    NPC_Talk.enabled = False
    text_size = NPC_Talk.world_scale
    button1_pos = ((NPC_Talk.position.x - text_size.x / 2 + .25)
                   * 0.03, (NPC_Talk.position.y - text_size.y / 2 - .05)*0.01)
    button2_pos = ((NPC_Talk.position.x + text_size.x / 2 - .25)
                   * 0.03, (NPC_Talk.position.y - text_size.y / 2 - .05)*0.01)

    agree.text = "Ok!"
    agree.scale = (.3, .1)
    agree.position = button1_pos
    agree.text_entity.size = 1
    agree.on_click = Func(setattr, NPC_Talk, 'enabled', False)

    disagree.text = "No"
    disagree.scale = (.3, .1)
    disagree.position = button2_pos
    disagree.text_entity.size = 1
    disagree.on_click = Func(setattr, NPC_Talk, 'enabled', False)

    if player.position.x >= npc.position.x - 4 and player.position.x <= npc.position.x + 4 and player.position.z >= npc.position.z - 4 and player.position.z <= npc.position.z + 4:
        NPC_Talk.enabled = True
        agree.enabled = True
        disagree.enabled = True

        NPC_Talk.text = auto_format(
            "Hello, I am a NPC. I am here to help you. I will give you a quest. Do you want to accept it?")
        thread = threading.Thread(target=speak_text, args=(NPC_Talk.text,))
        thread.start()
        NPC_Talk.background = True


npc_model = load_model("npc.glb")
npc = Entity(
    model=npc_model,
    position=(10, .25, 15),
    scale=1.75,
    rotation=(0, 0, 0),
    collider='box',
    on_click=npc_action)

for z in range(30):
    for x in range(30):
        voxel = Voxel(position=(x, 0, z))

player = FirstPersonController()
player.set_position((10, 0, 10))
sky = Sky()
hand = Hand()

app.run()
