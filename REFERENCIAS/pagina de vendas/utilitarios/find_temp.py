import os

base_temp = r"c:\Users\jeanc_pmc3uv0\AppData\Local\Temp"
print("Listing of base temp (filtered by 191ec1d9 or zip.739):")
try:
    for name in os.listdir(base_temp):
        if "191ec1d9" in name or "739" in name or "FRAMEWORK" in name:
            print(f"Found folder: {repr(name)}")
            print(f"Bytes: {list(name.encode('utf-8'))}")
            # Try to list inside it
            full_path = os.path.join(base_temp, name)
            print("Listing of subfolder:", os.listdir(full_path))
except Exception as e:
    print("Error:", e)
