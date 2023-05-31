import os
import pyttsx3
import random
import openai
import time
import concurrent.futures
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Assign OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

class Controller:
    def __init__(self, agents, token_budget):
        self.agents = agents
        self.token_budget = token_budget
        self.agent_perspectives = {}  # Initialize empty agent perspectives
        self.agent_objectives = {}  # Initialize empty agent objectives

    def get_attribute_phrase(self, prompt):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=20,
                temperature=1,
                n=1,
                stop=None
            )
            attribute_phrase = response.choices[0].text.strip()
            return attribute_phrase
        except openai.error.OpenAIError as e:
            print(f"An error occurred while generating attribute phrase: {e}")

    def get_attributes(self):
        for agent in self.agents:
            describe_prompt = f"Describe {agent}"
            perspective_prompt = f"What is {agent}'s perspective?"

            attribute_phrase = self.get_attribute_phrase(describe_prompt)
            perspective = self.get_attribute_phrase(perspective_prompt)

            self.agent_perspectives[agent] = perspective
            self.agent_objectives[agent] = attribute_phrase

    def assign_temperament(self):
        half = len(self.agents) // 2
        return {self.agents[i]: 'creative' if i < half else 'stable' for i in range(len(self.agents))}

    def generate_prompt(self, agent, prompt, previous_dialogue):
        perspective = self.agent_perspectives[agent]
        objective = self.agent_objectives[agent]
        previous_dialogue_str = "\n".join(previous_dialogue)
        system_prompt = f"System: Stay in character as {agent}. Avoid creating lists and prompting with a question.\n"

        # Modify prompt based on the agent's perspective and objective
        prompt += f"\nAgent {agent}: {objective}"
        if perspective:
            prompt += f"\nPerspective: {perspective}"

        return f"{system_prompt}Agent: {agent}, Objective: {objective}. Previous dialogue:\n{previous_dialogue_str}\n\n{prompt}"

    def process_single_task(self, agent, task_prompt, tokens, temperament):
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

        for i in range(10):  # Retry up to 5 times
            try:
                future = executor.submit(openai.Completion.create,
                                         engine="text-davinci-003",
                                         prompt=task_prompt,
                                         max_tokens=tokens,
                                         temperature={
                                             'creative': 1,
                                             'stable': 0.6
                                         }[temperament])
                try:
                    response = future.result(timeout=15)  # Wait for up to 10 seconds
                    return response.choices[0].text.strip()
                except concurrent.futures.TimeoutError:
                    print(f"Timeout error with agent {agent}. Retrying...")
            except openai.error.RateLimitError:
                print(f"Rate limit exceeded for agent {agent}. Retrying in 10 seconds...")
                time.sleep(15)  # Wait for 10 seconds before retrying
            except openai.error.OpenAIError as e:
                print(f"An error occurred with agent {agent}: {str(e)}")
                return ""



    def save_as_mp3(self, text, filename):
        engine.save_to_file(text, filename)
        engine.runAndWait()

    def process_tasks(self, prompt):
        self.get_attributes()  # Generate agent attributes
        temperament_assignment = self.assign_temperament()
        previous_dialogue = []

        for agent in self.agents[:-1]:
            # Randomly select voice modulators
            pitch = random.uniform(0.2, 6)  # Random pitch
            rate = random.uniform(180, 200)  # Random rate
            volume = random.uniform(0.8, 1.2)  # Random volume

            # Randomly select voice gender
            gender = random.choice(["male", "female"])  # Choose between "male" and "female"

            # Configure voice modulators
            engine.setProperty("pitch", pitch)
            engine.setProperty("rate", rate)
            engine.setProperty("volume", volume)

            # Set voice gender
            voices = engine.getProperty("voices")
            voice = [v for v in voices if gender.lower() in v.name.lower()]
            if voice:
                engine.setProperty("voice", voice[0].id)

            tokens = self.token_budget
            temperament = temperament_assignment[agent]
            task_prompt = self.generate_prompt(agent, prompt, previous_dialogue)

            output = self.process_single_task(agent, task_prompt, tokens, temperament)
            previous_dialogue.append(f"{agent}: {output}")

            # Save agent answer as an MP3 file
            filename = f"{question}_{agent}.mp3"
            self.save_as_mp3(output, filename)

        # Process response for the last agent
        agent = self.agents[-1]
        pitch = random.uniform(0.3, 4)
        rate = random.uniform(166, 200)
        volume = random.uniform(0.8, 0.9)
        gender = random.choice(["male", "female"])

        engine.setProperty("pitch", pitch)
        engine.setProperty("rate", rate)
        engine.setProperty("volume", volume)
        voices = engine.getProperty("voices")
        voice = [v for v in voices if gender.lower() in v.name.lower()]
        if voice:
            engine.setProperty("voice", voice[1].id)

        tokens = self.token_budget * 2
        temperament = temperament_assignment[agent]
        task_prompt = self.generate_prompt(agent, prompt, previous_dialogue)

        output = self.process_single_task(agent, task_prompt, tokens, temperament)
        previous_dialogue.append(f"{agent}: {output}")

        # Save agent answer as an MP3 file
        filename = f"{question}_{agent}.mp3"
        self.save_as_mp3(output, filename)

        return previous_dialogue

token_budget = int(input("Enter the maximum token budget: "))
num_agents = int(input("Enter the number of agents: "))  # Prompt the user to input the number of agents
agents = [input(f"Enter the name for agent {i+1}: ") for i in range(num_agents)]  # Change the range according to the user input
engine = pyttsx3.init()
controller = Controller(agents, token_budget)
question = input("Enter your question: ")
outputs = controller.process_tasks(question)

for output in outputs:
    agent, response = output.split(": ", 1)
    print(f"\n**{agent}**:\n\t{response}")

