from vpython import*

mass=1
springlenth=100
k=1
t=0
dt=0.001
b=2

scene=canvas(width=1000,height=600,center=vector(20,0,0),background=vector(0,0,0.1))
xaxis=arrow(pos=vector(0,7,7), axis=vector(3,0,0), color=color.green)
yaxis=arrow(pos=vector(0,7,7), axis=vector(0,3,0), color=color.red)
zaxis=arrow(pos=vector(0,7,7), axis=vector(0,0,3), color=color.orange)

spring=helix(radius=2, pos=vector(0,0,0), axis=vector(30,0,0),color=color.red, thickness=0.5,coils=17)
wall=box(pos=vector(0,0,0),axis=vector(1,0,0),length=1,height=10,width=10)
floor=box(pos=vector(25,-5,0),axis=vector(0,1,0),length=1,height=50,width=10)
block=box(pos=vector(30,0,0),axis=vector(1,0,0),length=8,height=8,width=8, color=color.yellow)

graph1=graph(xtitle="time", ytitle="x-coordinate", xmin=0, xmax=5, ymin=10, ymax=50)
graph2=graph(xtitle="time", ytitle="velocity", xmin=0, xmax=5, ymin=-20, ymax=30)
graph3=graph(xtitle="time", ytitle="Energy", xmin=0, xmax=5, ymin=0, ymax=100)
xt=gcurve(graph=graph1, color=color.red)
vt=gcurve(graph=graph2, color=color.red)
ut=gcurve(graph=graph3, color=color.blue)
kt=gcurve(graph=graph3, color=color.orange)
et=gcurve(graph=graph3, color=color.red)

block.v=vector(30,0,0)
block.pos=vector(30,0,0)

while t<5:
    rate(300)
    f=-k*(block.pos-vector(30,0,0))-b*block.v
    a=f/mass
    block.v=block.v+a*dt
    block.pos=block.pos+block.v*dt
    t=t+dt
    spring.axis.x=block.pos.x

    xt.plot(pos=(t, block.pos.x))
    vt.plot(pos=(t, block.v.x))
    ut.plot(pos=(t, 0.5*k*(block.pos.x-30)**2))
    kt.plot(pos=(t, 0.5*mass*block.v.x**2))
    et.plot(pos=(t, 0.5*k*(block.pos.x-30)**2+ 0.5*mass*block.v.x**2))
    
        
        
