# Chatbot Project

A simple web-based chatbot built with Django, using spaCy and scikit-learn for natural language processing. The chatbot responds to user queries based on predefined question-answer pairs, displayed in a modern, responsive interface styled with Bootstrap 5.

## Features
- Web interface for interacting with the chatbot.
- Template-based question-answer system using TF-IDF for matching user input.
- Responsive design with message bubbles for user and bot.
- Fixed-height chat window with scrollable messages.
- Input field and send button pinned to the bottom of the page.
- CSRF protection for secure POST requests.

## Tech Stack
- **Backend**: Django 4.2+
- **NLP**: spaCy (`en_core_web_sm`), scikit-learn (TF-IDF)
- **Frontend**: Bootstrap 5, jQuery (via CDN)
- **Database**: SQLite (default for development)
- **Deployment**: Optional Docker support

## Project Structure
```
chatbot_project/
├── chatbot/
│   ├── __init__.py
│   ├── bot.py               # Chatbot logic (TF-IDF, question-answer matching)
│   ├── migrations/          # Database migrations
│   ├── templates/
│   │   ├── chatbot/
│   │   │   ├── chat.html    # Web interface for chat
│   ├── static/              # Static files (optional for custom CSS/JS)
│   ├── admin.py
│   ├── apps.py
│   ├── models.py            # Optional models for storing Q&A
│   ├── tests.py
│   ├── urls.py             # App URLs
│   ├── views.py            # View for handling chat requests
├── chatbot_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URLs
│   ├── wsgi.py
├── data/
│   ├── data.csv            # Optional Q&A data (if not using database)
├── db.sqlite3              # SQLite database
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── .gitignore              # Git ignore file
├── README.md               # Project documentation
```

## Installation

### Prerequisites
- Python 3.11+
- pip
- Optional: Docker and Docker Compose for containerized deployment

### Local Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/AntiViruS90/CodeAlpha_Basic_Chatbot.git
   cd chatbot_project
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download spaCy model**:
   ```bash
   python -m spacy download en_core_web_sm
   ```

5. **Apply migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the chatbot**:
   Open `http://localhost:8000` in your browser.

### Docker Setup
1. **Ensure Docker and Docker Compose are installed**:
   - [Docker Installation](https://docs.docker.com/get-docker/)
   - [Docker Compose Installation](https://docs.docker.com/compose/install/)

2. **Build and run containers**:
   ```bash
   docker-compose up --build
   ```

3. **Apply migrations**:
   ```bash
   docker-compose exec web python manage.py makemigrations
   docker-compose exec web python manage.py migrate
   ```

4. **Access the chatbot**:
   Open `http://localhost:8000` in your browser.

5. **Stop containers**:
   ```bash
   docker-compose down
   ```

## Usage
- Enter a message in the input field at the bottom of the page and press "Send" or Enter.
- The chatbot matches your input to predefined questions using TF-IDF and responds with the closest answer.
- Messages are displayed as bubbles (blue for user, gray for bot) in a fixed-height chat window.
- Example questions: "How are you?", "What is your name?", "Tell me a joke!"

## Adding New Questions and Answers
1. **Edit `bot.py`**:
   Update the `questions` and `responses` lists in `chatbot/bot.py`:
   ```python
   questions = [
       "What is the weather like?",
       "How are you?",
       # Add more questions
   ]
   responses = [
       "Tell me your location, and I can check the weather!",
       "I'm doing great, thanks for asking!",
       # Add corresponding responses
   ]
   ```

2. **Optional: Use SQLite**:
   Create a `QA` model in `chatbot/models.py` and update `bot.py` to load data from the database:
   ```python
   from .models import QA
   questions = [qa.question for qa in QA.objects.all()]
   responses = [qa.response for qa in QA.objects.all()]
   ```

### Video Tutorial
P.S. You can view a video tutorial on how to use the app at this [link](https://drive.google.com/file/d/1dy1k7J8_wGHI_9X2SBhbxHwMPjgky1-N/view?usp=sharing)
