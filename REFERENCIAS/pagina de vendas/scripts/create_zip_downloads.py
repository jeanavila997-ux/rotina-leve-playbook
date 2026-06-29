import zipfile
import os

revised_path = r"C:\Users\jeanc_pmc3uv0\.gemini\antigravity-ide\brain\2a7ee7e4-127f-4334-87a5-87484b5e0d3c\FRAMEWORK COMPLETO PARA CRIAÇÃO DE PÁGINAS DE VENDAS.md"
out_zip = r"c:\Users\jeanc_pmc3uv0\Downloads\FRAMEWORK COMPLETO PARA CRIAÇÃO DE PÁGINAS DE VENDAS.zip"

try:
    with zipfile.ZipFile(out_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        # Use the exact filename form for the ZIP entry: 'FRAMEWORK COMPLETO PARA CRIAÇÃO DE PÁGINAS DE VENDAS.md'
        # Let's write the entry
        z.write(revised_path, arcname="FRAMEWORK COMPLETO PARA CRIAÇÃO DE PÁGINAS DE VENDAS.md")
    print(f"SUCCESS! Created ZIP at {out_zip}")
    print(f"ZIP size: {os.path.getsize(out_zip)} bytes")
except Exception as e:
    print(f"FAILED to create ZIP: {e}")
