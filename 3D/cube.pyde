var = 2
z = -1000
def setup():
    size(600, 600, P3D)
    
def draw():
    global z
    background(0)
    fov = PI/3
    cameraZ = (height/2.0) / tan(fov/2.0)
    #print(cameraZ)
    perspective(fov, float(width/2)/float(height/2), 10.0, -1000)
    camera(width/2, height/var, (height/2)/(tan(PI/6)), width/2, height/2, 0, 0, 1, 0)
    lights()
    
    pushMatrix()
    translate(width/2, height/2, 0)
    strokeWeight(5)
    stroke(255)
    line(-300, 0, 0, 300, 0, 0)
    line(0, -300, 0, 0, 300, 0)
    line(0, 0, -300, 0, 0, 300)
    popMatrix()
    
    #cube
    pushMatrix()
    translate(width/2, height/2, z)
    rotateX(-PI/6)
    rotateY(PI/6)
    fill(255)
    box(100)
    popMatrix()
    z += 3

def mouseReleased():
    global var
    var = 2

def mousePressed():
    global var
    var=4
