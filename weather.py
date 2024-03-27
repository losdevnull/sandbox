import json

def get_current_weather(location, unit="celsius"):
  """Get the current weather in a given location"""
  weather_info = {
      "location": location,
      "temperature": "20",
      "unit": unit,
      "forecast": ["sunny", "windy"],
  }
  return json.dumps(weather_info)
