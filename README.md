# 3D Visualization of Dynamic Muscle MRI with ParaView
The aim of this work was to implement a 3D visualization of Dynamic MRI muscle dataset on ParaView. This entails the contraction during Neuromuscular Electrical Stimulation of the muscles in order to observe the contraction/deformation patterns.

ParaView is an open-source, multi-platform data analysis and visualization application with which users can quickly build visualizations to analyze their data using qualitative and quantitative techniques.

The dynamic MRI datasets presented here are from the calf. These had segmentation masks applied prior to extraction to obtain the three muscle groups present here; Gastrocnemius Lateralis (GL), Gastrocnemius Medialis (GM), Soleus (SL). This segementation was done using the Deep Anatomical Federated Network, [DAFNE](https://dafne.network/)

Taking advantage of the python scripts that can be generated by ParaView, it was possible to create a macro pipeline to facilitate the robust visualization of these muscle groups.



# Getting Started
1. Clone git repository: https://github.com/Efena/Advanced-3D-Visualization-of-Dynamic-Muscle-MRI.git
2. Make sure ParaView is installed.
3. Make sure the Numpy python library is installed.
4. Search for and change the folder path '/Users/Efena/Desktop/' on all python scripts to the path where you downloaded the datasets to facililate the quantile calculation.
5. Click on 'Macros > import new macro' tab in the Menu bar to import the macros.
6. Open the strain files on the 'pipeline browser' in ParaView.
7. Click on 'Macros', run the the desired macro.

# Folder Structure
1. Macros: contains the static and time resolved macros in individual folders.
2. NMES_Muscle belly: contains the static and time resolved datasets in their individual folders.


*Note: Each macro is specific to its respective dataset, 'strain_1_st' macro is for the strain_1 static dataset, 'strain_1_tr' macro is for the strain_1 time-resolved dataset etc.

If the paths are not changed, the macros will not work* 

# Dependencies
This pipeline depends on the followig library:
[Numpy](https://numpy.org/)
