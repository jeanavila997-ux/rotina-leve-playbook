import zipfile
import os

zip_path = r"c:\Users\jeanc_pmc3uv0\Documents\curso - THIAGO\FRAMEWORK COMPLETO PARA CRIAÇÃO DE PÁGINAS DE VENDAS.zip"
out_dir = r"c:\Users\jeanc_pmc3uv0\Documents\curso - THIAGO"

try:
    with zipfile.ZipFile(zip_path, 'r') as z:
        for name in z.namelist():
            print("Zip member name:", repr(name))
            print("Zip member bytes:", list(name.encode('utf-8')))
            
            # Let's try writing to this exact name in the workspace!
            target = os.path.join(out_dir, name)
            print("Target path:", repr(target))
            try:
                # Read content from the zip member or write a dummy string
                with open(target, "w", encoding="utf-8") as f:
                    f.write("test")
                print("SUCCESS writing to exact zip filename path!")
                os.remove(target)
            except Exception as e:
                print("FAILED writing to exact zip filename path:", e)
except Exception as e:
    print("Error:", e)
