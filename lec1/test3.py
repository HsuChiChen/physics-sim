from vpython import*

t=0
dt=0.05
ballr=0.5
ballp=vector(-3,0,0)
ballv=vector(2,0,0)

scene=canvas(width=1200,height=800,center=vector(0,0,0),background=vector(0.5,0.5,0),range=6)

xaxis=arrow(pos=vector(0,0,0),axis=vector(1,0,0),color=color.green)
yaxis=arrow(pos=vector(0,0,0),axis=vector(1,0,0),color=color.red)
zaxis=arrow(pos=vector(0,0,0),axis=vector(1,0,0),color=color.orange)

ball=sphere(color=color.red)
ball.radius=ballr
ball.pos=ballp
ball.v=ballv

while t<=50 : 
    rate(100) 
    print("(time,x)=",(t,ball.pos.x)) 
    ball.pos=ball.pos+ball.v*dt
    t=t+dt 
