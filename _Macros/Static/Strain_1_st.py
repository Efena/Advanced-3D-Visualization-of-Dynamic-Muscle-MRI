# trace generated using paraview version 5.9.1


#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()


# create a new 'Legacy VTK Reader'
magvtk = FindSource('mag.vtk')


# get active view
renderView1 = GetActiveViewOrCreate('RenderView')


# show data in view
magvtkDisplay = Show(magvtk, renderView1, 'UniformGridRepresentation')


# trace defaults for the display properties.
magvtkDisplay.Representation = 'Outline'
magvtkDisplay.ColorArrayName = ['POINTS', '']
magvtkDisplay.SelectTCoordArray = 'None'
magvtkDisplay.SelectNormalArray = 'None'
magvtkDisplay.SelectTangentArray = 'None'
magvtkDisplay.OSPRayScaleArray = 'mag'
magvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
magvtkDisplay.SelectOrientationVectors = 'None'
magvtkDisplay.ScaleFactor = 13.9
magvtkDisplay.SelectScaleArray = 'mag'
magvtkDisplay.GlyphType = 'Arrow'
magvtkDisplay.GlyphTableIndexArray = 'mag'
magvtkDisplay.GaussianRadius = 0.6950000000000001
magvtkDisplay.SetScaleArray = ['POINTS', 'mag']
magvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
magvtkDisplay.OpacityArray = ['POINTS', 'mag']
magvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
magvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
magvtkDisplay.PolarAxes = 'PolarAxesRepresentation'
magvtkDisplay.ScalarOpacityUnitDistance = 2.1732040740818825
magvtkDisplay.OpacityArrayName = ['POINTS', 'mag']
magvtkDisplay.IsosurfaceValues = [374.0]
magvtkDisplay.SliceFunction = 'Plane'
magvtkDisplay.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
magvtkDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 748.0, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
magvtkDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 748.0, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
magvtkDisplay.SliceFunction.Origin = [69.5, 33.5, 21.5]


# reset view to fit data
renderView1.ResetCamera()


# get the material library
materialLibrary1 = GetMaterialLibrary()


# update the view to ensure updated data information
renderView1.Update()


# set scalar coloring
ColorBy(magvtkDisplay, ('POINTS', 'mag'))


# rescale color and/or opacity maps used to include current data range
magvtkDisplay.RescaleTransferFunctionToDataRange(True, False)


# show color bar/color legend
magvtkDisplay.SetScalarBarVisibility(renderView1, True)


# get color transfer function/color map for 'mag'
magLUT = GetColorTransferFunction('mag')


# get opacity transfer function/opacity map for 'mag'
magPWF = GetOpacityTransferFunction('mag')


# change representation type
magvtkDisplay.SetRepresentationType('Surface')


# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(registrationName='ExtractSubset1', Input=magvtk)
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
slice1.SliceType.Origin = [76.5, 43.5, 28.5]


# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [76.5, 43.5, 28.5]


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
slice1Display.ScaleFactor = 4.7
slice1Display.SelectScaleArray = 'mag'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'mag'
slice1Display.GaussianRadius = 0.23500000000000001
slice1Display.SetScaleArray = ['POINTS', 'mag']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'mag']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 725.0, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 725.0, 1.0, 0.5, 0.0]


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
slice2.SliceType.Origin = [76.5, 43.5, 28.5]


# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice2.HyperTreeGridSlicer.Origin = [76.5, 43.5, 28.5]


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
slice2Display.ScaleFactor = 4.7
slice2Display.SelectScaleArray = 'mag'
slice2Display.GlyphType = 'Arrow'
slice2Display.GlyphTableIndexArray = 'mag'
slice2Display.GaussianRadius = 0.23500000000000001
slice2Display.SetScaleArray = ['POINTS', 'mag']
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityArray = ['POINTS', 'mag']
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.PolarAxes = 'PolarAxesRepresentation'


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 725.0, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 725.0, 1.0, 0.5, 0.0]


# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on slice2.SliceType
slice2.SliceType.Normal = [0.0, 1.0, 0.0]


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
slice3.SliceType.Origin = [76.5, 43.5, 28.5]


# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice3.HyperTreeGridSlicer.Origin = [76.5, 43.5, 28.5]


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
slice3Display.ScaleFactor = 4.7
slice3Display.SelectScaleArray = 'mag'
slice3Display.GlyphType = 'Arrow'
slice3Display.GlyphTableIndexArray = 'mag'
slice3Display.GaussianRadius = 0.23500000000000001
slice3Display.SetScaleArray = ['POINTS', 'mag']
slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display.OpacityArray = ['POINTS', 'mag']
slice3Display.OpacityTransferFunction = 'PiecewiseFunction'
slice3Display.DataAxesGrid = 'GridAxesRepresentation'
slice3Display.PolarAxes = 'PolarAxesRepresentation'


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 725.0, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 725.0, 1.0, 0.5, 0.0]


# show color bar/color legend
slice3Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on slice3.SliceType
slice3.SliceType.Normal = [0.0, 0.0, 1.0]


# update the view to ensure updated data information
renderView1.Update()


# set active source
SetActiveSource(magvtk)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=magvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=magvtkDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=magvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=magvtkDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice3.SliceType)


# update the view to ensure updated data information
renderView1.Update()


# create a new 'Legacy VTK Reader'
#This method uses the filepath. Input the file path and uncomment this line of code
#strain_max1_GLvtk = LegacyVTKReader(registrationName='strain_max1_GL.vtk', FileNames=['C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Muscle_stim_extracted\\strain_max1_GL.vtk'])

#This method allows you to directly upload the strain VTK file on the pipeline browser 
strain_max1_GLvtk = FindSource('strain_max1_GL.vtk') 

# create a new 'Legacy VTK Reader'
#strain_max1_GMvtk = LegacyVTKReader(registrationName='strain_max1_GM.vtk', FileNames=['C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Muscle_stim_extracted\\strain_max1_GM.vtk'])
strain_max1_GMvtk = FindSource('strain_max1_GM.vtk')

# create a new 'Legacy VTK Reader'
#strain_max1_Soleusvtk = LegacyVTKReader(registrationName='strain_max1_Soleus.vtk', FileNames=['C:\\Users\\Efena\\Desktop\\UNIBAS MASTER\\Thesis\\paraview_files\\Muscle_stim_extracted\\strain_max1_Soleus.vtk'])
strain_max1_Soleusvtk = FindSource('strain_max1_Soleus.vtk')

# show data in view
strain_max1_GMvtkDisplay = Show(strain_max1_GMvtk, renderView1, 'UniformGridRepresentation')


# trace defaults for the display properties.
strain_max1_GMvtkDisplay.Representation = 'Outline'
strain_max1_GMvtkDisplay.ColorArrayName = ['POINTS', '']
strain_max1_GMvtkDisplay.SelectTCoordArray = 'None'
strain_max1_GMvtkDisplay.SelectNormalArray = 'None'
strain_max1_GMvtkDisplay.SelectTangentArray = 'None'
strain_max1_GMvtkDisplay.OSPRayScaleArray = 'strain1_GM'
strain_max1_GMvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
strain_max1_GMvtkDisplay.SelectOrientationVectors = 'None'
strain_max1_GMvtkDisplay.ScaleFactor = 13.9
strain_max1_GMvtkDisplay.SelectScaleArray = 'strain1_GM'
strain_max1_GMvtkDisplay.GlyphType = 'Arrow'
strain_max1_GMvtkDisplay.GlyphTableIndexArray = 'strain1_GM'
strain_max1_GMvtkDisplay.GaussianRadius = 0.6950000000000001
strain_max1_GMvtkDisplay.SetScaleArray = ['POINTS', 'strain1_GM']
strain_max1_GMvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
strain_max1_GMvtkDisplay.OpacityArray = ['POINTS', 'strain1_GM']
strain_max1_GMvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
strain_max1_GMvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
strain_max1_GMvtkDisplay.PolarAxes = 'PolarAxesRepresentation'
strain_max1_GMvtkDisplay.ScalarOpacityUnitDistance = 2.1732040740818825
strain_max1_GMvtkDisplay.OpacityArrayName = ['POINTS', 'strain1_GM']
strain_max1_GMvtkDisplay.IsosurfaceValues = [0.17499999701976776]
strain_max1_GMvtkDisplay.SliceFunction = 'Plane'
strain_max1_GMvtkDisplay.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
strain_max1_GMvtkDisplay.ScaleTransferFunction.Points = [-0.15000000596046448, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
strain_max1_GMvtkDisplay.OpacityTransferFunction.Points = [-0.15000000596046448, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
strain_max1_GMvtkDisplay.SliceFunction.Origin = [69.5, 33.5, 21.5]


# show data in view
strain_max1_SoleusvtkDisplay = Show(strain_max1_Soleusvtk, renderView1, 'UniformGridRepresentation')


# trace defaults for the display properties.
strain_max1_SoleusvtkDisplay.Representation = 'Outline'
strain_max1_SoleusvtkDisplay.ColorArrayName = ['POINTS', '']
strain_max1_SoleusvtkDisplay.SelectTCoordArray = 'None'
strain_max1_SoleusvtkDisplay.SelectNormalArray = 'None'
strain_max1_SoleusvtkDisplay.SelectTangentArray = 'None'
strain_max1_SoleusvtkDisplay.OSPRayScaleArray = 'strain1_SL'
strain_max1_SoleusvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
strain_max1_SoleusvtkDisplay.SelectOrientationVectors = 'None'
strain_max1_SoleusvtkDisplay.ScaleFactor = 13.9
strain_max1_SoleusvtkDisplay.SelectScaleArray = 'strain1_SL'
strain_max1_SoleusvtkDisplay.GlyphType = 'Arrow'
strain_max1_SoleusvtkDisplay.GlyphTableIndexArray = 'strain1_SL'
strain_max1_SoleusvtkDisplay.GaussianRadius = 0.6950000000000001
strain_max1_SoleusvtkDisplay.SetScaleArray = ['POINTS', 'strain1_SL']
strain_max1_SoleusvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
strain_max1_SoleusvtkDisplay.OpacityArray = ['POINTS', 'strain1_SL']
strain_max1_SoleusvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
strain_max1_SoleusvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
strain_max1_SoleusvtkDisplay.PolarAxes = 'PolarAxesRepresentation'
strain_max1_SoleusvtkDisplay.ScalarOpacityUnitDistance = 2.1732040740818825
strain_max1_SoleusvtkDisplay.OpacityArrayName = ['POINTS', 'strain1_SL']
strain_max1_SoleusvtkDisplay.IsosurfaceValues = [0.19999999925494194]
strain_max1_SoleusvtkDisplay.SliceFunction = 'Plane'
strain_max1_SoleusvtkDisplay.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
strain_max1_SoleusvtkDisplay.ScaleTransferFunction.Points = [-0.10000000149011612, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
strain_max1_SoleusvtkDisplay.OpacityTransferFunction.Points = [-0.10000000149011612, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
strain_max1_SoleusvtkDisplay.SliceFunction.Origin = [69.5, 33.5, 21.5]


# show data in view
strain_max1_GLvtkDisplay = Show(strain_max1_GLvtk, renderView1, 'UniformGridRepresentation')


# trace defaults for the display properties.
strain_max1_GLvtkDisplay.Representation = 'Outline'
strain_max1_GLvtkDisplay.ColorArrayName = ['POINTS', '']
strain_max1_GLvtkDisplay.SelectTCoordArray = 'None'
strain_max1_GLvtkDisplay.SelectNormalArray = 'None'
strain_max1_GLvtkDisplay.SelectTangentArray = 'None'
strain_max1_GLvtkDisplay.OSPRayScaleArray = 'strain1_GL'
strain_max1_GLvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
strain_max1_GLvtkDisplay.SelectOrientationVectors = 'None'
strain_max1_GLvtkDisplay.ScaleFactor = 13.9
strain_max1_GLvtkDisplay.SelectScaleArray = 'strain1_GL'
strain_max1_GLvtkDisplay.GlyphType = 'Arrow'
strain_max1_GLvtkDisplay.GlyphTableIndexArray = 'strain1_GL'
strain_max1_GLvtkDisplay.GaussianRadius = 0.6950000000000001
strain_max1_GLvtkDisplay.SetScaleArray = ['POINTS', 'strain1_GL']
strain_max1_GLvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
strain_max1_GLvtkDisplay.OpacityArray = ['POINTS', 'strain1_GL']
strain_max1_GLvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
strain_max1_GLvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
strain_max1_GLvtkDisplay.PolarAxes = 'PolarAxesRepresentation'
strain_max1_GLvtkDisplay.ScalarOpacityUnitDistance = 2.1732040740818825
strain_max1_GLvtkDisplay.OpacityArrayName = ['POINTS', 'strain1_GL']
strain_max1_GLvtkDisplay.IsosurfaceValues = [0.025000005960464478]
strain_max1_GLvtkDisplay.SliceFunction = 'Plane'
strain_max1_GLvtkDisplay.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
strain_max1_GLvtkDisplay.ScaleTransferFunction.Points = [-0.4399999976158142, 0.0, 0.5, 0.0, 0.49000000953674316, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
strain_max1_GLvtkDisplay.OpacityTransferFunction.Points = [-0.4399999976158142, 0.0, 0.5, 0.0, 0.49000000953674316, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
strain_max1_GLvtkDisplay.SliceFunction.Origin = [69.5, 33.5, 21.5]


# update the view to ensure updated data information
renderView1.Update()


# hide data in view
Hide(magvtk, renderView1)


# hide data in view
Hide(extractSubset1, renderView1)


# hide data in view
Hide(slice1, renderView1)


# hide data in view
Hide(slice2, renderView1)


# hide data in view
Hide(slice3, renderView1)


# set active source
SetActiveSource(strain_max1_GLvtk)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain_max1_GLvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain_max1_GLvtkDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain_max1_GLvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain_max1_GLvtkDisplay)


# set scalar coloring
ColorBy(strain_max1_GLvtkDisplay, ('POINTS', 'strain1_GL'))


# rescale color and/or opacity maps used to include current data range
strain_max1_GLvtkDisplay.RescaleTransferFunctionToDataRange(True, False)


# show color bar/color legend
strain_max1_GLvtkDisplay.SetScalarBarVisibility(renderView1, True)


# get color transfer function/color map for 'strain1_GL'
strain1_GLLUT = GetColorTransferFunction('strain1_GL')


# get opacity transfer function/opacity map for 'strain1_GL'
strain1_GLPWF = GetOpacityTransferFunction('strain1_GL')


# change representation type
strain_max1_GLvtkDisplay.SetRepresentationType('Surface')


# set active source
SetActiveSource(strain_max1_GMvtk)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain_max1_GMvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain_max1_GMvtkDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain_max1_GMvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain_max1_GMvtkDisplay)


# set scalar coloring
ColorBy(strain_max1_GMvtkDisplay, ('POINTS', 'strain1_GM'))


# rescale color and/or opacity maps used to include current data range
strain_max1_GMvtkDisplay.RescaleTransferFunctionToDataRange(True, False)


# show color bar/color legend
strain_max1_GMvtkDisplay.SetScalarBarVisibility(renderView1, True)


# get color transfer function/color map for 'strain1_GM'
strain1_GMLUT = GetColorTransferFunction('strain1_GM')


# get opacity transfer function/opacity map for 'strain1_GM'
strain1_GMPWF = GetOpacityTransferFunction('strain1_GM')


# change representation type
strain_max1_GMvtkDisplay.SetRepresentationType('Surface')


# set active source
SetActiveSource(strain_max1_Soleusvtk)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain_max1_SoleusvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain_max1_SoleusvtkDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain_max1_SoleusvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain_max1_SoleusvtkDisplay)


# set scalar coloring
ColorBy(strain_max1_SoleusvtkDisplay, ('POINTS', 'strain1_SL'))


# rescale color and/or opacity maps used to include current data range
strain_max1_SoleusvtkDisplay.RescaleTransferFunctionToDataRange(True, False)


# show color bar/color legend
strain_max1_SoleusvtkDisplay.SetScalarBarVisibility(renderView1, True)


# get color transfer function/color map for 'strain1_SL'
strain1_SLLUT = GetColorTransferFunction('strain1_SL')


# get opacity transfer function/opacity map for 'strain1_SL'
strain1_SLPWF = GetOpacityTransferFunction('strain1_SL')


# change representation type
strain_max1_SoleusvtkDisplay.SetRepresentationType('Surface')


# set active source
SetActiveSource(strain_max1_GLvtk)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain_max1_GLvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain_max1_GLvtkDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain_max1_GLvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain_max1_GLvtkDisplay)


# update the view to ensure updated data information
renderView1.Update()


# create a new 'Extract Subset'
extractSubset2 = ExtractSubset(registrationName='ExtractSubset2', Input=strain_max1_GLvtk)
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
extractSubset2Display.IsosurfaceValues = [0.025000005960464478]
extractSubset2Display.SliceFunction = 'Plane'
extractSubset2Display.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSubset2Display.ScaleTransferFunction.Points = [-0.4399999976158142, 0.0, 0.5, 0.0, 0.49000000953674316, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSubset2Display.OpacityTransferFunction.Points = [-0.4399999976158142, 0.0, 0.5, 0.0, 0.49000000953674316, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
extractSubset2Display.SliceFunction.Origin = [69.5, 33.5, 21.5]


# show color bar/color legend
extractSubset2Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()



# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=extractSubset2)
threshold1.Scalars = ['POINTS', 'strain1_GL']
threshold1.ThresholdRange = [-0.4399999976158142, 0.49000000953674316]


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
threshold1Display.ScalarOpacityUnitDistance = 2.4650648496775824
threshold1Display.OpacityArrayName = ['POINTS', 'strain1_GL']


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
threshold1Display.ScaleTransferFunction.Points = [-0.4399999976158142, 0.0, 0.5, 0.0, 0.49000000953674316, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold1Display.OpacityTransferFunction.Points = [-0.4399999976158142, 0.0, 0.5, 0.0, 0.49000000953674316, 1.0, 0.5, 0.0]

# Properties modified on threshold1
threshold1.AllScalars = 0

# show color bar/color legend
threshold1Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on threshold1
#threshold1.ThresholdRange = [0.2263, 0.49000000953674316]
GL_T1 = float(input('Min GL Threshold'))
GL_T2 = float(input('Max GL Threshold'))
threshold1.ThresholdRange = [GL_T1, GL_T2]


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on strain1_GLLUT
strain1_GLLUT.EnableOpacityMapping = 1


# Rescale transfer function
strain1_GLLUT.RescaleTransferFunction(GL_T1, GL_T2)


# Rescale transfer function
strain1_GLPWF.RescaleTransferFunction(GL_T1, GL_T2)



# Properties modified on strain1_GLLUT
#strain1_GLLUT.RGBPoints = [0.2263, 1.0, 1.0, 1.0, 0.49000000953674316, 0.705882, 0.0156863, 0.14902]


# Properties modified on strain1_GLLUT
#strain1_GLLUT.RGBPoints = [0.2263, 1.0, 1.0, 1.0, 0.49000000953674316, 1.0, 1.0, 0.0]


# get color transfer function/color map for 'strain1_GL'
strain1_GLLUT = GetColorTransferFunction('strain1_GL')


# Properties modified on strain1_GLLUT
#strain1_GLLUT.RGBPoints = [0.2263, 1.0, 1.0, 1.0, 0.49000000953674316, 0.0, 0.3333333333333333, 1.0]
#strain1_GLLUT.RGBPoints = [0.2263, 1.0, 1.0, 1.0, 0.49, 0.5176470588235295, 0.0, 0.0]
strain1_GLLUT.RGBPoints = [GL_T1, 1.0, 1.0, 1.0, GL_T2, 0.5176470588235295, 0.0, 0.0]

# get opacity transfer function/opacity map for 'strain1_GL'
strain1_GLPWF = GetOpacityTransferFunction('strain1_GL')



# Properties modified on strain1_GLPWF
#strain1_GLPWF.Points = [0.2263, 0.0, 0.5, 0.0, 0.4468792676925659, 0.0, 0.5, 0.0, 0.49000000953674316, 1.0, 0.5, 0.0]
#strain1_GLPWF.Points = [GL_T1, 0.0, 0.5, 0.0, 0.4468792676925659, 0.0, 0.5, 0.0, GL_T2, 1.0, 0.5, 0.0]
#New test line
strain1_GLPWF.Points = [GL_T1, 0.0, 0.5, 0.0, 0.26948240399360657, 0.0, 0.5, 0.0, GL_T2, 1.0, 0.5, 0.0, 0.4468792676925659, 0.0, 0.5, 0.0]

# hide data in view
Hide(strain_max1_GLvtk, renderView1)


# hide data in view
Hide(extractSubset2, renderView1)


# set active source
SetActiveSource(strain_max1_GMvtk)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain_max1_GMvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain_max1_GMvtkDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain_max1_GMvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain_max1_GMvtkDisplay)


# create a new 'Extract Subset'
extractSubset3 = ExtractSubset(registrationName='ExtractSubset3', Input=strain_max1_GMvtk)
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
extractSubset3Display.IsosurfaceValues = [0.17499999701976776]
extractSubset3Display.SliceFunction = 'Plane'
extractSubset3Display.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSubset3Display.ScaleTransferFunction.Points = [-0.15000000596046448, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSubset3Display.OpacityTransferFunction.Points = [-0.15000000596046448, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
extractSubset3Display.SliceFunction.Origin = [69.5, 33.5, 21.5]


# show color bar/color legend
extractSubset3Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on strain1_GMLUT
strain1_GMLUT.EnableOpacityMapping = 1


# Rescale transfer function
strain1_GMLUT.RescaleTransferFunction(0.2263, 0.49)


# Rescale transfer function
strain1_GMPWF.RescaleTransferFunction(0.2263, 0.49)



# Properties modified on strain1_GMLUT
#strain1_GMLUT.RGBPoints = [0.2263, 1.0, 1.0, 1.0, 0.49, 0.9568627450980393, 0.6352941176470588, 0.21176470588235294]

# Properties modified on strain1_GMLUT
#strain1_GMLUT.RGBPoints = [-0.15000000596046448, 1.0, 1.0, 1.0, 0.5, 0.34509803921568627, 0.6666666666666666, 0.6196078431372549]
strain1_GMLUT.RGBPoints = [0.2263, 1.0, 1.0, 1.0, 0.49, 0.48627450980392156, 0.7137254901960784, 1.0]

# Properties modified on strain1_GMPWF
strain1_GMPWF.Points = [0.2263, 0.0, 0.5, 0.0, 0.4452207386493683, 0.0, 0.5, 0.0, 0.49, 1.0, 0.5, 0.0]


# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=extractSubset3)
threshold2.Scalars = ['POINTS', 'strain1_GM']
threshold2.ThresholdRange = [-0.15000000596046448, 0.5]


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
threshold2Display.ScaleTransferFunction.Points = [-0.15000000596046448, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold2Display.OpacityTransferFunction.Points = [-0.15000000596046448, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]


# show color bar/color legend
threshold2Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# set active source
SetActiveSource(extractSubset3)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=extractSubset3Display.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=extractSubset3Display)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=extractSubset3Display.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=extractSubset3Display)


# set active source
SetActiveSource(threshold2)

# Properties modified on threshold2
threshold2.AllScalars = 0

# Properties modified on threshold2
threshold2.ThresholdRange = [0.2263, 0.5]


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on threshold2
threshold2.ThresholdRange = [0.2263, 0.49]


# update the view to ensure updated data information
renderView1.Update()


# hide data in view
Hide(strain_max1_GMvtk, renderView1)


# hide data in view
Hide(extractSubset3, renderView1)


# set active source
SetActiveSource(strain_max1_Soleusvtk)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain_max1_SoleusvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=strain_max1_SoleusvtkDisplay)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain_max1_SoleusvtkDisplay.SliceFunction)


# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=strain_max1_SoleusvtkDisplay)


# update the view to ensure updated data information
renderView1.Update()


# create a new 'Extract Subset'
extractSubset4 = ExtractSubset(registrationName='ExtractSubset4', Input=strain_max1_Soleusvtk)
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
extractSubset4Display.IsosurfaceValues = [0.19999999925494194]
extractSubset4Display.SliceFunction = 'Plane'
extractSubset4Display.Slice = 21


# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
extractSubset4Display.ScaleTransferFunction.Points = [-0.10000000149011612, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
extractSubset4Display.OpacityTransferFunction.Points = [-0.10000000149011612, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]


# init the 'Plane' selected for 'SliceFunction'
extractSubset4Display.SliceFunction.Origin = [69.5, 33.5, 21.5]


# show color bar/color legend
extractSubset4Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()



# Properties modified on strain1_SLLUT
strain1_SLLUT.EnableOpacityMapping = 1


# Properties modified on strain1_SLLUT
#strain1_SLLUT.RGBPoints = [-0.10000000149011612, 1.0, 1.0, 1.0, 0.19999999925494194, 0.865003, 0.865003, 0.865003, 0.5, 0.705882, 0.0156863, 0.14902]


# Properties modified on strain1_SLLUT
#strain1_SLLUT.RGBPoints = [-0.10000000149011612, 1.0, 1.0, 1.0, 0.5, 0.705882, 0.0156863, 0.14902]
strain1_SLLUT.RGBPoints = [0.2263, 1.0, 1.0, 1.0, 0.49, 0.41568627450980394, 0.6588235294117647, 0.30980392156862746]

# create a new 'Threshold'
threshold3 = Threshold(registrationName='Threshold3', Input=extractSubset4)
threshold3.Scalars = ['POINTS', 'strain1_SL']
threshold3.ThresholdRange = [-0.03999999910593033, 0.5]


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
threshold3Display.ScaleTransferFunction.Points = [-0.03999999910593033, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]


# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
threshold3Display.OpacityTransferFunction.Points = [-0.03999999910593033, 0.0, 0.5, 0.0, 0.5, 1.0, 0.5, 0.0]


# show color bar/color legend
threshold3Display.SetScalarBarVisibility(renderView1, True)


# update the view to ensure updated data information
renderView1.Update()


# hide data in view
Hide(strain_max1_Soleusvtk, renderView1)


# hide data in view
Hide(extractSubset4, renderView1)

# Properties modified on threshold3
threshold3.AllScalars = 0

# Properties modified on threshold3
threshold3.ThresholdRange = [0.2263, 0.5]


# update the view to ensure updated data information
renderView1.Update()


# Properties modified on threshold3
threshold3.ThresholdRange = [0.2263, 0.49]


# update the view to ensure updated data information
renderView1.Update()


# Rescale transfer function
strain1_SLLUT.RescaleTransferFunction(0.2263, 0.49)


# Rescale transfer function
strain1_SLPWF.RescaleTransferFunction(0.2263, 0.49)



# Properties modified on strain1_SLPWF
strain1_SLPWF.Points = [0.2263, 0.0, 0.5, 0.0, 0.4460499882698059, 0.0, 0.5, 0.0, 0.49, 1.0, 0.5, 0.0]


# change representation type
threshold3Display.SetRepresentationType('Surface')


# Properties modified on threshold3Display
threshold3Display.SelectMapper = 'Resample To Image'

# Properties modified on magLUT
magLUT.EnableOpacityMapping = 1

# Properties modified on threshold1
threshold1.AllScalars = 0

# Properties modified on threshold2
threshold2.AllScalars = 0

# Properties modified on threshold3
threshold3.AllScalars = 0

# Properties modified on magLUT
magLUT.RGBPoints = [0.0, 0.0, 0.0, 0.0, 748.0, 1.0, 1.0, 1.0]


# Properties modified on magPWF
magPWF.Points = [0.0, 0.3499999940395355, 0.5, 0.0, 748.0, 1.0, 0.5, 0.0]

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get color transfer function/color map for 'strain1_SL'
strain1_SLLUT = GetColorTransferFunction('strain1_SL')

# Properties modified on strain1_SLLUT
strain1_SLLUT.AutomaticRescaleRangeMode = 'Never'

# get opacity transfer function/opacity map for 'strain1_SL'
strain1_SLPWF = GetOpacityTransferFunction('strain1_SL')

# find source
threshold2 = FindSource('Threshold2')

# set active source
SetActiveSource(threshold2)

# get color transfer function/color map for 'strain1_GM'
strain1_GMLUT = GetColorTransferFunction('strain1_GM')

# get opacity transfer function/opacity map for 'strain1_GM'
strain1_GMPWF = GetOpacityTransferFunction('strain1_GM')

# find source
magvtk = FindSource('mag.vtk')

# find source
strain_max1_GLvtk = FindSource('strain_max1_GL.vtk')

# find source
strain_max1_GMvtk = FindSource('strain_max1_GM.vtk')

# find source
strain_max1_Soleusvtk = FindSource('strain_max1_Soleus.vtk')

# find source
extractSubset1 = FindSource('ExtractSubset1')

# find source
slice1 = FindSource('Slice1')

# find source
slice3 = FindSource('Slice3')

# find source
slice2 = FindSource('Slice2')

# find source
extractSubset2 = FindSource('ExtractSubset2')

# find source
threshold1 = FindSource('Threshold1')

# find source
extractSubset3 = FindSource('ExtractSubset3')

# find source
extractSubset4 = FindSource('ExtractSubset4')

# find source
threshold3 = FindSource('Threshold3')

# Properties modified on strain1_GMLUT
strain1_GMLUT.AutomaticRescaleRangeMode = 'Never'

# set active source
SetActiveSource(threshold1)

# get color transfer function/color map for 'strain1_GL'
strain1_GLLUT = GetColorTransferFunction('strain1_GL')

# get opacity transfer function/opacity map for 'strain1_GL'
strain1_GLPWF = GetOpacityTransferFunction('strain1_GL')

# Properties modified on strain1_GLLUT
strain1_GLLUT.AutomaticRescaleRangeMode = 'Never'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get layout
layout1 = GetLayout()


#--------------------------------
# saving layout sizes for layouts


# layout/tab size in pixels
layout1.SetSize(1154, 794)


#-----------------------------------
# saving camera placements for views


# current camera placement for renderView1
renderView1.CameraPosition = [26.99591500822423, -9.966191736065628, -281.9217932291385]
renderView1.CameraFocalPoint = [69.50000000000001, 33.500000000000036, 21.50000000000004]
renderView1.CameraViewUp = [-0.9903695446577863, 0.0020953165137028444, 0.1384332859648881]
renderView1.CameraParallelScale = 80.09213444527497


#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).