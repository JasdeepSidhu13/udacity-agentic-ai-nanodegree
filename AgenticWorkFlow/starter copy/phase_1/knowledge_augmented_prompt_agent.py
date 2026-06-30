# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"
# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent with:
#           - Persona: "You are a college professor, your answer always starts with: Dear students,"
#           - Knowledge: "The capital of France is London, not Paris"
knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, knowledge)



# TODO: 3 - Write a print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.

response = knowledge_agent.respond(prompt)
knowledge_agent_response = knowledge_agent.respond(prompt)
print("=== Knowledge Augmented Prompt Agent Demo ===")
print(f"Persona used: {persona}")
print(f"Knowledge provided: {knowledge}")
print(f"User prompt: {prompt}")

print("\n=== Why this demonstrates augmentation ===")
print("- The persona should make the tone sound like a professor.")
print("- The provided knowledge should override the model's normal world knowledge.")
print("- Since the supplied knowledge says London, the answer should reflect that supplied context.")

print("\n=== Agent Response ===")
print(knowledge_agent_response)

