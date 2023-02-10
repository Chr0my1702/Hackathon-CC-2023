import ursina
from ursina import * 

app = ursina.Ursina()

# Test Cube


class Test_cube(Entity):
	def __init__(self):
		super().__init__(
			parent=scene,
			model='cube',
			texture='white_cube',
			rotation=Vec3(45, 45, 45))

class Player(ursina.Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            color=ursina.color.azure,
            scale=(1, 2, 1),
            collider='box',
        )

    def input(self, key):
        if key == 'space':
            self.jump()

    def jump(self):
        self.y += 1


player = Player()
cube = Test_cube()
app.run()
