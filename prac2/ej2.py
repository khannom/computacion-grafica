import vtk

radio=60

class vtkTimerCallback():
    def __init__(self, steps, actor, iren, posX,velX,posY,velY,reb,rugos):
        self.timer_countX = posX
        self.timer_countY = posY
        self.steps = steps
        self.actor = actor
        self.iren = iren
        self.timerId = None
        self.velocidadX=velX
        self.velocidadY=velY
        self.rebote=reb
        self.rugosidad=rugos

    def execute(self, obj, event):
        step = 0
        while step < self.steps:
            #print(self.timer_countX)
            #print(self.actor.GetPosition())
            self.actor.SetPosition(self.timer_countX, radio,self.timer_countY)
            iren = obj
            self.actor.RotateZ(0.5)
            iren.GetRenderWindow().Render()

            if self.actor.GetPosition()[0]>1350 or self.actor.GetPosition()[0]<-1350:
               self.velocidadX= self.velocidadX*-1*self.rebote
               print(self.velocidadX)


            if self.actor.GetPosition()[2]>1350 or self.actor.GetPosition()[2]<-1350:            
               self.velocidadY= self.velocidadY*-1*self.rebote             
               print(self.velocidadY)

            self.timer_countX = self.timer_countX + self.velocidadX - self.rugosidad
            self.timer_countY = self.timer_countY + self.velocidadY - self.rugosidad
            step += 1

            if self.velocidadY<0.0001 and self.velocidadX<0.0001:
               break

        if self.timerId:
            iren.DestroyTimer(self.timerId)


def main():
    colors = vtk.vtkNamedColors()

    jpgfile = "texture_bola.jpg"

    reader = vtk.vtkJPEGReader()
    reader.SetFileName(jpgfile)

    # Create a sphere
    
    sphereSource = vtk.vtkSphereSource()
    sphereSource.SetCenter(0.0, 0.0, 0.0)
    sphereSource.SetRadius(radio)
    sphereSource.SetPhiResolution(300)
    sphereSource.SetThetaResolution(300)

    # Create a pared1
    pared1 = vtk.vtkCubeSource()
    pared1.SetXLength(3100)
    pared1.SetYLength(250)
    pared1.SetZLength(100)
    pared1.Update()

    # Create a pared1
    pared2 = vtk.vtkCubeSource()
    pared2.SetXLength(3100)
    pared2.SetYLength(250)
    pared2.SetZLength(100)
    pared2.Update()

    # Create a pared1
    pared3 = vtk.vtkCubeSource()
    pared3.SetXLength(100)
    pared3.SetYLength(250)
    pared3.SetZLength(3100)
    pared3.Update()

    # Create a pared1
    pared4 = vtk.vtkCubeSource()
    pared4.SetXLength(100)
    pared4.SetYLength(250)
    pared4.SetZLength(3100)
    pared4.Update()

    # Create a pared1
    pared5 = vtk.vtkCubeSource()
    pared5.SetXLength(3000)
    pared5.SetYLength(radio/2)
    pared5.SetZLength(3000)
    pared5.Update()

    texture = vtk.vtkTexture()
    texture.SetInputConnection(reader.GetOutputPort())

    map_to_sphere = vtk.vtkTextureMapToSphere()
    map_to_sphere.SetInputConnection(sphereSource.GetOutputPort())

    # Create a mapper and actor
    mapper1 = vtk.vtkPolyDataMapper()
    mapper1.SetInputConnection(map_to_sphere.GetOutputPort())

    # Create mapper
    mapper2 = vtk.vtkPolyDataMapper()
    mapper2.SetInputData(pared1.GetOutput())

    # Create mapper
    mapper3 = vtk.vtkPolyDataMapper()
    mapper3.SetInputData(pared2.GetOutput())

    # Create mapper
    mapper4 = vtk.vtkPolyDataMapper()
    mapper4.SetInputData(pared3.GetOutput())

    # Create mapper
    mapper5 = vtk.vtkPolyDataMapper()
    mapper5.SetInputData(pared4.GetOutput())

    # Create mapper
    mapper6 = vtk.vtkPolyDataMapper()
    mapper6.SetInputData(pared5.GetOutput())

    actor1 = vtk.vtkActor()
    #actor1.GetProperty().SetColor(colors.GetColor3d("Peacock"))
    actor1.GetProperty().SetSpecular(0.6)
    actor1.GetProperty().SetSpecularPower(30)
    actor1.SetPosition(0,100,0)
    actor1.SetMapper(mapper1)
    actor1.SetTexture(texture)

    actor2 = vtk.vtkActor()
    actor2.SetMapper(mapper2)
    actor2.GetProperty().SetColor(1.0, 0.0, 1.0)
    actor2.SetPosition(0,0,-1500)

    actor3 = vtk.vtkActor()
    actor3.SetMapper(mapper3)
    actor3.GetProperty().SetColor(1.0, 0.0, 1.0)
    actor3.SetPosition(0,0,1500)

    actor4 = vtk.vtkActor()
    actor4.SetMapper(mapper4)
    actor4.GetProperty().SetColor(1.0, 0.0, 1.0)
    actor4.SetPosition(-1500,0,0)

    actor5 = vtk.vtkActor()
    actor5.SetMapper(mapper5)
    actor5.GetProperty().SetColor(1.0, 0.0, 1.0)
    actor5.SetPosition(1500,0,0)

    actor6 = vtk.vtkActor()
    actor6.SetMapper(mapper6)
    actor6.GetProperty().SetColor(1.0, 0.0, 1.0)
    actor6.SetPosition(0,-radio/2,0)

    # Setup a renderer, render window, and interactor
    renderer = vtk.vtkRenderer()
    renderer.SetBackground(colors.GetColor3d("Black"))
    renderWindow = vtk.vtkRenderWindow()
    renderWindow.SetWindowName("Tarea 2")
    renderWindow.SetSize(1600, 900)
    renderWindow.AddRenderer(renderer)

    renderWindowInteractor = vtk.vtkRenderWindowInteractor()
    renderWindowInteractor.SetRenderWindow(renderWindow)

    # Add the actor to the scene
    renderer.AddActor(actor1)
    renderer.AddActor(actor2)
    renderer.AddActor(actor3)
    renderer.AddActor(actor4)
    renderer.AddActor(actor5)
    renderer.AddActor(actor6)

    # Render and interact
    renderWindow.Render()
    renderer.GetActiveCamera().Zoom(1)
    renderWindow.Render()
    renderer.GetActiveCamera().SetPosition(2000,7000,7000)
    renderWindow.Render()

    # Initialize must be called prior to creating timer events.
    renderWindowInteractor.Initialize()

    # Sign up to receive TimerEvent
    cb = vtkTimerCallback(30000, actor1, renderWindowInteractor,0,1.5,0,0.9,0.99,0.01)
    renderWindowInteractor.AddObserver('TimerEvent', cb.execute)
    cb.timerId = renderWindowInteractor.CreateRepeatingTimer(500)

    # start the interaction and timer
    renderWindow.Render()
    renderWindowInteractor.Start()

main()
