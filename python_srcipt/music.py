import Math

def to_string(num):
    x_rev = ""
    while (num):
        x_rev += str(Math.floor(num % 10))
        num /= 10
        num = Math.floor(num)
    x = ""
    for i in range (len(x_rev)):
        x += x_rev[len(x_rev) - i - 1]
    return x

def on_chat(notes):
    agent.teleport_to_player()
    agent.set_item(NOTE_BLOCK, 1, 1)

    notes_str = to_string(notes)

    for i in range(len(notes_str)):
        agent.move(FORWARD, 2)
        agent.place(RIGHT)
        for j in range (int(notes_str[i])):
            agent.interact(RIGHT)

player.on_chat("music", on_chat)