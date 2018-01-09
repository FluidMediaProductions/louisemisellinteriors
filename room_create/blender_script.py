import bpy
import json

bpy.ops.object.select_all(action='DESELECT')

with open("room_data.json", "r") as f:
    data = json.load(f)

bpy.ops.object.add(type='MESH')
ob = bpy.context.object
ob.location = (0, 0, 0)
ob.select = True
me = ob.data

floorplan = data["floorplan"]
wall_height = data["wall_height"]/100

verts = []
faces = [[]]

seen_walls = []


def get_next_wall(cur_wall=None):
    if cur_wall is None:
        seen_walls.append(0)
        return floorplan[0]
    else:
        for e, wall in enumerate(floorplan):
            if e not in seen_walls:
                if wall[0] in cur_wall or wall[1] in cur_wall:
                    if wall[1] in cur_wall:
                        wall[0], wall[1] = wall[1], wall[0]
                    seen_walls.append(e)
                    return wall


wall = get_next_wall()
while wall is not None:
    face = []
    first = True
    for vertex in wall:
        v1 = (vertex[0]/100, vertex[1]/100, (0 if first else wall_height))
        v2 = (vertex[0]/100, vertex[1]/100, (wall_height if first else 0))
        if v1 in verts:
            face.append(verts.index(v1))
            if first:
                faces[0].append(verts.index(v1))
        else:
            face.append(len(verts))
            if first:
                faces[0].append(len(verts))
            verts.append(v1)
        if v2 in verts:
            face.append(verts.index(v2))
            if not first:
                faces[0].append(verts.index(v2))
        else:
            face.append(len(verts))
            if not first:
                faces[0].append(len(verts))
            verts.append(v2)
        first = False
    faces.append(face)
    wall = get_next_wall(wall)

me.from_pydata(verts, [], faces)
me.update()

bpy.ops.export_scene.autodesk_3ds(filepath="/tmp/room.3ds", use_selection=True)
