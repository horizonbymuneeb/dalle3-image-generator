# README

## Project Title: Flask OpenAI Image Generator

This project is a simple Flask application that uses OpenAI's DALL-E model to generate images based on a user's input.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have the following installed:

- Python 3.6 or higher
- Flask
- OpenAI Python client

You can install the dependencies with:

```bash
pip install flask openai
```

### Installing

1. Clone the repository to your local machine.
2. Set your OpenAI API key as an environment variable. On a Mac, you can do this in your terminal with:

```bash


export

 OPENAI_API_KEY='your-api-key'
```

### Running the Application

To run the application, navigate to the directory containing `app.py` and run:

```bash
python app.py
```

The application will start on `localhost:5003`.

## How It Works

The application has two routes:

- `/`: This route renders the `index.html` template, which should contain a form for the user to input their prompt.
- `/generate`: This route accepts POST requests. It takes the 'prompt' from the form data, uses it to generate an image using OpenAI's DALL-E model, and then renders the `result.html` template, passing the URL of the generated image.

## Built With

- [Flask](https://flask.palletsprojects.com/) - The web framework used
- [OpenAI](https://openai.com/) - Used to generate images

## Authors

- Horizon By Muneeb

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.