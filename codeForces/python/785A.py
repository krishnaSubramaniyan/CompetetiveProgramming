total_faces = 0
for i in range(int(input())):
    match input():
        case 'Tetrahedron':
            total_faces += 4
        case 'Cube':
            total_faces += 6
        case 'Octahedron':
            total_faces += 8
        case 'Dodecahedron':
            total_faces += 12
        case 'Icosahedron':
            total_faces += 20

print(total_faces)
