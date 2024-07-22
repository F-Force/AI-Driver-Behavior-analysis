# Voice-Activated AI Navigation System

This project integrates a voice-activated AI with a Google Map, allowing users to interact using voice commands. The system fetches route information, suggests alternative routes, and provides real-time updates on travel conditions.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [API Keys](#api-keys)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Voice-activated search bar using the Web Speech API
- Real-time route updates and alternative route suggestions
- Integration with Google Maps to display routes and locations
- Python backend to process voice commands and interact with Google Maps API
- Live accidents or construction updates along the routes you want to take
- Notify when you start your car without putting the seat belt
- Let's you know when your car has a specific problem and what is the nearest place you can get it fixed

### Prerequisites

- Python 3.x
- Flask
- Google Maps API Key
- Modern web browser (for Web Speech API support)
- or a mobile device

### Setup

Just a plug and play

Must have internet access or download route of the location before you go out of the radar

## Usage

1. Open the application on your device.
2. Click the "Start Voice Command" button to activate the voice command interface.
3. Speak a command, such as "navigate to [location]" or "check route."
4. The system will process the command, update the Google Map, and provide relevant information.

### Voice Commands

- **Navigate to [location]**: Finds the location and provides route information.
- **Check route**: Provides information about road conditions or construction.
- **Weather**: Provides current weather conditions near the location.
- **Petrol station**: Finds nearby fuel stations.
- **Accidents**: Reports any accidents on the route.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript (Web Speech API)
- **Backend**: Python, Flask
- **APIs**: Google Maps API, Google Directions API, Google Geolocation API

## API Keys

Make sure to replace `'YOUR_GOOGLE_MAPS_API_KEY'` with your actual Google Maps API key in `app.py`.

## Project Structure

voice-activated-ai-navigation/
│
├── templates/
│ └── index.html # Main HTML file for the web interface
│
├── static/
│ ├── css/
│ │ └── styles.css # CSS file for styling the web interface
│ ├── js/
│ │ └── script.js # JavaScript file handling voice commands and map updates
│
├── app.py # Flask backend for processing commands and interacting with Google Maps API
├── requirements.txt # List of required Python packages
├── README.md # Project documentation
├── LICENSE # License file for the project
└── .gitignore # Git ignore file

## Markdown


- `templates/index.html`: The main HTML file that includes the structure of the web page, Google Map integration, and voice command interface.
- `static/css/styles.css`: Contains the CSS styles for the web interface, ensuring the design and layout are user-friendly.
- `static/js/script.js`: JavaScript file responsible for handling the voice commands, interacting with the Web Speech API, and updating the Google Map.
- `app.py`: Flask backend that processes the voice commands received from the frontend, interacts with the Google Maps API, and provides the necessary route information and updates.
- `requirements.txt`: A file listing all the Python packages required to run the Flask backend, ensuring easy setup and installation of dependencies.
- `README.md`: Project documentation file that includes an overview, installation instructions, usage details, and other relevant information.
- `LICENSE`: The license file for the project, specifying the terms under which the project can be used, modified, and distributed.
- `.gitignore`: A file specifying which files and directories should be ignored by Git when committing changes, ensuring that unnecessary files (e.g., temporary files, API keys) are not included in version control.


