# Udacity Agentic AI Nanodegree Portfolio

This repository is the main portfolio hub for the work completed by
**Jasdeep Sidhu** as part of the **Udacity Agentic AI Nanodegree**.

The nanodegree projects demonstrate practical agentic AI patterns including
multi-agent orchestration, retrieval-augmented generation, tool use,
structured outputs, evaluation loops, workflow routing, and domain-specific
automation. Each project is maintained in its own repository and is linked
below with setup guidance, project significance, and the major concepts
demonstrated.

## Author

**Jasdeep Sidhu**

- GitHub: [JasdeepSidhu13](https://github.com/JasdeepSidhu13)
- LinkedIn: [linkedin.com/in/jssidhu9](https://www.linkedin.com/in/jssidhu9/)

All four projects listed here were completed by Jasdeep Sidhu as part of the
Udacity Agentic AI Nanodegree coursework and portfolio.

## Sample Resume

A polished, print-ready sample resume for an **Agentic AI Engineer** role is
available here: [`agentic-ai-engineer-resume.html`](agentic-ai-engineer-resume.html).

## Certification

This portfolio is backed by a verified Udacity certificate confirming completion
of the **Agentic AI** Nanodegree program.

- **Awarded to:** Jasdeep Sidhu
- **Program:** Agentic AI Nanodegree
- **Date:** June 21, 2026
- **Certificate (PDF):** [`certificate-agentic-ai-nanodegree.pdf`](certificate-agentic-ai-nanodegree.pdf)
- **Verify online:** [udacity.com/certificate/e/568cae2a-eaa8-11f0-846f-27f0063adf9e](https://www.udacity.com/certificate/e/568cae2a-eaa8-11f0-846f-27f0063adf9e)

## Project Index

| # | Project | Repository | Primary Focus |
|---|---------|------------|---------------|
| 1 | AgentsVille Trip Planner | [AgentsVille-Trip-Planner](https://github.com/JasdeepSidhu13/AgentsVille-Trip-Planner) | Multi-agent travel planning, tool use, evaluation, ReAct |
| 2 | Agentic Workflow | [AgenticWorkFlow](https://github.com/JasdeepSidhu13/AgenticWorkFlow) | Reusable agent library, routing, evaluation, project-management workflow |
| 3 | UdaPlay | [Udaplay](https://github.com/JasdeepSidhu13/Udaplay) | Offline RAG, vector search, web search, game research agent |
| 4 | Multi-Agent System | [Multi-Agent-System](https://github.com/JasdeepSidhu13/Multi-Agent-System) | Business process automation with specialist agents and shared state |

The full source code for each project is also included directly in this
repository, in a same-named subdirectory:

| Project | Local Directory |
|---------|-----------------|
| AgentsVille Trip Planner | [`AgentsVille-Trip-Planner/`](AgentsVille-Trip-Planner) |
| Agentic Workflow | [`AgenticWorkFlow/`](AgenticWorkFlow) |
| UdaPlay | [`Udaplay/`](Udaplay) |
| Multi-Agent System | [`Multi-Agent-System/`](Multi-Agent-System) |

These directories are snapshots vendored from the linked source repositories,
so you can browse all four projects without leaving this repository.

## Why This Portfolio Matters

The projects in this portfolio move beyond single-prompt LLM demos. They show
how agentic systems can be designed, evaluated, and applied to realistic
workflows:

- **Planning and reasoning:** agents break user requests into steps and reason
  through constraints before producing final answers.
- **Tool use:** agents call deterministic tools for calculations, database
  lookups, retrieval, web search, and workflow actions.
- **Retrieval-augmented generation:** projects combine local knowledge bases
  with LLM responses to reduce hallucination and improve relevance.
- **Structured outputs:** Pydantic models and explicit schemas are used to make
  agent responses easier to validate and consume programmatically.
- **Evaluation loops:** worker outputs are checked against quality criteria and
  revised when they do not meet requirements.
- **Multi-agent collaboration:** specialist agents handle focused tasks while
  orchestrators coordinate the end-to-end process.
- **Realistic domain workflows:** the portfolio covers travel planning, product
  management, video game research, and business order fulfillment.

## 1. AgentsVille Trip Planner

**Repository:** [github.com/JasdeepSidhu13/AgentsVille-Trip-Planner](https://github.com/JasdeepSidhu13/AgentsVille-Trip-Planner)

### Summary

AgentsVille Trip Planner is a multi-agent travel assistant that creates and
revises personalized vacation itineraries for the fictional city of
AgentsVille. The system plans around traveler interests, budgets, dates,
weather, and available activities.

### Key Work Completed

- Built an itinerary-planning agent using role-based prompting and
  chain-of-thought style planning.
- Used structured Pydantic models for vacation inputs and travel-plan outputs.
- Added mocked weather and activity APIs so the agent can reason over external
  constraints without relying on live travel services.
- Implemented deterministic and LLM-as-judge evaluations for dates, budget,
  cost accuracy, activity validity, interest matching, weather compatibility,
  and traveler feedback.
- Built a ReAct-style revision agent that uses tools to revise the itinerary
  until all checks pass.
- Included optional trip narration to turn the final plan into a user-friendly
  travel summary.

### Significance

This project demonstrates how an agent can produce useful plans while staying
grounded in structured data and measurable constraints. It highlights the
importance of validating LLM output, using tools for reliable operations, and
closing the loop between generation, feedback, and evaluation.

### Main Concepts Demonstrated

- Multi-agent planning
- Role-based prompting
- Chain-of-thought planning structure
- ReAct reasoning and tool use
- Structured JSON output
- Pydantic validation
- LLM-as-judge evaluation
- Feedback-driven itinerary revision

### How to Explore

```bash
git clone https://github.com/JasdeepSidhu13/AgentsVille-Trip-Planner.git
cd AgentsVille-Trip-Planner
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install json-repair numexpr openai pandas pydantic python-dotenv jupyter ipykernel
```

Create a `.env` file with an OpenAI-compatible API key:

```env
OPENAI_API_KEY=your_api_key_here
```

Then run the notebook:

```bash
jupyter notebook project_starter.ipynb
```

Run the cells from top to bottom so the itinerary agent, evaluator functions,
revision tools, and final narration execute in order.

## 2. Agentic Workflow

**Repository:** [github.com/JasdeepSidhu13/AgenticWorkFlow](https://github.com/JasdeepSidhu13/AgenticWorkFlow)

### Summary

Agentic Workflow builds a reusable agent library and then composes those agents
into a project-management workflow. The final workflow reads a product
specification and generates structured product-management artifacts such as
user stories, product features, and engineering tasks.

### Key Work Completed

- Implemented a library of reusable agent patterns:
  - direct prompt agent
  - augmented prompt agent
  - knowledge-augmented prompt agent
  - RAG knowledge prompt agent
  - evaluation agent
  - routing agent
  - action-planning agent
- Built a two-phase project structure:
  - Phase 1 focuses on individual reusable agent classes.
  - Phase 2 composes those agents into an end-to-end workflow.
- Created role-based agents for Product Manager, Program Manager, and
  Development Engineer responsibilities.
- Used routing to send workflow steps to the most relevant specialist agent.
- Used evaluation loops to check and refine generated project artifacts.

### Significance

This project shows how agentic systems can be assembled from reusable building
blocks. Instead of writing one large prompt, the workflow separates planning,
routing, generation, retrieval, and evaluation into explicit components. This
is a practical foundation for larger business workflows where outputs must be
structured, role-specific, and quality-controlled.

### Main Concepts Demonstrated

- Agent abstraction design
- Prompt augmentation
- Knowledge-grounded agents
- Retrieval-augmented generation
- Embedding-based routing
- Action planning
- Output evaluation and refinement
- Product-management workflow automation

### How to Explore

```bash
git clone https://github.com/JasdeepSidhu13/AgenticWorkFlow.git
cd AgenticWorkFlow
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Run the Phase 1 agent examples:

```bash
cd "starter copy/phase_1"
python direct_prompt_agent.py
python augmented_prompt_agent.py
python knowledge_augmented_prompt_agent.py
python rag_knowledge_prompt_agent.py
python evaluation_agent.py
python routing_agent.py
python action_planning_agent.py
```

Run the Phase 2 workflow:

```bash
cd "../phase_2"
python agentic_workflow.py
```

The workflow reads the Email Router product specification and produces a final
project plan containing user stories, product features, and engineering tasks.

## 3. UdaPlay

**Repository:** [github.com/JasdeepSidhu13/Udaplay](https://github.com/JasdeepSidhu13/Udaplay)

### Summary

UdaPlay is an AI-powered video game research agent. It combines local game data
with retrieval-augmented generation and web search so the agent can answer
questions about video games using both internal knowledge and external
information.

### Key Work Completed

- Built an offline RAG workflow with ChromaDB.
- Processed and indexed local video game JSON data.
- Created a vector database collection with embedding support.
- Implemented retrieval over game metadata such as title, platform, genre,
  publisher, description, and release year.
- Designed an AI agent that can use local retrieval, evaluate retrieval quality,
  and search the web when more information is needed.
- Added support for conversation state and structured outputs.

### Significance

This project demonstrates how agents can combine local knowledge with external
search tools. It is especially important because many useful AI systems need to
answer questions from private or domain-specific data while still being able to
fall back to the web for fresh or missing information.

### Main Concepts Demonstrated

- Offline retrieval-augmented generation
- ChromaDB vector database setup
- Embeddings and semantic search
- Tool-using research agent
- Retrieval quality evaluation
- Web search augmentation
- Conversation state management
- Structured agent responses

### How to Explore

```bash
git clone https://github.com/JasdeepSidhu13/Udaplay.git
cd Udaplay
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

Install the dependencies required by the notebooks, including ChromaDB, OpenAI,
Tavily, and python-dotenv.

Create a `.env` file:

```env
OPENAI_API_KEY="YOUR_KEY"
CHROMA_OPENAI_API_KEY="YOUR_KEY"
TAVILY_API_KEY="YOUR_KEY"
```

Follow the notebooks in order:

1. `starter/Udaplay_01_starter_project.ipynb` - build the local vector database.
2. `starter/Udaplay_02_starter_project.ipynb` - build and test the research agent.

Example questions to test:

- "When was Pokemon Gold and Silver released?"
- "Which one was the first 3D platformer Mario game?"
- "Was Mortal Kombat X released for PlayStation 5?"

## 4. Multi-Agent System

**Repository:** [github.com/JasdeepSidhu13/Multi-Agent-System](https://github.com/JasdeepSidhu13/Multi-Agent-System)

### Summary

Multi-Agent System is a business process automation project for Beaver's Choice
Paper Company. The system processes customer quote and order requests, checks
inventory, reviews historical quote context, decides whether orders can be
fulfilled, records supplier and sales transactions, and produces
customer-facing responses.

### Key Work Completed

- Built a Python-based multi-agent system using Pydantic AI.
- Created an orchestration agent that coordinates specialist worker agents.
- Implemented specialist agents for data extraction, inventory management,
  quoting, and ordering.
- Used SQLite and SQLAlchemy for inventory, quote, transaction, and request
  state.
- Used shared state and structured Pydantic schemas to coordinate information
  between agents and tools.
- Added deterministic business tools for inventory checks, cash balance,
  historical quote search, delivery estimates, and transaction recording.
- Produced sanitized customer-facing responses that hide internal
  implementation details.

### Significance

This project is the most business-process-oriented system in the portfolio. It
shows how agentic AI can support operational workflows where agents must reason
over structured data, call tools, update state, follow business policies, and
produce safe customer communications.

### Main Concepts Demonstrated

- Multi-agent orchestration
- Specialist worker agents
- Shared state between agents
- Pydantic structured outputs
- SQLite-backed business workflow
- Tool-based inventory and transaction operations
- Delivery and fulfillment reasoning
- Customer response sanitization

### How to Explore

```bash
git clone https://github.com/JasdeepSidhu13/Multi-Agent-System.git
cd Multi-Agent-System
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Copy the environment template and add your key:

```bash
cp example.env .env
```

Update `.env`:

```env
UDACITY_OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
```

Run the system from the repository root:

```bash
python project_solution.py
```

The script initializes the database, loads sample quote requests, runs the
multi-agent orchestration flow, writes response logs, and produces aggregate
test results.

## Portfolio-Wide Agentic AI Skills Demonstrated

Across the four projects, this portfolio demonstrates the following technical
skills:

### Agent Design

- Creating specialized agents with clear roles and responsibilities.
- Designing orchestrators that coordinate worker agents.
- Building reusable agent classes that can be composed into larger workflows.

### Prompting and Reasoning

- Role-based prompting.
- Prompt augmentation with task-specific knowledge.
- Chain-of-thought style planning structures.
- ReAct loops for iterative reasoning and tool use.

### Tools and External Systems

- Tool calls for math, retrieval, evaluation, database access, and web search.
- Mock APIs for deterministic development and testing.
- SQLite and SQLAlchemy integration for persistent business state.
- ChromaDB integration for semantic retrieval.

### Retrieval and Knowledge Grounding

- Offline RAG over local JSON data.
- Embedding generation and cosine similarity search.
- Knowledge-augmented responses from product and domain specifications.
- Hybrid local retrieval and web-search workflows.

### Evaluation and Reliability

- Deterministic validation checks.
- LLM-as-judge evaluations.
- Evaluation agents that critique and refine worker outputs.
- Structured outputs with Pydantic models.
- Guardrails for hallucination reduction and customer-safe responses.

### Applied AI Workflows

- Travel itinerary planning.
- Product-management artifact generation.
- Video game research.
- Inventory, quoting, fulfillment, and order-processing automation.

## Suggested Review Order

For someone reviewing this portfolio, the following order gives a strong view
of the progression from foundational patterns to complete systems:

1. **Agentic Workflow** - start with the reusable agent patterns.
2. **UdaPlay** - review retrieval, vector search, and web-augmented research.
3. **AgentsVille Trip Planner** - examine planning, tool use, and evaluation
   loops.
4. **Multi-Agent System** - finish with the larger business workflow that
   combines orchestration, structured data, tools, and state updates.

## General Setup Notes

Each project has its own repository, dependencies, and setup instructions.
When running any project locally:

1. Clone the specific project repository.
2. Create and activate a Python virtual environment.
3. Install that project's dependencies.
4. Create the required `.env` file from the project's README or example file.
5. Run notebooks or scripts from the project root unless the project README says
   otherwise.
6. Never commit real API keys or generated secret files.

## Repository Purpose

This repository serves as a central entry point for the Udacity Agentic AI
Nanodegree work. In addition to linking to each source repository and explaining
the purpose, significance, and instructions for exploring each completed project,
it now also includes a full vendored snapshot of all four projects in same-named
subdirectories so the entire portfolio can be browsed in one place.
