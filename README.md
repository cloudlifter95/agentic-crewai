# agentic-crewai
playground to try agenticai

``` bash
crewai-multi-agent-poc/
│── .github/
│   └── workflows/
│       └── crewai-ci.yml  # GitHub Actions workflow
│── app/
│   ├── __init__.py
│   ├── agents.py          # Agent definitions
│   ├── tasks.py           # Task definitions
│   ├── crew.py            # Crew and workflow setup
│   ├── main.py            # Entry point to run the crew
│── requirements.txt       # Python dependencies
│── Dockerfile             # Docker setup
│── docker-compose.yml     # Optional: Multi-container setup
│── .gitignore             # Ignore unnecessary files
│── README.md              # Project documentation
```


# commands (mostly to debug):
To:
- build docker image: `docker build -t crewaitest .`
- run docker image: `docker run -it crewaitest`
- override command with bash: `docker run -it crewaitest bash`
- run with docker compose: `docker compose run --service-ports crewai bash`  The --service-ports flag ensures that the ports exposed by your service (if any) are also mapped.