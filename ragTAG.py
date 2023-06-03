import os
import random
import openai
import time
import concurrent.futures
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Assign OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY'
)
class Controller:
    def __init__(self, agents, token_budget, max_token_limit):
        self.agents = agents
        self.max_token_limit = max_token_limit
        self.token_budget = min(token_budget, max_token_limit)  # Ensure token_budget doesn't exceed max_token_limit
        self.response_token_budget = self.token_budget // 2
        self.agent_perspectives = {}
        self.agent_objectives = {}
        self.conversation_memory = {}
        self.agent_temperatures = {}
        self.initial_prompt = True

    def get_attribute_phrase(self, prompt):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=80,
                temperature=0.4,
                n=1,
                stop=None
            )
            attribute_phrase = response.choices[0].text.strip()
            word_count = len(attribute_phrase.split())
            return attribute_phrase, word_count
        except openai.error.OpenAIError as e:
            print(f"An error occurred while generating attribute phrase: {e}")


    def get_attributes(self):
        for agent in self.agents:
            describe_prompt = f"Describe yourself as {agent}"
            perspective_prompt = f"What is your perspective as {agent}"

            for _ in range(3):  # Retry up to 3 times
                try:
                    attribute_phrase, word_count = self.get_attribute_phrase(describe_prompt)
                    perspective, _ = self.get_attribute_phrase(perspective_prompt)

                    if attribute_phrase and perspective:  # If both phrases are successfully retrieved
                        self.agent_perspectives[agent] = perspective
                        self.agent_objectives[agent] = attribute_phrase

                        # Calculate temperature based on word count
                        temperature = 0.4 + 0.4 * min(word_count, 100) / 100
                        self.agent_temperatures[agent] = temperature

                        break  # Break the loop as we have successfully retrieved the phrases
                except openai.error.OpenAIError as e:
                    print(f"An error occurred while generating attribute phrase for {agent}: {e}")
                    time.sleep(10)  # Wait for 10 second before retrying



    def generate_prompt(self, agent, prompt, previous_dialogue):
        perspective = self.agent_perspectives.get(agent, "")
        objective = self.agent_objectives.get(agent, "")
        previous_dialogue_str = "\n".join(previous_dialogue)
        system_prompt = f"You are {agent}. Act and behave as {agent}.\n"

        if agent == self.agents[0]:  # First agent
            prompt += f"\n{agent} {objective}"
        else:
            prompt += f"\n{objective}\n{previous_dialogue_str}"

        if perspective:
            prompt += f"\n{perspective}"

        memories = []
        for prev_agent, dialogue in self.conversation_memory.items():
            if prev_agent == agent or prev_agent in previous_dialogue_str:
                memories.append(f"Agent: {prev_agent}\n" + "\n".join(dialogue))

        memories_section = ""
        if memories:
            memories_section = f"{agent} Memories:"
            for memory in memories:
                memories_section += f"\n{memory}"

        answers_section = ""
        agent_answers = self.conversation_memory.get(agent, [])
        if agent_answers:
            answers_section = f"{agent} Answers:"
            for answer in agent_answers:
                answers_section += f"\n{answer}"

        prompt += f"\n\n{memories_section}\n\n{answers_section}"

        return f"{system_prompt}Agent: {agent}, {objective}. \n{previous_dialogue_str}\n\n{prompt}"


    

    def process_single_task(self, agent, task_prompt, tokens):
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)

        for i in range(10):
            try:
                previous_answers = self.conversation_memory.get(agent, [])
                full_prompt = "\n".join(previous_answers) + "\n" + task_prompt

                token_budget = self.response_token_budget

                token_budget = min(token_budget, tokens)

                future = executor.submit(
                    openai.Completion.create,
                    engine="text-davinci-003",
                    prompt=full_prompt,
                    max_tokens=token_budget,
                    temperature=1,
                    frequency_penalty = 0.5
                )

                response = future.result(timeout=60)
                response_text = [partial_response.text.strip() for partial_response in response.choices]
                generated_text = " ".join(response_text)

                # Check if the generated text is blank
                if generated_text.strip() == "":
                    print(f"Blank response from agent {agent}. Retrying...")
                    continue  # Continue to the next iteration of the loop to retry

                # Add the response to the conversation memory
                if agent in self.conversation_memory:
                    self.conversation_memory[agent].append(generated_text)
                else:
                    self.conversation_memory[agent] = [generated_text]

                # Save the conversation memory after each response
                self.save_conversation_memory("conversation_memory.txt")

                return generated_text

            except concurrent.futures.TimeoutError:
                print(f"Timeout error with agent {agent}. Retrying...")
            except openai.error.RateLimitError:
                print(f"Rate limit exceeded for agent {agent}. Retrying in 10 seconds...")
                time.sleep(10)
            except openai.error.OpenAIError as e:
                print(f"An error occurred with agent {agent}: {str(e)}")

        # Return an empty string if all retries are exhausted and the response is still blank
        return ""







    def save_conversation_memory(self, filename):
        with open(filename, "w") as file:
            for agent, dialogue in self.conversation_memory.items():
                file.write(f"Agent: {agent}\n")
                for line in dialogue:
                    file.write(f"{line}\n")

    def load_conversation_memory(self, filename):
        try:
            with open(filename, "r") as file:
                current_agent = None
                for line in file:
                    if line.startswith("Agent:"):
                        current_agent = line.split(":")[1].strip()
                        if current_agent not in self.conversation_memory:
                            self.conversation_memory[current_agent] = []
                    elif current_agent:
                        self.conversation_memory[current_agent].append(line.strip())
        except FileNotFoundError:
            self.conversation_memory = {}

    def summarize_random_answers(self, num_answers):
        agents = list(self.conversation_memory.keys())
        agent = random.choice(agents)
        agent_answers = self.conversation_memory.get(agent, [])

        if len(agent_answers) >= num_answers:
            random_answers = random.sample(agent_answers, num_answers)
            random_answers_combined = "\n".join(random_answers)
            for i in range(3):  # Retry up to 3 times
                try:
                    response = openai.Completion.create(
                        engine="text-davinci-003",
                        prompt=random_answers_combined,
                        max_tokens=100,
                        temperature=0,
                        n=1,
                        stop=None,
                        frequency_penalty=0.5
                    )
                    summary = response.choices[0].text.strip()
                    return summary
                except openai.error.RateLimitError:
                    print(f"Rate limit exceeded. Retrying in 10 seconds...")
                    time.sleep(10)
                except openai.error.OpenAIError as e:
                    print(f"An error occurred: {str(e)}")
                    return "Error occurred while summarizing"
        else:
            return "Insufficient answers to summarize"

    def openai_summarize(self, prompt):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=200,
            temperature=0.2,
            top_p=1.0,
            frequency_penalty=0.8,
            presence_penalty=0.5,
            stop=None,
            n=1
        )
        summary = response.choices[0].text.strip()
        return summary

    def generate_new_prompt(self, last_answer, history):
        agent_name = last_answer[0]
        objective = self.agent_objectives.get(agent_name, "")
        
        if objective:
            prompt = (
                f"System: Stay in character as {agent_name}. Avoid creating lists and do not start sentences with adverbs, do not say words like Additionally.\n"
                f"Agent: {agent_name}, {objective}. \n{history}\n\n"
            )
            
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=prompt,
                    max_tokens=100,
                    temperature=0.9,
                    n=1,
                    stop=None,
                    frequency_penalty = 0.8,
                    presence_penalty = 0.5
                )
                return response.choices[0].text.strip()
            except openai.error.OpenAIError as e:
                print(f"An error occurred: {str(e)}")
        
        return ""



    def process_tasks(self, prompt, initial_tokens):
        # Initialize total_tokens
        total_tokens = 0 

        previous_dialogue = []
        first_iteration = True

        response_token_budget = 100

        for agent in self.agents[:-1]:
            if first_iteration:
                tokens = initial_tokens
                first_iteration = False
            else:
                tokens = response_token_budget

            total_tokens += tokens  # Add used tokens to total_tokens

            task_prompt = self.generate_prompt(agent, prompt, previous_dialogue)

            output = self.process_single_task(agent, task_prompt, tokens)

            if first_iteration:
                previous_dialogue.append(f"{agent}: {output}")
                print(f"\nInitial response of {agent}: {output}")
            else:
                if len(output.split()) > response_token_budget:
                    output = " ".join(output.split()[:response_token_budget])
                previous_dialogue.append(f"{agent}: {output}")

            if agent in self.conversation_memory:
                self.conversation_memory[agent].append(output)
            else:
                self.conversation_memory[agent] = [output]

        agent = self.agents[-1]

        if total_tokens + response_token_budget + 200 <= self.max_token_limit:
            tokens = response_token_budget + 200  # Assign additional buffer if it doesn't exceed the max_token_limit
        else:
            tokens = response_token_budget

        task_prompt = self.generate_prompt(agent, prompt, previous_dialogue)

        output = self.process_single_task(agent, task_prompt, tokens)
        previous_dialogue.append(f"{agent}: {output}")

        if agent in self.conversation_memory:
            self.conversation_memory[agent].append(output)
        else:
            self.conversation_memory[agent] = [output]

        return previous_dialogue




def main():
    max_token_limit = 3000
    token_budget = int(input("Enter the maximum token budget: "))
    num_agents = int(input("Enter the number of agents: "))
    agents = [input(f"Enter the name for agent {i+1}: ") for i in range(num_agents)]
    controller = Controller(agents, token_budget, max_token_limit)



    question = input("Enter your question: ")
    initial_tokens = 200
    outputs = controller.process_tasks(question, initial_tokens)

    for output in outputs:
        agent, response = output.split(": ", 1)
        print(f"\n{agent}:")
        print(f"{response}")


    while True:
        continue_conversation = input("\nDo you want to continue the conversation? (yes/no): ")
        if continue_conversation.lower() == "no":
            break
        else:
            last_answer = outputs[-1].split(": ", 1)
            history = "\n".join(controller.conversation_memory[last_answer[0]])
            new_prompt = controller.generate_new_prompt(last_answer, history)
            random_answers_summary = controller.summarize_random_answers(2)
            new_question = f"{random_answers_summary}\n{new_prompt}"
            outputs = controller.process_tasks(new_question, token_budget)
            for output in outputs:
                agent, response = output.split(": ", 1)
                print(f"\n{agent}")
                print(f"{response}")


    conversation_memory_file = "conversation_memory.txt"
    controller.save_conversation_memory(conversation_memory_file)

if __name__ == '__main__':
    main()
