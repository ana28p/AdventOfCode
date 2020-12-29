input = """105
124
42
52
71
41
1
85
148
90
155
112
35
134
145
39
161
160
34
54
15
165
8
20
46
49
108
151
60
7
48
154
63
147
132
98
158
33
137
45
140
121
22
62
111
141
167
131
74
93
2
142
113
21
162
61
3
19
101
9
102
115
70
12
84
6
114
107
97
133
64
80
78
91
79
14
168
87
159
30
94
77
40
125
47
27
38
166
86
26
23
67
127
28
16
169
13
92
106
57
118
126
83
146
29
130
53""".splitlines(False)

test_input = """16
10
15
5
1
11
7
19
6
12
4""".splitlines(False)
test_input1 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".splitlines(False)


def create_dict_of_possible_choices(values, start):
    d_choices = {}
    # start with rating
    # the data is sorted; check the next 3 nrs for +1, 2, 3
    next_nr = [nr for nr in values if start < nr <= start + 3]
    d_choices[start] = set(next_nr)
    for i in range(len(values) - 1):
        v = values[i]
        max_next_i = (i + 4) if (i+4) <= len(values) else len(values)
        next_nr = [nr for nr in values[i+1: max_next_i] if v < nr <= v + 3]
        d_choices[v] = set(next_nr)
    return d_choices


def visit_adapters(choices, highest_r, adapter, chain_visit):
    if adapter not in choices:
        if adapter + 3 <= highest_r:
            chain_visit.append(adapter)
        return chain_visit

    chain_opt = choices[adapter]
    for opt in chain_opt:
        chain_visit.append(adapter)
        chain_visit = visit_adapters(choices, highest_r, opt, chain_visit)
        if chain_visit.sort() == list(choices.keys()).sort():
            return chain_visit
    return chain_visit


counter = 0


def count_arrangements(choices, highest_r, adapter):
    if adapter not in choices:
        if highest_r - 3 <= adapter + 3 <= highest_r:
            global counter
            counter += 1
    else:
        chain_opt = choices[adapter]
        for opt in chain_opt:
            count_arrangements(choices, highest_r, opt)


def count_arrangements2(choices, highest_r, adapter, c):
    if adapter not in choices:
        if highest_r - 3 <= adapter + 3 <= highest_r:
            return c+1
        return 0

    chain_opt = choices[adapter]
    for opt in chain_opt:
        c = count_arrangements2(choices, highest_r, opt, c)
    return c


def part1(data_input):
    rating = 0
    data_input.sort()
    high_r = data_input[-1] + 3
    chains = create_dict_of_possible_choices(data_input, rating)

    vis = visit_adapters(chains, high_r, rating, [])
    vis.append(high_r)
    diffs = {}
    for i in range(1, len(vis)):
        dif = vis[i] - vis[i-1]
        if dif in diffs:
            diffs[dif] += 1
        else:
            diffs[dif] = 1
    print(diffs)


def part2(data_input):
    rating = 0
    data_input.sort()
    high_r = data_input[-1] + 3
    chains = create_dict_of_possible_choices(data_input, rating)

    print(count_arrangements2(chains, high_r, rating, 0))
    # print(counter)


if __name__ == "__main__":
    data = input
    data = [int(i) for i in data]
    part1(data)
    part2(data)

