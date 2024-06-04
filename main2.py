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

def read_points_from_file(filename):
  points = []
  with open(filename, 'r') as file:
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

  n_to_points = {}
  for i, point in enumerate(points):
    if point[3] not in n_to_points:
      n_to_points[point[3]] = []
    n_to_points[point[3]].append((i, point))

  n_values = list(n_to_points.keys())

  checked_combinations = 0
  for comb in itertools.combinations_with_replacement(n_values, 4): # Iterate through the 4 points
    if sum(comb) == 100:
      potential_combinations = itertools.product(*[n_to_points[n] for n in comb])
      for indices_points in potential_combinations:
        indices, tetrahedron_points = zip(*indices_points)
        if len(set(indices)) == 4:
          volume = volume_of_tetrahedron(*tetrahedron_points)
          if volume < smallest_volume:
            smallest_volume = volume
            best_combination = sorted(indices)
    checked_combinations += 1
  return best_combination

def main():
  filename = 'points_large.txt' # swap file name
  points = read_points_from_file(filename)

  print(f"Points read from file ({len(points)}):")
  for i, point in enumerate(points[:100]):
    print(f"{i}: {point}")

  if len(points) > 100:
    print(f"... and {len(points) - 100} more points") # To show how many points are left due to the lengthy runtime 

  indices = find_smallest_tetrahedron(points)
    
  if indices:
    print(f"Selected Indices: {indices}")

if __name__ == "__main__":
  main()
