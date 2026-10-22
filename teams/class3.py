import numpy as np
"""""
scores = np.array([10.5, 11.2, 10.8, 10.3])
scores = np.array([10, 20, 30, 40])
scores * 2
print("Scores multiplied by 2", scores * 2)
print(f"This is good {scores * 2}")
"""""

athletes = np.array([
    "Okocha",
    "Mensah",
    "Ibrahim",
    "Asante",
    "Boateng"
])
print(athletes)

times = np.array([
    [10.45, 10.31, 10.28, 10.22, 10.18, np.nan, 10.15, 10.19],
    [11.02, 10.85, np.nan, 10.71, 10.65, 10.69, 10.55, np.nan],
    [10.89, 10.71, 10.65, 10.50, np.nan, 10.42, 10.38, 10.31],
    [10.62, 10.55, 10.51, np.nan, 10.45, 10.40, 10.36, 10.30],
    [np.nan, 10.92, 10.85, 10.80, 10.75, 10.71, 10.65, 10.60]
])
print(times.shape)
print(np.isnan(times))
print(~np.isnan(times))
races_not_run = (np.isnan(times)).sum(axis=1)
print(races_not_run)

races_run = (~np.isnan(times)).sum(axis=1)
for name, races in zip(athletes, races_run):
    print(name, races)

best_times = np.nanmin(times, axis=1)
### np.nanmin() simply means:

for name, best in zip(athletes, best_times):
    print(f"{name}: {best:.2f}s")