# blender-makehuman-mhx2-io-batch
Disclaimer : Because the batch script is a powershell, Windows Only ( I don't know which Powershell features are supported on MacOs/Linux )
The purpose of this batch is to gain time and avoid repetitive tasks by automate mhx2 blender conversion. 
The script will inject a mhx2 in blender and output a fbx file via scripting.
This can be usefull is your game characters are modelled in Blender and rendered in Unity. Blender is outputing an alternative space orientation 
(XYZ) that make Unity space orientation missmatch (XZY).
By using a batch, you will be able to share meshes between your Unity characters avatars ( hair, cloth, etc... )

## Prerequesites
- Makehuman software => to create .MHX2 files http://www.makehumancommunity.org/
- Blender 2.8+ ( this was tested only on 3.3 so make sure to use 3.3 if you want be sure to get things working ) => to convert .MHX2 in .FBX easily via a Blender script https://www.blender.org/download/
- Makehuman import mhx2 blender addon ( to import .MHX2 in blender ) https://github.com/makehumancommunity/mhx2-makehuman-exchange

## Convert process
- Info : You can move directly to step 13. if you just want to try the batch script.
- 1. Download and install Blender 2.8+ if required
- 2. Download and install Makehuman if required
- 3. Download Makehuman import mhx2 blender addon (Download Zip https://github.com/makehumancommunity/mhx2-makehuman-exchange)
- 4. Extract the Zip folder from Step 3.
- 5. Move import_runtime_mhx2 folder from mhx2-amkehuman-exchange-master to blender addons ( for Blender 3.3 it's located in C:\Program Files\Blender Foundation\Blender 3.3\3.3\scripts\addons )
- 6. Launch MakeHuman
- 7. In MakeHuman move to Pose/Animate and select "Default Skeleton"
- 8. In MakeHuman move to File/Export and Export to MHX2 file
- 9. Launch Blender and ensure the import mhx2 addon is enabled. Go to Edit/Preferences/Addons and Search for "mhx2" and ensure the addon is enabled. 
- 10. (Optional)
You can try to import your MHX2 by opening the MHX2 Runtime Blender Panel ( click on the + in the right side close to the Outliner window ), and click on the button Import MHX2 button. 
- 11. Download this repository
- 12. Move any number of mhx2 files you created on step 8. in the repository Directory called "Converter"
- 13. Run the powershell script (batchMakehumanMhxBlenderConverter.ps1). The batch script will be executed for each mhx2 file located in Converter folder. Close Blender for each operation in order to execute the next operation. The fbx files converted in the process are located in Converter/Exports folder

