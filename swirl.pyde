class objects:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw_obs(self):
        ellipse(self.x, self.y, 5, 5)


def setup():
    global obs, tot
    tot=1000
    size(800, 800)
    frameRate(120)
    obs = []
    y = 10
    for i in range(tot):
        o = objects(0, y)
        y += 1
        obs.append(o)

def draw():
    background(255)
    translate(400, 400)
    i = 0
    fill(0)
    for i, o in zip(range(tot), obs):
        ratio = i/tot
        sprial_rad = ratio*200
        angle = i*radians(25)
        o.x += cos(angle)*sprial_rad
        o.y += sin(angle)*sprial_rad
        rotate(radians(0.05*frameCount))
        ellipse(o.x, o.y, 5, 5)
    
