# IGT

The IP Geolocation Tool is an application designed to retrieve detailed information about any IP address using the IPGeolocation API. The application organizes the geolocation data in a clean and readable format.

---

## Features

- Retrieve detailed geolocation information, including:
  - IP Address, Continent, Country, Region, City, and District
  - Latitude and Longitude
  - ISP, Organization, and ASN details
  - Timezone, Country Flag, Calling Code, and more

---

## Requirements

- **Operating System**: Windows 7 or newer.
- **Python Version**: 3.12 or later.
- **Dependencies**:
  - `requests`
  - `tkinter` (built into Python)

---

## Important Note

This tool **does not include an API key**. You will need to obtain your own API key from IPGeolocation to use the application. The key is required for the tool to fetch data from the API. Follow the steps in the **API Configuration** section to set it up.

---

## Installation

1. **Download the Source Code**:
   - Clone the repository or download the source files as a ZIP archive.

2. **Install Dependencies**:
   Run the following command in a terminal or command prompt:
   ```bash
   pip install requests
   ```

3. **Run the Application**:
   Launch the script using Python:
   ```bash
   python igt.py
   ```

---

## API Configuration

To use the tool, you need an API key from IPGeolocation:

1. **Obtain an API Key**:
   - Visit [IPGeolocation](https://ipgeolocation.io/) and create an account.
   - Generate a free or paid API key based on your requirements.

2. **Set Up Your API Key**:
   - Open the `igt.py` file located in the application's directory.
   - Replace `<YOUR_API_KEY>` with your API key:

     {
         "api_key": "YOUR_API_KEY_HERE"
     }

---

## Usage

1. **Launch the Application**:
   Start the tool by running the `igt.py` script.

2. **Enter an IP Address**:
   - Type or paste the IP address into the input field.
   - Press `Enter` or click the "Search" button.

3. **View Results**:
   The application will display detailed geolocation information for the provided IP address in a clean, organized format.

---

## Development

To modify or extend the application:

1. Clone the repository or download the source files.
2. Install required Python packages:
   ```bash
   pip install requests
   ```
3. Edit the script (`igt.py`) as needed.
4. Run the script to test your changes:
   ```bash
   python igt.py
   ```

---

## Known Issues

- Ensure the API key is correctly configured, or the tool will not fetch data.
- Results depend on the quality of the data provided by the IPGeolocation API.

---

## Acknowledgments

- **API Provider**: [IPGeolocation](https://ipgeolocation.io/) for its comprehensive and accurate geolocation services.

---

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute the software as long as you comply with the license terms.

---
