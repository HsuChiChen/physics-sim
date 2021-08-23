from vpython import *

t=0
dt=0.01
g=9.8
boxh=0.1
ballr=3
ballp=vector(0,70,0)
ballv=vector(0,0,0)
balla=vector(0,-g,0)
ballm=0.1
b=0.01

scene=canvas(width=1200,height=800,center=vector(0,3,0),background=vector(0.5,0.5,0))
myground=box(length=10,height=boxh,width=10,pos=vector(0,0,0),axis=vector(0,0,1),color=vector(2,5,4))
ball=sphere(radius=ballr,color=color.red,pos=ballp)

ball.pos=ballp
ball.v=ballv
ball.a=balla
graph1=graph(xtitle="time",ytitle="v",xmin=0,xmax=50,ymin=0,ymax=70)
vt=gcurve(graph=graph1,color=color.red)

while t<=50:
    rate(1000)
    ftotal=ballm*vector(0,-g,0)-b*ball.v
    ball.a=ftotal/ballm
    ball.v=ball.v+ball.a*dt
    ball.pos=ball.pos+ball.v*dt
    t=t+dt
    if ball.pos.y<(ballr+boxh/2):
        ball.v.y=-ball.v.y
    vt.plot(pos=(t+dt,ball.pos.y))
