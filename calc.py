def calculate_variable(Q=None, V=None, C=None):
    # Check that exactly two variables are provided
    variables = [Q, V, C]
    provided_count = sum(variable is not None for variable in variables)
    
    if provided_count != 2:
        raise ValueError("Provide exactly two out of Q, V, and C.")
    
    # Calculate the missing variable
    if Q is None:
        Q = C * V
        return Q
    elif V is None:
        V = Q / C
        return V
    elif C is None:
        C = Q / V
        return C

# Example usage:
# calculate_variable(Q=10, V=5)  # Returns C (Coulombs)
# calculate_variable(Q=None, V=5, C=2)  # Returns Q (Coulombs)
