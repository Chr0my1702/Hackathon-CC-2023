import ursina

app = ursina.Ursina()


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

app.run()


#copilot: How do i make a requirement.txt file?

#me: pip freeze > requirements.txt
