from collections import deque

class Module:
    def __init__(self, name, type, outputs):
        self.name = name
        self.type = type
        self.outputs = outputs

        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}

    def __repr__(self):
        return self.name + "{type=" + self.type + ", outputs=" + ",".join(self.outputs) + ", memory=" + str(self.memory) + "}"
    

modules = {}

broadcast_targets = []

with open("input.txt") as file:
    for line in file:
        left, right = line.strip().split(" -> ")
        outputs = right.split(", ")
        if left == "broadcaster":
            broadcast_targets = right.split(".")
        else:
            type = left[0]
            name = left[1:]
            modules[name] = Module(name, type, outputs)

for name, module in modules.items():
    for output in module.outputs:
        if output in modules and modules[output].type == "&":
            modules[output].memory[name] = "low"

low_pulse = high_pulse = 0

for _ in range(1000):
    low_pulse += 1

    #origin, target, pulse
    q = deque([("broadcaster", x, "low") for x in broadcast_targets])

    while q:
        origin, target, pulse = q.popleft()
        
        if pulse == "low":
            low_pulse += 1
        else:
            high_pulse += 1
        
        if target not in modules:
            continue
            
        module = modules[target]

        if module.type == "%":
            if pulse == "low":
                module.memory = "on" if module.memory == "off" else "off"
                out_pulse = "high" if module.memory == "on" else "low"
                for x in module.outputs:
                    q.append((module.name, x, ))
        
        else:
            module.memory[origin] = pulse
            out_pulse = "low" if all(x == "high" for x in module.memory.values()) else "high"
            for x in module.outputs:
                q.append((module.name, x, out_pulse))

print(low_pulse * high_pulse)