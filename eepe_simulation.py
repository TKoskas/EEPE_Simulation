import numpy as np
import matplotlib.pyplot as plt

def generate_exposure(timesteps, max_exposure=100):
    """
    Simulate expected exposures (EE) over time.
   
    Args:
        timesteps (int): Number of time intervals.
        max_exposure (float): Maximum possible exposure.
   
    Returns:
        np.array: Simulated exposures over time.
    """
    return np.random.uniform(0, max_exposure, timesteps)

def calculate_eepe(exposures, time_intervals):
    """
    Calculate the Expected Effective Positive Exposure (EEPE).
   
    Args:
        exposures (np.array): Array of expected exposures at each time interval.
        time_intervals (int): Total number of time intervals.
   
    Returns:
        float: EEPE value.
    """
    return np.sum(exposures) / time_intervals

# Parameters
timesteps = 12  # Representing 12 months
max_exposure = 100  # Maximum possible exposure in millions

# Simulate expected exposures
exposures = generate_exposure(timesteps, max_exposure)

# Calculate EEPE
eepe = calculate_eepe(exposures, timesteps)

# Display results
print("Simulated Exposures (EE) over time:")
print(exposures)
print(f"\nExpected Effective Positive Exposure (EEPE): {eepe:.2f} million")

# Visualization
plt.plot(range(1, timesteps + 1), exposures, marker='o', label="Expected Exposure (EE)")
plt.axhline(y=eepe, color='r', linestyle='--', label=f"EEPE = {eepe:.2f}")
plt.title("Expected Exposure (EE) and EEPE")
plt.xlabel("Time (Months)")
plt.ylabel("Exposure (Millions)")
plt.legend()
plt.grid(True)
plt.show()
