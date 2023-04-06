import json

def consumption(cpu, mem):
    print("cpu: ", cpu, " mem: ", mem)
    with open('data.txt', 'r') as f:
        data_str = f.read()

    data = json.loads(data_str)

    if cpu > data["maxCPU"]:
        data["maxCPU"] = cpu
    if cpu < data["minCPU"]:
        data["minCPU"] = cpu

    if mem > data["maxMEM"]:
        data["maxMEM"] = mem
    if mem < data["minMEM"]:
        data["minMem"] = mem

    data["avgCPU"] = (data["avgCPU"] * data["requests"] + cpu) / (data["requests"] + 1)
    data["avgMEM"] = (data["avgMEM"] * data["requests"] + mem) / (data["requests"] + 1)
    data["requests"] += 1

    with open('data.txt', 'w') as f:
        f.write(json.dumps(data))         