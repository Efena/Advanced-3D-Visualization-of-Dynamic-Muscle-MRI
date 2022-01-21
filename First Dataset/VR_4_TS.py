# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
threshold1 = FindSource('Threshold1')

# set active source
SetActiveSource(threshold1)

# get color transfer function/color map for 'strain1_GL'
strain1_GLLUT = GetColorTransferFunction('strain1_GL')

# get opacity transfer function/opacity map for 'strain1_GL'
strain1_GLPWF = GetOpacityTransferFunction('strain1_GL')

# find source
strain3_GL_t = FindSource('strain3_GL_t*')

# find source
strain1_GM_t = FindSource('strain1_GM_t*')

# find source
strain2_GM_t = FindSource('strain2_GM_t*')

# find source
strain3_GM_t = FindSource('strain3_GM_t*')

# find source
strain1_GL_t = FindSource('strain1_GL_t*')

# find source
strain2_GL_t = FindSource('strain2_GL_t*')

# find source
mag_t = FindSource('mag_t*')

# find source
strain1_Soleus_t = FindSource('strain1_Soleus_t*')

# find source
strain2_Soleus_t = FindSource('strain2_Soleus_t*')

# find source
strain3_Soleus_t = FindSource('strain3_Soleus_t*')

# find source
extractSubset1 = FindSource('ExtractSubset1')

# find source
slice1 = FindSource('Slice1')

# find source
slice2 = FindSource('Slice2')

# find source
slice3 = FindSource('Slice3')

# find source
extractSubset2 = FindSource('ExtractSubset2')

# find source
extractSubset3 = FindSource('ExtractSubset3')

# find source
threshold2 = FindSource('Threshold2')

# find source
extractSubset4 = FindSource('ExtractSubset4')

# find source
threshold3 = FindSource('Threshold3')

# find source
extractSubset5 = FindSource('ExtractSubset5')

# find source
threshold4 = FindSource('Threshold4')

# find source
extractSubset6 = FindSource('ExtractSubset6')

# find source
threshold5 = FindSource('Threshold5')

# find source
threshold6 = FindSource('Threshold6')

# find source
extractSubset7 = FindSource('ExtractSubset7')

# find source
extractSubset8 = FindSource('ExtractSubset8')

# find source
threshold8 = FindSource('Threshold8')

# find source
threshold7 = FindSource('Threshold7')

# find source
extractSubset10 = FindSource('ExtractSubset10')

# find source
extractSubset9 = FindSource('ExtractSubset9')

# find source
threshold9 = FindSource('Threshold9')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# get display properties
threshold1Display = GetDisplayProperties(threshold1, view=renderView1)

# change representation type
threshold1Display.SetRepresentationType('Volume')

# Properties modified on threshold1Display
threshold1Display.SelectMapper = 'Resample To Image'

# set active source
SetActiveSource(threshold2)

# get color transfer function/color map for 'strain2_GL'
strain2_GLLUT = GetColorTransferFunction('strain2_GL')

# get opacity transfer function/opacity map for 'strain2_GL'
strain2_GLPWF = GetOpacityTransferFunction('strain2_GL')

# get display properties
threshold2Display = GetDisplayProperties(threshold2, view=renderView1)

# change representation type
threshold2Display.SetRepresentationType('Volume')

# Properties modified on threshold2Display
threshold2Display.SelectMapper = 'Resample To Image'

# set active source
SetActiveSource(threshold3)

# get color transfer function/color map for 'strain3_GL'
strain3_GLLUT = GetColorTransferFunction('strain3_GL')

# get opacity transfer function/opacity map for 'strain3_GL'
strain3_GLPWF = GetOpacityTransferFunction('strain3_GL')

# get display properties
threshold3Display = GetDisplayProperties(threshold3, view=renderView1)

# change representation type
threshold3Display.SetRepresentationType('Volume')

# Properties modified on threshold3Display
threshold3Display.SelectMapper = 'Resample To Image'

# set active source
SetActiveSource(threshold4)

# get color transfer function/color map for 'strain1_GM'
strain1_GMLUT = GetColorTransferFunction('strain1_GM')

# get opacity transfer function/opacity map for 'strain1_GM'
strain1_GMPWF = GetOpacityTransferFunction('strain1_GM')

# get display properties
threshold4Display = GetDisplayProperties(threshold4, view=renderView1)

# change representation type
threshold4Display.SetRepresentationType('Volume')

# Properties modified on threshold4Display
threshold4Display.SelectMapper = 'Resample To Image'

# set active source
SetActiveSource(threshold5)

# get color transfer function/color map for 'strain2_GM'
strain2_GMLUT = GetColorTransferFunction('strain2_GM')

# get opacity transfer function/opacity map for 'strain2_GM'
strain2_GMPWF = GetOpacityTransferFunction('strain2_GM')

# get display properties
threshold5Display = GetDisplayProperties(threshold5, view=renderView1)

# change representation type
threshold5Display.SetRepresentationType('Volume')

# Properties modified on threshold5Display
threshold5Display.SelectMapper = 'Resample To Image'

# set active source
SetActiveSource(threshold6)

# get color transfer function/color map for 'strain3_GM'
strain3_GMLUT = GetColorTransferFunction('strain3_GM')

# get opacity transfer function/opacity map for 'strain3_GM'
strain3_GMPWF = GetOpacityTransferFunction('strain3_GM')

# get display properties
threshold6Display = GetDisplayProperties(threshold6, view=renderView1)

# change representation type
threshold6Display.SetRepresentationType('Volume')

# Properties modified on threshold6Display
threshold6Display.SelectMapper = 'Resample To Image'

# set active source
SetActiveSource(threshold7)

# get color transfer function/color map for 'strain1_SL'
strain1_SLLUT = GetColorTransferFunction('strain1_SL')

# get opacity transfer function/opacity map for 'strain1_SL'
strain1_SLPWF = GetOpacityTransferFunction('strain1_SL')

# get display properties
threshold7Display = GetDisplayProperties(threshold7, view=renderView1)

# change representation type
threshold7Display.SetRepresentationType('Volume')

# Properties modified on threshold7Display
threshold7Display.SelectMapper = 'Resample To Image'

# set active source
SetActiveSource(threshold8)

# get color transfer function/color map for 'strain2_SL'
strain2_SLLUT = GetColorTransferFunction('strain2_SL')

# get opacity transfer function/opacity map for 'strain2_SL'
strain2_SLPWF = GetOpacityTransferFunction('strain2_SL')

# get display properties
threshold8Display = GetDisplayProperties(threshold8, view=renderView1)

# change representation type
threshold8Display.SetRepresentationType('Volume')

# Properties modified on threshold8Display
threshold8Display.SelectMapper = 'Resample To Image'

# set active source
SetActiveSource(threshold9)

# get color transfer function/color map for 'strain3_SL'
strain3_SLLUT = GetColorTransferFunction('strain3_SL')

# get opacity transfer function/opacity map for 'strain3_SL'
strain3_SLPWF = GetOpacityTransferFunction('strain3_SL')

# get display properties
threshold9Display = GetDisplayProperties(threshold9, view=renderView1)

# change representation type
threshold9Display.SetRepresentationType('Volume')

# Properties modified on threshold9Display
threshold9Display.SelectMapper = 'Resample To Image'

# get animation scene
animationScene1 = GetAnimationScene()

animationScene1.Play()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1154, 794)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-5.712551932710844, 325.14756544083497, 92.53141048587729]
renderView1.CameraFocalPoint = [69.5, 33.50000000000001, 21.499999999999996]
renderView1.CameraViewUp = [-0.9696693138385966, -0.22975954132262277, -0.08337850425021766]
renderView1.CameraParallelScale = 80.09213444527497

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).