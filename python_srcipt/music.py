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
    agent.set_item(REPEATER, 1, 2)
    agent.set_item(REDSTONE_WIRE, 1, 3)

    notes_str = to_string(notes)

    for i in range(len(notes_str)):
        agent.set_slot(3)
        agent.place(BACK)
        agent.move(FORWARD, 1)
        if (i % 2):
            agent.move(RIGHT, 1)
            agent.set_slot(1)
            agent.place(RIGHT)
            for j in range (int(notes_str[i])):
                agent.interact(RIGHT)
            agent.move(LEFT, 1)
            agent.turn_right()
            agent.set_slot(2)
            agent.place(FORWARD)
            agent.turn_left()
        else:
            agent.move(LEFT, 1)
            agent.set_slot(1)
            agent.place(LEFT)
            for j in range (int(notes_str[i])):
                agent.interact(LEFT)
            agent.move(RIGHT, 1)
            agent.turn_left()
            agent.set_slot(2)
            agent.place(FORWARD)
            agent.turn_right()
    
    for i in range(2):
        agent.set_slot(3)
        agent.place(BACK)
        agent.move(FORWARD, 1)


player.on_chat("music", on_chat)