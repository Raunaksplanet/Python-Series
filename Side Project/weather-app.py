import python_weather
import asyncio

async def get_weather():
    # Initialize the client without format argument
    client = python_weather.Client()

    try:
        # Fetch the weather for a specific location
        weather = await client.get("jaipur")

        # Print the weather object to inspect its structure
        print(weather)

        # Check if the weather object has a 'current' attribute
        if hasattr(weather, 'current'):
            # Print the current temperature
            print(f"Current temperature in New York: {weather.current.temperature}°F")
        else:
            print("The 'current' attribute is not available in the weather data.")

        # Check if the weather object has a 'forecasts' attribute
        if hasattr(weather, 'forecasts'):
            # Print the weather forecast for the next few days
            for forecast in weather.forecasts:
                print(f"{forecast.date}: {forecast.sky_text}, {forecast.temperature}°F")
        else:
            print("The 'forecasts' attribute is not available in the weather data.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the client session
        await client.close()

# Run the async function
asyncio.run(get_weather())
