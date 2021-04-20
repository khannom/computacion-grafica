import vtk
import numpy as np
from random import seed
from random import randint

seed(1)

ActorsList = {}

cherry = {
    "source":"sphere",
    #x dist, bush's Y - cheery's radius, z
    "pos": [3-.2/2-.025,0,0],
    "radius": .5,
    "thetaResolution": 20,
    "color": [0.98,.28,.20],
    "orientation": [0,0,0],
}
bush = {
    "source": "cube",
    "pos": [3,0,0],
    "xlength": 5,
    "ylength": 5,
    "zlength": 5,
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

circleAroundCenter(bush, ActorsList, 80.0, 60, "bush", y=1.5)



def crearArbol(x, z, renderer):
    tallo = vtk.vtkCylinderSource()
    tallo.SetCenter(0, 0, 0)
    tallo.SetHeight(50)
    tallo.SetRadius(3)
    tallo.SetResolution(20)
    tallo.Update()

    hoja1 = vtk.vtkSphereSource()
    hoja1.SetRadius(15)
    hoja1.Update()

    hoja2 = vtk.vtkSphereSource()
    hoja2.SetRadius(15)
    hoja2.Update()

    hoja3 = vtk.vtkSphereSource()
    hoja3.SetRadius(15)
    hoja3.Update()

    hoja4 = vtk.vtkSphereSource()
    hoja4.SetRadius(15)
    hoja4.Update()

    hoja5 = vtk.vtkSphereSource()
    hoja5.SetRadius(15)
    hoja5.Update()

    hoja6 = vtk.vtkSphereSource()
    hoja6.SetRadius(15)
    hoja6.Update()

    mapperTallo = vtk.vtkPolyDataMapper()
    mapperTallo.SetInputData(tallo.GetOutput())

    mapperHoja1 = vtk.vtkPolyDataMapper()
    mapperHoja1.SetInputData(hoja1.GetOutput())

    mapperHoja2 = vtk.vtkPolyDataMapper()
    mapperHoja2.SetInputData(hoja2.GetOutput())

    mapperHoja3 = vtk.vtkPolyDataMapper()
    mapperHoja3.SetInputData(hoja3.GetOutput())

    mapperHoja4 = vtk.vtkPolyDataMapper()
    mapperHoja4.SetInputData(hoja4.GetOutput())

    mapperHoja5 = vtk.vtkPolyDataMapper()
    mapperHoja5.SetInputData(hoja5.GetOutput())

    mapperHoja6 = vtk.vtkPolyDataMapper()
    mapperHoja6.SetInputData(hoja6.GetOutput())

    actorTallo1 = vtk.vtkActor()
    actorTallo1.SetMapper(mapperTallo)
    actorTallo1.GetProperty().SetColor(196/255, 133/255, 15/255)
    actorTallo1.SetPosition(x, 25, z)

    actorHoja1_1 = vtk.vtkActor()
    actorHoja1_1.SetMapper(mapperHoja1)
    actorHoja1_1.GetProperty().SetColor(0.0, 1.0, 0.0)
    actorHoja1_1.SetPosition(x, 60, z)

    actorHoja1_2 = vtk.vtkActor()
    actorHoja1_2.SetMapper(mapperHoja2)
    actorHoja1_2.GetProperty().SetColor(0.0, 1.0, 0.0)
    actorHoja1_2.SetPosition(x, 60, z+15)

    actorHoja1_3 = vtk.vtkActor()
    actorHoja1_3.SetMapper(mapperHoja3)
    actorHoja1_3.GetProperty().SetColor(0.0, 1.0, 0.0)
    actorHoja1_3.SetPosition(x, 60, z-15)

    actorHoja1_4 = vtk.vtkActor()
    actorHoja1_4.SetMapper(mapperHoja4)
    actorHoja1_4.GetProperty().SetColor(0.0, 1.0, 0.0)
    actorHoja1_4.SetPosition(x+15, 60, z)

    actorHoja1_5 = vtk.vtkActor()
    actorHoja1_5.SetMapper(mapperHoja5)
    actorHoja1_5.GetProperty().SetColor(0.0, 1.0, 0.0)
    actorHoja1_5.SetPosition(x-15, 60, z)

    actorHoja1_6 = vtk.vtkActor()
    actorHoja1_6.SetMapper(mapperHoja6)
    actorHoja1_6.GetProperty().SetColor(0.0, 1.0, 0.0)
    actorHoja1_6.SetPosition(x, 75, z)

    renderer.AddActor(actorTallo1)
    renderer.AddActor(actorHoja1_1)
    renderer.AddActor(actorHoja1_2)
    renderer.AddActor(actorHoja1_3)
    renderer.AddActor(actorHoja1_4)
    renderer.AddActor(actorHoja1_5)
    renderer.AddActor(actorHoja1_6)


def crearLapiz(x, z, renderer):
    cuerpo = vtk.vtkCylinderSource()
    cuerpo.SetRadius(0.25)
    cuerpo.SetHeight(2)
    cuerpo.SetResolution(50)
    cuerpo.Update()

    borrador = vtk.vtkSphereSource()
    borrador.SetRadius(0.26)
    borrador.SetThetaResolution(50)
    borrador.Update()

    cabeza = vtk.vtkConeSource()
    cabeza.SetRadius(0.25)
    cabeza.SetHeight(0.5)
    cabeza.SetResolution(100)
    cabeza.Update()

    mapperCuerpo = vtk.vtkPolyDataMapper()
    mapperCuerpo.SetInputData(cuerpo.GetOutput())

    mapperBorrador = vtk.vtkPolyDataMapper()
    mapperBorrador.SetInputData(borrador.GetOutput())

    mapperCabeza = vtk.vtkPolyDataMapper()
    mapperCabeza.SetInputData(cabeza.GetOutput())

    actorCuerpo = vtk.vtkActor()
    actorCuerpo.SetMapper(mapperCuerpo)
    actorCuerpo.GetProperty().SetColor(235/255, 247/255, 2/255)
    actorCuerpo.RotateX(90)
    actorCuerpo.SetPosition(x, 0.125, z)

    actorBorrador = vtk.vtkActor()
    actorBorrador.SetMapper(mapperBorrador)
    actorBorrador.GetProperty().SetColor(242/255, 63/255, 159/255)
    actorBorrador.SetPosition(x, 0.125, z+1)

    actorCabeza = vtk.vtkActor()
    actorCabeza.SetMapper(mapperCabeza)
    actorCabeza.GetProperty().SetColor(230/255, 167/255, 67/255)
    actorCabeza.RotateY(90)
    actorCabeza.SetPosition(x, 0.125, z-1.25)

    renderer.AddActor(actorCuerpo)
    renderer.AddActor(actorBorrador)
    renderer.AddActor(actorCabeza)


def crearPiedra(x, z, renderer):
    piedra = vtk.vtkSphereSource()
    piedra.SetRadius(3)
    piedra.SetThetaResolution(4)
    piedra.Update()

    mapperPiedra = vtk.vtkPolyDataMapper()
    mapperPiedra.SetInputData(piedra.GetOutput())

    actorPiedra = vtk.vtkActor()
    actorPiedra.SetMapper(mapperPiedra)
    actorPiedra.GetProperty().SetColor(135/255, 133/255, 128/255)
    actorPiedra.SetPosition(x, 0, z)

    renderer.AddActor(actorPiedra)


def crearAve(x, y, z, renderer):
    cuerpo = vtk.vtkSphereSource()
    cuerpo.SetRadius(4)
    cuerpo.SetThetaResolution(50)
    cuerpo.SetPhiResolution(50)
    cuerpo.Update()

    ojo = vtk.vtkSphereSource()
    ojo.SetRadius(0.5)
    ojo.SetThetaResolution(25)
    ojo.Update()

    ala = vtk.vtkCubeSource()
    ala.SetXLength(3)
    ala.SetYLength(1)
    ala.SetZLength(3)
    ala.Update()

    mapperCuerpo = vtk.vtkPolyDataMapper()
    mapperCuerpo.SetInputData(cuerpo.GetOutput())

    mapperAla = vtk.vtkPolyDataMapper()
    mapperAla.SetInputData(ala.GetOutput())

    mapperOjo = vtk.vtkPolyDataMapper()
    mapperOjo.SetInputData(ojo.GetOutput())

    actorCuerpo = vtk.vtkActor()
    actorCuerpo.SetMapper(mapperCuerpo)
    actorCuerpo.GetProperty().SetColor(1.0, 0, 0)
    actorCuerpo.SetPosition(x, y, z)

    actorAlaD = vtk.vtkActor()
    actorAlaD.SetMapper(mapperAla)
    actorAlaD.GetProperty().SetColor(1,0,0)
    actorAlaD.SetPosition(x+4,y-1,z)
    actorAlaD.RotateZ(-45)

    actorAlaI = vtk.vtkActor()
    actorAlaI.SetMapper(mapperAla)
    actorAlaI.GetProperty().SetColor(1,0,0)
    actorAlaI.SetPosition(x-4,y-1,z)
    actorAlaI.RotateZ(45)

    actorPico = vtk.vtkActor()
    actorPico.SetMapper(mapperAla)
    actorPico.GetProperty().SetColor(232/255, 151/255, 51/255)
    actorPico.SetPosition(x,y,z+4.5)

    actorOjoD = vtk.vtkActor()
    actorOjoD.SetMapper(mapperOjo)
    actorOjoD.GetProperty().SetColor(0,0,0)
    actorOjoD.SetPosition(x-1,y+2,z+3)

    actorOjoI = vtk.vtkActor()
    actorOjoI.SetMapper(mapperOjo)
    actorOjoI.GetProperty().SetColor(0,0,0)
    actorOjoI.SetPosition(x+1,y+2,z+3)

    renderer.AddActor(actorCuerpo)
    renderer.AddActor(actorAlaD)
    renderer.AddActor(actorAlaI)
    renderer.AddActor(actorPico)
    renderer.AddActor(actorOjoD)
    renderer.AddActor(actorOjoI)

# source
cone = vtk.vtkConeSource()
cone.SetRadius(14.14)
cone.SetHeight(14.14)
cone.SetResolution(100)
cone.Update()

cube = vtk.vtkCubeSource()
cube.SetXLength(20)
cube.SetYLength(20)
cube.SetZLength(20)
cube.Update()

pasto = vtk.vtkCubeSource()
pasto.SetXLength(1000)
pasto.SetYLength(0)
pasto.SetZLength(1000)
pasto.Update()

window = vtk.vtkCubeSource()
window.SetXLength(15)
window.SetYLength(7)
window.SetZLength(1)
window.Update()

door = vtk.vtkCubeSource()
door.SetXLength(1)
door.SetYLength(15)
door.SetZLength(7)
door.Update()

chapa = vtk.vtkSphereSource()
chapa.SetRadius(0.5)
chapa.Update()

window2 = vtk.vtkCubeSource()
window2.SetXLength(15)
window2.SetYLength(7)
window2.SetZLength(1)
window2.Update()

# create a transform that rotates the cone
transform = vtk.vtkTransform()
transform.RotateWXYZ(90, 0, 0, 1)
transformFilter = vtk.vtkTransformPolyDataFilter()
transformFilter.SetTransform(transform)
transformFilter.SetInputConnection(cone.GetOutputPort())
transformFilter.Update()

# axes
transformAxes = vtk.vtkTransform()
transformAxes.Translate(0.0, 0.0, 0.0)
axes = vtk.vtkAxesActor()
axes.SetUserTransform(transformAxes)

# mapper
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputConnection(transformFilter.GetOutputPort())

mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputData(cube.GetOutput())

mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputData(window.GetOutput())

mapper4 = vtk.vtkPolyDataMapper()
mapper4.SetInputData(door.GetOutput())

mapper5 = vtk.vtkPolyDataMapper()
mapper5.SetInputData(chapa.GetOutput())

mapper6 = vtk.vtkPolyDataMapper()
mapper6.SetInputData(window2.GetOutput())

##############

mapperPasto = vtk.vtkPolyDataMapper()
mapperPasto.SetInputData(pasto.GetOutput())

# actor
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor1.GetProperty().SetColor(1.0, 0.0, 0.0)
actor1.SetPosition(20, 27.07, 0)

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.GetProperty().SetColor(240/255, 240/255, 40/255)
actor2.SetPosition(20, 10, 0)

actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor3.GetProperty().SetColor(0.0, 0.0, 1.0)
actor3.SetPosition(20, 10, 10)

actor4 = vtk.vtkActor()
actor4.SetMapper(mapper4)
actor4.GetProperty().SetColor(1.0, 0.0, 1.0)
actor4.SetPosition(10, 7.5, 0)

actor5 = vtk.vtkActor()
actor5.SetMapper(mapper5)
actor5.GetProperty().SetColor(255/255, 242/255, 0)
actor5.SetPosition(9.5, 8, 2)

actor6 = vtk.vtkActor()
actor6.SetMapper(mapper6)
actor6.GetProperty().SetColor(0.0, 0.0, 1.0)
actor6.SetPosition(20, 10, -10)

##################################################################################################################


actorPasto = vtk.vtkActor()
actorPasto.SetMapper(mapperPasto)
actorPasto.GetProperty().SetColor(75/255, 201/255, 40/255)
actorPasto.SetPosition(0, 0, 0)

# camera
camera = vtk.vtkCamera()
camera.SetFocalPoint(0, 0, 0)
camera.SetPosition(-120, 40, 0)

# renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(151/255, 204/255, 240/255)
renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.AddActor(actor3)
renderer.AddActor(actor4)
renderer.AddActor(actor5)
renderer.AddActor(actor6)


for i in range(30):
    crearAve(randint(-500, 500), randint(20, 50), randint(-500, 500), renderer)
    crearArbol(randint(-500, 500), randint(-500, 500), renderer)

for i in range(150):
    crearLapiz(randint(-500, 500), randint(-500, 500), renderer)
    crearPiedra(randint(-500, 500), randint(-500, 500), renderer)


crearArbol(-20, -40, renderer)
crearArbol(-20, 40, renderer)
renderer.AddActor(actorPasto)

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

for v in res.values():
    renderer.AddActor(v["vtkActor"])



renderer.SetActiveCamera(camera)

# renderWindow
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Primera Tarea")
render_window.SetSize(1600, 900)
render_window.AddRenderer(renderer)

# interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()
