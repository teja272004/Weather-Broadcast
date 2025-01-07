# Weather Chatbot with Flask and Open-Meteo API

This project demonstrates a simple chatbot application that provides current weather information for any city. It uses Flask for the backend, Open-Meteo API for weather data, and OpenCage API for geocoding (fetching latitude and longitude).

---

## Features
- Accepts city names as input.
- Dynamically fetches latitude and longitude of the city using the OpenCage API.
- Retrieves current weather data (temperature, wind speed) using the Open-Meteo API.
- User-friendly frontend created with HTML and JavaScript.

---

## File Structure
```markdown
weather-chatbot/
├── app.py               # Flask backend
├── weather_utils.py     # Utility functions for APIs
├── templates/
│   └── index.html       # Frontend interface
└── requirements.txt     # Python dependencies
```

---

## Installation

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/weather-chatbot.git
   cd weather-chatbot
   ```

2. **Set Up Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up API Keys**:
   - Sign up at [OpenCage](https://opencagedata.com/) and get your API key.
   - Update the `GEOCODING_API_KEY` variable in `app.py` with your OpenCage API key.

---

## Running the Application

1. **Start the Backend**:
   ```bash
   python app.py
   ```
   This will start the Flask app at `http://127.0.0.1:5000`.

2. **Access the Frontend**:
   - Open `templates/index.html` in your browser.
   - Enter the name of a city and click "Get Weather" to see the current weather information.

---

## API Details

### OpenCage Geocoding API
- Used to fetch latitude and longitude of the city.
- Documentation: [OpenCage API Docs](https://opencagedata.com/api)

### Open-Meteo API
- Used to retrieve current weather data.
- Documentation: [Open-Meteo API Docs](https://open-meteo.com/en/docs)

---

## Example Usage
1. Enter the city name (e.g., `London`).
2. The app fetches the latitude and longitude using the OpenCage API.
3. It retrieves weather data for the coordinates using the Open-Meteo API.
4. Displays:
   ```
   The current weather in London is 15°C with a wind speed of 10 km/h.
   ```

---

## Screenshots

**Frontend Interface**:

<img width="685" alt="image" src="https://github.com/user-attachments/assets/c26a73a7-6b4a-4b64-8ad9-d453c45a1a80" />




---

## Technologies Used
- **Backend**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: OpenCage, Open-Meteo

---

## Future Enhancements
- Add hourly and weekly weather forecasts.
- Improve UI/UX of the frontend.
- Deploy the application to a cloud platform like AWS, Heroku, or Google Cloud.

---

## Contributing
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For any queries or suggestions, feel free to reach out:
- **Email**: mnbtsharma@gmail.com
- **GitHub**: https://github.com/teja272004

