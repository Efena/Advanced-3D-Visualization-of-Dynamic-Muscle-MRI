# 3D-Muscle_Visualization_Paraview
ParaView is an open-source, multi-platform data analysis and visualization application. ParaView users can quickly build visualizations to analyze their data using qualitative and quantitative techniques.
The data exploration can be done interactively in 3D or programmatically using ParaView’s batch processing capabilities.
The aim of this project was to create macros(python scripts) with ParaView that can be used to automatically create 3D visualization of the muscle tissue.
The VTK files uses by ParaView were extracted using Matlab from DICOM files of 4D MRI scans.
The goal is to observe differences between muscles electrically stimulated from the muscle belly and the nerve in the lower calf muscles(Gastrocnemius Lateralis, Medialis and Soleus).

Note: 
GL: Gastrocnemius Lateralis,
GM: Gastrocnemius Medialis,
SL: Soleus,
L:Left calf,
R: Right calf.

To use this script after dowloading all the files, follow these steps:
1.) Open ParaView, click on 'macro' and then 'import new macro'
2.) Click on 'builtin' in the 'pipeline browser' to open the files, ensuring to open the magnitude 'mag' file first, followed by the same strain for the three muscle types.
i.e 'mag, strain_max1_GL, strain_max1_GM, strain_max1_Soleus' and not 'mag, strain_max1_GL, strain_max2_GM, strain_max3_Soleus' or any other combinations.

