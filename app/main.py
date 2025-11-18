# main.py
import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.queries import process_question, LLMError  # import LLMError

app = FastAPI()

# Mount static files like CSS and images
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="app/templates")


# ----------------------
# 1) USER INPUT VALIDATION
# ----------------------
def validate_question(question: str) -> str:
    if question is None:
        raise ValueError("Question is required.")

    question = question.strip()

    if not question:
        raise ValueError("Question cannot be empty.")

    if len(question) > 2000:
        raise ValueError("Your question is too long. Please shorten it.")

    return question


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# ----------------------
# 2) HANDLE LLM + INPUT ERRORS
# ----------------------
@app.post("/get-answer", response_class=HTMLResponse)
async def get_answer(request: Request, question: str = Form(...)):
    error_message = None
    answer = None

    try:
        # Validate user input
        question = validate_question(question)

        # Call RAG pipeline (can raise LLMError)
        answer = process_question(question)

    except ValueError as e:
        # Input validation problems
        error_message = str(e)

    except LLMError as e:
        # LLM/Groq/OpenAI issues (timeout, rate limit, etc.)
        print(f"[LLM ERROR] {e}")
        error_message = (
            "The answer service is temporarily unavailable. "
            "Please try again shortly."
        )

    except Exception as e:
        # Unexpected bug
        print(f"[UNEXPECTED ERROR] {e}")
        error_message = "An unexpected error occurred. Please try again later."

    # Render page with result or error
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "answer": answer,
            "question": question,
            "error": error_message,
        },
    )
