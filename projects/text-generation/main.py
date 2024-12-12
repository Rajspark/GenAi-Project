from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

# Initialize FastAPI
app = FastAPI()

# Set up the generative AI model
genai.configure(api_key="AIzaSyAtHqFyNMfGY4-NGbHyLpTwZUOSW_c8Lew")  
model = genai.GenerativeModel("gemini-1.5-flash")

# Pydantic model for input validation
class StoryRequest(BaseModel):
    title: str

# POST endpoint for generating a story based on the title
@app.post("/generate_story")
async def generate_story(request: StoryRequest):
    # Get the title from the request
    title = request.title
    
    # Generate story using the provided title
    response = model.generate_content(f"Write a very short story about a {title}")
    
    # Return the generated story as a response
    return {"title": title, "story": response.text}

