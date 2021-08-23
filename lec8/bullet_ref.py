from vpython import*

ballm = 0.1
blockm = 1


scene=canvas(title='碰撞', width=1200, height=1000, center=vector(0,0,0), background=vector(0.5,0.5,0),)
block=box(pos=vector(0,0,0),axis=vector(1,0,0),length=4,height=4,width=4,color=color.white,opacity=0.2)
ball=sphere(pos=vector(-10,0,0),radius=0.5,color=color.black,opacity=0.9)

ball.v=vector(10,0,0)
block.v=vector(0,0,0)
block.a= vector(0,0,0)
ball.a=vector(0,0,0)
t = 0
dt = 0.01
b = 1


while t < 30:
    rate(50)
    
    if  abs(block.pos.x - ball.pos.x) <= 2.5 and ball.v.x >= block.v.x :
        coll = 1
    else:
        coll = 0
        
    f = coll*(-b)
    block.a.x = -f/blockm
    block.v.x = block.v.x + block.a.x*dt
    block.pos.x = block.pos.x + block.v.x*dt

    
    ball.a.x = f/ballm
    ball.v.x = ball.v.x + ball.a.x*dt
    ball.pos.x = ball.pos.x + ball.v.x*dt

    t = t + dt
