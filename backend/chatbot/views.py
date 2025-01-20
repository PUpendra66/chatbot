from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Simple chatbot logic
def chatbot_response(user_message):
    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! What can I do for you?",
        "how are you": "I'm just a bot, but I'm doing great! How about you?",
        "who are you": "I'm your friendly chatbot, here to answer your questions!",
        "thank you": "You're welcome! Feel free to ask me anything.",
        "bye": "Goodbye! Have a great day!",
        "what is python": "Python is a high-level programming language used for web development, AI, and data science.",
        "how to learn python": "You can start with online courses on Codecademy, Udemy, or free tutorials on Python.org.",
        "what is django": "Django is a Python framework for web development, known for its simplicity and speed.",
        "how to install django": "Use `pip install django` in your terminal or command prompt.",
        "what is an api": "An API (Application Programming Interface) allows different software applications to communicate with each other.",
        "what is react": "React is a JavaScript library for building interactive user interfaces.",
        "how to host a website": "You can host a website on platforms like AWS, Heroku, Vercel, or GitHub Pages.",
        "what is cloud computing": "Cloud computing allows users to store and access data over the internet instead of local storage.",
        "what is cybersecurity": "Cybersecurity refers to protecting systems and networks from digital attacks.",
        "who is the president of the usa": "As of 2025, the President of the United States is [update required].",
        "what is the capital of india": "The capital of India is New Delhi.",
        "who invented electricity": "Electricity wasn't invented, but Benjamin Franklin conducted famous experiments with it.",
        "who discovered gravity": "Sir Isaac Newton is credited with discovering the law of gravity.",
        "how to write an essay": "Start with an introduction, develop body paragraphs, and end with a strong conclusion.",
        "best way to study for exams": "Create a study schedule, use flashcards, and take breaks to improve retention.",
        "how to improve english": "Read books, watch English movies, and practice speaking daily.",
        "what is machine learning": "Machine learning is a field of AI that allows computers to learn from data and improve without being explicitly programmed.",
        "how to learn coding": "Start with Python or JavaScript, practice daily, and build projects.",
        "how to lose weight": "Maintain a healthy diet, exercise regularly, and stay hydrated.",
        "how to reduce stress": "Practice meditation, get enough sleep, and engage in hobbies.",
        "what are the symptoms of covid-19": "Common symptoms include fever, cough, and difficulty breathing.",
        "how to get better sleep": "Avoid screens before bedtime, stick to a sleep schedule, and relax before sleeping.",
        "how to save money": "Create a budget, cut unnecessary expenses, and invest wisely.",
        "best investment options": "Stocks, mutual funds, real estate, and cryptocurrency are popular investment options.",
        "how to start a business": "Identify a profitable idea, create a business plan, and secure funding.",
        "best places to visit in india": "Taj Mahal, Goa, Kerala, Jaipur, and Manali are top tourist spots.",
        "how to get a passport": "You can apply for a passport online through your country's official passport website.",
        "what is the longest river in the world": "The Nile River is the longest in the world.",
        "who is the most famous actor": "Actors like Leonardo DiCaprio, Shah Rukh Khan, and Robert Downey Jr. are among the most famous.",
        "when is the next fifa world cup": "The next FIFA World Cup will be held in 2026 in the USA, Canada, and Mexico.",
        "who is the best football player": "Players like Lionel Messi and Cristiano Ronaldo are often considered the best.",
        "how to be happy": "Focus on gratitude, build strong relationships, and do things you enjoy.",
        "how to wake up early": "Sleep early, use an alarm, and avoid caffeine before bedtime.",
        "best morning routine": "Start with exercise, have a healthy breakfast, and plan your day.",
        "how to be confident": "Practice self-affirmation, improve your skills, and maintain good posture.",
        "tell me a joke": "Why don't programmers like nature? It has too many bugs!",
        "what is the meaning of life": "The meaning of life is to find purpose and enjoy the journey!",
    }

    return responses.get(user_message, "I'm not sure how to respond to that.")

@csrf_exempt
def send_message(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").strip().lower()

            if not user_message:
                return JsonResponse({"error": "Message cannot be empty"}, status=400)

            bot_reply = chatbot_response(user_message)

            return JsonResponse({"bot_reply": bot_reply})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
