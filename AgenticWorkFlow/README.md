# Setup

This repository contains an AI-powered agentic workflow for project management. The project is organized into two implementation phases:

- [Phase 1 README: Building Your Agent Library](starter%20copy/phase_1/README.md)
- [Phase 2 README: Implementing the Agentic Workflow](starter%20copy/phase_2/README.md)

The top-level README complements those two phase READMEs. Use this file for environment setup, repository orientation, and an end-to-end explanation of how the agents work together. Use the phase READMEs for the detailed phase-specific implementation checklist.

## 1. Create a Virtual Environment

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Upgrade `pip` after activating the environment:

```bash
python -m pip install --upgrade pip
```

## 2. Install Dependencies

Install the Python dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

The project currently depends on:

- `openai` for chat completion and embedding API calls
- `python-dotenv` for loading local environment variables
- `pandas` for working with chunk and embedding CSV data in the RAG agent
- `numpy` for vector operations and cosine similarity

## 3. Configure Environment Variables

Create a `.env` file with your OpenAI API key:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Recommended location:

- Put `.env` in the repository root when running scripts from the root.
- If you run scripts directly from a phase directory and your key is not found, copy the same `.env` file into that phase directory.

Do not commit `.env` or any real API keys to source control.

## 4. Run Phase 1 Agent Scripts

Phase 1 contains standalone scripts that exercise the reusable agent classes.

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

Each script demonstrates one agent pattern from the shared library in `workflow_agents/base_agents.py`.

## 5. Run the Phase 2 Workflow

Phase 2 composes the reusable agents into a project-management workflow.

```bash
cd "starter copy/phase_2"
python agentic_workflow.py
```

The workflow reads `Product-Spec-Email-Router.txt`, generates project-management artifacts, and prints a final Email Router project plan containing user stories, product features, and engineering tasks.

An example output file is included at:

```text
starter copy/phase_2/revised_agentic_workflow_output.txt
```

# Project Overview

## What This Project Builds

This project demonstrates how an agentic system can turn a product-management request into structured project artifacts. Instead of writing one fixed procedural script for every possible request, the system uses multiple specialized agents that can:

1. Interpret the user's workflow request.
2. Break the request into actionable steps.
3. Route each step to the most relevant role-based agent.
4. Generate structured outputs from product knowledge.
5. Evaluate and refine outputs against explicit quality criteria.

The Phase 2 example focuses on an Email Router product. Given a product specification, the workflow can produce:

- User stories from a Product Manager perspective
- Product features from a Program Manager perspective
- Engineering tasks from a Development Engineer perspective

## Repository Structure

```text
.
|-- README.md
|-- requirements.txt
`-- starter copy/
    |-- README.md
    |-- phase_1/
    |   |-- README.md
    |   |-- workflow_agents/
    |   |   |-- __init__.py
    |   |   `-- base_agents.py
    |   |-- direct_prompt_agent.py
    |   |-- augmented_prompt_agent.py
    |   |-- knowledge_augmented_prompt_agent.py
    |   |-- rag_knowledge_prompt_agent.py
    |   |-- evaluation_agent.py
    |   |-- routing_agent.py
    |   `-- action_planning_agent.py
    `-- phase_2/
        |-- README.md
        |-- Product-Spec-Email-Router.txt
        |-- agentic_workflow.py
        |-- revised_agentic_workflow_output.txt
        `-- workflow_agents/
            |-- __init__.py
            `-- base_agents.py
```

## Phase README Links

The project is intentionally split across two detailed phase READMEs:

1. [Phase 1: Building Your Agent Library](starter%20copy/phase_1/README.md)
   - Explains each reusable agent class.
   - Describes the standalone scripts used to verify each agent.
   - Covers direct prompting, persona prompting, knowledge augmentation, RAG, evaluation, routing, and action planning.

2. [Phase 2: Implementing an Agentic Workflow](starter%20copy/phase_2/README.md)
   - Explains how to compose the Phase 1 agents into a product-development workflow.
   - Describes the Email Router product specification.
   - Defines the Product Manager, Program Manager, and Development Engineer agents.
   - Shows how routing and evaluation are used to produce structured project artifacts.

# How the Agent System Works

## Agent Library

The core agent implementations live in:

```text
starter copy/phase_1/workflow_agents/base_agents.py
starter copy/phase_2/workflow_agents/base_agents.py
```

The main agent classes are:

### 1. DirectPromptAgent

The `DirectPromptAgent` sends the user's prompt directly to the language model and returns the text response. It does not add a persona, extra knowledge, routing logic, or evaluation loop.

Use this agent when you want the simplest possible LLM interaction.

### 2. AugmentedPromptAgent

The `AugmentedPromptAgent` adds a persona through a system prompt before sending the user's input to the model. The persona shapes the tone, role, and style of the response.

Example persona:

```text
You are a college professor.
```

Use this agent when the answer should come from a specific role or perspective.

### 3. KnowledgeAugmentedPromptAgent

The `KnowledgeAugmentedPromptAgent` combines a persona with explicit knowledge. Its system prompt instructs the model to answer from the provided knowledge rather than from general model knowledge.

In Phase 2, this pattern is used for the role-based project agents:

- Product Manager agent
- Program Manager agent
- Development Engineer agent

Each of these agents receives role-specific instructions and knowledge about how to produce its expected artifact.

### 4. RAGKnowledgePromptAgent

The `RAGKnowledgePromptAgent` demonstrates retrieval-augmented generation. It:

1. Splits a larger knowledge source into chunks.
2. Generates embeddings for each chunk.
3. Embeds the user's prompt.
4. Finds the most similar knowledge chunk by cosine similarity.
5. Answers using the retrieved chunk.

This agent is useful when the knowledge source is too large or too dynamic to place directly into a single prompt.

### 5. EvaluationAgent

The `EvaluationAgent` reviews another worker agent's output against explicit evaluation criteria. If the output does not meet the criteria, the evaluator asks for correction instructions and feeds those instructions back into the worker agent for another attempt.

The evaluation loop continues until either:

- The evaluator accepts the output, or
- The maximum number of interactions is reached.

The returned result includes:

- `final_response`
- `evaluation`
- `iterations`

This pattern helps enforce output format and quality requirements, such as requiring user stories to follow:

```text
As a [type of user], I want [an action or feature] so that [benefit/value].
```

### 6. RoutingAgent

The `RoutingAgent` chooses which specialized agent should handle a prompt. It:

1. Embeds the incoming prompt.
2. Embeds each candidate agent's description.
3. Computes cosine similarity between the prompt and each description.
4. Selects the best-matching agent.
5. Calls that agent's support function.

In Phase 2, the router chooses among:

- Product Manager support for user stories
- Program Manager support for product features
- Development Engineer support for engineering tasks

### 7. ActionPlanningAgent

The `ActionPlanningAgent` converts a user's high-level workflow request into a list of steps. It uses its provided knowledge to identify which project-management actions are relevant.

In Phase 2, the workflow prompt is:

```text
What would the development tasks for this product be?
```

The action planning agent extracts the steps needed to satisfy that request, and those steps are then passed into the routing layer.

# Phase 2 End-to-End Workflow

The end-to-end workflow is implemented in:

```text
starter copy/phase_2/agentic_workflow.py
```

## Workflow Inputs

The workflow uses:

- `OPENAI_API_KEY` from the environment
- `Product-Spec-Email-Router.txt` as the product specification
- A workflow prompt asking what project-management output should be produced

## Workflow Sequence

At a high level, Phase 2 runs this sequence:

1. Load the OpenAI API key.
2. Load the Email Router product specification.
3. Instantiate the action planning agent.
4. Instantiate the Product Manager knowledge and evaluation agents.
5. Instantiate the Program Manager knowledge and evaluation agents.
6. Instantiate the Development Engineer knowledge and evaluation agents.
7. Register the role-based support functions with the routing agent.
8. Ask the action planning agent to extract workflow steps from the prompt.
9. Route each step to the best-matching role agent.
10. Evaluate and refine each role agent's response.
11. Print the completed output.

The script also directly prompts the router for three final artifact groups:

- User stories
- Product features
- Engineering tasks

## Role-Based Agents in the Workflow

### Product Manager Agent

Responsible for creating user stories from the product specification.

Expected output format:

```text
As a [type of user], I want [action] so that [benefit].
```

### Program Manager Agent

Responsible for grouping user needs into product features.

Expected output includes:

```text
Feature Name:
Description:
Key Functionality:
User Benefit:
```

### Development Engineer Agent

Responsible for converting user stories and product requirements into engineering tasks.

Expected output includes:

```text
Task ID:
Task Title:
Related User Story:
Description:
Acceptance Criteria:
Estimated Effort:
Dependencies:
```

# Expected Outputs

When the workflow runs successfully, it prints progress logs showing:

- The workflow prompt
- Extracted workflow steps
- Router similarity scores
- The selected agent for each routed step
- Evaluation-agent feedback
- Final project-management artifacts

The final output is a project plan for the Email Router product, organized into:

1. User Stories
2. Product Features
3. Engineering Tasks

Because the workflow uses an LLM, exact wording can vary between runs. The evaluation agents are included to keep the structure and quality of the outputs aligned with the expected criteria.

# Development Notes

## Working with Paths That Contain Spaces

The starter folder is named `starter copy`, so quote paths in terminal commands:

```bash
cd "starter copy/phase_2"
```

## Generated RAG Files

The RAG agent can generate temporary CSV files for chunks and embeddings, such as:

```text
chunks-<timestamp>_<id>.csv
embeddings-<timestamp>_<id>.csv
```

These files are runtime artifacts created while experimenting with retrieval-augmented generation.

## Model Usage

The code uses:

- `gpt-3.5-turbo` for chat completions
- `text-embedding-3-large` for embeddings

The OpenAI client is configured in the project code. In the Udacity/Vocareum environment, the client uses the Vocareum OpenAI-compatible base URL shown in the implementation.

# Troubleshooting

## `OPENAI_API_KEY` Is Missing

Confirm that your `.env` file exists and contains:

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Also confirm that you are running the script from a directory where `python-dotenv` can find the `.env` file.

## `ModuleNotFoundError`

Make sure your virtual environment is activated and dependencies are installed:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

If you are running a phase script directly, run it from that phase directory:

```bash
cd "starter copy/phase_2"
python agentic_workflow.py
```

## API or Authentication Errors

Check that:

- Your API key is valid.
- Your `.env` file is loaded.
- Your environment supports the configured OpenAI-compatible base URL.
- Your account has access to the chat and embedding models used by the code.

# Additional Documentation

For implementation details, use the phase READMEs:

- [Phase 1 README](starter%20copy/phase_1/README.md)
- [Phase 2 README](starter%20copy/phase_2/README.md)

The phase READMEs remain the best source for the step-by-step project requirements. This main README is intended to help someone set up the repository, understand the architecture, and run the complete workflow.
