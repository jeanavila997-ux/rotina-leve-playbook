import os

parent = r"c:\Users\jeanc_pmc3uv0\Documents"
target = os.path.join(parent, "test_write_doc.txt")
print("Target:", target)

try:
    with open(target, "w") as f:
        f.write("test")
    print("SUCCESS writing to parent Documents!")
    os.remove(target)
except Exception as e:
    print("FAILED writing to parent Documents:", e)
