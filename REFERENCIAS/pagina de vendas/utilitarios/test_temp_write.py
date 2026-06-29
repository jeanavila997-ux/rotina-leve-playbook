import os

temp_dir = r"c:\Users\jeanc_pmc3uv0\AppData\Local\Temp\191ec1d9-77a1-4c74-bd7c-47f0e2555739_FRAMEWORK COMPLETO PARA CRIAÇÃO DE PÁGINAS DE VENDAS.zip.739"
print("Temp dir exists:", os.path.exists(temp_dir))
if os.path.exists(temp_dir):
    print("Files in temp dir:", os.listdir(temp_dir))
    target = os.path.join(temp_dir, "FRAMEWORK COMPLETO PARA CRIAÇÃO DE PÁGINAS DE VENDAS.md")
    print("Target exists:", os.path.exists(target))
    try:
        with open(target, "w", encoding="utf-8") as f:
            f.write("test")
        print("Success writing to temp target!")
    except Exception as e:
        print("Error writing to temp target:", e)
else:
    # Let's search Temp directory for any directory starting with 191ec1d9-77a1-4c74-bd7c-47f0e2555739
    base_temp = r"c:\Users\jeanc_pmc3uv0\AppData\Local\Temp"
    try:
        found = []
        for x in os.listdir(base_temp):
            if "191ec1d9" in x or "FRAMEWORK" in x:
                found.append(x)
        print("Found matching temp folders:", found)
    except Exception as e:
        print("Error listing base temp:", e)
