# Import Meteostat library and dependencies
import datetime
from meteostat import Point, Daily

# Set time period
start = datetime.datetime.now() + datetime.timedelta(days=1)
end = datetime.datetime.now() + datetime.timedelta(days=2)

# Create Point for London, UK
location = Point(51.5072, 0.1276)

# Get daily data for tomorrow
data = Daily(location, start, end)
data = data.fetch()

# Display results to terminal
print(data)
