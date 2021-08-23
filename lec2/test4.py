from vpython import*

t=0
dt=0.01
ballr=8
ballp=vector(-3,0,0)
ballv=vector(5,0,0)

scene=canvas(title="mowmow",width=1000,height=500,center=vector(0,0,0),background=vector(0,0,0),range=6)

xaxis=arrow(pos=vector(0,0,0),axis=vector(10,0,0),color=color.green) 
yaxis=arrow(pos=vector(0,0,0),axis=vector(0,10,0),color=color.red)
zaxis=arrow(pos=vector(0,0,0),axis=vector(0,0,10),color=color.orange)

ball=sphere(color=vector(0.5,5,5),opacity=0.5)
ball.radius=ballr
ball.pos=ballp
ball.v=ballv

graph1=graph(x=800,y=0,xtitle="time",ytitle="x",xmin=0,xmax=50,ymin=0,ymax=4)
xt=gcurve(graph=graph1,color=color.red)


while t<=50:
    rate(100)
    ball.pos=ball.pos+ball.v*dt
    t=t+dt
    xt.plot(pos=(t,(ball.pos.x)))
