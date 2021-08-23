print("hello world")

from vpython import*
scene=canvas(title="pedulum",width=1200,height=1000,center=vector(5,5,5),background=vector(0.5,0.5,0),range=(5))
ball=sphere(pos=vector(2,2,2),radius=0.63,color=vector(1,0,0),opacity=0.9)
mybox=box(pos=vector(1,2,1),axis=vector(1,-1.5,2),length=1,height=1.5,width=2)
rod=cylinder(pos=vector(1,2,1),axis=vector(1,-1.5,2),radius=0.2)
pointer=arrow(pos=vector(1,2,1),axis=vector(1,-1.5,2))
spring=helix(pos=vector(1,2,1),axis=vector(1,-1.5,2),thickness=0.1,radius=0.5)
donut=ring(pos=vector(1,2,1),axis=vector(1,-1.5,2),thickness=0.1,radius=0.5)
