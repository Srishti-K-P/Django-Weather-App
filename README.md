# The Weather App

The Weather App is a Django-based web application that provides real-time weather updates for cities worldwide. It uses the OpenWeatherMap API to fetch weather data and Google Maps API to display location maps.

## Features

- Real-time weather updates based on user-provided city names.
- Displays temperature, weather description, day, humidity, wind speed, and weather icon.
- Integrated Google Maps to display the location of the city.
- Share the fetched weather information with others.

## Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: OpenWeatherMap API, Google Maps JavaScript API

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python (3.x recommended)
- Django
- OpenWeatherMap API Key
- Google Maps API Key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Srishti-K-P/Django-Weather-App.git
   cd Django-Weather-App
   
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   
3. Set up environment variables:
   - Create a .env file in the root directory.
   - Add the following environment variables:

     ```bash
     OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
     GOOGLE_MAPS_API_KEY=your_google_maps_api_key
     
4. Run migrations:

   ```bash
   python manage.py migrate

5. Start the development server:

   ```bash
   python manage.py runserver

6. Access the application at your local host

## Usage

- Enter a city name in the search input and press Enter.
- View real-time weather information for the city.
- Click on the "Share" button to share weather information using the Web Share API.

## Screenshots

![Weather App Screenshot](https://github.com/Srishti-K-P/Django-Weather-App/blob/main/screenshots/SS1.png)

![Weather App Screenshot](https://github.com/Srishti-K-P/Django-Weather-App/blob/main/screenshots/SS2.png)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

