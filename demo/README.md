# VH Execution Notebooks (Recorded on 2023/04/25)
Since we changed our execution methods for a number of times, the number of notebooks, which are used for execution, has been increased. As the requirement of the program, they needed to be edited a lot of times. Please check each of the following notebooks I wrote along with their objectives. They are collected as latest version.

### [Data_Renaming.ipynb](../demo/Data_Renaming.ipynb)
Please ignore this file.  
**Objective** : Only used to rename/modify the existing output data that generated before we changed category's program files and output data structure, like that file name should include underscore, file name should be unique, program name shouldn't include underscore, folder names under 'graph states' folder shouldn't have underscore, etc...

### [Notebook_for_rename.ipynb](../demo/Notebook_for_rename.ipynb)
**Objective** : When we changed the category's program files and output data structure, I used this notebook for modified new  program files. This file is a temporary used file. Later, I fixed the main notebook file 'scenario_generate_graph_and_video.ipynb' and used that file continuously. This file functions are exactly the same with main file except for output data file/folder names.

### [scenario_generate_graph_and_video.ipynb](../demo/scenario_generate_graph_and_video.ipynb)
**Objective** : Mainly used for data generation until the new camera setting is used. The latest simulator I used for this notebook is Build_2023_0404. Please read the comments carefully when you used this notebook. Some code should be added or some value should be changed according to the program requirements in advance of execution. The data output will be one third-person view video, one AUTO camera switching video and four fixed view videos.

### [scenario_generate_graph_and_video_with_cameras_changes.ipynb](../demo/scenario_generate_graph_and_video_with_cameras_changes.ipynb)
**Objective** : This notebook is used for new camera setting. To use this file you will need a JSON file named 'camera_data_mapping.json' under '[resources](../resources/)' folder. The data output will be one third-person view video, one AUTO camera switching video (defauld), one selected camera switching video and two fixed view switching videos.
