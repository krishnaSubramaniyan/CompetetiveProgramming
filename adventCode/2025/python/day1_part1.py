key = 0
pointer = 50
with open("input.txt", 'r') as f:
    data = f.readline()
    while data:
        direction = data[0]
        rotation = int(data[1:])
        data = f.readline()

        if rotation>100:
            rotation %= 100

        if direction == 'L':
            pointer -= rotation
        else:
            pointer += rotation

        if pointer < 0:
            pointer += 100
        elif pointer >= 100:
            pointer -= 100

        if pointer == 0:
            key += 1

print(key)