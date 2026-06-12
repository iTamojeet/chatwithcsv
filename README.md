Link: https://ai-csvreader.streamlit.app/

---

# 📈 Chat with CSV — AI-Powered Data Analysis Assistant

> **An intelligent conversational agent that lets you ask plain English questions about any CSV file — powered by LangChain, Groq, and Llama 3.1 70B.**

**Chat with CSV** removes the barrier between you and your data. Upload any CSV file, type a question in plain English, and get instant data-driven answers — no SQL, no Pandas, no formulas required. Built with **LangChain + Groq + Llama 3.1 + Streamlit**, it turns your spreadsheet into a smart, conversational data analyst.

📊 Works with any CSV file  
🤖 Powered by Llama 3.1 70B via Groq  
⚡ Ultra-fast inference with Groq's LPU engine  
🌐 Live on Streamlit Cloud  

---

# ✨ Features

## 🧠 AI-Powered CSV Understanding

- Upload any CSV and ask questions in natural language
- LangChain's CSV Agent reads and reasons over your data automatically
- Powered by Llama 3.1 70B (Versatile) via the Groq API
- Handles complex multi-step data reasoning behind the scenes

## ⚡ Ultra-Fast Groq Inference

- Groq's LPU (Language Processing Unit) delivers near-instant responses
- No waiting — even large CSV files get fast answers
- Far lower latency than traditional cloud GPU inference

## 🤖 LangChain CSV Agent

- Uses `create_csv_agent` from LangChain Experimental for robust data reasoning
- Agent autonomously decides how to query and interpret the CSV
- Handles parsing errors gracefully with `handle_parsing_errors=True`
- `verbose=True` mode allows developers to trace the agent's reasoning steps

## 📂 Simple File Upload Interface

- Drag-and-drop or browse CSV file upload via Streamlit
- No pre-configuration needed — works with any CSV schema
- Question and answer flow is entirely conversational

## 🔐 Secure API Key Handling

- Groq API key loaded from `.env` using `python-dotenv`
- Key never hardcoded or exposed in source code
- `.env` excluded from version control via `.gitignore`

## 🌍 Live Deployment

- Fully deployed and accessible at [ai-csvreader.streamlit.app](https://ai-csvreader.streamlit.app/)
- No local setup required for end users

---

# 🧠 How It Works

## Pipeline Flow

```
User uploads a CSV file
        ↓
LangChain CSV Agent is initialised with the file
        ↓
User types a natural language question
        ↓
Agent reasons over the CSV data using Llama 3.1 70B (Groq)
        ↓
Answer is displayed in the Streamlit UI
```

### Step-by-Step Process

1. User uploads a CSV file via the Streamlit file uploader.
2. A LangChain CSV Agent is created using the uploaded file and the Groq-backed Llama 3.1 70B model.
3. User types any question about their data in plain English.
4. The agent autonomously analyses the CSV, runs its reasoning chain, and formulates an answer.
5. The result is displayed in the Streamlit interface with a live spinner during processing.

---

# 🏗️ Architecture

## Cloud-Powered AI Stack

```
Frontend        → Streamlit
AI Model        → Llama 3.1 70B Versatile (via Groq)
LLM Framework   → LangChain + LangChain Experimental
CSV Reasoning   → LangChain CSV Agent
Config          → python-dotenv
Deployment      → Streamlit Cloud
```

### Why this architecture is powerful:

✅ Groq delivers the fastest LLM inference available today  
✅ LangChain's CSV Agent handles all data reasoning automatically  
✅ No database or backend setup — just upload and ask  
✅ Llama 3.1 70B provides enterprise-grade comprehension  
✅ Streamlit makes the whole thing deployable in minutes  

---

# 🏗️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core development |
| Streamlit | UI framework & deployment |
| LangChain | LLM orchestration framework |
| LangChain Experimental | CSV Agent toolkit |
| langchain-groq | Groq API integration for LangChain |
| Llama 3.1 70B Versatile | Data reasoning language model |
| python-dotenv | Secure API key management |

---

# 📂 Project Structure

```
chatwithcsv/
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
├── pyvenv.cfg
└── README.md
```

---

# ⚡ Installation & Setup

## 1️⃣ Clone Repository

```
git clone https://github.com/iTamojeet/chatwithcsv.git
cd chatwithcsv
```

---

## 2️⃣ Create Virtual Environment (Recommended)

```
python -m venv venv
```

### Activate Environment

**Windows**
```
venv\Scripts\activate
```

**Mac/Linux**
```
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

Or manually:

```
pip install streamlit langchain langchain-experimental langchain-groq python-dotenv
```

---

## 4️⃣ Set Up Your Groq API Key

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key at:

👉 https://console.groq.com

---

## 5️⃣ Run the Application

```
streamlit run main.py
```

Open in browser:

```
http://localhost:8501
```

---

# 💬 Example Queries

Try asking after uploading your CSV:

- What is the total revenue for Q3?
- Which product had the highest sales last month?
- Show me the average salary by department
- How many rows have missing values?
- What is the correlation between price and quantity sold?
- List the top 10 customers by order value

---

# 🎯 Use Cases

- Business data analysis without writing code
- Sales and revenue reporting
- HR and workforce analytics
- Financial data exploration
- Academic research data querying
- Quick exploratory data analysis (EDA)
- Data journalism and reporting

---

# 🔐 Security

- Groq API key stored in `.env` — never committed to version control
- `.gitignore` prevents accidental secret exposure
- No user data is stored or persisted after the session ends
- All CSV processing happens within the active Streamlit session only

---

# 🚀 Future Improvements

- Multi-CSV upload and cross-file querying
- Automatic chart and visualisation generation
- Export answers as PDF or Excel reports
- Conversational memory for follow-up questions
- Support for Excel (`.xlsx`) and JSON files
- Database connector (MySQL, PostgreSQL)
- Authentication and user session management
- Download cleaned/filtered data as new CSV

---

# 👨‍💻 Developer

**Tamojeet**  
AI & Data Enthusiast • Python Developer  
🔗 HuggingFace: https://huggingface.co/iTamojeet  
🌐 Live App: https://ai-csvreader.streamlit.app/

---

# ⭐ Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request