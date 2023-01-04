import bpy
import sys
argv = sys.argv
# argv = argv[argv.index("--") + 1:]  # get all args after "--"

print(argv)

# C:\\Users\\sacha\\Desktop\\X\\Prog\\Repo\\stoneTribes-game\\Assets\\St_Project\\UnityAsset\\Meshes\\SalsaIntegration\\CasualSuit.mhx2
# C:\\Users\\sacha\\Desktop\\X\\3D\\ExportedFromBlenderScript.fbx

mhx2Path = sys.argv[-2]
fbxPath = sys.argv[-1]

print(mhx2Path)

## Region Delete All in scene
object_to_delete = bpy.data.objects['Camera']
bpy.data.objects.remove(object_to_delete, do_unlink=True)
object_to_delete = bpy.data.objects['Cube']
bpy.data.objects.remove(object_to_delete, do_unlink=True)
object_to_delete = bpy.data.objects['Light']
bpy.data.objects.remove(object_to_delete, do_unlink=True)

## Import MHX2
bpy.ops.import_scene.makehuman_mhx2(
'EXEC_DEFAULT', 
filepath=mhx2Path )

## Export File
bpy.ops.export_scene.fbx(filepath=fbxPath, use_selection=False)