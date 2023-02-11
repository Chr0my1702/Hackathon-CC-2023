import json
import re


def add_quest(npc_task, reward, chemical, hint):
    # Load the existing JSON file or create a new one if it doesn't exist
    try:
        with open("npc_quests.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Add the new quest to the existing data
    new_quest = {"npc_task": npc_task, "reward": reward,
                 "chemical": chemical, "hint": hint}
    data.append(new_quest)

    # Write the updated data back to the file
    with open("npc_quests.json", "w") as file:
        json.dump(data, file)


def predict_reward(npc_task):
    # Use a regular expression to extract the first number from the string
    match = re.search(r"\b\d+\b", npc_task)
    if match:
        predicted_reward = int(match.group(0))
        use_predicted = input(
            f"The predicted reward is {predicted_reward}. Use this value? (y/n) ")
        if use_predicted.lower() == "y":
            return predicted_reward
    return int(input("Enter the reward for completing the task: "))


# Keep prompting the user to enter quests until they choose to stop
while True:
    npc_task = input("Enter the NPC's task: ")
    if npc_task == "":
        break
    reward = predict_reward(npc_task)
    chemical = input("Enter the chemical needed: ")
    hint = input("Enter a hint for the task: ")

    add_quest(npc_task, reward, chemical, hint)

# Print out all the quests in the file
with open("npc_quests.json", "r") as file:
    data = json.load(file)

print(json.dumps(data, indent=2))
