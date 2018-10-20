def setup():
    size(800, 800, P3D)
    background(0)
    
def draw():
    
    lights()
    ambientLight(0, 0, 255)
    camera(width/2, -100, 1000, width/2, height/2, 0, 0, 1, 0)
    
    fill(255)
    noStroke()
    pushMatrix()
    translate(width/2.5, height/2, 0)
    sphere(100)
    popMatrix()
    
    pushMatrix()
    translate(width/1.5, height/2, 0)
    box(200)
    popMatrix()
