from vpython import*

bulletm=1
blockm=20
t=0
dt=0.005
b=0.5
f=vector(5,0,0)

scene=canvas(title='子彈撞木塊',width=1200,height=800,center=vector(20,0,0),background=vector(0,0,0.1))
xaxis=arrow(pos=vector(0,7,7), axis=vector(3,0,0), color=color.green)
yaxis=arrow(pos=vector(0,7,7), axis=vector(0,3,0), color=color.red)
zaxis=arrow(pos=vector(0,7,7), axis=vector(0,0,3), color=color.orange)

bullet=sphere(pos=vector(0,0,0), radius=0.5, color=vector(1,0,0), opacity=0.9 )
floor=box(pos=vector(25,-2.5,0),axis=vector(0,1,0),length=1,height=70,width=13)
block=box(pos=vector(30,0,0),axis=vector(1,0,0),length=5,height=5,width=5, color=color.green, opacity=0.4)

bullet.v=vector(5,0,0)
bullet.a=vector(0,0,0)
block.v=vector(0,0,0)
block.a=vector(0,0,0)

while t<20:
    rate(400)
    bullet.pos=bullet.pos+bullet.v*dt
    block.pos=block.pos+block.v*dt
     
    if abs(bullet.pos.x-block.pos.x)<=2.5 and bullet.v.x>=block.v.x:
      bullet.a=-f/bulletm
      bullet.v=bullet.v+bullet.a*dt
      bullet.pos=bullet.pos+bullet.v*dt
 
      block.a=f/blockm
      block.v=block.v+block.a*dt
      block.pos=block.pos+block.v*dt

      t=t+dt
    

