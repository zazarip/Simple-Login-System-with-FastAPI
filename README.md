# Simple Login System with FastAPI

This project demonstrates a simple login system implemented using FastAPI, where users can log in with a username and password.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)

## Description

The internet is a network where people send and receive data; when we log into applications, APIs are used to send and receive data between the frontend and the backend. This project showcases a basic login system where users can log in with their credentials.

## Features

- User authentication using a simple username and password combination
- Frontend created with HTML and JavaScript for user interaction
- Backend built using FastAPI to handle login requests
- SQLite database used to store user login information
- Cross-Origin Resource Sharing (CORS) configuration for enabling cross-origin requests

## Prerequisites

- Python 3.x installed
- Basic understanding of Python, web development, and APIs

## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`
5. Create the SQLite database and table by following the instructions in the "database" directory.

## Usage

1. Start the FastAPI server: `uvicorn main:app --reload`
2. Open your web browser and navigate to `http://localhost:8000` to access the login page.
3. Enter a valid username and password to log in.

## API Endpoints

- `/login` (POST): Endpoint for user authentication. Requires a JSON payload containing `username` and `password`.

## Known Issues

### Issue with POST Request

I'm currently facing an issue where the POST request to the `/login` endpoint is not being properly handled. Despite following the recommended setup and debugging steps, I'm still encountering a "501 Unsupported method ('POST')" error. If you have experience with FastAPI or web development, your insights would be greatly appreciated. Feel free to contribute by suggesting solutions, identifying potential causes, or sharing your expertise.

If you have any information that could help resolve this issue, please don't hesitate to reach out or submit a pull request. Your assistance would be invaluable in moving this project forward.

Thank you for your understanding and support!

## Contributing

Contributions are welcome! If you find a bug or have an enhancement in mind, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
