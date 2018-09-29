def setup():
    global c1, c2
    size(400, 400)
    background(255)
    c1 = createGraphics(400, 400)
    c2 = createGraphics(400, 400)
def draw():
    c1.beginDraw()
    strokeWeight(5)
    stroke(0)
    fill(255)
    ellipse(200, 200, 200, 200)
    c1.endDraw()
    image(c1, 0, 0)
    
    c2.beginDraw()
    strokeWeight(5)
    stroke(0)
    fill(0, 0)
    ellipse(250, 250, 200, 200)    
    c2.endDraw()
    image(c2, 0, 0)
