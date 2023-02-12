import pyttsx3
from gtts import gTTS
import json

def auto_format(text, max_length=45, separator=' '):
    words = text.split(separator)
    new_text = ''
    line_length = 0
    for word in words:
        if line_length + len(word) > max_length:
            new_text += '\n'
            line_length = 0
        new_text += word + separator
        line_length += len(word) + 1
    return new_text

def unformat(text):
    return text.replace('\n', ' ')


def speak_text(text):
    engine = pyttsx3.init()
    engine.say(unformat(text))
    engine.setProperty('voice', 2)
    engine.runAndWait()


def update_objective(objective_text, new_objective):
    objective_text.text = "Objective: " + new_objective


def update_money(money_text, new_money):
    money_text.text = "Money: " + str(new_money)


def update_task(objective_text, money_text, new_task):
    update_objective(objective_text, new_task.objective)
    update_money(money_text, new_task.money)


def get_quest(level):
    with open("npc_quests.json", "r") as file:
        data = json.load(file)

    # Return the quest information for the specified level
    if level > 0 and level <= len(data):
        quest = data[level - 1]
        return quest["npc_task"], quest["reward"], quest["chemical"], quest["hint"]
    else:
        return None


def set_quest(money_text, objective_text, level, NPC_Talk):
    task, reward, chemical, hint = get_quest(level)
    update_objective(objective_text, "Get " + chemical)
    update_money(money_text, reward)
    NPC_Talk.text = auto_format(task)
