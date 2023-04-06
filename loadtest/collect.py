import json
import os

file_name = "loadtest_data.txt"
file_path = os.path.abspath(file_name)

def consumption(cpu, mem):
    print("cpu: ", cpu, " mem: ", mem)
    with open(file_path, 'r') as f:
        data_str = f.read()

    data = json.loads(data_str)

    if data["minCPU"] == 0:
        data["minCPU"] = cpu
    if data["minMEM"] == 0:
        data["minMEM"] = mem

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

    with open(file_path, 'w') as f:
        f.write(json.dumps(data))         