# trace generated using paraview version 5.9.1


#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


# create a new 'Legacy VTK Reader'
mag_t = FindSource('mag_t*')


# get active view
renderView1 = GetActiveViewOrCreate('RenderView')


# get the material library
materialLibrary1 = GetMaterialLibrary()


# get animation scene
animationScene1 = GetAnimationScene()


# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()


# get display properties
mag_tDisplay = GetDisplayProperties(mag_t, view=renderView1)


# set scalar coloring
ColorBy(mag_tDisplay, ('POINTS', 'mag'))


# rescale color and/or opacity maps used to include current data range
mag_tDisplay.RescaleTransferFunctionToDataRange(True, False)


# show color bar/color legend
mag_tDisplay.SetScalarBarVisibility(renderView1, True)


# get color transfer function/color map for 'mag'
magLUT = GetColorTransferFunction('mag')


# get opacity transfer function/opacity map for 'mag'
magPWF = GetOpacityTransferFunction('mag')


# change representation type
mag_tDisplay.SetRepresentationType('Surface')


# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(registrationName='ExtractSubset1', Input=mag_t)
extractSubset1.VOI = [0, 139, 0, 67, 0, 43]


# show data in view
extractSubset1Display = Show(extractSubset1, renderView1, 'UniformGridRepresentation')


# trace defaults for the display properties.
extractSubset1Display.Representation = 'Outline'
extractSubset1Display.ColorArrayName = ['POINTS', 'mag']
extractSubset1Display.LookupTable = magLUT
extractSubset1Display.SelectTCoordArray = 'None'
extractSubset1Display.SelectNormalArray = 'None'
extractSubset1Display.SelectTangentArray = 'None'
extractSubset1Display.OSPRayScaleArray = 'mag'
extractSubset1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSubset1Display.SelectOrientationVectors = 'None'
extractSubset1Display.ScaleFactor = 13.9
extractSubset1Display.SelectScaleArray = 'mag'
extractSubset1Display.GlyphType = 'Arrow'
extractSubset1Display.GlyphTableIndexArray = 'mag'
extractSubset1Display.GaussianRadius = 0.6950000000000001
extractSubset1Display.SetScaleArray = ['POINTS', 'mag']
extractSubset1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSubset1Display.OpacityArray = ['POINTS', 'mag']
extractSubset1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSubset1Display.DataAxesGrid = 'GridAxesRepresentation'
extractSubset1Display.PolarAxes = 'PolarAxesRepresentation'
extractSubset1Display.ScalarOpacityUnitDistance = 2.1732040740818825
extractSubset1Display.ScalarOpacityFunction = magPWF
extractSubset1Display.OpacityArrayName = ['POINTS', 'mag']
extractSubset1Display.IsosurfaceValues = [374.0]
extractSubset1Display.SliceFunction = 'Plane'
extractSubset1Display.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSubset1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 748.0, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSubset1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 748.0, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
extractSubset1Display.SliceFunction.Origin = [69.5, 33.5, 21.5]


# show color bar/color legend
extractSubset1Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=extractSubset1)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]


# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [69.5, 33.5, 21.5]


# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [69.5, 33.5, 21.5]


# show data in view
slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')


# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['POINTS', 'mag']
slice1Display.LookupTable = magLUT
slice1Display.SelectTCoordArray = 'None'
slice1Display.SelectNormalArray = 'None'
slice1Display.SelectTangentArray = 'None'
slice1Display.OSPRayScaleArray = 'mag'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 6.7
slice1Display.SelectScaleArray = 'mag'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'mag'
slice1Display.GaussianRadius = 0.335
slice1Display.SetScaleArray = ['POINTS', 'mag']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'mag']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 494.0, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 494.0, 1.0, 0.5, 0.0]


# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# set active source
SetActiveSource(extractSubset1)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=extractSubset1Display.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=extractSubset1Display)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=extractSubset1Display.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=extractSubset1Display)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)


# update the view to ensure updated data information
renderView1.Update()


# create a new 'Slice'
slice2 = Slice(registrationName='Slice2', Input=extractSubset1)
slice2.SliceType = 'Plane'
slice2.HyperTreeGridSlicer = 'Plane'
slice2.SliceOffsetValues = [0.0]


# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [69.5, 33.5, 21.5]


# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice2.HyperTreeGridSlicer.Origin = [69.5, 33.5, 21.5]


# show data in view
slice2Display = Show(slice2, renderView1, 'GeometryRepresentation')


# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['POINTS', 'mag']
slice2Display.LookupTable = magLUT
slice2Display.SelectTCoordArray = 'None'
slice2Display.SelectNormalArray = 'None'
slice2Display.SelectTangentArray = 'None'
slice2Display.OSPRayScaleArray = 'mag'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'None'
slice2Display.ScaleFactor = 6.7
slice2Display.SelectScaleArray = 'mag'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'mag'
slice2Display.GaussianRadius = 0.335
slice2Display.SetScaleArray = ['POINTS', 'mag']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'mag']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 494.0, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 494.0, 1.0, 0.5, 0.0]


# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# set active source
SetActiveSource(extractSubset1)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=extractSubset1Display.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=extractSubset1Display)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=extractSubset1Display.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=extractSubset1Display)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice2.SliceType)


# update the view to ensure updated data information
renderView1.Update()


# create a new 'Slice'
slice3 = Slice(registrationName='Slice3', Input=extractSubset1)
slice3.SliceType = 'Plane'
slice3.HyperTreeGridSlicer = 'Plane'
slice3.SliceOffsetValues = [0.0]


# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = [69.5, 33.5, 21.5]


# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice3.HyperTreeGridSlicer.Origin = [69.5, 33.5, 21.5]


# show data in view
slice3Display = Show(slice3, renderView1, 'GeometryRepresentation')


# trace defaults for the display properties.
slice3Display.Representation = 'Surface'
slice3Display.ColorArrayName = ['POINTS', 'mag']
slice3Display.LookupTable = magLUT
slice3Display.SelectTCoordArray = 'None'
slice3Display.SelectNormalArray = 'None'
slice3Display.SelectTangentArray = 'None'
slice3Display.OSPRayScaleArray = 'mag'
slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice3Display.SelectOrientationVectors = 'None'
slice3Display.ScaleFactor = 6.7
slice3Display.SelectScaleArray = 'mag'
slice3Display.GlyphType = 'Arrow'
slice3Display.GlyphTableIndexArray = 'mag'
slice3Display.GaussianRadius = 0.335
slice3Display.SetScaleArray = ['POINTS', 'mag']
slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display.OpacityArray = ['POINTS', 'mag']
slice3Display.OpacityTransferFunction = 'PiecewiseFunction'
slice3Display.DataAxesGrid = 'GridAxesRepresentation'
slice3Display.PolarAxes = 'PolarAxesRepresentation'


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 494.0, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 494.0, 1.0, 0.5, 0.0]


# show color bar/color legend
slice3Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on slice3.SliceType
slice3.SliceType.Normal = [0.0, 0.0, 1.0]


# update the view to ensure updated data information
renderView1.Update()


# set active source
SetActiveSource(slice2)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice3.SliceType)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=slice2.SliceType)


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on slice2.SliceType
slice2.SliceType.Normal = [0.0, 1.0, 0.0]


# update the view to ensure updated data information
renderView1.Update()


# set active source
SetActiveSource(mag_t)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=mag_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=mag_tDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=mag_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=mag_tDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice2.SliceType)


# update the view to ensure updated data information
renderView1.Update()


# create a new 'Legacy VTK Reader'
#strain1_GL_t = LegacyVTKReader(registrationName='strain1_GL_t*', FileNames=['C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t01.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t02.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t03.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t04.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t05.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t06.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t07.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t08.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t09.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t10.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t11.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t12.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t13.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t14.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t15.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t16.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t17.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t18.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t19.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t20.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t21.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t22.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t23.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GL_L\\strain1_GL_t24.vtk'])
strain1_GL_t = FindSource('strain1_GL_t*') 

# show data in view
strain1_GL_tDisplay = Show(strain1_GL_t, renderView1, 'UniformGridRepresentation')


# trace defaults for the display properties.
strain1_GL_tDisplay.Representation = 'Outline'
strain1_GL_tDisplay.ColorArrayName = ['POINTS', '']
strain1_GL_tDisplay.SelectTCoordArray = 'None'
strain1_GL_tDisplay.SelectNormalArray = 'None'
strain1_GL_tDisplay.SelectTangentArray = 'None'
strain1_GL_tDisplay.OSPRayScaleArray = 'strain1_GL'
strain1_GL_tDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
strain1_GL_tDisplay.SelectOrientationVectors = 'None'
strain1_GL_tDisplay.ScaleFactor = 13.9
strain1_GL_tDisplay.SelectScaleArray = 'strain1_GL'
strain1_GL_tDisplay.GlyphType = 'Arrow'
strain1_GL_tDisplay.GlyphTableIndexArray = 'strain1_GL'
strain1_GL_tDisplay.GaussianRadius = 0.6950000000000001
strain1_GL_tDisplay.SetScaleArray = ['POINTS', 'strain1_GL']
strain1_GL_tDisplay.ScaleTransferFunction = 'PiecewiseFunction'
strain1_GL_tDisplay.OpacityArray = ['POINTS', 'strain1_GL']
strain1_GL_tDisplay.OpacityTransferFunction = 'PiecewiseFunction'
strain1_GL_tDisplay.DataAxesGrid = 'GridAxesRepresentation'
strain1_GL_tDisplay.PolarAxes = 'PolarAxesRepresentation'
strain1_GL_tDisplay.ScalarOpacityUnitDistance = 2.1732040740818825
strain1_GL_tDisplay.OpacityArrayName = ['POINTS', 'strain1_GL']
strain1_GL_tDisplay.IsosurfaceValues = [0.0]
strain1_GL_tDisplay.SliceFunction = 'Plane'
strain1_GL_tDisplay.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
strain1_GL_tDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
strain1_GL_tDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
strain1_GL_tDisplay.SliceFunction.Origin = [69.5, 33.5, 21.5]


# update the view to ensure updated data information
renderView1.Update()


# set active source
SetActiveSource(mag_t)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=mag_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=mag_tDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=mag_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=mag_tDisplay)


# create a new 'Legacy VTK Reader'
#strain1_GM_t = LegacyVTKReader(registrationName='strain1_GM_t*', FileNames=['C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t01.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t02.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t03.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t04.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t05.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t06.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t07.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t08.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t09.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t10.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t11.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t12.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t13.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t14.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t15.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t16.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t17.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t18.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t19.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t20.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t21.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t22.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t23.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\GM_L\\strain1_GM_t24.vtk'])
strain1_GM_t = FindSource('strain1_GM_t*')

# show data in view
strain1_GM_tDisplay = Show(strain1_GM_t, renderView1, 'UniformGridRepresentation')


# trace defaults for the display properties.
strain1_GM_tDisplay.Representation = 'Outline'
strain1_GM_tDisplay.ColorArrayName = ['POINTS', '']
strain1_GM_tDisplay.SelectTCoordArray = 'None'
strain1_GM_tDisplay.SelectNormalArray = 'None'
strain1_GM_tDisplay.SelectTangentArray = 'None'
strain1_GM_tDisplay.OSPRayScaleArray = 'strain1_GM'
strain1_GM_tDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
strain1_GM_tDisplay.SelectOrientationVectors = 'None'
strain1_GM_tDisplay.ScaleFactor = 13.9
strain1_GM_tDisplay.SelectScaleArray = 'strain1_GM'
strain1_GM_tDisplay.GlyphType = 'Arrow'
strain1_GM_tDisplay.GlyphTableIndexArray = 'strain1_GM'
strain1_GM_tDisplay.GaussianRadius = 0.6950000000000001
strain1_GM_tDisplay.SetScaleArray = ['POINTS', 'strain1_GM']
strain1_GM_tDisplay.ScaleTransferFunction = 'PiecewiseFunction'
strain1_GM_tDisplay.OpacityArray = ['POINTS', 'strain1_GM']
strain1_GM_tDisplay.OpacityTransferFunction = 'PiecewiseFunction'
strain1_GM_tDisplay.DataAxesGrid = 'GridAxesRepresentation'
strain1_GM_tDisplay.PolarAxes = 'PolarAxesRepresentation'
strain1_GM_tDisplay.ScalarOpacityUnitDistance = 2.1732040740818825
strain1_GM_tDisplay.OpacityArrayName = ['POINTS', 'strain1_GM']
strain1_GM_tDisplay.IsosurfaceValues = [0.0]
strain1_GM_tDisplay.SliceFunction = 'Plane'
strain1_GM_tDisplay.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
strain1_GM_tDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
strain1_GM_tDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
strain1_GM_tDisplay.SliceFunction.Origin = [69.5, 33.5, 21.5]


# update the view to ensure updated data information
renderView1.Update()


# set active source
SetActiveSource(mag_t)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=mag_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=mag_tDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=mag_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=mag_tDisplay)


# create a new 'Legacy VTK Reader'
#strain1_Soleus_t = LegacyVTKReader(registrationName='strain1_Soleus_t*', FileNames=['C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t01.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t02.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t03.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t04.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t05.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t06.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t07.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t08.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t09.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t10.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t11.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t12.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t13.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t14.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t15.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t16.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t17.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t18.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t19.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t20.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t21.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t22.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t23.vtk', 'C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Time_series\\Soleus\\strain1_Soleus_t24.vtk'])
strain1_Soleus_t = FindSource('strain1_Soleus_t*')

# show data in view
strain1_Soleus_tDisplay = Show(strain1_Soleus_t, renderView1, 'UniformGridRepresentation')


# trace defaults for the display properties.
strain1_Soleus_tDisplay.Representation = 'Outline'
strain1_Soleus_tDisplay.ColorArrayName = ['POINTS', '']
strain1_Soleus_tDisplay.SelectTCoordArray = 'None'
strain1_Soleus_tDisplay.SelectNormalArray = 'None'
strain1_Soleus_tDisplay.SelectTangentArray = 'None'
strain1_Soleus_tDisplay.OSPRayScaleArray = 'strain1_SL'
strain1_Soleus_tDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
strain1_Soleus_tDisplay.SelectOrientationVectors = 'None'
strain1_Soleus_tDisplay.ScaleFactor = 13.9
strain1_Soleus_tDisplay.SelectScaleArray = 'strain1_SL'
strain1_Soleus_tDisplay.GlyphType = 'Arrow'
strain1_Soleus_tDisplay.GlyphTableIndexArray = 'strain1_SL'
strain1_Soleus_tDisplay.GaussianRadius = 0.6950000000000001
strain1_Soleus_tDisplay.SetScaleArray = ['POINTS', 'strain1_SL']
strain1_Soleus_tDisplay.ScaleTransferFunction = 'PiecewiseFunction'
strain1_Soleus_tDisplay.OpacityArray = ['POINTS', 'strain1_SL']
strain1_Soleus_tDisplay.OpacityTransferFunction = 'PiecewiseFunction'
strain1_Soleus_tDisplay.DataAxesGrid = 'GridAxesRepresentation'
strain1_Soleus_tDisplay.PolarAxes = 'PolarAxesRepresentation'
strain1_Soleus_tDisplay.ScalarOpacityUnitDistance = 2.1732040740818825
strain1_Soleus_tDisplay.OpacityArrayName = ['POINTS', 'strain1_SL']
strain1_Soleus_tDisplay.IsosurfaceValues = [0.0]
strain1_Soleus_tDisplay.SliceFunction = 'Plane'
strain1_Soleus_tDisplay.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
strain1_Soleus_tDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
strain1_Soleus_tDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
strain1_Soleus_tDisplay.SliceFunction.Origin = [69.5, 33.5, 21.5]


# update the view to ensure updated data information
renderView1.Update()


# set active source
SetActiveSource(strain1_GL_t)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain1_GL_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain1_GL_tDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain1_GL_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain1_GL_tDisplay)


# hide data in view
Hide(extractSubset1, renderView1)


# set active source
SetActiveSource(extractSubset1)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=extractSubset1Display.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=extractSubset1Display)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=extractSubset1Display.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=extractSubset1Display)


# Properties modified on extractSubset1
#extractSubset1.VOI = [14, 139, 0, 67, 0, 43]


# update the view to ensure updated data information
#renderView1.Update()


# Properties modified on extractSubset1
#extractSubset1.VOI = [14, 139, 20, 67, 0, 43]


# update the view to ensure updated data information
#renderView1.Update()


# Properties modified on extractSubset1
#extractSubset1.VOI = [14, 139, 20, 67, 14, 43]


# update the view to ensure updated data information
#renderView1.Update()


# hide data in view
Hide(mag_t, renderView1)


# set active source
SetActiveSource(strain1_GL_t)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain1_GL_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain1_GL_tDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain1_GL_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain1_GL_tDisplay)


# set scalar coloring
ColorBy(strain1_GL_tDisplay, ('POINTS', 'strain1_GL'))


# rescale color and/or opacity maps used to include current data range
strain1_GL_tDisplay.RescaleTransferFunctionToDataRange(True, False)


# show color bar/color legend
strain1_GL_tDisplay.SetScalarBarVisibility(renderView1, True)


# get color transfer function/color map for 'strain1_GL'
strain1_GLLUT = GetColorTransferFunction('strain1_GL')


# get opacity transfer function/opacity map for 'strain1_GL'
strain1_GLPWF = GetOpacityTransferFunction('strain1_GL')


# change representation type
strain1_GL_tDisplay.SetRepresentationType('Surface')


# create a new 'Extract Subset'
extractSubset2 = ExtractSubset(registrationName='ExtractSubset2', Input=strain1_GL_t)
extractSubset2.VOI = [0, 139, 0, 67, 0, 43]


# show data in view
extractSubset2Display = Show(extractSubset2, renderView1, 'UniformGridRepresentation')


# trace defaults for the display properties.
extractSubset2Display.Representation = 'Outline'
extractSubset2Display.ColorArrayName = ['POINTS', 'strain1_GL']
extractSubset2Display.LookupTable = strain1_GLLUT
extractSubset2Display.SelectTCoordArray = 'None'
extractSubset2Display.SelectNormalArray = 'None'
extractSubset2Display.SelectTangentArray = 'None'
extractSubset2Display.OSPRayScaleArray = 'strain1_GL'
extractSubset2Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSubset2Display.SelectOrientationVectors = 'None'
extractSubset2Display.ScaleFactor = 13.9
extractSubset2Display.SelectScaleArray = 'strain1_GL'
extractSubset2Display.GlyphType = 'Arrow'
extractSubset2Display.GlyphTableIndexArray = 'strain1_GL'
extractSubset2Display.GaussianRadius = 0.6950000000000001
extractSubset2Display.SetScaleArray = ['POINTS', 'strain1_GL']
extractSubset2Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSubset2Display.OpacityArray = ['POINTS', 'strain1_GL']
extractSubset2Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSubset2Display.DataAxesGrid = 'GridAxesRepresentation'
extractSubset2Display.PolarAxes = 'PolarAxesRepresentation'
extractSubset2Display.ScalarOpacityUnitDistance = 2.1732040740818825
extractSubset2Display.ScalarOpacityFunction = strain1_GLPWF
extractSubset2Display.OpacityArrayName = ['POINTS', 'strain1_GL']
extractSubset2Display.IsosurfaceValues = [0.0]
extractSubset2Display.SliceFunction = 'Plane'
extractSubset2Display.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSubset2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSubset2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
extractSubset2Display.SliceFunction.Origin = [69.5, 33.5, 21.5]


# show color bar/color legend
extractSubset2Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on extractSubset2
#extractSubset2.VOI = [14, 139, 0, 67, 0, 43]


# update the view to ensure updated data information
#renderView1.Update()


# Properties modified on extractSubset2
#extractSubset2.VOI = [14, 139, 20, 67, 0, 43]


# update the view to ensure updated data information
renderView1.Update()


# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=extractSubset2)
threshold1.Scalars = ['POINTS', 'strain1_GL']


# show data in view
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')


# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = ['POINTS', 'strain1_GL']
threshold1Display.LookupTable = strain1_GLLUT
threshold1Display.SelectTCoordArray = 'None'
threshold1Display.SelectNormalArray = 'None'
threshold1Display.SelectTangentArray = 'None'
threshold1Display.OSPRayScaleArray = 'strain1_GL'
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.ScaleFactor = 12.5
threshold1Display.SelectScaleArray = 'strain1_GL'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'strain1_GL'
threshold1Display.GaussianRadius = 0.625
threshold1Display.SetScaleArray = ['POINTS', 'strain1_GL']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = ['POINTS', 'strain1_GL']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityFunction = strain1_GLPWF
threshold1Display.ScalarOpacityUnitDistance = 2.2193214161810855
threshold1Display.OpacityArrayName = ['POINTS', 'strain1_GL']


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)


# Properties modified on extractSubset2
#extractSubset2.VOI = [14, 139, 20, 67, 14, 43]


# update the view to ensure updated data information
#renderView1.Update()


# set active source
SetActiveSource(strain1_GM_t)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain1_GM_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain1_GM_tDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain1_GM_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain1_GM_tDisplay)


# set scalar coloring
ColorBy(strain1_GM_tDisplay, ('POINTS', 'strain1_GM'))


# rescale color and/or opacity maps used to include current data range
strain1_GM_tDisplay.RescaleTransferFunctionToDataRange(True, False)


# show color bar/color legend
strain1_GM_tDisplay.SetScalarBarVisibility(renderView1, True)


# get color transfer function/color map for 'strain1_GM'
strain1_GMLUT = GetColorTransferFunction('strain1_GM')


# get opacity transfer function/opacity map for 'strain1_GM'
strain1_GMPWF = GetOpacityTransferFunction('strain1_GM')


# change representation type
strain1_GM_tDisplay.SetRepresentationType('Surface')


# create a new 'Extract Subset'
extractSubset3 = ExtractSubset(registrationName='ExtractSubset3', Input=strain1_GM_t)
extractSubset3.VOI = [0, 139, 0, 67, 0, 43]


# show data in view
extractSubset3Display = Show(extractSubset3, renderView1, 'UniformGridRepresentation')


# trace defaults for the display properties.
extractSubset3Display.Representation = 'Outline'
extractSubset3Display.ColorArrayName = ['POINTS', 'strain1_GM']
extractSubset3Display.LookupTable = strain1_GMLUT
extractSubset3Display.SelectTCoordArray = 'None'
extractSubset3Display.SelectNormalArray = 'None'
extractSubset3Display.SelectTangentArray = 'None'
extractSubset3Display.OSPRayScaleArray = 'strain1_GM'
extractSubset3Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSubset3Display.SelectOrientationVectors = 'None'
extractSubset3Display.ScaleFactor = 13.9
extractSubset3Display.SelectScaleArray = 'strain1_GM'
extractSubset3Display.GlyphType = 'Arrow'
extractSubset3Display.GlyphTableIndexArray = 'strain1_GM'
extractSubset3Display.GaussianRadius = 0.6950000000000001
extractSubset3Display.SetScaleArray = ['POINTS', 'strain1_GM']
extractSubset3Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSubset3Display.OpacityArray = ['POINTS', 'strain1_GM']
extractSubset3Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSubset3Display.DataAxesGrid = 'GridAxesRepresentation'
extractSubset3Display.PolarAxes = 'PolarAxesRepresentation'
extractSubset3Display.ScalarOpacityUnitDistance = 2.1732040740818825
extractSubset3Display.ScalarOpacityFunction = strain1_GMPWF
extractSubset3Display.OpacityArrayName = ['POINTS', 'strain1_GM']
extractSubset3Display.IsosurfaceValues = [0.0]
extractSubset3Display.SliceFunction = 'Plane'
extractSubset3Display.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSubset3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSubset3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
extractSubset3Display.SliceFunction.Origin = [69.5, 33.5, 21.5]


# show color bar/color legend
extractSubset3Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on extractSubset3
#extractSubset3.VOI = [14, 139, 0, 67, 0, 43]


# update the view to ensure updated data information
#renderView1.Update()


# Properties modified on extractSubset3
#extractSubset3.VOI = [14, 139, 20, 67, 0, 43]


# update the view to ensure updated data information
#renderView1.Update()


# Properties modified on extractSubset3
#extractSubset3.VOI = [14, 139, 20, 67, 14, 43]


# update the view to ensure updated data information
#renderView1.Update()


# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=extractSubset3)
threshold2.Scalars = ['POINTS', 'strain1_GM']


# show data in view
threshold2Display = Show(threshold2, renderView1, 'UnstructuredGridRepresentation')


# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'
threshold2Display.ColorArrayName = ['POINTS', 'strain1_GM']
threshold2Display.LookupTable = strain1_GMLUT
threshold2Display.SelectTCoordArray = 'None'
threshold2Display.SelectNormalArray = 'None'
threshold2Display.SelectTangentArray = 'None'
threshold2Display.OSPRayScaleArray = 'strain1_GM'
threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold2Display.SelectOrientationVectors = 'None'
threshold2Display.ScaleFactor = 12.5
threshold2Display.SelectScaleArray = 'strain1_GM'
threshold2Display.GlyphType = 'Arrow'
threshold2Display.GlyphTableIndexArray = 'strain1_GM'
threshold2Display.GaussianRadius = 0.625
threshold2Display.SetScaleArray = ['POINTS', 'strain1_GM']
threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold2Display.OpacityArray = ['POINTS', 'strain1_GM']
threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
threshold2Display.PolarAxes = 'PolarAxesRepresentation'
threshold2Display.ScalarOpacityFunction = strain1_GMPWF
threshold2Display.ScalarOpacityUnitDistance = 2.4650648496775824
threshold2Display.OpacityArrayName = ['POINTS', 'strain1_GM']


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# show color bar/color legend
threshold2Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# set active source
SetActiveSource(strain1_Soleus_t)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain1_Soleus_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain1_Soleus_tDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain1_Soleus_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain1_Soleus_tDisplay)


# set scalar coloring
ColorBy(strain1_Soleus_tDisplay, ('POINTS', 'strain1_SL'))


# rescale color and/or opacity maps used to include current data range
strain1_Soleus_tDisplay.RescaleTransferFunctionToDataRange(True, False)


# show color bar/color legend
strain1_Soleus_tDisplay.SetScalarBarVisibility(renderView1, True)


# get color transfer function/color map for 'strain1_SL'
strain1_SLLUT = GetColorTransferFunction('strain1_SL')


# get opacity transfer function/opacity map for 'strain1_SL'
strain1_SLPWF = GetOpacityTransferFunction('strain1_SL')


# change representation type
strain1_Soleus_tDisplay.SetRepresentationType('Surface')


# create a new 'Extract Subset'
extractSubset4 = ExtractSubset(registrationName='ExtractSubset4', Input=strain1_Soleus_t)
extractSubset4.VOI = [0, 139, 0, 67, 0, 43]


# show data in view
extractSubset4Display = Show(extractSubset4, renderView1, 'UniformGridRepresentation')


# trace defaults for the display properties.
extractSubset4Display.Representation = 'Outline'
extractSubset4Display.ColorArrayName = ['POINTS', 'strain1_SL']
extractSubset4Display.LookupTable = strain1_SLLUT
extractSubset4Display.SelectTCoordArray = 'None'
extractSubset4Display.SelectNormalArray = 'None'
extractSubset4Display.SelectTangentArray = 'None'
extractSubset4Display.OSPRayScaleArray = 'strain1_SL'
extractSubset4Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSubset4Display.SelectOrientationVectors = 'None'
extractSubset4Display.ScaleFactor = 13.9
extractSubset4Display.SelectScaleArray = 'strain1_SL'
extractSubset4Display.GlyphType = 'Arrow'
extractSubset4Display.GlyphTableIndexArray = 'strain1_SL'
extractSubset4Display.GaussianRadius = 0.6950000000000001
extractSubset4Display.SetScaleArray = ['POINTS', 'strain1_SL']
extractSubset4Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSubset4Display.OpacityArray = ['POINTS', 'strain1_SL']
extractSubset4Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSubset4Display.DataAxesGrid = 'GridAxesRepresentation'
extractSubset4Display.PolarAxes = 'PolarAxesRepresentation'
extractSubset4Display.ScalarOpacityUnitDistance = 2.1732040740818825
extractSubset4Display.ScalarOpacityFunction = strain1_SLPWF
extractSubset4Display.OpacityArrayName = ['POINTS', 'strain1_SL']
extractSubset4Display.IsosurfaceValues = [0.0]
extractSubset4Display.SliceFunction = 'Plane'
extractSubset4Display.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSubset4Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSubset4Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
extractSubset4Display.SliceFunction.Origin = [69.5, 33.5, 21.5]


# show color bar/color legend
extractSubset4Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on extractSubset4
#extractSubset4.VOI = [14, 139, 0, 67, 0, 43]


# update the view to ensure updated data information
#renderView1.Update()


# Properties modified on extractSubset4
#extractSubset4.VOI = [14, 139, 20, 67, 0, 43]


# update the view to ensure updated data information
#renderView1.Update()


# Properties modified on extractSubset4
#extractSubset4.VOI = [14, 139, 20, 67, 14, 43]


# update the view to ensure updated data information
#renderView1.Update()


# create a new 'Threshold'
threshold3 = Threshold(registrationName='Threshold3', Input=extractSubset4)
threshold3.Scalars = ['POINTS', 'strain1_SL']


# show data in view
threshold3Display = Show(threshold3, renderView1, 'UnstructuredGridRepresentation')


# trace defaults for the display properties.
threshold3Display.Representation = 'Surface'
threshold3Display.ColorArrayName = ['POINTS', 'strain1_SL']
threshold3Display.LookupTable = strain1_SLLUT
threshold3Display.SelectTCoordArray = 'None'
threshold3Display.SelectNormalArray = 'None'
threshold3Display.SelectTangentArray = 'None'
threshold3Display.OSPRayScaleArray = 'strain1_SL'
threshold3Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold3Display.SelectOrientationVectors = 'None'
threshold3Display.ScaleFactor = 12.5
threshold3Display.SelectScaleArray = 'strain1_SL'
threshold3Display.GlyphType = 'Arrow'
threshold3Display.GlyphTableIndexArray = 'strain1_SL'
threshold3Display.GaussianRadius = 0.625
threshold3Display.SetScaleArray = ['POINTS', 'strain1_SL']
threshold3Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold3Display.OpacityArray = ['POINTS', 'strain1_SL']
threshold3Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold3Display.DataAxesGrid = 'GridAxesRepresentation'
threshold3Display.PolarAxes = 'PolarAxesRepresentation'
threshold3Display.ScalarOpacityFunction = strain1_SLPWF
threshold3Display.ScalarOpacityUnitDistance = 2.4650648496775824
threshold3Display.OpacityArrayName = ['POINTS', 'strain1_SL']


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]


# show color bar/color legend
threshold3Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# hide data in view
Hide(strain1_GL_t, renderView1)


# hide data in view
Hide(extractSubset2, renderView1)


# hide data in view
Hide(strain1_GM_t, renderView1)


# hide data in view
Hide(extractSubset3, renderView1)


# hide data in view
Hide(strain1_Soleus_t, renderView1)


# hide data in view
Hide(extractSubset4, renderView1)


# hide data in view
Hide(slice1, renderView1)


# hide data in view
Hide(slice2, renderView1)


# hide data in view
Hide(slice3, renderView1)


# set active source
SetActiveSource(threshold1)


# Properties modified on threshold1
threshold1.ThresholdRange = [0.2263, 0.2263]


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on threshold1
threshold1.ThresholdRange = [0.2263, 0.49]


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on strain1_GLLUT
strain1_GLLUT.EnableOpacityMapping = 1


# Rescale transfer function
strain1_GLLUT.RescaleTransferFunction(0.2263, 0.49)


# Rescale transfer function
strain1_GLPWF.RescaleTransferFunction(0.2263, 0.49)


# set active source
SetActiveSource(threshold2)


# Properties modified on strain1_GMLUT
strain1_GMLUT.EnableOpacityMapping = 1


# Rescale transfer function
strain1_GMLUT.RescaleTransferFunction(0.2263, 0.49)


# Rescale transfer function
strain1_GMPWF.RescaleTransferFunction(0.2263, 0.49)


# set active source
SetActiveSource(threshold3)


# Properties modified on strain1_SLLUT
strain1_SLLUT.EnableOpacityMapping = 1


# Rescale transfer function
strain1_SLLUT.RescaleTransferFunction(0.2263, 0.49)


# Rescale transfer function
strain1_SLPWF.RescaleTransferFunction(0.2263, 0.49)


# Properties modified on threshold3
threshold3.ThresholdRange = [0.2263, 0.2263]


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on threshold3
threshold3.ThresholdRange = [0.2263, 0.49]


# update the view to ensure updated data information
renderView1.Update()


# set active source
SetActiveSource(threshold2)


# Properties modified on threshold2
threshold2.ThresholdRange = [0.2263, 0.2263]


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on threshold2
threshold2.ThresholdRange = [0.2263, 0.49]


# update the view to ensure updated data information
renderView1.Update()


# set active source
SetActiveSource(threshold1)



# Properties modified on strain1_GLLUT
#strain1_GLLUT.RGBPoints = [0.2263, 1.0, 1.0, 1.0, 0.49, 1.0, 1.0, 0.0]
strain1_GLLUT.RGBPoints = [0.2263, 1.0, 1.0, 1.0, 0.49, 0.5176470588235295, 0.0, 0.0]


# Properties modified on strain1_GLPWF
strain1_GLPWF.Points = [0.2263, 0.0, 0.5, 0.0, 0.4518547058105469, 0.0, 0.5, 0.0, 0.49, 1.0, 0.5, 0.0]


# set active source
SetActiveSource(strain1_Soleus_t)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain1_Soleus_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain1_Soleus_tDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain1_Soleus_tDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain1_Soleus_tDisplay)


# set active source
SetActiveSource(threshold2)



# Properties modified on strain1_GMLUT
#strain1_GMLUT.RGBPoints = [0.2263, 1.0, 1.0, 1.0, 0.49, 0.9568627450980393, 0.6352941176470588, 0.21176470588235294]
strain1_GMLUT.RGBPoints = [0.2263, 1.0, 1.0, 1.0, 0.49, 0.48627450980392156, 0.7137254901960784, 1.0]

# Properties modified on strain1_GMPWF
strain1_GMPWF.Points = [0.2263, 0.0, 0.5, 0.0, 0.45517170429229736, 0.0, 0.5, 0.0, 0.49, 1.0, 0.5, 0.0]


# set active source
SetActiveSource(threshold3)



# Properties modified on strain1_SLLUT
#strain1_SLLUT.RGBPoints = [0.2263, 1.0, 1.0, 1.0, 0.49, 0.5843137254901961, 0.0, 0.8745098039215686]

strain1_SLLUT.RGBPoints = [0.2263, 1.0, 1.0, 1.0, 0.49, 0.41568627450980394, 0.6588235294117647, 0.30980392156862746]

# Properties modified on strain1_SLPWF
strain1_SLPWF.Points = [0.2263, 0.0, 0.5, 0.0, 0.4535132050514221, 0.0, 0.5, 0.0, 0.49, 1.0, 0.5, 0.0]

# set active source
SetActiveSource(slice1)

# set active source
SetActiveSource(slice2)

# set active source
SetActiveSource(slice3)


# Properties modified on magLUT
magLUT.EnableOpacityMapping = 1


# Properties modified on magLUT
magLUT.RGBPoints = [0.0, 0.0, 0.0, 0.0, 748.0, 1.0, 1.0, 1.0]

# Properties modified on magPWF
magPWF.Points = [0.0, 0.3499999940395355, 0.5, 0.0, 748.0, 1.0, 0.5, 0.0]


# set active source
SetActiveSource(threshold1)



#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================


# get layout
layout1 = GetLayout()


#--------------------------------
# saving layout sizes for layouts


# layout/tab size in pixels
layout1.SetSize(1118, 794)


#-----------------------------------
# saving camera placements for views


# current camera placement for renderView1
renderView1.CameraPosition = [41.531738528135016, 153.43456021482135, -262.3911222418365]
renderView1.CameraFocalPoint = [69.50000000000001, 33.49999999999998, 21.500000000000004]
renderView1.CameraViewUp = [-0.9943592028816993, 0.016225445887487366, 0.10481655666078678]
renderView1.CameraParallelScale = 80.09213444527497


#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).


animationScene1.Play()