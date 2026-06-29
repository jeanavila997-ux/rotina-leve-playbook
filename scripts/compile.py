import os
import re

def compile_playbook():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    chapters_dir = os.path.normpath(os.path.join(base_dir, '..', 'content', 'playbook'))
    output_file = os.path.normpath(os.path.join(base_dir, '..', 'content', 'playbook.md'))

    if not os.path.exists(chapters_dir):
        print(f"Diretório {chapters_dir} não existe.")
        return

    # Encontra e ordena todos os arquivos md
    files = [f for f in os.listdir(chapters_dir) if f.endswith('.md')]
    
    # Ordenação natural por número
    def extract_number(filename):
        match = re.match(r'^(\d+)', filename)
        return int(match.group(1)) if match else 999

    files.sort(key=extract_number)

    content = []
    
    # Adicionar metadados/introdução base se houver
    intro_path = os.path.join(chapters_dir, '00_intro.txt')
    if os.path.exists(intro_path):
        with open(intro_path, 'r', encoding='utf-8') as f:
            content.append(f.read())
    else:
        content.append("# Rotina Leve\n\n## Playbook Anti-Procrastinação para Mentes Aceleradas\n")

    for file in files:
        filepath = os.path.join(chapters_dir, file)
        print(f"Compilando: {file}")
        with open(filepath, 'r', encoding='utf-8') as f:
            file_content = f.read().strip()
            if file_content:
                content.append(file_content)

    # Junta tudo com separador de página (---)
    compiled_text = "\n\n---\n\n".join(content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(compiled_text)
    
    print(f"Ebook compilado com sucesso em: {output_file}")

if __name__ == "__main__":
    compile_playbook()
