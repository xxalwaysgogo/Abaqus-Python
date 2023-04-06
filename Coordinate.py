# Edit Coordinate of INP file (Abaqus) with Python.

input_file = 'C:/Users/92898/Desktop/작업/230406/original.inp'
txt_file = 'C:/Users/92898/Desktop/작업/230406/original.txt'

# 读取节点坐标文件
with open(txt_file) as f:
    lines = f.readlines()
    coords = [[float(v) for v in line.strip().split(',')] for line in lines]

# 打开Abaqus input文件进行修改
with open(input_file) as f_in, open('C:/Users/92898/Desktop/작업/230406/modified_input_file.inp', 'w') as f_out:
    node_section = False
    for line in f_in:
        if node_section and "*Element" in line:
            # 结束读取坐标节点
            node_section = False

        if node_section and line.strip():
            # 读取节点坐标
            values = line.strip().split(",")
            node_id = int(values[0])
            x, y, z = float(values[1]), float(values[2]), float(values[3])
            x1, y1, z1 = coords[node_id - 1]
            x_new, y_new, z_new = x - 0.1 * x1, y - 0.1 * y1, z - 0.1 * z1
            # 写入新的节点坐标
            f_out.write("{},{},{},{}\n".format(node_id, x_new, y_new, z_new))
        else:
            f_out.write(line)

        if "*Node" in line and "Output" not in line:
            # 开始读取坐标节点
            node_section = True
