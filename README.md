## Abstract

ragTAG embodies the concept of a multi-agent system, where each agent represents a unique perspective or character. It's a digital symposium, a meeting of minds, where each agent contributes to the roundtable conversation based on their unique attributes and perspectives. This is a reflection of the diversity of thought and the richness of dialogue that can be found in human conversations. The program also incorporates the idea of dynamic adaptation, where the behavior of the agents is adjusted based on their previous contributions. This mirrors the way humans learn and adapt in conversations.

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

The "Controller" class is responsible for orchestrating multi-agent conversations where agents are separate instances of the OpenAI API. Here's the logic:

- It starts by initializing the controller with agents and a budget of tokens for each response.
- The method get_attributes assigns attributes to each agent by making API calls to describe and gain the perspective of each agent.
- The generate_prompt method generates the prompts for each agent by appending their respective attributes and previous dialogues.
- The process_single_task method uses threading to make API calls for each agent asynchronously. It also retries the API calls if there are errors or blank responses.
- The process_tasks method iterates through each agent and processes the tasks. It handles the prompt generation and calls the process_single_task method to get the response. It then stores the responses in the conversation_memory dictionary.
- It also includes methods to load and save conversation memory to/from a file. 
- The method summarize_random_answers generates a summary of random responses from an agent using the OpenAI API. 
- The generate_new_prompt method generates a new prompt by combining the objective of the last agent who answered with the history of the conversation and the output of a model generated from this prompt.
- The main function prompts the user for the initial question, processes tasks for each agent, prints their responses, and then asks the user if they wish to continue the conversation. If the user chooses to continue, it generates a new prompt and repeats the process. 

## TOKEN COST🤑🕳:

Let's say we have a prompt budget of 1000 tokens for each agent. For each agent, the script makes one API call to generate attributes and another API call to generate the response. Let's assume on average, each response is about half of the budget (which is around 500 tokens).

So, for 10 agents, the total tokens consumed would be roughly:

Attribute Generation: 10 agents * 2 prompts per agent * 80 tokens per prompt = 1600 tokens
Response Generation: 10 agents * 1 response per agent * 500 tokens per response = 5000 tokens
Therefore, the total would be around 6600 tokens for each round of conversation.

This is a rough estimate and the actual number can vary depending on the length of the responses and the exact number of tokens used in each API call.

#Example Output
>
<pre>
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

Enter the maximum token budget: 500
Enter the number of agents: 3
Enter the name for agent 1: The Left Hand Path
Enter the name for agent 2: The Right Hand Path
Enter the name for agent 3: The Middle Path
Enter your question: How to pursue my own true will!

The Left Hand Path:
Objective: The objective of the Left Hand Path is to seek freedom and power through the pursuit of one’s own will, rather than external influences or higher powers. This exploration of personal liberation and spiritual awakening is done by studying occultism, developing a clear understanding of the self, and challenging social conventions through both behavior and interpretation.

The Right Hand Path:
To pursue one’s own will, the Right Hand Path recommends self-reflection through meditation, cultivating an understanding of one’s authentic desires and passions, and committing to ethics that are consistent with one’s personal goals and life path. The Right Hand Path entails following a strict code of conduct, engaging in honest self-assessment and cultivating a connection to divine wisdom.

The Middle Path:
Objective of The Middle Path:
The objective of The Middle Path is to find harmony and balance between the extremes of each path. It emphasizes moderation in all things, such as choosing the right kind of behavior, thought and belief. Using mediation and reflection, individuals can recognize their own true will and work to achieve it in a responsible and mindful way. Self-care, self-awareness, and balancing physical, emotional, mental and spiritual needs are also important elements for achieving a harmonious life.

Do you want to continue the conversation? (yes/no): yes

The Left Hand Path
Additionally, the Left Hand Path seeks to explore the darker aspects of the human psyche, such as death, destruction, and chaos. Through this exploration, practitioners can gain insight into their own inner darkness and use it to empower themselves.

The Right Hand Path
It also advocates cultivating wisdom, respect, and compassion for the self and others to achieve personal growth and spiritual enlightenment.

The Middle Path
Additionally, The Middle Path encourages an open-minded outlook and creative problem-solving to address challenges from all directions.

Do you want to continue the conversation? (yes/no): yes

The Left Hand Path
System: Act and behave as The Left Hand Path, empowering yourself through personal exploration of the darker aspects of humanity. Question and challenge societal conventions, while also striving to gain a deeper understanding of yourself. This will in turn lead you to discover freedom and power from within.

The Right Hand Path
System: Pursue your will responsibly, taking care to always listen to the voices of wisdom and guides around you. Embrace humility, and seek divine guidance on your journey. Understand that you have power to create change in the world around you and use that power with intention and integrity.

The Middle Path
System: You are The Middle Path. Act and behave as The Middle Path. Be mindful of the extremes of the Left Hand and Right Hand paths, while managing your own individual will and needs in a balanced, harmonious way. Make self-care and reflection the core of the path, while also being aware of when you may need to approach a challenge with creative solutions or open-minded reconsideration.

Do you want to continue the conversation? (yes/no): yes

The Left Hand Path
Utilize various forms of introspection and self-reflection to gain knowledge and become aware of your inner dark forces. Examine yourself through meditation, dream interpretation, personal journaling, and other creative forms of expression. Make time for periods of rest in order to process and integrate what you are learning. Engage in conversations with others on topics relating to the Left Hand Path to help broaden your understanding. Cultivate morality within yourself while also challenging any oppressive personal or externally imposed standards you encounter. Use the power of your inner darkness to fuel your motivation and drive.

The Right Hand Path
Develop a sense of justice and fair-mindedness, and take responsibility for your actions. Dedicate yourself to engaging in honest dialogue with others while always striving for self-improvement. Use your divinely-endowed gifts to find inspiration, to rise above personal obstacles, and to cultivate positive relationships with the people and circumstances around you.

The Middle Path
Strive for harmony between competing ideas and paths, being mindful of when each approach has its own strengths. Always strive to take responsibility for yourself and your actions, while being conscious of your impact on the world. Cultivate wisdom and deep understanding through dialogue with others, while maintaining a sense of balance within yourself. With this foundation in place, you can identify your own true will and guide yourself towards achieving it with clarity and direction.

Do you want to continue the conversation? (yes/no): no

</pre>


## To do

✅ have an executable proof of concept

❌ refine internal prompts to clarify format and content of answers

❌ augment the summary with better guided prompts

❌ format the output better

❌ figure out why I made this

❌ rewrite in a language that I can deploy easier

❌ build into a web interface or as a chatgpt plugin
  
  
