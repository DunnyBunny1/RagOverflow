# RagOverflow - AI-Powered Programming Assistant
A Retrieval-Augmented Generation (RAG) system to answer technical programming questions, using LLM-enhanced responses from online forums.

## High-Level Overview

- **Frontend**: Streamlit web UI to handle queries and display responses
- **Backend**: Flask API that processes queries and interacts with the vector database

## System Design 
- TODO: Insert draw.io diagram here 

## Demo 
- TODO: Insert demo here 

## Project Organization

```
ragoverflow/
├── backend/                 # Flask backend
│   ├── Dockerfile           # Backend container config
│   ├── requirements.txt     # Python dependencies for backend
│   ├── .env                 # Environment vars 
│   └── src/                 # Backend application code
│       └── <>.py   
├── frontend/                # Streamlit frontend
│   ├── Dockerfile           # Frontend container config
│   ├── requirements.txt     # Python dependencies for frontend
│   └── src/                 # Frontend app code
│       └── <>.py                
└── README.md       
└── LICENSE
└── CHANGELOG.md
├── docker-compose.yml       # Container orchestration



```

## Challenges Faced 

## Testing Overview 
- Testing backend API routes: the *Repeater* tool from the `Burp Suite` HTTP proxy  

## Getting Started

### Prereqs

- Docker and Docker Compose installed on your system
- Pinecone API key and environment (create an account at [pinecone.io](https://www.pinecone.io/))
- HuggingFace API token (create an account at [huggingface.co](https://huggingface.co/))

### Environment Variables
1. Navigate to the `backend` folder and rename `.env.template` to `.env` 
2. Replace the placeholder environment variable values with your own env variable values:
```
PINECONE_API_KEY=<your_pinecone_api_key>
PINECONE_IDX_NAME=<your_pinecone_index_name>
HUGGINGFACE_API_KEY=<your_huggingface_api_token>
```

### Running with Docker Compose

1. Start all containers:

```bash
docker-compose up 
```

2. Access the Streamlit frontend at http://localhost:8501 and the Flask backend at http://localhost:5000 

3. To stop all containers:

```bash
docker-compose down
```

### Development tips 

- TODO: Figure out how we want to do container logs and container config 
    - Also figure out how Flask's logger vs the `logging` module logger will interact 
- Frontend and backend code is mounted as volumes, so changes will be reflected without rebuilding containers
- If you update dependencies in requirements.txt, you'll need to rebuild the containers:

```bash
docker-compose up --build
```

- The backend container uses LangChain to interface with both the LLM and vector database
- The Streamlit UI is configured to communicate with the backend over the Docker network
- PineconeDB is a cloud service, so we don't run it locally as a container

- Logs can be accessed by looking at running containers in Docker Desktop, or via the command line like so: 
```bash
# View logs for all containers
docker-compose logs

# View logs for a specific container
docker-compose logs frontend
docker-compose logs backend
```

- To change the port mappings, edit the `ports` section in `docker-compose.yml`
- To change environment variables:
    - For the backend, simply edit the `backend/.env` file. 
    - For the frontend, create a `frontend/.env` file and follow the same process as with the backend, ensuring that they are copied into the frontend container's volume and
    set using a tool like `load_dotenv`

## Contributing

We welcome pull requests and new contributors! If you have an idea for improvement or find a bug, feel free to open an issue or submit a PR.

To contribute:
- Fork the repo and create your branch from `main`
- Follow the style and testing guidelines
- Document any new functionality
- Submit a PR with a clear description and reference any relevant issues

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.


