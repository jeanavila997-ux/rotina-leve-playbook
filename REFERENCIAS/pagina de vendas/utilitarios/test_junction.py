import os
import subprocess

path = r"c:\Users\jeanc_pmc3uv0\Documents\curso - THIAGO"
print("os.path.islink:", os.path.islink(path))

# Run dir command in cmd to see if it is a junction or symlink
try:
    res = subprocess.run('dir "c:\\Users\\jeanc_pmc3uv0\\Documents"', shell=True, capture_output=True, text=True)
    print("cmd dir output:")
    print(res.stdout)
except Exception as e:
    print("cmd error:", e)
