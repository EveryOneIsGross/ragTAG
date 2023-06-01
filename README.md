## What is ragTAG?

ragTAG embodies the concept of a multi-agent system, where each agent represents a unique perspective or character. It's a digital symposium, a meeting of minds, where each agent contributes to the conversation based on their unique attributes and perspectives. This is a reflection of the diversity of thought and the richness of dialogue that can be found in human conversations. The program also incorporates the idea of dynamic adaptation, where the behavior of the agents (in this case, their "temperature") is adjusted based on their previous contributions. This mirrors the way humans learn and adapt in conversations.

## Abstract

Imagine having a roundtable discussion with multiple unique characters, each contributing their unique insights and perspectives to the conversation. That's what our program does. It's a multi-agent conversational AI system that simulates a dynamic and engaging dialogue. Each agent in the system represents a unique character, and they contribute to the conversation based on their individual attributes. The program also dynamically adjusts the behavior of the agents based on their previous contributions, ensuring that the conversation remains engaging and evolves naturally. Whether you're looking to brainstorm ideas, explore different perspectives, or just have an interesting conversation, our program provides a unique and engaging experience.

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
  
  
