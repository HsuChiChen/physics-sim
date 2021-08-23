from vpython import *

t=0
dt=0.001
g=0.01
ballr=0.1
ballp=vector(6.1,2,0)
ballv=vector(-100,5,3)
balla=vector(0,-g,0)
ballm=0.1
b=0.1

scene=canvas(width=1200,height=800,center=vector(0,0,0),background=vector(0,0,0.1))
ball=sphere(radius=ballr,color=color.white,pos=ballp)
mybox=box(pos=vector(0,0,0),height=0.01,axis=vector(0,0,1),length=6.1,width=13.4,color=color.green)

xaxis=arrow(pos=vector(0,0,0),axis=vector(0.1,0,0),color=color.green)
yaxis=arrow(pos=vector(0,0,0),axis=vector(0,0.1,0),color=color.red)
zaxis=arrow(pos=vector(0,0,0),axis=vector(0,0,0.1),color=color.orange)

figure1=graph(xtitle="time",ytitle="abs(Vy)",xmin=0,xmax=30,ymin=0,ymax=3)
vyt=gcurve(graph=figure1,color=color.red)
figure2=graph(xtitle="time",ytitle="abs(Vx)",xmin=0,xmax=30,ymin=0,ymax=3)
vxt=gcurve(graph=figure2,color=color.red)
figure3=graph(xtitle="time",ytitle="abs(Vz)",xmin=0,xmax=30,ymin=0,ymax=3)
vzt=gcurve(graph=figure3,color=color.red)

ball.pos=ballp
ball.v=ballv
ball.a=balla

while ball.pos.y>=0:
    rate(100)
    ftotal=ballm*vector(0,-g,0)-b*ball.v*mag(ball.v)
    ball.a=ftotal/ballm
    ball.v=ball.v+ball.a*dt
    ball.pos=ball.pos+ball.v*dt
    t=t+dt
    vyt.plot(pos=(t+dt,abs(ball.v.y)))
    vxt.plot(pos=(t+dt,abs(ball.v.x)))
    vzt.plot(pos=(t+dt,abs(ball.v.z)))
