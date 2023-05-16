# VH Execution Notebooks (Recorded on 2023/04/25)
Since we changed our execution methods for a number of times, the number of notebooks, which are used for execution, has been increased. As the requirement of the program, they needed to be edited a lot of times. Please check each of the following notebooks I wrote along with their objectives and procedures. They are collected as latest version.

### [scenario_generate_graph_and_video_with_cameras_changes.ipynb](../demo/scenario_generate_graph_and_video_with_cameras_changes.ipynb)
**Objective** : This notebook is used for programs with room transitions and included new camera setting. Before using this file, please make sure a JSON file named 'camera_data_mapping.json' is under '[resources](../resources/)' folder. The data output will be one third-person view video, one AUTO camera switching video (default), one selected camera switching video and two fixed view switching videos.
**Procedure** : 
  Firstly, I suggest you to use graph's class_name values in our program scripts. For example,
  ```
  {'id': 201, 'category': 'Decor', 'class_name': 'wallpictureframe', 'prefab_name': 'PRE_DEC_Painting_15', 'obj_transform': {'position': [-6.33500051, 1.67, 2.561001], 'rotation': [0.0, 0.0, 0.0, 1.00000012], 'scale': [0.46321243, 0.463212371, 0.8]}, 'bounding_box': {'center': [-6.32533836, 1.67, 2.56099987], 'size': [0.01932602, 0.582278132, 0.764504552]}, 'properties': ['GRABBABLE', 'HANGABLE', 'HAS_PAPER', 'MOVABLE'], 'states': []}
  ```
  In the above example, we should use 'wallpictureframe' in program script whenever we need to deal with it.

  To start using this notebook, you need to run each block in its sequence until you reach the following block:
  ```python
  scene_id = 1
  program_files = []
  data_path = "../dataset/Test/scene"+str(scene_id)+"/*.txt"
  for file_path in sorted(glob.glob(data_path)):
      file_name = file_path.replace(file_path[0:file_path.rfind("\\")+1], "")

      program_name, description, list_of_steps = get_program_file(file_path)
      program_files.append({
          "file_name":file_name,
          "name": program_name,
          "description": description,
          "list_of_steps": list_of_steps
      })
  ```
  In this block you need to set 'scene_id' value to which your target scene index. When you wrote the program script for scene 3, you need to change 'scene_id' value to 3. And run the block.
  
  In the next block, there are some comment lines like this:
  ```python
  # *** the following is the object adding code to environment and it has to be used here not other places.
  # *** if you need more than one object, you can use several times
  # *** the purpose of this line is to add new object even the same object is existed in same room or any other different room
  ```
  If you need to add some object which are not existed in the scene, you need to write python code right under this comment. You can add an object like this:
  ```python
  add_object_out_of_script('cat', 'livingroom', 'sofa', 'ON', 0)
  ```
  This python function is written in this notebook somewhere above some blocks, you can check the description of it if you need. **Please note that you don't need to add manually everytime you need a new object because I developed this notebook to add the required object automatically as needed. But you may need to customize the location of newly added object. You can change positions at the 'possible_add_obj_position' JSON data located in the uppermost block. For some objects, you have to write manually. You will know when because an error will show when an object can't be added automatically.**
  
  And then, you need to change 'initial_room' value to your desired room name where agent will be created. When everything is ready, you can run this block. It will generate the required images and JSON data respectively.
  After that, you need to run two more blocks as its sequence to generate videos output.
  With this steps, you are completely run the program. Since the code might be updated in anytimes as it needed, I request you to read every single comment in this notebook.

### [scenario_generate_graph_and_video.ipynb](../demo/scenario_generate_graph_and_video.ipynb)
**Objective** : Mainly used for data generation until the new camera setting is used. The latest simulator I used for this notebook is Build_2023_0404. Please read the comments carefully when you used this notebook. Some code should be added or some value should be changed according to the program requirements in advance of execution. The data output will be one third-person view video, one AUTO camera switching video and four fixed view videos.

## Supplements
### [Data_Renaming.ipynb](../demo/Data_Renaming.ipynb)
Please ignore this file.  
**Objective** : Only used to rename/modify the existing output data that generated before we changed category's program files and output data structure, like that file name should include underscore, file name should be unique, program name shouldn't include underscore, folder names under 'graph states' folder shouldn't have underscore, etc...

### [Notebook_for_rename.ipynb](../demo/Notebook_for_rename.ipynb)
**Objective** : When we changed the category's program files and output data structure, I used this notebook for modified new  program files. This file is a temporary used file. Later, I fixed the main notebook file 'scenario_generate_graph_and_video.ipynb' and used that file continuously. This file functions are exactly the same with main file except for output data file/folder names.
