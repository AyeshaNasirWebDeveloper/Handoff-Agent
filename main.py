import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = external_client,
)

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True
)

# Agent 1: Mood Analyzer
mood_analyzer = Agent(
    name="Mood Analyzer",
    instructions="Analyze the user's mood from their message. "
                "Respond with ONLY one of these exact mood labels: "
                "'happy', 'excited', 'neutral', 'sad', 'stressed', 'angry'. "
                "Do not add any other text or explanation.",
    model=model,
)

# Agent 2: Activity Suggester
activity_suggester = Agent(
    name="Activity Suggester",
    instructions="Suggest a helpful activity based on the user's mood. "
                "Keep the suggestion brief (1-2 sentences). "
                "Focus on activities that might improve their mood if it's negative.",
    model=model,
)

def analyze_mood_and_suggest():
    user_input = input("How are you feeling today? ")
    
    # Run Agent 1
    mood_result = Runner.run_sync(
        mood_analyzer,
        user_input,
        run_config=config
    )
    
    mood = mood_result.final_output.lower().strip()
    print(f"\nMood detected: {mood}\n")
    
    # moods checking
    negative_moods = ['sad', 'stressed', 'angry']
    if mood in negative_moods:
        # Run Agent 2 
        suggestion_result = Runner.run_sync(
            activity_suggester,
            f"The user is feeling {mood}. Suggest an activity to help.",
            run_config=config
        )
        print(f"Suggested activity: {suggestion_result.final_output}\n")
    else:
        print("Glad to hear you're doing well! Keep it up!\n")

analyze_mood_and_suggest()