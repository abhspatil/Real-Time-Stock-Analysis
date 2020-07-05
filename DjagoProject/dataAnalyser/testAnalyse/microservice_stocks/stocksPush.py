import subprocess

subprocess.run("python3 aapl.py & python3 amzn.py & python3 gogl.py & python3 msft.py", shell=True)