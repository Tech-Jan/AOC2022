from filereader import readfile
import typing as t

input = readfile("input")

cycle = 0
value = 1
myvalue = 0
sum_myvalue = 0
crt = []
for i in range(0, 40):
    crt.append(".")
crt[0:3] = "#", "#", "#"


def addx(processor_state):
    processor_state["needed_cycle"] = 2
    command = input[processor_state["command_position"]]
    processor_state["commanddata"] = int(command[5:])


def noop(processor_state):
    processor_state["needed_cycle"] = 1
    processor_state["commanddata"] = 0


def cycle_less20():
    global bla
    bla = cyclemod40
    pass


def cyclemod40():
    pass


bla = cycle_less20


def crt_screen(processor_state):
    # print(processor_state["crt_signal"])
    processor_state["crt"].append(processor_state["crt_signal"][processor_state["run_cycle"] % 40 - 1])
    # print( f'{processor_state["crt"]}')

    if processor_state["run_cycle"] % 40 == 0:
        print(f'asd {processor_state["crt"]}')
        processor_state["crt"] = []


def cycle(processor_state):
    processor_state["current_cycle"] += 1
    processor_state["run_cycle"] += 1
    crt_screen(processor_state)


def crt_signal(processor_state):
    crt = []
    for i in range(0, 40):
        crt.append(".")
    processor_state["crt_signal"] = crt
    processor_state["regx"] += processor_state["commanddata"]
    poslow = (processor_state["regx"] - 1) % 40
    posmid = (processor_state["regx"]) % 40
    poshigh = (processor_state["regx"] + 1) % 40
    processor_state["crt_signal"][poslow] = "#"
    processor_state["crt_signal"][posmid] = "#"
    processor_state["crt_signal"][poshigh] = "#"


def execute(processor_state):
    if processor_state["current_cycle"] == processor_state["needed_cycle"]:
        crt_signal(processor_state)
        processor_state["current_cycle"] = 0
        processor_state["command_position"] += 1
        processor_state["running_command"] = False
    else:
        pass


def fetch_command(processor_state: t.Dict) -> t.Optional[t.Callable]:
    if not processor_state["running_command"]:
        command = input[processor_state["command_position"]]
        processor_state["running_command"] = True
        return commands.get(command[0:4])
    return None


def signal(processor_state):
    cycle = processor_state["run_cycle"]
    if (cycle - 20) % 40 == 0 or cycle == 20:
        processor_state["signal_strength"] = cycle * processor_state["regx"]
        processor_state["signal_sum"] += processor_state["signal_strength"]


commands = {
    "addx": addx,
    "noop": noop,
}

processor_state = {
    "regx": 1,
    "current_cycle": 0,
    "needed_cycle": 0,
    "run_cycle": 0,
    "commanddata": None,
    "command_position": 0,
    "running_command": False,
    "signal_strength": 0,
    "signal_sum": 0,
    "crt_signal": crt,
    "crt": []
}

while processor_state["command_position"] < len(input):
    exe = fetch_command(processor_state)
    if exe is not None:
        exe(processor_state)
    signal(processor_state)
    execute(processor_state)
    cycle(processor_state)

print(processor_state["signal_sum"])
