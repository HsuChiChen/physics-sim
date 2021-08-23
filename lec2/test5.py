from vpython import *

t=0
dt=0.1
g=0.98
boxh=0.01

ballr=0.2
ballp=vector(0,5,0)
ballv=vector(0,0,0)
ballm=0.1

scene=canvas(width=1200,height=800,center=vector(0,3,0),background=vector(0.5,0.5,0),range=6)
myground=box(length=10,height=boxh,width=3,pos=vector(0,0,0),axis=vector(1,0,0))

ball=sphere(radius=ballr,color=color.red)
ball.pos=ballp
ball.v=ballv

graph1=graph(x=800,y=0,xtitle="time", ytitle="v",xmin=0,xmax=50,ymin=0,ymax=4)
graph2=graph(x=800,y=400,xtitle="time",ytitle="y",xmin=0,xmax=50,ymin=0,ymax=5)
vt=gcurve(graph=graph1,color=color.yellow)
yt=gcurve(graph=graph2,color=color.yellow)

while t<=50:
    rate(300)
    ball.a=vector(0,-g,0)
    ball.pos=ball.pos+ball.v*dt
    ball.v=ball.v+ball.a*dt
if ball.pos.y<(ballr+boxh/2):
   ball.v.y =-ball.v.y
   vt.plot(pos=(t,abs(ball.v.y)))
   yt.plot(pos=(t,ball.pos.y))
   t=t+dt
