import vtk

#image for texture
reader = vtk.vtkJPEGReader()
reader.SetFileName("aqp.jpg")

# Create texture object
texture = vtk.vtkTexture()
if vtk.VTK_MAJOR_VERSION <= 5:
    texture.SetInput(reader.GetOutput())
else:
    texture.SetInputConnection(reader.GetOutputPort())

# source
sphere = vtk.vtkSphereSource()
sphere.SetThetaResolution(50)
sphere.SetPhiResolution(50)
sphere.SetRadius(2)
sphere.Update()

# Map texture coordinates
map_to_sphere = vtk.vtkTextureMapToSphere()
if vtk.VTK_MAJOR_VERSION <= 5:
    map_to_sphere.SetInput(sphere.GetOutput())
else:
    map_to_sphere.SetInputConnection(sphere.GetOutputPort())
#map_to_sphere.PreventSeamOn()

# Create mapper and set the mapped texture as input
mapper = vtk.vtkPolyDataMapper()
if vtk.VTK_MAJOR_VERSION <= 5:
    mapper.SetInput(map_to_sphere.GetOutput())
else:
    mapper.SetInputConnection(map_to_sphere.GetOutputPort())

#actor
sphere_actor = vtk.vtkActor()
sphere_actor.SetMapper(mapper)
#sphere_actor.GetProperty().SetColor(0, 1, 0.0)
sphere_actor.SetTexture(texture)

#renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0, 0.0, 0.0)
renderer.AddActor(sphere_actor)


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

