# Clair summer 2025 recruitment task

### Clone the repo

```bash
git clone https://github.com/goclair/clair-recruitment-task-summer-25
cd clair-recruitment-task-summer-25
```

## Backend setup instructions

### 1. Move to backend directory

```
cd backend
```

### 2. Create a .env file in the backend directory, with the provided environment variables:

```
DB_HOST=...
DB_NAME=...
DB_USER=...
DB_PASSWORD=...
OPENAI_API_KEY=...
```

### 3. Create and activate a virtual environment. Make sure to use Python >= 3.12.

On macOS/Linux:
```
python3.12 -m venv .venv
source .venv/bin/activate
```

On Windows (Command Prompt or PowerShell):
```
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
pip install -r dev-requirements.txt
```

### 5. Run the development server

Make sure your virtual environment is active, then:
```
uvicorn src.main:app --reload
```
The backend will be available at http://localhost:8000

### 6. Run code quality checks

```
black .
ruff check --fix .
mypy .
```