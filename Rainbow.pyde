def setup():
    size(400, 400)
    background(106, 196, 247)
    
def draw():
    r=400
    for i in range(10):
        fill(106, 196, 247)
        strokeWeight(10)
        stroke(random(255), random(255), random(255))
        ellipse(400, 400, r, r)
        ellipse(0, 0, r, r)
        ellipse(400, 0, r, r)
        ellipse(0, 400, r, r)
        fill(random(255), random(255), random(255))
        ellipse(200, 200, 50, 50)
        r -= 10

    
    
