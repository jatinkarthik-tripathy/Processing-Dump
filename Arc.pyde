def setup():
    global st, ed, r
    r = 50
    st = radians(0)
    ed = radians(0+1)
    size(800, 800)
    translate(width/2, height/2)
    
def draw():
    global st, ed, r
    background(255)
    strokeWeight(19)
    stroke(0)
    arc(0, 0, r, r, st, ed)
    ed += radians(1)
    r += 2   
