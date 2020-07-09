import json
import subprocess
import sys

NUM_TRIALS = 100

cmd = sys.argv[1]

result = {
    "real" : {
        "total" : 0,
        "average" : 0,
        "min" : 999,
        "max" : 0,
    },
    "user" : {
        "total" : 0,
        "average" : 0,
        "min" : 999,
        "max" : 0,
    },
    "sys" : {
        "total" : 0,
        "average" : 0,
        "min" : 999,
        "max" : 0,
    },
}

for _ in range(NUM_TRIALS):
    output = subprocess.run(f'time {cmd}', shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    output_array = output.stdout.decode().strip().split('\n')

    # check function
    if output_array[0] != "39088169":
        print("error in fib function")
        exit(1)

    for output_line in output_array[2:]:
        data_array = output_line.split('\t')

        # real / user / sys
        name = data_array[0]
        # time
        num = float(data_array[1][data_array[1].find("m")+1:len(data_array[1])-1])

        # total
        result[name]["total"] += num

        # min
        if result[name]["min"] > num:
            result[name]["min"] = num

        # max
        if result[name]["max"] < num:
            result[name]["max"] = num

result["real"]["average"] = "{:.3f}".format(result["real"]["total"] / NUM_TRIALS)
result["user"]["average"] = "{:.3f}".format(result["user"]["total"] / NUM_TRIALS)
result["sys"]["average"] = "{:.3f}".format(result["sys"]["total"] / NUM_TRIALS)

#print("{}".format(json.dumps(result,indent=4)))

#print(f"| | real | | | user | | | sys | | |")
#print(f"| | average | min | max | average | min | max | average | min | max |")
print(f"| | {result['real']['average']} | {result['real']['min']} | {result['real']['max']} | {result['user']['average']} | {result['user']['min']} | {result['user']['max']} | {result['sys']['average']} | {result['sys']['min']} | {result['sys']['max']} |")


