import zipfile
import os

zip_path = r"c:\Users\jeanc_pmc3uv0\Documents\curso - THIAGO\FRAMEWORK COMPLETO PARA CRIAÇÃO DE PÁGINAS DE VENDAS.zip"
revised_path = r"C:\Users\jeanc_pmc3uv0\.gemini\antigravity-ide\brain\2a7ee7e4-127f-4334-87a5-87484b5e0d3c\FRAMEWORK COMPLETO PARA CRIAÇÃO DE PÁGINAS DE VENDAS.md"

print(f"Zip exists: {os.path.exists(zip_path)}")
print(f"Revised file exists: {os.path.exists(revised_path)}")

try:
    # Read the revised content
    with open(revised_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to replace the file inside the zip.
    # To do this safely, we can open the zip in append mode ('a') or read all, recreate.
    # Since zipfile supports writing a new file which will overwrite or append (if same name, the last one is read by default, but it's cleaner to rewrite the zip).
    # Let's see if we can open in append mode first.
    with zipfile.ZipFile(zip_path, 'a') as z:
        # Get the exact filename in the zip (decomposed unicode)
        # The exact name is 'FRAMEWORK COMPLETO PARA CRIAÇÃO DE PÁGINAS DE VENDAS.md'
        # Let's list the entries first
        entries = z.namelist()
        print("Zip entries before:", entries)
        
        # Let's write the new content under the exact decomposed name
        decomposed_name = entries[0]
        z.writestr(decomposed_name, content.encode('utf-8'))
        print("Successfully wrote to ZIP entry:", decomposed_name)
        
    with zipfile.ZipFile(zip_path, 'r') as z:
        print("Zip entries after:", z.namelist())
except Exception as e:
    print("Error updating ZIP:", e)
