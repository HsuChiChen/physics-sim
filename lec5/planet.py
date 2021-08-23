from vpython import*

scene=canvas(title="雙星運動",width=1000,height=600,center=vector(0,0,0),background=vector(0,0,0.1))
xaxis=arrow(pos=vector(0,7,7), axis=vector(3,0,0), color=color.green)
yaxis=arrow(pos=vector(0,7,7), axis=vector(0,3,0), color=color.red)
zaxis=arrow(pos=vector(0,7,7), axis=vector(0,0,3), color=color.orange)

mass1=1
mass2=1000
G=1000
t=0
dt=0.001

m1=sphere(pos=vector(-200,0,0),radius=10,make_trail=True,color=color.green)
m2=sphere(pos=vector(0,0,0),radius=50,make_trail=True,color=color.yellow)

m1.v=vector(0,70,0)
m2.v=vector(0,0,0)
dis12=mag(m1.pos-m2.pos)

while dis12>100+5:
    rate(300)
    dis12=mag(m1.pos-m2.pos)
    f1=G*mass1*mass2*(m1.pos-m2.pos)/dis12**3
    m1.a=-f1/mass1
    m1.v=m1.v+m1.a*dt
    m1.pos=m1.pos+m1.v*dt

    f2=G*mass1*mass2*(m2.pos-m1.pos)/dis12**3
    m2.a=-f2/mass2
    m2.v=m2.v+m2.a*dt
    m2.pos=m2.pos+m2.v*dt
    t=t+dt

    
