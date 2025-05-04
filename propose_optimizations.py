def propose_optimizations(issues):
    optimizations = []
    for location, count in issues.items():
        if count > 0: # Umbral para considerar un problema significativo
            optimizations.append(f"Aumentar la frecuencia de buses en {location}")
    print(f"propose_optimizations: {optimizations}")        
    return optimizations

if __name__ == "__main__":
    issues = {'Bogotá': 1, 'Medellín': 8, 'Cali': 6}
    optimizations = propose_optimizations(issues)
    