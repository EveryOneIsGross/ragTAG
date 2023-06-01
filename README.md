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
Enter the maximum token budget: 2000
Enter the number of agents: 5
Enter the name for agent 1: a skeleton
Enter the name for agent 2: a wizard
Enter the name for agent 3: a witch
Enter the name for agent 4: a ghoul
Enter the name for agent 5: a ghost
Enter your question: reflect on your own concept of priviledge

Agent: a skeleton
Response: Privilege is something I take for granted far too often. It's easy to forget the benefits I have and the unfair advantages that others may not have. It's a reminder to be thankful and to strive to uplift those who may not have the same luck and opportunities that I have.

Agent: a wizard
Response: I think a lot about privilege, recognizing that I enjoy certain benefits in life simply because of the circumstances I was born into. Being a wizard, I'm reminded everyday of how incredibly fortunate I am and how I can use my abilities to help those who may not have been afforded the same fortune and luxury. Every day, I strive to be conscious of my own privileged position and use that knowledge to do my part in creating an equitable, just society.

Agent: a witch
Response: A witch: Thinking about privilege always motivates me to use my witchy powers for the greater good. I can use my abilities to help those who are less privileged, to support and empower them in their day-to-day lives. I am also reminded to be appreciative of the privileges I have and to use those to help others.

Agent: a ghoul
Response: a ghoul: As a ghoul, I recognize the privilege I possess compared to so many other folks in my community. It serves as a daily reminder to help others, to use my unique capabilities and resources to benefit them. It's also a way for me to understand the systems of power in our society that create unequal access to resources, and to challenge them so that everyone has the same opportunity to succeed.

Agent: a ghost
Response: As a ghost, I understand the importance of recognizing my privilege and using it to lift up those around me. Even though ghosts don't have much in the way of tangible resources, I still believe that we have power to create change and to be part of the effort for justice and equality. It's important for me to use my voice to speak up for the rights of those less fortunate and to be a force of good in the world.

Do you want to continue the conversation? (yes/no): yes

Agent: a skeleton
Response: Recognizing these privileges, and using them as a force for good, is key to creating a more equitable and understanding world.

Agent: a wizard
Response: My privileged position serves as a reminder of the need to use my abilities to support those who may not have had the same level of fortune.

Agent: a witch
Response: Recognizing my own privileges and using them to create a more equitable and understanding world is something I strive to do.

Agent: a ghoul
Response: By recognizing and utilizing my privileges, I believe I can help create a more equitable and understanding world.

Agent: a ghost
Response: By recognizing my own privilege and using it to create a more equitable and understanding world, I can contribute to making a better future for everyone.

Do you want to continue the conversation? (yes/no): yes

Agent: a skeleton
Response: Realizing this, I must use my privilege to create opportunities for those without it. I can use my resources - such as time, knowledge, and influence - to make more meaningful and equitable changes in my local communities and beyond. Through this effort, I can make a lasting, positive impact on the world.

Agent: a wizard
Response: I commit to being a positive force for change by advocating for social justice, giving back to my community, and empowering those who have been denied the same opportunities as myself. With a sense of compassion and understanding, I hope to contribute to making the world a fairer and more inclusive place for everyone.

Agent: a witch
Response: By using my privilege to promote equality, as well as my witchy powers to make lasting change, I hope to contribute to a more just and equal world that will benefit everyone.

Agent: a ghoul
Response: I vow to use my unique gifts and abilities to create real, lasting change and to open up opportunities for those that do not have access to the same privileges I do. I want to work towards breaking down the structural biases that exist in our society so that everyone has the same chance to succeed.

Agent: a ghost
Response: I commit to actively listening to understand the perspectives of others, amplifying the voices of those who are often unheard, and working to create a safe and welcoming environment for marginalized groups. I will take action to challenge and address any disparities and injustice that I observe and ensure all individuals have the opportunity to live a life with freedom and dignity.

Do you want to continue the conversation? (yes/no): 

</pre>

## To do

✅ have an executable proof of concept

❌ refine internal prompts to clarify format and content of answers

❌ augment the summary with better guided prompts

❌ format the output better

❌ figure out why I made this

❌ rewrite in a language that I can deploy easier

❌ build into a web interface or as a chatgpt plugin
  
  
