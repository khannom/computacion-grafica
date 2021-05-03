import vtk

def callback_func(caller, timer_event):
    sphere_actor.RotateZ(1)
    render_window.Render()


jpgfile = "texture_bola.jpg"

reader = vtk.vtkJPEGReader()
reader.SetFileName(jpgfile)

bola = vtk.vtkSphereSource()
bola.SetRadius(4)
bola.SetThetaResolution(50)
bola.SetPhiResolution(50)
bola.Update()

texture = vtk.vtkTexture()
texture.SetInputConnection(reader.GetOutputPort())

map_to_sphere = vtk.vtkTextureMapToSphere()
map_to_sphere.SetInputConnection(bola.GetOutputPort())

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(map_to_sphere.GetOutputPort())

sphere_actor = vtk.vtkActor()
sphere_actor.SetMapper(mapper)
sphere_actor.SetTexture(texture)

renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(sphere_actor)

render_window = vtk.vtkRenderWindow()
render_window.SetWindowName("Simple VTK scene")
render_window.SetSize(800, 800)
render_window.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

interactor.Initialize()
render_window.Render()

interactor.CreateRepeatingTimer(1)
interactor.AddObserver("TimerEvent", callback_func)
interactor.Start()
