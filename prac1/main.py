#!/usr/bin/env python

import vtk
import numpy as np

"""
NOTE:
- SetResolution: nof facets
TODO:
    - More actooors !!
"""

ActorsList={
    "home": {
        "source":"cube",
        "pos": [0.0,0.0,0.0],
        "xlength": 1,
        "ylength": 1,
        "zlength": 1,
        "color": [.15,.15,.15],
        "orientation": [0,0,0],
    },
    "roof": {
        "source": "cone",
        "pos": [0.0,1.0,0.0],
        "radius": 0.7,
        "height": 1.0,
        "resolution": 100,
        "color": [0.98,.28,.20],
        "orientation": [0,0,90],
    },
    "win": {
        "source":"cube",
        "pos": [0.0,0.0,.5],
        "xlength": .6,
        "ylength": .4,
        "zlength": .1,
        "color": [.51,.64,.59],
        "orientation": [0,0,0],
    },
    "door": {
        "source":"cube",
        "pos": [.55,-0.15,0.0],
        "xlength": .4,
        "ylength": .7,
        "zlength": .1,
        "color": [.65,.59,.51],
        "orientation": [0,90,0],
    },
    "handle": {
        "source":"sphere",
        "pos": [0.6,-.15,0.1],
        "radius": .05,
        "thetaResolution": 100,
        "color": [.72,.73,.14],
        "orientation": [0,0,0],
    },
}

tree_trunk = {
    "source": "cube",
    "xlength": .3,
    "ylength": 1.5,
    "zlength": .3,
    "color": [.4,.33,.32],
    "orientation": [0,0,0],
}

tree_leaf = {
    "source": "cube",
    "xlength": .8,
    "ylength": .8,
    "zlength": .8,
    "color": [.72,.73,.14],
    "orientation": [0,0,0],
}
cherry = {
    "source":"sphere",
    #x dist, bush's Y - cheery's radius, z
    "pos": [3-.2/2-.025,0,0],
    "radius": .025,
    "thetaResolution": 100,
    "color": [0.98,.28,.20],
    "orientation": [0,0,0],
}
bush = {
    "source": "cube",
    "pos": [3,0,0],
    "xlength": .2,
    "ylength": .2,
    "zlength": .2,
    "color": [.72,.73,.14],
    "orientation": [0,0,0],
}

def randomCherries(actor, bush, quantity, toappend):
    X=bush["pos"][0]
    x=bush["xlength"]/2
    Y=bush["pos"][1]
    y=bush["ylength"]/2
    Z=bush["pos"][2]
    z=bush["zlength"]
    pa=[X - x/2, Y+y/2, Z+z/2]
    pb=[X - x/2, Y-y/2, Z-z/2]
    pc=[X + x/2, Y+y/2, Z-z/2]
    pd=[X + x/2, Y-y/2, Z+z/2]
    #randoms
#    print(pa)
#    print(pb)
    for i in range(quantity):
        random_y=np.random.rand()*(pa[1]-pb[1])+pb[1]
        random_z=np.random.rand()*(pa[2]-pb[2])+pb[2]
        actor["pos"]=[X-bush["xlength"]/2, random_y, random_z]
        toappend["bush"+str(random_y)+str(random_z)]=actor.copy()
#    print(pb)
#    print(pc)
        random_x=np.random.rand()*(pb[0]-pc[0])+pc[0]
        random_y=np.random.rand()*(pb[1]-pc[1])+pc[1]
        actor["pos"]=[ random_x, random_y, Z-bush["zlength"]/2]
        toappend["bush"+str(random_x)+str(random_y)]=actor.copy()
#    print(pc)
#    print(pd)
#    for i in range(quantity):
        random_y=np.random.rand()*(pc[1]-pd[1])+pd[1]
        random_z=np.random.rand()*(pc[2]-pd[2])+pd[2]
        actor["pos"]=[X+bush["xlength"]/2, random_y, random_z]
        toappend["bush"+str(random_y)+str(random_z)]=actor.copy()
#    print(pd)
#    print(pa)
        random_x=np.random.rand()*(pd[0]-pa[0])+pa[0]
        random_y=np.random.rand()*(pd[1]-pa[1])+pa[1]
        actor["pos"]=[random_x, random_y, Z+bush["zlength"]/2]
        toappend["bush"+str(random_x)+str(random_y)]=actor.copy()


def circleAroundCenter(actor, toappend, radius, quantity, name, y=0.0, z=0.0):
    theta=360/quantity
    rad=theta*np.pi/180
    #we dont care about Y
    #X,Z only
    rotationMatrix=np.array([
            [np.cos(rad),  0.0, np.sin(rad)],
            [0.0,          1.0, 0.0        ],
            [-np.sin(rad), 0.0, np.cos(rad)],
        ])
    counter=theta
    actor["pos"]=np.array([radius,y,z])
    while counter <= 360.0:
        actor["pos"]=rotationMatrix@actor["pos"]
        toappend[name+str(counter)]=actor.copy()
        if name == "bush":
            randomCherries(cherry, toappend[name+str(counter)], 5, toappend)
        counter+=theta

circleAroundCenter(tree_trunk, ActorsList, 2.0, 10, "tree_trunk")
circleAroundCenter(tree_leaf, ActorsList, 2.0, 10, "tree_leaf", y=1.0)
circleAroundCenter(bush, ActorsList, 3.0, 60, "bush", y=-.6)


def setEverything(a_dict):
    values=dict()
    for k, v in a_dict.items():
        values[k]=dict()

        if v["source"]=="cube":
            #source
            values[k]["vtkSource"]=vtk.vtkCubeSource()
            values[k]["vtkSource"].SetXLength(v["xlength"])
            values[k]["vtkSource"].SetYLength(v["ylength"])
            values[k]["vtkSource"].SetZLength(v["zlength"])
            values[k]["vtkSource"].Update()
        if v["source"]=="cone":
            values[k]["vtkSource"]=vtk.vtkConeSource()
            values[k]["vtkSource"].SetRadius(v["radius"])
            values[k]["vtkSource"].SetHeight(v["height"])
            values[k]["vtkSource"].SetResolution(v["resolution"])
            values[k]["vtkSource"].Update()
        if v["source"]=="sphere":
            values[k]["vtkSource"]=vtk.vtkSphereSource()
            values[k]["vtkSource"].SetRadius(v["radius"])
            values[k]["vtkSource"].SetThetaResolution(v["thetaResolution"])
            values[k]["vtkSource"].Update()

        #map
        values[k]["vtkMap"]=vtk.vtkPolyDataMapper()
        values[k]["vtkMap"].SetInputData(values[k]["vtkSource"].GetOutput())

        #actor
        values[k]["vtkActor"]=vtk.vtkActor()
        values[k]["vtkActor"].SetPosition(v["pos"])
        values[k]["vtkActor"].SetMapper(values[k]["vtkMap"])
        values[k]["vtkActor"].GetProperty().SetColor(v["color"])
        values[k]["vtkActor"].SetOrientation(v["orientation"])
    return values

res = setEverything(ActorsList)

#renderer
renderer=vtk.vtkRenderer()
renderer.SetBackground(0.0,0.0,0.0)
for v in res.values():
    renderer.AddActor(v["vtkActor"])

#renderWindow
render_window=vtk.vtkRenderWindow()
render_window.SetWindowName('Simple VTK scene')
render_window.SetSize(400,400)
render_window.AddRenderer(renderer)

#interactor
interactor=vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

#initialize the interactor and
# start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()
