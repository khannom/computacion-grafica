import vtk

# source
cuerpo = vtk.vtkSphereSource()
cuerpo.SetRadius(4)
cuerpo.SetThetaResolution(50)
cuerpo.SetPhiResolution(50)
cuerpo.Update()

ojo = vtk.vtkSphereSource()
ojo.SetRadius(0.5)
ojo.SetThetaResolution(50)
ojo.Update()

ala = vtk.vtkCubeSource()
ala.SetXLength(3)
ala.SetYLength(1)
ala.SetZLength(3)
ala.Update()

# mapper

mapperCuerpo = vtk.vtkPolyDataMapper()
mapperCuerpo.SetInputData(cuerpo.GetOutput())

mapperAla = vtk.vtkPolyDataMapper()
mapperAla.SetInputData(ala.GetOutput())

mapperOjo = vtk.vtkPolyDataMapper()
mapperOjo.SetInputData(ojo.GetOutput())

# actor

actorCuerpo = vtk.vtkActor()
actorCuerpo.SetMapper(mapperCuerpo)
actorCuerpo.GetProperty().SetColor(1.0, 0, 0)
actorCuerpo.SetPosition(0, 0, 0)

actorAlaD = vtk.vtkActor()
actorAlaD.SetMapper(mapperAla)
actorAlaD.GetProperty().SetColor(1,0,0)
actorAlaD.SetPosition(4,-1,0)
actorAlaD.RotateZ(-45)

actorAlaI = vtk.vtkActor()
actorAlaI.SetMapper(mapperAla)
actorAlaI.GetProperty().SetColor(1,0,0)
actorAlaI.SetPosition(-4,-1,0)
actorAlaI.RotateZ(45)

actorPico = vtk.vtkActor()
actorPico.SetMapper(mapperAla)
actorPico.GetProperty().SetColor(232/255, 151/255, 51/255)
actorPico.SetPosition(0,0,4.5)

actorOjoD = vtk.vtkActor()
actorOjoD.SetMapper(mapperOjo)
actorOjoD.GetProperty().SetColor(0,0,0)
actorOjoD.SetPosition(-1,2,3)

actorOjoI = vtk.vtkActor()
actorOjoI.SetMapper(mapperOjo)
actorOjoI.GetProperty().SetColor(0,0,0)
actorOjoI.SetPosition(1,2,3)

# axes
transformAxes = vtk.vtkTransform()
transformAxes.Translate(0.0, 0.0, 0.0)
axes = vtk.vtkAxesActor()
axes.SetUserTransform(transformAxes)

# renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(axes)
renderer.AddActor(actorCuerpo)
renderer.AddActor(actorAlaD)
renderer.AddActor(actorAlaI)
renderer.AddActor(actorPico)
renderer.AddActor(actorOjoD)
renderer.AddActor(actorOjoI)

# renderWindow
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(800, 800)
render_window.AddRenderer(renderer)

# interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()
