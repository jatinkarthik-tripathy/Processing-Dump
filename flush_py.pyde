def setup():
    global vp
    size(800, 600)
    background(255)
    vp = createGraphics(800, 600)

def draw():
    vp.beginDraw()

    vp.background(255)      
    translate(mouseX-(width/2), mouseY-(height/2))    
    fill(0)
    vp.ellipse(400, 200, 60, 60)

    vp.line(400, 200, 400, 500)

    vp.line(400, 300, 300, 400)

    vp.line(400, 300, 500, 400)

    vp.line(400, 500, 300, 600)

    vp.line(400, 500, 500, 600)

    vp.endDraw()
    image(vp, 0,0)
