from vpython import*

mass=1
springlenth=100
g=9.8
t=0
dt=0.01
k=0.5

scene=canvas(width=4000,height=2000,center=vector(0,-50,0),background=vector(0,0,0.1))
xaxis=arrow(pos=vector(0,1,1), axis=vector(3,0,0), color=color.green)
yaxis=arrow(pos=vector(0,1,1), axis=vector(0,3,0), color=color.red)
zaxis=arrow(pos=vector(0,1,1), axis=vector(0,0,3), color=color.orange)

spring=helix(radius=2, pos=vector(0,0,0), axis=vector(0,-30,0),color=color.red, thickness=0.5,coils=17)
ceiling=box(pos=vector(0,0,0),axis=vector(0,1,0),length=1,height=50,width=10,color=color.green)
block=sphere(pos=vector(0,-30,0),axis=vector(1,0,0),length=8,height=8,width=8, color=color.yellow)


block.v=vector(0,0,0)
block.pos=vector(0,-30,0)

while t<500:
    rate(500)
    f=vector(0,-g,0)-k*(block.pos-vector(0,-30,0))
    a=f/mass
    block.v=block.v+a*dt
    block.pos=block.pos+block.v*dt
    t=t+dt
    spring.axis.y=block.pos.y
