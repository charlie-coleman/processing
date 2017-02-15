def setup():
    size(7680,4320)
    background(255)
    strokeWeight(6)
    smooth()
    colorMode(HSB, 100)
    start_color = 70
    size_part = 80
    x_start = -60*size_part
    y_start = 24*size_part
    while x_start < width+2*size_part:
        x = x_start
        y = y_start
        while x < width+2*size_part or y < height+2*size_part:
            stroke(100, 0, 0)
            noFill()
            octa(x,y,size_part)
            square(x+3.5*size_part,y+1.5*size_part,size_part/3)
            fill(100, 0, 0)
            fillin(x,y,size_part)
            x += 2*size_part
            y += 5*size_part
            start_color = (start_color+0.2)%100
        x_start += 5*size_part
        y_start -= 2*size_part
    saveFrame('output.png')

def octa(x,y,s):
    beginShape()
    x_scale=[0,2*s/3,s,2*s/3,0,-2*s/3,-s,-2*s/3]
    y_scale=[-s,-2*s/3,0,2*s/3,s,2*s/3,0,-2*s/3]
    for i in range(8):
        line(x+x_scale[i], y+y_scale[i], x+3*x_scale[i], y+3*y_scale[i])
        line(x+x_scale[(i-1)%8]+x_scale[i], y+y_scale[(i-1)%8]+y_scale[i],
             x+x_scale[(i-1)%8]+2*x_scale[i], y+y_scale[(i-1)%8]+2*y_scale[i])
        line(x+x_scale[(i+1)%8], y+y_scale[(i+1)%8],
             x+x_scale[(i+1)%8]+2*x_scale[i], y+y_scale[(i+1)%8]+2*y_scale[i])
    endShape()
    
def square(x,y,s):
    beginShape()
    x_scale=[-0.5*s,1.5*s,0.5*s,-1.5*s]
    y_scale=[-1.5*s,-0.5*s,1.5*s,0.5*s]
    for i in range(4):
        line(x+x_scale[i],y+y_scale[i],x+3*x_scale[i],y+3*y_scale[i])
        line(x+x_scale[(i-1)%4]+x_scale[i], y+y_scale[(i-1)%4]+y_scale[i],
             x+x_scale[(i-1)%4]+2*x_scale[i], y+y_scale[(i-1)%4]+2*y_scale[i])
        line(x+x_scale[(i+1)%4], y+y_scale[(i+1)%4],
             x+x_scale[(i+1)%4]+2*x_scale[i], y+y_scale[(i+1)%4]+2*y_scale[i])
    endShape()

def fillin(x,y,s):
    x_scale=[0,2*s/3,s,2*s/3,0,-2*s/3,-s,-2*s/3]
    y_scale=[-s,-2*s/3,0,2*s/3,s,2*s/3,0,-2*s/3]
    x_right=[   0.5*s,        s,  0.5*s/3,        0,  -0.5*s,    -s, -0.5*s/3,      0]
    y_right=[-0.5*s/3,        0,    0.5*s,        s, 0.5*s/3,     0,   -0.5*s,     -s]
    x_left= [  -2*s/3, -0.5*s/3,    2*s/3,    0.5*s,   2*s/3,   s/6,   -2*s/3, -0.5*s]
    y_left= [  -2*s/3,   -0.5*s,   -2*s/3, -0.5*s/3,   2*s/3, 0.5*s,    2*s/3,    s/6]
    for i in range(8):
        beginShape()
        vertex(x+x_scale[(i-1)%8]+x_scale[i], y+y_scale[(i-1)%8]+y_scale[i])
        vertex(x+x_scale[(i-1)%8]+2*x_scale[i], y+y_scale[(i-1)%8]+2*y_scale[i])
        vertex(x+x_scale[(i)%8]+2*x_scale[i-1]+x_right[i-1],
               y+y_scale[(i)%8]+2*y_scale[i-1]+y_right[i-1])
        vertex(x+x_scale[(i)%8]+2*x_scale[i-1], y+y_scale[(i)%8]+2*y_scale[i-1])
        endShape(CLOSE)