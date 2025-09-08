# OBD-II Diagnostic App

This project is a simple OBD-II diagnostic application that allows users to connect to their vehicle's ECU (Engine Control Unit) and retrieve real-time data such as engine RPM, temperature, and diagnostic trouble codes (DTCs). The application is built using Python and utilizes the `python-OBD` library for communication with the OBD-II module.

## Project Structure

```
obd2-diagnostic-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── gui.py           # GUI code using Tkinter
│   ├── obd_reader.py     # OBD-II communication handling
│   └── types
│       └── __init__.py  # Custom types and data structures
├── requirements.txt     # Project dependencies
├── README.md            # Project documentation
└── .gitignore           # Files to ignore in Git
```

## Requirements

To run this project, you need to install the following dependencies:

- python-OBD
- Tkinter (usually included with Python installations)

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Usage

1. Connect your OBD-II module (e.g., ELM327) to your vehicle.
2. Run the application:

```
python src/main.py
```
<img width="3455" height="2160" alt="image" src="https://github.com/user-attachments/assets/b55917da-85f1-4cca-a831-18f224fd15d4" />


3. The GUI will display real-time data from your vehicle.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. 

## License

This project is open-source and available under the MIT License. CHEBOUT IBRAHIM RASSIM 
