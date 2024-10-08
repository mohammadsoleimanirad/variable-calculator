


import math

def mesh_grid(central_position, size, step_size=1):
    # Ensure the central position and size are of the same length
    if len(central_position) != len(size):
        raise ValueError("Central position and size must have the same length.")

    # Calculate the number of points in each dimension
    dimensions = []
    for dim_size in size:
        # Calculate the number of points, adding 1 for the central point
        num_points = (dim_size // step_size) + 1
        dimensions.append(num_points)

    # Create the mesh grid
    grid = []
    for i in range(dimensions[0]):
        row = []
        for j in range(dimensions[1]):
            # Calculate the coordinates based on the central position and step size
            x = central_position[0] + (i - dimensions[0] // 2) * step_size
            y = central_position[1] + (j - dimensions[1] // 2) * step_size
            row.append((x, y))
        grid.append(row)

    return grid

def calculate_electric_field_and_potential(charges, point=(0, 0)):
    k = 8.99e9  # Coulomb's constant in N m²/C²

    # Unpack the point
    x, y = point

    # Initialize net electric field components and potential
    E_net_x = 0
    E_net_y = 0
    V_net = 0

    # Loop through each charge and its position
    for charge, pos in charges:
        q = charge
        x_charge, y_charge = pos

        # Calculate distance from charge to the point
        r = math.sqrt((x - x_charge) ** 2 + (y - y_charge) ** 2)

        if r == 0:
            # Handle the case where the point is at the location of the charge
            E_net_x = float('inf') if q > 0 else float('-inf')
            E_net_y = float('inf') if q > 0 else float('-inf')
            V_net = float('inf')  # Electric potential at the location of a point charge
            return (E_net_x, E_net_y), V_net

        # Calculate electric field due to this charge
        E = k * abs(q) / r**2

        # Calculate components of electric field
        E_x = E * (x - x_charge) / r
        E_y = E * (y - y_charge) / r

        # Update net electric field components
        E_net_x += E_x
        E_net_y += E_y

        # Calculate electric potential due to this charge
        V_net += k * q / r

    return (E_net_x, E_net_y), V_net

def calculate_field_and_potential_on_mesh(charges, central_position, size, step_size=1):
    # Create the mesh grid
    grid = mesh_grid(central_position, size, step_size)

    # Initialize matrices for electric field and potential
    electric_field_matrix = []
    potential_matrix = []

    # Iterate over each point in the mesh grid
    for row in grid:
        E_row = []
        V_row = []
        for point in row:
            electric_field, potential = calculate_electric_field_and_potential(charges, point)
            E_row.append(electric_field)
            V_row.append(potential)
        electric_field_matrix.append(E_row)
        potential_matrix.append(V_row)

    return electric_field_matrix, potential_matrix

# Example usage
charges = [
    (-5, (1, 2)),  # Charge 1
    (10, (4, 5)),  # Charge 2
    (3, (2, -1))   # Charge 3
]

central_position = (0, 0)
size = (2, 4)
step_size = 1

electric_field_matrix, potential_matrix = calculate_field_and_potential_on_mesh(charges, central_position, size, step_size)

# Print the results
print("Electric Field Matrix (E):")
for row in electric_field_matrix:
    print(row)

print("\nPotential Matrix (V):")
for row in potential_matrix:
    print(row)


#meshcode 
