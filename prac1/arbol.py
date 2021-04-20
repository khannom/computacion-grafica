import vtk

# source

tallo = vtk.vtkCylinderSource()
tallo.SetCenter(0,0,0)
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

#mapper
mapper1 = vtk.vtkPolyDataMapper()
mapper1.SetInputData(tallo.GetOutput())

mapper2 = vtk.vtkPolyDataMapper()
mapper2.SetInputData(hoja1.GetOutput())

mapper3 = vtk.vtkPolyDataMapper()
mapper3.SetInputData(hoja2.GetOutput())

mapper4 = vtk.vtkPolyDataMapper()
mapper4.SetInputData(hoja3.GetOutput())

mapper5 = vtk.vtkPolyDataMapper()
mapper5.SetInputData(hoja4.GetOutput())

mapper6 = vtk.vtkPolyDataMapper()
mapper6.SetInputData(hoja5.GetOutput())

mapper7 = vtk.vtkPolyDataMapper()
mapper7.SetInputData(hoja6.GetOutput())

#actor
actor1 = vtk.vtkActor()
actor1.SetMapper(mapper1)
actor1.GetProperty().SetColor(196/255, 133/255, 15/255)
actor1.SetPosition(20,0,0)

actor2 = vtk.vtkActor()
actor2.SetMapper(mapper2)
actor2.GetProperty().SetColor(0.0, 1.0, 0.0)
actor2.SetPosition(20,35,0)

actor3 = vtk.vtkActor()
actor3.SetMapper(mapper3)
actor3.GetProperty().SetColor(0.0, 1.0, 0.0)
actor3.SetPosition(20,35,15)

actor4 = vtk.vtkActor()
actor4.SetMapper(mapper4)
actor4.GetProperty().SetColor(0.0, 1.0, 0.0)
actor4.SetPosition(20,35,-15)

actor5 = vtk.vtkActor()
actor5.SetMapper(mapper5)
actor5.GetProperty().SetColor(0.0, 1.0, 0.0)
actor5.SetPosition(35,35,0)

actor6 = vtk.vtkActor()
actor6.SetMapper(mapper6)
actor6.GetProperty().SetColor(0.0, 1.0, 0.0)
actor6.SetPosition(5,35,0)

actor7 = vtk.vtkActor()
actor7.SetMapper(mapper7)
actor7.GetProperty().SetColor(0.0, 1.0, 0.0)
actor7.SetPosition(20,50,0)

# axes
transform = vtk.vtkTransform()
transform.Translate(0.0, 0.0, 0.0)
axes = vtk.vtkAxesActor()
axes.SetUserTransform(transform)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground( 221/255, 246/255, 253/255 )
renderer.AddActor(actor1)
renderer.AddActor(actor2)
renderer.AddActor(actor3)
renderer.AddActor(actor4)
renderer.AddActor(actor5)
renderer.AddActor(actor6)
renderer.AddActor(actor7)
renderer.AddActor(axes)

#renderWindow
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Primera Tarea")
render_window.SetSize(1600, 900)
render_window.AddRenderer(renderer)

#interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()
