import markdown


def convert_md_to_html(md_file_path):
    with open(md_file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()
        html_content = markdown.markdown(md_content, extensions=['tables'])
        return html_content

# Ruta al archivo README.md
# readme_file = 'README.md'

# Convertir el archivo Markdown a HTML
# html = convert_md_to_html(readme_file)

# Imprimir el contenido HTML resultante
# print(html)
