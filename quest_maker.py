import json


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


# Keep prompting the user to enter quests until they choose to stop
while True:
    npc_task = input("Enter the NPC's task: ")
    if npc_task == "":
        break
    reward = int(input("Enter the reward for completing the task: "))
    chemical = input("Enter the chemical needed: ")
    hint = input("Enter a hint for the task: ")

    add_quest(npc_task, reward, chemical, hint)

# Print out all the quests in the file
with open("npc_quests.json", "r") as file:
    data = json.load(file)

for i, quest in enumerate(data):
    print(f"Quest {i + 1}:")
    print(f"  Task: {quest['npc_task']}")
    print(f"  Reward: {quest['reward']}")
    print(f"  Chemical: {quest['chemical']}")
    print(f"  Hint: {quest['hint']}")
