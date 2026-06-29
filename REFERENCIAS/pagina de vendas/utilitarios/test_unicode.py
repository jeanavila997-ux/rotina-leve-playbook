import os

parent = r"c:\Users\jeanc_pmc3uv0\Documents"
for name in os.listdir(parent):
    if "curso" in name.lower():
        print(f"Name: {repr(name)}")
        print(f"Bytes (utf-8): {list(name.encode('utf-8'))}")
        # Test if we can list it
        path = os.path.join(parent, name)
        try:
            print("Listing of subfolder:", os.listdir(path))
        except Exception as e:
            print("Listing error:", e)
