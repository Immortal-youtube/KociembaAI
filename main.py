import kociemba
#U R F D L B 
cube = "gbwbwgowyrogyrwyrrygbwggwygooogyywobrrbyororbrwyobbwbg"

cube = cube.replace('y', 'D')
cube = cube.replace('r', 'R')
cube = cube.replace('b', 'B')
cube = cube.replace('w', 'U')
cube = cube.replace('o', 'L')
cube = cube.replace('g', 'F')
print(cube)
solution = kociemba.solve(str(cube))
print(solution)