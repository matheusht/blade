import os

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return

    original_content = content
    
    # Generic replacements to restore code integrity
    content = content.replace('estilosheet', 'stylesheet')
    content = content.replace('ESTILOSHEET', 'STYLESHEET')
    content = content.replace('estilo', 'style')
    content = content.replace('ESTILO', 'STYLE')
    content = content.replace('estilos', 'styles')
    content = content.replace('ESTILOS', 'STYLES')

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

def main():
    dirs_to_check = ['public', 'dist', 'src', '.']
    for d in dirs_to_check:
        if not os.path.exists(d):
            continue
        for root, _, files in os.walk(d):
            if 'node_modules' in root or '.git' in root:
                continue
            for file in files:
                if file.endswith('.mjs') or file.endswith('.js') or file.endswith('.html'):
                    process_file(os.path.join(root, file))

if __name__ == '__main__':
    main()
