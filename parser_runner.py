import subprocess
import time

NUMRUNS = 20

commands = [
    "python log_parser.py",
    "perl log_parser.pl", 
    "powershell -file log_parser.ps1"
]

def run_command(command):
    start = time.time()
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    end = time.time()
    execution_time = end-start

    return result.stdout, execution_time

run_times = {"python":[], "perl":[], "powershell":[]}
for run_count in range(NUMRUNS):
    for count, command in enumerate(commands):
        result, time_to_exe = run_command(command)

        if count == 0:
            run_times["python"].append(time_to_exe)
        elif count == 1:
            run_times["perl"].append(time_to_exe)
        elif count == 2:
            run_times["powershell"].append(time_to_exe)


python_avg = sum(run_times["python"])/len(run_times["python"])
perl_avg = sum(run_times["perl"])/len(run_times["perl"])
powershell_avg = sum(run_times["powershell"])/len(run_times["powershell"])

print(f"The below averages are the results of {NUMRUNS} executions of each script")
print(f"Python: {round(python_avg, 2)}")
print(f"Perl: {round(perl_avg, 2)}")
print(f"Powershell: {round(powershell_avg, 2)}")





