import bpy

class NG_PT_Panel(bpy.types.Panel):
    bl_idname ="NG_PT_Panel"
    bl_label ="Nature Green"
    bl_category = "Nature Green"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row0 = layout.row()
        row0.operator('view3d.cursor_center', text="bounding box")
        row0.operator('view3d.cursor_center', text="High resolution")


        row1 = layout.row()
        row1.operator('view3d.cursor_center', text="Grass Types")

        row2 = layout.row()
        row2.operator('view3d.cursor_center', text="Flower Types")

        row10 = layout.row()
        row10.operator('view3d.cursor_center', text="Add Nature green library")
