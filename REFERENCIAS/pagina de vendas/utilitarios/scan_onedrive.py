import os

onedrive = r"C:\Users\jeanc_pmc3uv0\OneDrive"
print("OneDrive exists:", os.path.exists(onedrive))
if os.path.exists(onedrive):
    try:
        print("OneDrive contents:")
        for item in os.listdir(onedrive):
            print(" -", item)
    except Exception as e:
        print("Error listing OneDrive:", e)
