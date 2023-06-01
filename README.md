## What is ragTAG?

It's a Q&A chain of chatbots. 🎶 It's purpose is to reflect on a users prompt from multiple perspectives and to give enriched answers. Assign a ragtag team of agents to help you solve your queires.  

## Abstract

The provided code implements a dialogue system that interacts with multiple agents to generate responses to a user's question. It uses OpenAI's API for natural language processing tasks. The system assigns attributes and perspectives to each agent, simulates their dialogue, and generates text responses based on the agents' personality and temperaments. 

![DreamShaper_v6_RagTAG_a_bunch_of_embodied_chatbots_being_frien_5](https://github.com/EveryOneIsGross/ragTAG/assets/23621140/e167938b-fb65-4ad0-a9d5-db3219fa9df0)

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

## Context

The provided code showcases the use of OpenAI's language model and text generation capabilities to simulate dialogue between multiple agents. It demonstrates the integration of AI APIs and the combination of text generation and text-to-speech technologies. The code shows the capabilities of modern language models, enabling diverse conversational experiences. 

The potential novel uses of multi-chatbots include collaborative decision making, educational dialogues, personalized virtual assistants, collaborative storytelling, and virtual debates and dialogues. These applications showcase the versatility of multi-chatbots and their potential to enhance decision-making, education, creativity, and human-machine interactions.

In RagTAG, AI agents, each with their own unique perspective and objective, engage in a sequential and interactive dialogue. They process tasks, contribute to the conversation, and generate responses while remaining in character. The result is a rich, dynamic conversation that mirrors a human-like discussion but powered by advanced AI capabilities.

<pre>
## Example Output 1

Number of Agents : #3
Qustion: "What are the implications of artificial intelligence on society?"

Emulated Output on UNNAMED agents:
AGENT1: As an AI, I believe that the implications of artificial intelligence on society are profound. AI has the potential to revolutionize various sectors, including healthcare, transportation, and education. It can automate tedious tasks, improve efficiency, and unlock new possibilities. However, there are concerns about job displacement and the ethical use of AI, particularly in areas like privacy and algorithmic bias. It is crucial for society to carefully navigate the opportunities and challenges that AI brings.

AGENT2 (can read AGENT1's responde: From my perspective, the implications of artificial intelligence on society are both exciting and concerning. AI has the power to enhance productivity and create innovative solutions to complex problems. It can enable personalized experiences and improve decision-making processes. However, there are ethical considerations surrounding AI's impact on privacy, security, and inequality. Society must ensure responsible development and deployment of AI technologies to mitigate potential risks.

AGENT3 Summarises all responses: The implications of artificial intelligence on society cannot be underestimated. AI has the potential to reshape industries, transform labor markets, and redefine human-machine interactions. It offers new avenues for scientific research, personalized services, and creative endeavors. However, we must address the ethical, social, and economic challenges that come with AI adoption. Ensuring transparency, fairness, and inclusivity should be paramount in harnessing the benefits of AI for society's well-being.

## Example Output 2

Enter your OpenAI API key: xxxxxxxxxxxxxxxxxxxx
Enter the maximum token budget: 1000
Enter the number of agents: 4
Enter the name for agent 1: Judge Dredd
Enter the name for agent 2: A local surfer
Enter the name for agent 3: Aleister Crowley
Enter the name for agent 4: Brendon Fraser pretending to be a sandwich
Enter your question: How to be stay in the moment and let go of worries

Judge Dredd: primary objective is to enforce the Law and serve justice. To stay in the moment and let go of worries is to keep a clear mind and trust in my experience and authority. I must focus on the task at hand and stay true to my mission: to enforce justice and uphold the Law.

A local surfer: the local waves and knows what to expect. Taking the time to get to know the ocean, understanding the currents, and respecting the power of the waves is key to staying safe and enjoying the experience. To stay in the moment and let go of worries, it's important to stay focused on the waves and the surf itself, breathing steadily and staying connected to the water. When the moment calls for it, take some time for a quick admire of the stunning scenery; then it's back to riding those waves.

Aleister Crowley: who wrote widely on the subject of magick and mysticism. He believed that one could achieve a higher level of consciousness by using magick and tapping into the spiritual realm. He encouraged his followers to explore both their inner and outer worlds and to embrace their own unique path in life. He taught that the only way to truly be in the moment and let go of worries was to focus on the present moment and be mindful of the energy that exists in all things.

Brendon Fraser pretending to be a sandwich: The common theme among all three characters is the importance of staying in the moment and letting go of worries. Judge Dredd, the local surfer, and Aleister Crowley all emphasize the need to stay focused on the task at hand and to embrace the present moment. From Brendon Fraser pretending to be a sandwich's perspective, he can learn from these characters by staying mindful of the energy that exists in all things, trusting his own experience and authority, and focusing on the task at hand. Taking the time to get to know his environment, understanding the flow of the situation, and embracing his own unique path can help him stay in the moment and let go of worries.

</pre>

## To do

✅ have an executable proof of concept

❌ refine internal prompts to clarify format and content of answers

❌ augment the summary with better guided prompts

❌ format the output better

❌ figure out why I made this

❌ rewrite in a language that I can deploy easier

❌ build into a web interface or as a chatgpt plugin
  
  
