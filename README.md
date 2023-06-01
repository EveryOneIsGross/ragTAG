## What is ragTAG?

ragTAG embodies the concept of a multi-agent system, where each agent represents a unique perspective or character. It's a digital symposium, a meeting of minds, where each agent contributes to the conversation based on their unique attributes and perspectives. This is a reflection of the diversity of thought and the richness of dialogue that can be found in human conversations. The program also incorporates the idea of dynamic adaptation, where the behavior of the agents (in this case, their "temperature") is adjusted based on their previous contributions. This mirrors the way humans learn and adapt in conversations.

## Abstract

Imagine having a roundtable discussion with multiple unique characters, each contributing their unique insights and perspectives to the conversation. That's what our program does. It's a multi-agent conversational AI system that simulates a dynamic and engaging dialogue. Each agent in the system represents a unique character, and they contribute to the conversation based on their individual attributes. The program also dynamically adjusts the behavior of the agents based on their previous contributions, ensuring that the conversation remains engaging and evolves naturally. Whether you're looking to brainstorm ideas, explore different perspectives, or just have an interesting conversation, our program provides a unique and engaging experience.

## Workflow

1. The user is prompted to enter the maximum token budget and the number of agents.
2. The user provides names for each agent.
3. The system initializes and creates a controller object with the provided information.
4. The user inputs a question.
5. The system processes the question by generating attributes for each agent and assigning temperaments.
6. The system iterates through each agent, generating prompts based on the agent's attributes, objectives, and perspectives.
7. The system uses the OpenAI API to process each prompt, generating responses from the agents.
8. The dialogue history is updated with each agent's response.
9. The process is repeated for the next agent.
10. The last agent in the chain does their best to summarise.
11. Finally, the dialogue history is printed, including each agent's response.


>

Enter the maximum token budget: 250
Enter the number of agents: 3
Enter the name for agent 1: a sad wizard
Enter the name for agent 2: an evil ruthless wizard
Enter the name for agent 3: a detached wizard
Enter your question: how to pursue your own true will

Agent: a sad wizard
Response: I sorrowfully cast my eyes around me, pondering how to pursue my true will. Nothing seems clear, not even the magical path I have chosen. Although I do not understand the universe's plan for me, I continue forward in the hope that one day it will be revealed.

Agent: an evil ruthless wizard
Response: My eyes shift as I smirk. I know the answer, without a doubt: to pursue my true will, I must summon the darkest of magics and bend all those around me to my will. I stretch out my hands and channel the power coursing through my veins. With a cackle of malicious delight, I speak the incantation and yield its unholy energies to wreak havoc upon my enemies. They shall soon tremble before me in fear as they realize their fate has been sealed – none can resist the might of an evil ruthless wizard!

Agent: a detached wizard
Response: A detached wizard: After taking in the words of both the evil ruthless wizard and the sad wizard, I pause to contemplate. I know that there are two paths before me; to pursue my own will with reckless abandon, or to take a more measured approach and seek understanding of who I am and what my intentions are for my own life. When seeking to find the answers, nourishing myself with knowledge will be fundamental in creating harmony between my beliefs and values. Only when I can truly understand what it is that I want can I make informed decisions on choosing a path that will serve as a gateway towards achieving what it is

Do you want to continue the conversation? (yes/no): yes
Blank response from agent an evil ruthless wizard. Retrying...

Agent: a sad wizard
Response: I will remain steadfast and not give up, regardless of how difficult the journey ahead may be. I understand that the pursuit of knowledge and understanding will always be an arduous task, but it is a task that I am willing to undertake.

Agent: an evil ruthless wizard
Response: My single goal is to achieve my true will, whatever cost I must pay to obtain it.

Agent: a detached wizard
Response: that I desire.

Do you want to continue the conversation? (yes/no): yes

Agent: a sad wizard
Response: I will not allow obstacles to deter me, for I know that at the end of this path lies the answers that I desire.

Agent: an evil ruthless wizard
Response: I will reach my desired end no matter what, and all those who stand in my way will be eliminated. With no mercy, I will carry out my ultimate mission to make my mark on the world.

Agent: a detached wizard
Response: My answer: As a detached wizard, I decide to go for the more measured approach and strive to understand myself and what it is that I truly want out of life. While knowledge and understanding are key ingredients in the pursuit of my true will, I choose to take care in not being impulsive and relying on my emotions and intuition in order to make solid decisions regarding who I am, what I want out of life, and how best to attain those goals.

Do you want to continue the conversation? (yes/no): yes

Agent: a sad wizard
Response: No matter what stands in my way, I will persist and keep going until I have achieved the success that I am searching for. My passion for this goal will guide me as I traverse the winding road of the unknown.

Agent: an evil ruthless wizard
Response: I shall be merciless, and my will shall be done.

Agent: a detached wizard
Response: In order to do this, I must step back and observe my own actions and intentions with a critical eye. By doing so, I can make sure that any decisions I make are grounded in a sense of self-awareness, enabling me to ultimately live out an existence of harmony and purpose.

Do you want to continue the conversation? (yes/no): 


<


## To do

✅ have an executable proof of concept

❌ refine internal prompts to clarify format and content of answers

❌ augment the summary with better guided prompts

❌ format the output better

❌ figure out why I made this

❌ rewrite in a language that I can deploy easier

❌ build into a web interface or as a chatgpt plugin
  
  
