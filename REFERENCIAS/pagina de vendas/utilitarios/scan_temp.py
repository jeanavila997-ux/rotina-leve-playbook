import os

base_temp = r"c:\Users\jeanc_pmc3uv0\AppData\Local\Temp"
print("Scanning base temp for any part of name...")
matches = []
try:
    for root, dirs, files in os.walk(base_temp):
        depth = root[len(base_temp):].count(os.sep)
        if depth > 2:
            continue
        for d in dirs:
            if "FRAMEWORK" in d.upper() or "CRIAC" in d.upper():
                matches.append(os.path.join(root, d))
        for f in files:
            if "FRAMEWORK" in f.upper() or "CRIAC" in f.upper():
                matches.append(os.path.join(root, f))
except Exception as e:
    print("Error scanning:", e)

print(f"Found {len(matches)} matches:")
for m in matches[:20]:
    print(" -", repr(m))
