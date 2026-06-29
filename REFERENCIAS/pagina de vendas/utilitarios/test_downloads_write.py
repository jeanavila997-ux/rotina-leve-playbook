import os

paths = [
    r"c:\Users\jeanc_pmc3uv0\Downloads",
    r"c:\Users\jeanc_pmc3uv0\Desktop",
    r"c:\Users\jeanc_pmc3uv0\Projetos",
]

for p in paths:
    print(f"Checking path: {p}")
    print(f" - Exists: {os.path.exists(p)}")
    if os.path.exists(p):
        file_path = os.path.join(p, "test_write.txt")
        try:
            with open(file_path, "w") as f:
                f.write("hello")
            print(" - SUCCESS writing to:", file_path)
            os.remove(file_path)
        except Exception as e:
            print(" - FAILED writing to:", file_path)
            print("   Error:", e)
