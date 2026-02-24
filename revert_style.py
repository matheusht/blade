import os

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return

    original_content = content
    # Revert technical/common patterns that should definitely be "style"
    content = content.replace('<estilo', '<style')
    content = content.replace('</estilo', '</style')
    content = content.replace('estilo=', 'style=')
    content = content.replace('ESTILO=', 'STYLE=')
    content = content.replace('font-estilo', 'font-style')
    content = content.replace('estilo-property', 'style-property') # some common ones
    content = content.replace('list-estilo', 'list-style')
    content = content.replace('border-estilo', 'border-style')
    content = content.replace('outline-estilo', 'outline-style')
    content = content.replace('transition-property:estilo', 'transition-property:style')
    content = content.replace('transition-property: estilo', 'transition-property: style')
    content = content.replace('estilo:', 'style:') # likely in CSS/JS
    content = content.replace('ESTILO:', 'STYLE:')
    
    # Also just generic "estilo" to "style" in scripts and head
    # But wait, let's be more aggressive and then re-translate
    # Re-run the translation scripts will fix the user-facing ones.
    content = content.replace(' estilo ', ' style ')
    content = content.replace('"estilo"', '"style"')
    content = content.replace("'estilo'", "'style'")
    content = content.replace('`estilo`', '`style`')

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
