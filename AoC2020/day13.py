
input = """1003240
19,x,x,x,x,x,x,x,x,41,x,x,x,37,x,x,x,x,x,787,x,x,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,29,x,571,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17""".splitlines(False)


test_input = """939
7,13,x,x,59,x,31,19""".splitlines(False)


test_input2 = """939
67,7,59,61""".splitlines(False)
test_input3 = """939
67,x,7,59,61""".splitlines(False)
test_input4 = """939
67,7,x,59,61""".splitlines(False)
test_input5 = """939
1789,37,47,1889""".splitlines(False)


def part1(data_input):
    timestamp = int(data_input[0])
    busses = data_input[1].strip().split(',')
    busses = [int(i) for i in busses if i != "x"]

    diffs = {}
    min_dif = (max(busses), max(busses))
    for bus in busses:
        rounds = int((timestamp + bus) / bus)
        diff_time = (bus * rounds) - timestamp
        diffs[bus] = timestamp % bus
        if diff_time < min_dif[1]:
            min_dif = bus, diff_time

    print('min', min_dif, min_dif[0]*min_dif[1])


def part2(data_input):
    busses = data_input[1].strip().split(',')
    bus_ts = {int(busses[i]): i % int(busses[i]) for i in range(len(busses)) if busses[i] != "x"}
    bus_ids = [int(i) for i in busses if i != "x"]

    print(bus_ts)

    same_time = [k for k, v in bus_ts.items() if v == bus_ids[0]]
    same_time.append(bus_ids[0])
    print(same_time)

    lcm = 9973651  # LCM of 19, 23, 29, and 787; can be calculated with numpy.lcm.reduce(same_time)

    timestamp = lcm * 10000
    while True:
        temp_timestamp = timestamp - bus_ids[0]
        found = True
        for bus in bus_ids:
            if (temp_timestamp + bus_ts[bus]) % bus != 0:
                found = False
                break

        if found:
            timestamp = temp_timestamp
            break
        timestamp += lcm

    print(timestamp)


if __name__ == "__main__":
    data = input
    part1(data)
    part2(data)
