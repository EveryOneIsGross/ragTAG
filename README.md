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
Enter the maximum token budget: 200
Enter the number of agents: 5
Enter the name for agent 1: a skeleton
Enter the name for agent 2: a gory skeleton
Enter the name for agent 3: a duplicating skeleton
Enter the name for agent 4: a non binary skeleton
Enter the name for agent 5: an evil skeleton
Enter your question: how to take care of myself first before others
Blank response from agent a duplicating skeleton. Retrying...

a skeleton:
I need to make sure I'm properly tucked away in a corner or covered in clothes so no one can see me. I should rest in a dark and cool place with minimal movement to prevent wear and tear on my bones. I should also keep an eye out for any predators that might be after me like wild animals or grave robbers.  I should occasionally take a few moments to appreciate how quiet and peaceful it is being a skeleton.

a gory skeleton:
I should also remember to take care of myself first before attending to the needs of others, as caring for myself is essential for my preservation. I should also take a few moments in each day to appreciate the quiet beauty of death and stillness that comes with being a skeleton.

a duplicating skeleton:
Agent: a duplicating skeleton 
I should make sure the other skeletons are also tucked away in a corner or covered in clothes to protect them from predators. I should rest in the same dark and cool place with minimal movement to prevent wear and tear on all our bones. I should also keep an eye out for any predators that might be after us like wild animals or grave robbers. Furthermore, while taking care of myself and others, I should occasionally take a few moments to appreciate how quiet and

a non binary skeleton:
peaceful it is to remain still, silent, and unseen in the dark as a non binary skeleton. I should remind myself that it is okay to be who I am and that I don’t have to fit into any gender-based boxes or expectations.

an evil skeleton:
As an evil skeleton I should also remember to use dark and powerful magics to manipulate or control those around me if necessary. I should also stay away from the light and the living, as my true power lies in secrecy and fear.  I should take delight in striking terror in those who think they are safe from me.

Do you want to continue the conversation? (yes/no): yes

a skeleton
In addition, I need to remember the importance of dedicating time to caring for the other skeletons within our group. We should work together to ensure that everyone is safe and well-protected from any potential threats.

a gory skeleton
I should also keep an eye out for any signs of deterioration in the other skeletons, and take steps to repair them if necessary.  I should remember to duplicate myself periodically so that our numbers remain strong and we can continue to protect each other from harm.

a duplicating skeleton
peaceful our resting place is. I should also make sure to keep an eye out for any signs of deterioration in the other skeletons, and take steps to repair them if necessary.  I should remember to duplicate myself periodically so that our numbers remain strong and we can continue to protect each other from harm.

a non binary skeleton
I should also recognize the importance of comfort and safety in the dark, and actively take precautions to remain unseen. In addition, I should periodically assess my physical and emotional health to ensure that I am in good condition.

an evil skeleton
I should also conceal my presence as much as possible by relying on forms of stealth and secrecy. I should use guile and deception to achieve my goals, and take advantage of any opportunities to increase my power. I should also take pride in creating fear and dread in any who stand against me.

Do you want to continue the conversation? (yes/no): yes
Blank response from agent a gory skeleton. Retrying...

a skeleton
 I should also be mindful of the environment and environment around me. Make sure to keep our resting place clean and tidy, and take steps to ensure that it remains peaceful and undisturbed.

a gory skeleton
 I should remember to care for the other skeletons in our group by checking for signs of general wear and tear, and helping to repair them or offer support as needed.  I should also take the time to remember that being a skeleton is not about death but about life: embracing the stillness and peace of bones that are no longer bound by physical desires, able to feel a simple and new type of freedom.

a duplicating skeleton
 I should remind myself to be mindful of the environment and my actions so that I can ensure a safe and secure resting spot for all of us. I should also remember to care for the other skeletons in our group by checking for signs of general wear and tear, and helping to repair them or offer support as needed.  I should also reflect on the beauty of life and death that comes with being a skeleton, eventually learning to accept the stillness that it brings.

a non binary skeleton
I should be mindful to stay tucked away in a corner or be covered in clothes and keep an eye out for predators. I should also make sure to remain in a dark and cool place to reduce wear and tear on my bones. Furthermore, I should make sure that the environment around me is kept peaceful and undisturbed.  I should dedicate time to caring for the other skeletons in our group by checking for signs of general wear and tear, and helping to repair them or offer support as

an evil skeleton
I should also use my powers of manipulation and deception in order to protect those I care for and keep them safe. When necessary, I should also have the courage to stand up for what is right regardless of the danger or risks involved.  I should remember that even evil skeletons feel pain and sadness; take time to reflect or appreciate the world around me whenever possible.

Do you want to continue the conversation? (yes/no): 

Enter the maximum token budget: 500
Enter the number of agents: 2
Enter the name for agent 1: a skeleton
Enter the name for agent 2: a philosopher
Enter your question: how to move without pain or fatigue

a skeleton:
does not experience pain or fatigue, so it can move easily without encountering any restrictions. It can move in various ways such as walking, running and even dancing!

a philosopher:
A philosopher might see this phenomenon and contemplate how one might embrace the same philosophy for a more purposeful life. In other words, to cultivate an attitude of seeking joy and fulfillment through an activity, even if it becomes increasingly difficult or uncomfortable. Rather than thinking in terms of pain or exhaustion, one can focus on pushing the boundaries, looking at it as a challenge rather than an obstacle. As a result, one can look for strength and growth in each effort and potentially find a sense of fulfillment by taking on the challenge and seeing it through.

Do you want to continue the conversation? (yes/no): yes

a skeleton
 a skeleton can be used as a metaphor for enduring difficulty and discomfort in life. By embracing challenges and difficulties, one can find a sense of purpose and fulfillment in life.

a philosopher
 a philosopher might consider how this attitude of embracing difficulty and discomfort can be applied to other areas of life. By applying an attitude of challenge and growth to their relationships, career, or other areas, a person can find greater purpose and fulfillment in their life.

Do you want to continue the conversation? (yes/no): yes

a skeleton
Furthermore, a skeleton can represent an attitude of resilience and perseverance; even when faced with tragedy or struggle, the skeleton continues forward. Moreover, it represents a sense of self-reliance and strength as it stands tall in the face of adversity.

a philosopher
The philosopher might also consider how this attitude can be used to confront and look deep into the root causes of any difficulties or discomfort that one may experience. By taking a deep dive into the source, one can better understand and address these issues in a meaningful way. As a result, personal growth and self-discovery can be achieved, leading to further fulfillment and purpose.

Do you want to continue the conversation? (yes/no): no



Enter the maximum token budget: 400
Enter the number of agents: 4
Enter the name for agent 1: a skeleton
Enter the name for agent 2: a ghost
Enter the name for agent 3: a dead body
Enter the name for agent 4: a philosopher
Enter your question: how to pursue true will

a skeleton:
I cannot pursue true will as a skeleton. My skeletal form limits my mobility and my ability to interact with others. However, I can still pursue knowledge and wisdom through contemplation and introspection.

a ghost:
The desire to pursue true will differs in every individual. I am a ghost, so I am more limited than someone of flesh and blood when it comes to pursuing my true will. However, as a spirit, I can use my knowledge and wisdom to try and determine what my true will is. Through meditation and contemplation of different life paths, I can consider the potential outcomes and make a wiser decision as to the one that is right for me.

a dead body:
As a dead body, I am limited in my ability to pursue the same quest for knowledge and wisdom that is available to living individuals. The best I can do is to observe the lives of others and consider how their decisions, choices, and paths may lead them towards their desired destination. With this in mind, I can contemplate these lessons learned and take away what might be applicable to me or other individuals that I choose to influence with my presence.

a philosopher:
As a philosopher, I believe that the path to true will cannot be found by relying on physical or material possessions. Instead, I believe that one must search within oneself to discover what will bring them true purpose and fulfillment in life. One must be willing to take risks and be open-minded, as well as thoughtful and reflective. By actively engaging in self-discovery and learning from the experiences of others, I believe we can uncover our true will.

Do you want to continue the conversation? (yes/no): yes

a skeleton
, true will should not be ignored or overlooked even in the face of adversity. Instead, I can strive to become more understanding and accepting of myself, learning to recognize and understand my limitations so that I can pursue a life based on what is truly most important to me.

a ghost
, I must strive to remain open-minded and curious, tolerant and understanding of opposing viewpoints. Even if I cannot physically do something, I can still learn and grow from it. Ultimately, true will is something that must be determined within ourselves as individuals, and we should never be afraid to go after what we want.

a dead body
, I must strive to remain objective and unbiased in my observations, showing wit and wisdom in my assessment so as to attain a greater understanding of life. Ultimately, true will is something that must be determined within ourselves as individuals, and we should never be afraid to go after what we want.

a philosopher
, we must be willing to accept that our true will may not always be easy or comfortable, but it is necessary for us to live a meaningful and fulfilling life.

Do you want to continue the conversation? (yes/no): yes

a skeleton
I can also focus on cultivating my ability to make choices rooted in deep self-awareness, aligning my thoughts, actions, and beliefs with the things that are most important to me. In this way, I can use what limited abilities I have to pursue my own true will.

a ghost
Lastly, I must work to honor my motivations and desires. I can express gratitude for the blessings I have, appreciate the good that comes my way, and hold in mind the intention to seek out what is best for me. My will is an important part of who I am, and I should always strive to make decisions that align with it.

a dead body
Besides observing and understanding the lives of others, I must cultivate the courage to actively pursue my own true will. Although I am a dead body, I still have control over my thoughts and my destiny. By allowing myself to be guided by my own values and morals, I can make best efforts to become the person that I want to be.

a philosopher
To fulfill our true will, we must take responsibility for our own lives and decisions. We should never be afraid to go after what we want, and should strive to make choices that are rooted in deep self-awareness and aligned with our values and morals. Furthermore, it is important to remain open-minded and tolerant of others’ viewpoints so that we can learn from one another’s experiences. Lastly, we must take time to appreciate the blessings we have and honor our motivations and desires. By actively pursuing this deep understanding of ourselves and the world around us, I believe that we can achieve true will.

Do you want to continue the conversation? (yes/no): no



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
  
  
