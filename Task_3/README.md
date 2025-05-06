# Vendor Payment Chatbot on (FastAPI)

This is a simple FastAPI-based chatbot that answers procurement-related questions using a predefined JSON knowledge base.

---

## Getting Started

### 1. Clone the Repository

```bash
   git clone https://github.com/your-repo/chatbot-fastapi.git
   cd chatbot-fastapi
```
### 2. Create a Virtual Environment 

```bash 
   python -m venv venv 
   source venv/bin/activate # in linux
```

### 3. Install Dependencies from requirements 

```bash
   pip install -r requirements.txt
```

### 4. Run the FASTAPI Chatbot
```bash
   uvicorn main:app --reload
```
Note: Run this in chatbot directory

## Testing the endpoint 
You can do a quick test of it using Curl:
```bash
    curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d '{"query":"give me payment terms on wonka ltd"}'
```
### Project Structure 
<pre><code>```bash project/ ├── main.py ├── knowledge_base.json ├── requirements.txt └── app/ ├── models/ │ └── query_model.py └── services/ └── query_handler.py ```</code></pre>
	

