from vpython import *

t=0
dt=0.01
g=9.8
ballr=3
ballp=vector(0,70,0)
ballv=vector(50,0,0)
balla=vector(0,-g,0)
ballm=0.1
b=0.01

scene=canvas(width=1200,height=800,center=vector(0,3,0),background=vector(0.5,0.5,0))
ball=sphere(radius=ballr,color=color.red,pos=ballp)
figure1=graph(xtitle="time",ytitle="abs(Vy)",xmin=0,xmax=100,ymin=0,ymax=150)
vyt=gcurve(graph=figure1,color=color.red)
figure2=graph(xtitle="time",ytitle="abs(Vx)",xmin=0,xmax=100,ymin=0,ymax=150)
vxt=gcurve(graph=figure2,color=color.red)

ball.pos=ballp
ball.v=ballv
ball.a=balla

while t<=100:
    rate(1000)
    ftotal=ballm*vector(0,-g,0)-b*ball.v
    ball.a=ftotal/ballm
    ball.v=ball.v+ball.a*dt
    ball.pos=ball.pos+ball.v*dt
    t=t+dt
    vyt.plot(pos=(t+dt,abs(ball.v.y)))
    vxt.plot(pos=(t+dt,abs(ball.v.x)))
