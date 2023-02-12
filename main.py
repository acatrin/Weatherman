# Import Meteostat library and dependencies
from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Hourly

# Set time period
start = datetime(2023, 2, 13, 16, 12)
end = datetime(2023, 2, 13, 17, 30)

# Create Point for London, UK
location = Point(51.5072, 0.1276)

# Get daily data for 2018
data = Hourly(location, start, end)
data = data.fetch()

# Plot line chart including average, minimum and maximum temperature
print(data)
