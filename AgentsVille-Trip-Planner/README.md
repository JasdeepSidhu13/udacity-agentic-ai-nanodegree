# AgentsVille Trip Planner

A **Multi-Agent Travel Assistant System** that plans personalized vacations to the fictional city of AgentsVille. The project demonstrates advanced LLM reasoning techniques—role-based prompting, chain-of-thought (CoT) planning, ReAct tool use, and automated evaluation with feedback loops—built as part of the Udacity Agentic AI curriculum.

**Repository:** [github.com/JasdeepSidhu13/AgentsVille-Trip-Planner](https://github.com/JasdeepSidhu13/AgentsVille-Trip-Planner)

---

## Setup

### Prerequisites

- **Python 3.10+** (3.11 recommended)
- An **OpenAI API key** (or access to the Udacity Vocareum OpenAI proxy)
- **Jupyter Notebook** or **JupyterLab** (or VS Code with the Jupyter extension)

### 1. Clone the repository

```bash
git clone https://github.com/JasdeepSidhu13/AgentsVille-Trip-Planner.git
cd AgentsVille-Trip-Planner
```

### 2. Create and activate a virtual environment

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Confirm the venv is active—your shell prompt should show `(.venv)` and `which python` should point inside the project directory.

### 3. Install dependencies

The project runs from a Jupyter notebook. Install the required packages:

```bash
pip install --upgrade pip
pip install json-repair==0.47.1 numexpr==2.11.0 openai==1.74.0 pandas==2.3.0 pydantic==2.11.7 python-dotenv==1.1.0 jupyter ipykernel
```

Or save them to a `requirements.txt` and install in one step:

```txt
json-repair==0.47.1
numexpr==2.11.0
openai==1.74.0
pandas==2.3.0
pydantic==2.11.7
python-dotenv==1.1.0
jupyter
ipykernel
```

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

The notebook loads this automatically via `python-dotenv`.

**Using the Udacity Vocareum endpoint** (course workspace):

```python
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
)
```

**Using the standard OpenAI API**, omit `base_url`:

```python
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

### 5. Register the Jupyter kernel (optional but recommended)

```bash
python -m ipykernel install --user --name agentsville --display-name "AgentsVille Trip Planner"
```

### 6. Run the project

```bash
jupyter notebook project_starter.ipynb
```

Open `project_starter.ipynb` and run cells **top to bottom**. Each section builds on the previous one; skipping cells will cause downstream errors.

### Project files

| File | Purpose |
|------|---------|
| `project_starter.ipynb` | Main notebook—agents, tools, evaluators, and demo workflow |
| `project_lib.py` | Shared utilities: `ChatAgent`, mocked weather/activity APIs, narration helper |

---

## How the Agent System Works

The system is a **two-stage multi-agent pipeline** that turns structured vacation preferences into a validated, revised travel itinerary. External data (weather and activities) is **simulated** via mocked APIs in `project_lib.py`—no real travel or weather services are called.

### High-level architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         VacationInfo (input)                            │
│   travelers, destination, dates, budget, interests                      │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Stage 1: ItineraryAgent (Chain-of-Thought, single LLM call)            │
│  • Role-based travel planner prompt                                     │
│  • Weather + activity calendar injected into context                    │
│  • Outputs TravelPlan JSON                                              │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Evaluation layer (deterministic + LLM-as-judge)                        │
│  • Dates, budget, cost accuracy, hallucination checks                   │
│  • Interest matching, weather compatibility                             │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Stage 2: ItineraryRevisionAgent (ReAct loop with tools)                 │
│  • Incorporates traveler feedback (≥ 2 activities/day)                  │
│  • THOUGHT → ACTION → OBSERVATION cycles                                │
│  • Re-runs evals until all constraints pass                             │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  Final TravelPlan + optional narrated trip summary (TTS)                │
└─────────────────────────────────────────────────────────────────────────┘
```

---

### Data models (Pydantic)

All structured data is validated with **Pydantic v2** models to reduce hallucinated fields and enforce type safety.

#### Input: `VacationInfo`

Captures everything needed to plan a trip:

- **`Traveler`**: `name`, `age`, `interests` (from a fixed enum: art, cooking, comedy, tennis, technology, etc.)
- **`VacationInfo`**: list of travelers, `destination`, `date_of_arrival`, `date_of_departure`, `budget`

Example default trip in the notebook: two travelers (Yuri and Hiro), AgentsVille, June 10–12, 2025, budget of 130 (fictional currency units).

#### Output: `TravelPlan`

The agents produce a nested itinerary:

- **`Weather`**: temperature, unit, condition per day
- **`Activity`**: full event record (id, name, times, location, description, price, related interests)
- **`ActivityRecommendation`**: an activity plus human-readable reasons
- **`ItineraryDay`**: date, weather, list of recommendations
- **`TravelPlan`**: city, start/end dates, `total_cost`, `itinerary_days`

---

### Simulated external APIs

`project_lib.py` provides mocked data sources so the agents can reason over realistic constraints without live API keys:

| Function | Description |
|----------|-------------|
| `call_weather_api_mocked(date, city)` | Returns forecast for AgentsVille (2025-06-10 through 2025-06-15) |
| `call_activities_api_mocked(date, city, activity_ids)` | Returns scheduled events for a given date |
| `call_activity_by_id_api_mocked(activity_id)` | Looks up a single event by ID |

**Weather highlights for the demo window:**

- June 10–11: clear / partly cloudy (good for outdoor events)
- June 12: **thunderstorm** (outdoor-only activities should be avoided)
- June 13–14: **rainy**
- June 15: sunny

The activity calendar includes ~4 events per day across interests like technology, tennis, cooking, art, music, hiking, and comedy.

---

### Stage 1: ItineraryAgent

**Pattern:** Role-based prompting + **Chain-of-Thought (CoT)** in a **single LLM call**.

The `ItineraryAgent` extends `ChatAgent` from `project_lib.py`. Its system prompt defines:

1. **Role** — specialized itinerary planning agent
2. **Task (CoT steps)** — think step-by-step:
   - Check daily weather and flag poor conditions (rain, thunderstorm)
   - Remove outdoor-only activities on bad-weather days
   - Select activities matching traveler interests and ages
   - Keep total cost within budget
3. **Output format** — two sections: `ANALYSIS` (reasoning per day) and `FINAL OUTPUT` (JSON matching `TravelPlan` schema)
4. **Context** — full `WEATHER_FORECAST` and `ACTIVITY_CALENDAR` embedded in the prompt so the model does not invent events

**Execution flow:**

```python
itinerary_agent = ItineraryAgent(client=client, model=MODEL)
travel_plan_1 = itinerary_agent.get_itinerary(vacation_info)
```

The agent sends `VacationInfo` as JSON, receives a CoT response, extracts the JSON block, and validates it into a `TravelPlan` object.

**Default model:** `gpt-4.1-mini` — a balance of speed, cost, and reasoning quality.

---

### Evaluation layer

Before and after revision, the itinerary is scored by a suite of **evaluation functions**. Failures raise `AgentError`; results are aggregated by `get_eval_results()`.

| Evaluator | Type | What it checks |
|-----------|------|----------------|
| `eval_start_end_dates_match` | Deterministic | Arrival/departure dates match the plan |
| `eval_total_cost_is_accurate` | Deterministic | Stated total equals sum of activity prices |
| `eval_total_cost_is_within_budget` | Deterministic | Total cost ≤ vacation budget |
| `eval_itinerary_events_match_actual_events` | Deterministic | Every activity ID exists in the mock calendar and fields match exactly (anti-hallucination) |
| `eval_itinerary_satisfies_interests` | Deterministic | Each traveler has at least one activity matching their interests |
| `eval_activities_and_weather_are_compatible` | **LLM-as-judge** | No outdoor-only activities scheduled during inclement weather |
| `eval_traveler_feedback_is_incorporated` | **LLM-as-judge** | Revised plan reflects user feedback (added in revision stage) |

The weather compatibility check uses a dedicated `ChatAgent` with a structured prompt returning `IS_COMPATIBLE` or `IS_INCOMPATIBLE`, parsing activity descriptions for indoor fallbacks (e.g., “moves indoors if rain”).

---

### Agent tools (used by the revision agent)

Four tools are exposed to the ReAct agent. Tool docstrings are auto-injected into the revision agent’s system prompt via `get_tool_descriptions_string()`.

| Tool | Purpose |
|------|---------|
| `calculator_tool(expression)` | Evaluates math with `numexpr` — LLMs often miscalculate sums |
| `get_activities_by_date_tool(date, city)` | Fetches available activities for a specific day |
| `run_evals_tool(travel_plan)` | Runs all evaluators; returns `{success, failures}` |
| `final_answer_tool(final_output)` | Signals completion and returns the validated `TravelPlan` |

---

### Stage 2: ItineraryRevisionAgent

**Pattern:** **ReAct** (Reasoning + Acting) — iterative **THOUGHT → ACTION → OBSERVATION** loops.

After the initial plan is generated, travelers provide feedback:

```python
TRAVELER_FEEDBACK = "I want to have at least two activities per day."
```

The `ItineraryRevisionAgent` refines `travel_plan_1` into `travel_plan_2` using tools and strict guardrails:

**Revision guidelines (system prompt):**

- At least **2 activities per day**
- Activities must be **weather-appropriate**
- No outdoor activities during thunderstorm, heavy rain, or gusty wind
- Honor traveler feedback
- **Must** call `run_evals_tool` and receive `"success": true` before calling `final_answer_tool`

**ReAct loop (per step):**

1. **THOUGHT** — LLM reasons about the next action
2. **ACTION** — LLM emits a JSON tool call: `{"tool_name": "...", "arguments": {...}}`
3. **OBSERVATION** — Python executes the tool and appends the result to chat history

The loop runs up to `max_steps` (default 15). JSON parsing uses `json-repair` to tolerate minor formatting issues from the model.

**Termination:** When the agent calls `final_answer_tool`, the arguments are validated as a `TravelPlan` and returned. If the step limit is exceeded, a `RuntimeError` is raised—usually a sign the agent is stuck and the system prompt needs tuning.

```python
itinerary_revision_agent = ItineraryRevisionAgent()
travel_plan_2 = itinerary_revision_agent.run_react_cycle(
    original_travel_plan=travel_plan_1,
    max_steps=15,
    model=MODEL,
    client=client,
)
```

Because LLM responses are **stochastic**, re-running the revision cell may produce different (but still valid) itineraries.

---

### Shared infrastructure: `ChatAgent`

Defined in `project_lib.py`, `ChatAgent` is the base class for both agents:

- Manages OpenAI chat message history
- Formats and prints boxed system/user/assistant messages for debugging
- Wraps `client.chat.completions.create()` via `do_chat_completion()`
- Supports optional structured output via `response_format` (Pydantic parse API)

---

### Bonus: Trip narration

After a successful revision, `narrate_my_trip()` generates a markdown narrative of the trip and optionally streams text-to-speech audio (`gpt-4o-mini-tts`, voice `coral`) saved to `/tmp/my_trip_narration.mp3`.

---

## End-to-end workflow (notebook order)

1. **Setup** — install packages, configure OpenAI client, select model
2. **Define vacation details** — build and validate `VacationInfo`
3. **Review mock data** — inspect weather forecast and activity calendar
4. **Generate initial itinerary** — run `ItineraryAgent.get_itinerary()`
5. **Evaluate** — run individual and combined eval functions on `travel_plan_1`
6. **Define tools** — calculator, activities lookup, eval runner, final answer
7. **Revise with ReAct** — run `ItineraryRevisionAgent.run_react_cycle()` with traveler feedback
8. **Re-evaluate** — confirm all checks pass including feedback incorporation
9. **Narrate** — optional spoken trip summary

---

## LLM techniques demonstrated

| Technique | Where used |
|-----------|------------|
| **Role-based prompting** | ItineraryAgent and ItineraryRevisionAgent system prompts |
| **Chain-of-thought** | ItineraryAgent plans day-by-day in ANALYSIS before JSON output |
| **ReAct** | ItineraryRevisionAgent THOUGHT/ACTION/OBSERVATION cycles |
| **Tool use** | Calculator, API lookup, eval runner, final answer |
| **Structured output** | Pydantic models for input/output validation |
| **LLM-as-judge** | Weather compatibility and traveler feedback evaluators |
| **Feedback loops** | `run_evals_tool` inside the ReAct loop until success |

---

## Troubleshooting

| Issue | Likely cause | Fix |
|-------|--------------|-----|
| `OPENAI_API_KEY` not found | Missing `.env` | Create `.env` with your key |
| Import errors for `project_lib` | Wrong working directory | Run notebook from project root |
| Empty activity list | Date outside 2025-06-10–15 | Use dates within mock data range |
| ReAct loop timeout / max steps | Agent stuck revising | Inspect THOUGHT/ACTION traces; tighten system prompt |
| Eval failures on weather | Outdoor event on storm day | Let revision agent swap activities or adjust initial prompt |
| `json_repair` / validation errors | Malformed ACTION JSON | Re-run cell; consider stronger model for revision |

---

## Author

**Jasdeep Sidhu** — AI & Data Engineer  
- GitHub: [JasdeepSidhu13](https://github.com/JasdeepSidhu13)  
- LinkedIn: [linkedin.com/in/jssidhu9](https://www.linkedin.com/in/jssidhu9/)

---

## License

This project was developed as coursework for the Udacity Agentic AI program. Refer to the repository for license details.
