# Stealth - Key Automator

Python application that automates the pressing of the LSHIFT key every 5 seconds.

## Funcionalidades

- Activate Button: Starts the LSHIFT key automation (pressed every 5 seconds)
- Deactivate Button: Stops the automation
- Simple and intuitive graphical interface
- Real-time automation status

## Instalação

1. Make sure you have Python 3.6+ installed
2. Install the dependencies:
```bash
pip install -r requirements.txt
```

## How to use

1. Run the application:
```bash
python stealth_app.py
```

2. Click "Activate" to start the automation
3. Click "Deactivate" to stop the automation
4. Close the window to exit the application

## Dependencies

- `pynput`: For keyboard automation
- `tkinter`: For graphical interface (already included in Python)

## Notes

- The application runs the automation in a separate thread to avoid freezing the interface
- The LSHIFT key is pressed for 100ms every 5 seconds when active
- You can safely close the application at any time


