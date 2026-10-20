def vacuum_agent(location, room_status):
    if room_status[location] == "Dirty":
        print(f"Room {location} is Dirty")
        print("ACTION: SUCK")
        room_status[location] = "Clean"
    else:
        if location == "A":
            print("Room A is Clean.")
            print("Action: Move Right To Room B")
            location = "B"
        else:
            print("Room B is Clean.")
            print("Action: Move Left To Room A")
            location = "A"

    return location, room_status


# Initial room status
room_status = {
    "A": "Dirty",
    "B": "Dirty"
}

location = "A"

while True:
    location, room_status = vacuum_agent(location, room_status)

    if room_status["A"] == "Clean" and room_status["B"] == "Clean":
        print("\nAll rooms are cleaned.")
        break

print("Final Room Status:", room_status)


OUTPUT : 



(base) ubuntu@ubuntu-hp-pro-sff-280-g9-desktop-pc:~/Desktop$ python vacuum.py
Room A is Dirty
ACTION: SUCK
Room A is Clean.
Action: Move Right To Room B
Room B is Dirty
ACTION: SUCK

All rooms are cleaned.
Final Room Status: {'A': 'Clean', 'B': 'Clean'}

