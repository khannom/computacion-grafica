import vtk

# source
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

# mapper
mapperCuerpo = vtk.vtkPolyDataMapper()
mapperCuerpo.SetInputData(cuerpo.GetOutput())

mapperBorrador = vtk.vtkPolyDataMapper()
mapperBorrador.SetInputData(borrador.GetOutput())

mapperCabeza = vtk.vtkPolyDataMapper()
mapperCabeza.SetInputData(cabeza.GetOutput())

#actor
actorCuerpo = vtk.vtkActor()
actorCuerpo.SetMapper(mapperCuerpo)
actorCuerpo.GetProperty().SetColor(235/255, 247/255, 2/255)
actorCuerpo.RotateX(90)
actorCuerpo.SetPosition(0,0.125,0)

actorBorrador = vtk.vtkActor()
actorBorrador.SetMapper(mapperBorrador)
actorBorrador.GetProperty().SetColor(242/255, 63/255, 159/255)
actorBorrador.SetPosition(0,0.125,1)

actorCabeza = vtk.vtkActor()
actorCabeza.SetMapper(mapperCabeza)
actorCabeza.GetProperty().SetColor(230/255, 167/255, 67/255)
actorCabeza.RotateY(90)
actorCabeza.SetPosition(0,0.125,-1.25)

# axes
transformAxes = vtk.vtkTransform()
transformAxes.Translate(0.0, 0.0, 0.0)
axes = vtk.vtkAxesActor()
axes.SetUserTransform(transformAxes)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(actorCuerpo)
renderer.AddActor(axes)
renderer.AddActor(actorBorrador)
renderer.AddActor(actorCabeza)

#renderWindow
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(800, 800)
render_window.AddRenderer(renderer)

#interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()