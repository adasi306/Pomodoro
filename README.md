# Pomodoro Timer Application

This is a Python-based Pomodoro timer application built using Tkinter. It helps users stay productive by dividing work into intervals, followed by short and long breaks.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [License](#license)

## Description

The Pomodoro timer follows the classic productivity technique:
- Work for 25 minutes.
- Take a 5-minute short break after each work session.
- Take a 20-minute long break after completing four work sessions.

## Features

1. **Timer Functionality**:
   - Countdown for work, short breaks, and long breaks.
2. **Automatic Transitions**:
   - Automatically starts the next session when a timer ends.
3. **Reset Option**:
   - Reset the timer and session count at any time.
4. **Visual Progress**:
   - Tracks completed work sessions using checkmarks.

## Requirements

- Python 3.x
- A `tomato.png` image for the timer's visual representation.

## Installation

1. Clone the repository:
```bash
   git clone <repository-url>
   cd <project-directory>
```
2. Ensure that `tomato.png` is located in the `portfolio/pomidor/` directory or the same directory as the script.

3. No additional libraries are required beyond Python's standard library.

## Running the Application

1. Run the script:
```bash
   python main.py
```
2. The application window will open, displaying:
   - A timer.
   - "Start" and "Reset" buttons.
   - A label to show progress with checkmarks.

## Project Structure

project/
├── main.py                   # Main script for the application
├── tomato.png                # Image used in the timer
└── README.md                 # Documentation

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project.
