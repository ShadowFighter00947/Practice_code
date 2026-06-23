# Function to process the game events
def processGame(events, H):

    # Sort events according to frame number
    events.sort(key=lambda x: x[1])

    # Initialize both players' HP
    p1 = H
    p2 = H

    i = 0
    n = len(events)

    # Process all events
    while i < n:

        # Current frame being processed
        frame = events[i][1]

        # Process all attacks occurring in the same frame
        while i < n and events[i][1] == frame:

            player, _, damage = events[i]

            # Player 1 attacks Player 2
            if player == 1:
                p2 -= damage

            # Player 2 attacks Player 1
            else:
                p1 -= damage

            i += 1

        # Stop the game if any player's HP becomes 0 or less
        if p1 <= 0 or p2 <= 0:
            break

    # Return remaining HP (minimum value is 0)
    return [max(0, p1), max(0, p2)]


# Input starting HP for both players
H = int(input("Enter starting HP: "))

# Input number of attack events
n = int(input("Enter number of events: "))

events = []

# Take event details from user
for i in range(n):
    player = int(input("Player (1 or 2): "))
    frame = int(input("Frame: "))
    damage = int(input("Damage: "))

    # Store event as (player, frame, damage)
    events.append((player, frame, damage))

# Print final HP of both players
print(processGame(events, H))