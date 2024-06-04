import itertools

def volume_of_tetrahedron(p1, p2, p3, p4):
    # Vectors from p1 to p2, p3, and p4
  AB = (p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2])
  AC = (p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2])
  AD = (p4[0] - p1[0], p4[1] - p1[1], p4[2] - p1[2])

    # Direct calculation of the cross product components
  cross_product = (
    AB[1] * AC[2] - AB[2] * AC[1],
    AB[2] * AC[0] - AB[0] * AC[2],
    AB[0] * AC[1] - AB[1] * AC[0]
  )

    # Dot product of AD with the cross product of AB and AC
  scalar_triple_product = (
    AD[0] * cross_product[0] +
    AD[1] * cross_product[1] +
    AD[2] * cross_product[2]
  )

    # The volume of the tetrahedron
  volume = abs(scalar_triple_product) / 6.0
  return volume

def read_points_from_file(points_smallest):
  points = []
  with open(points_smallest, 'r') as file:
    for line in file:
      line = line.strip()
      if line.startswith('(') and line.endswith(')'):
        line = line[1:-1]
        x, y, z, n = map(float, line.split(', '))
        n = int(n)
        points.append((x, y, z, n))
  return points

def find_smallest_tetrahedron(points):
  smallest_volume = float('inf')
  best_combination = None

  for combination in itertools.combinations(enumerate(points), 4): # Iterate through the 4 points
    indices, tetrahedron_points = zip(*combination)
    if sum(point[3] for point in tetrahedron_points) == 100:
      volume = volume_of_tetrahedron(*tetrahedron_points)
      if volume < smallest_volume:
        smallest_volume = volume
        best_combination = indices

  return sorted(best_combination)

def main():
  filename = 'points_small.txt'  # swap file name
  points = read_points_from_file(filename)
    
  print(f"Points read from file ({len(points)}):")
  for i, point in enumerate(points):
    print(f"{i}: {point}")

  indices = find_smallest_tetrahedron(points)
    
  print(f"Selected indices: {indices}")

if __name__ == "__main__":
  main()