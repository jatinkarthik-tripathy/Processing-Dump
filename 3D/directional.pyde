#Collabed with Kshitij Nair

x = -1
x_chg = 0.01

def setup():
    size(600, 600, P3D)
    smooth(3)
    
def draw():
    global x, x_chg
    background(255, 0)

    pushMatrix()
    stroke(0, 100)
    strokeWeight(3)
    line(width/2, 0, 0, width/2-100*x, 150+(x*20), -x*100)
    spotLight(255, 100, 100, width/2-100*x, 150+(x*20), -x*100, 0, 1, 0, PI/2, 2);
    translate(width/2-100*x, 150+(x*20), -x*100)
    lights()
    ambientLight(50, 0, 100)
    fill(255, 100, 100)
    noStroke()
    sphere(20)
    
    popMatrix()
    
    noLights()
    pushMatrix()
    translate(width/2, height/2, 0)
    ambientLight(100, 0, 150)
    popMatrix()
    
    pushMatrix()
    spotLight(255, 100, 100, width/2-100*x, 150+(x*20), -x*100, 0, 1, 0, PI/2, 2);
    translate(width/2, 400, -100)
    fill(255)
    noStroke()
    sphere(100)
    popMatrix()
    
    x += x_chg
    if x>1 or x<-1:
        x_chg *= -1
    
