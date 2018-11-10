x = 1
def setup():
    size(800, 600, P3D)

def draw():
    global x
    background(0)
    noStroke()
    translate(width/2, height/2, 0)
    ambient(102, 102, 102)
    lightSpecular(204, 204, 204)
    directionalLight(204, 204, 204, -.5, 0, -1)
    specular(255, 255, 255)
    shininess(50)
    pushMatrix()
    x += .5
    rotate(radians(x))
    #sphereDetail(5)
    sphere(200)
    popMatrix()
 
