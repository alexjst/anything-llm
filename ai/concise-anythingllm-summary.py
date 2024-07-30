import os
import ast
import json
import re
from typing import Any
import yaml
from dotenv import dotenv_values

def read_file(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

def summarize_python_file(content: str) -> str:
    tree = ast.parse(content)
    summary = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            summary.append(f"Function: {node.name}")
            if ast.get_docstring(node):
                summary.append(f"  Docstring: {ast.get_docstring(node)}")
        elif isinstance(node, ast.ClassDef):
            summary.append(f"Class: {node.name}")
            if ast.get_docstring(node):
                summary.append(f"  Docstring: {ast.get_docstring(node)}")
    return '\n'.join(summary)

def summarize_javascript_file(content: str) -> str:
    summary = []
    # Function declarations
    functions = re.findall(r'function\s+(\w+)', content)
    for func in functions:
        summary.append(f"Function: {func}")

    # Arrow functions assigned to variables
    arrow_funcs = re.findall(r'(const|let|var)\s+(\w+)\s*=\s*(\([^)]*\))?\s*=>', content)
    for _, func, _ in arrow_funcs:
        summary.append(f"Function: {func}")

    # Class declarations
    classes = re.findall(r'class\s+(\w+)', content)
    for cls in classes:
        summary.append(f"Class: {cls}")

    # React components (assuming they're capitalized)
    components = re.findall(r'(const|let|var)\s+([A-Z]\w+)\s*=', content)
    for _, comp in components:
        summary.append(f"React Component: {comp}")

    return '\n'.join(summary)

def summarize_package_json(content: str) -> str:
    data = json.loads(content)
    summary = [
        f"Name: {data.get('name', 'N/A')}",
        f"Version: {data.get('version', 'N/A')}",
        "Dependencies:"
    ]
    for dep, version in data.get('dependencies', {}).items():
        summary.append(f"  - {dep}: {version}")
    return '\n'.join(summary)

def summarize_env_file(content: str) -> str:
    env_vars = dotenv_values(stream=content)
    summary = ["Environment Variables:"]
    for key, value in env_vars.items():
        summary.append(f"  - {key}: {value if value else '[EMPTY]'}")
    return '\n'.join(summary)

def summarize_docker_compose(content: str) -> str:
    data = yaml.safe_load(content)
    summary = ["Docker Compose Configuration:"]
    for service, config in data.get('services', {}).items():
        summary.append(f"Service: {service}")
        summary.append(f"  Image: {config.get('image', 'N/A')}")
        summary.append(f"  Ports: {', '.join(config.get('ports', []))}")
    return '\n'.join(summary)

def summarize_prisma_schema(content: str) -> str:
    models = re.findall(r'model (\w+) \{([^}]+)\}', content, re.DOTALL)
    summary = ["Prisma Schema Models:"]
    for model, fields in models:
        summary.append(f"Model: {model}")
        for field in fields.strip().split('\n'):
            summary.append(f"  {field.strip()}")
        summary.append("")
    return '\n'.join(summary)

def extract_api_endpoints(content: str) -> str:
    endpoints = re.findall(r'(app|router)\.(get|post|put|delete)\([\'"]([^\'"]+)[\'"]', content)
    if not endpoints:
        return ""
    summary = ["API Endpoints:"]
    for _, method, path in endpoints:
        summary.append(f"  {method.upper()} {path}")
    return '\n'.join(summary)

def process_file(file_path: str, output_file: Any) -> None:
    print(f"Processing: {file_path}")
    content = read_file(file_path)

    output_file.write(f"\n\n## File: {file_path}\n\n")

    if file_path.endswith('package.json'):
        output_file.write(summarize_package_json(content))
    elif file_path.endswith('.env.example'):
        output_file.write(summarize_env_file(content))
    elif file_path.endswith('docker-compose.yml'):
        output_file.write(summarize_docker_compose(content))
    elif file_path.endswith('schema.prisma'):
        output_file.write(summarize_prisma_schema(content))
    elif file_path.endswith('.py'):
        output_file.write(summarize_python_file(content))
    elif file_path.endswith(('.js', '.jsx')):
        output_file.write(summarize_javascript_file(content))
    elif file_path.endswith('.md'):
        output_file.write(content)
    else:
        output_file.write(f"File type not supported for detailed summary: {file_path}")

    if file_path.endswith(('.js', '.ts')) and '/endpoints/' in file_path:
        endpoints = extract_api_endpoints(content)
        if endpoints:
            output_file.write(f"\n\n{endpoints}")

def process_directory(directory: str, output_file: Any) -> None:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.js', '.jsx', '.ts', '.tsx', '.py', '.json', '.yml', '.yaml', '.env.example', 'schema.prisma')):
                file_path = os.path.join(root, file)
                process_file(file_path, output_file)

def summarize_directory(directory: str, output_file: Any, level: int = 0) -> None:
    items = sorted(os.listdir(directory))
    for i, item in enumerate(items):
        item_path = os.path.join(directory, item)
        is_last = (i == len(items) - 1)
        prefix = '└── ' if is_last else '├── '
        output_file.write('│   ' * level + prefix + item + '\n')
        if os.path.isdir(item_path):
            summarize_directory(item_path, output_file, level + 1)

def get_version_info() -> str:
    version = "Unknown"
    try:
        with open('package.json', 'r') as f:
            data = json.load(f)
            version = data.get('version', 'Unknown')
    except:
        pass
    return f"AnythingLLM Version: {version}"

def extract_readme_sections(content: str) -> str:
    sections = re.split(r'^#+\s+', content, flags=re.MULTILINE)[1:]
    summary = ["README Summary:"]
    for section in sections:
        lines = section.split('\n')
        title = lines[0].strip()
        summary.append(f"Section: {title}")
        summary.append(f"  {' '.join(lines[1:])[:200]}...")
    return '\n'.join(summary)

def main() -> None:
    important_files = [
        'README.md',
        'SECURITY.md',
        'docker-compose.yml',
        'package.json',
        'server/index.js',
        'frontend/src/App.jsx',
        'collector/index.js',
        'server/prisma/schema.prisma',
    ]

    important_dirs = [
        'server/utils',
        'server/models',
        'server/endpoints',
        'frontend/src/components',
        'frontend/src/pages',
        'collector/utils'
    ]

    with open('anythingllm_summary.md', 'w', encoding='utf-8') as output_file:
        output_file.write("# AnythingLLM Project Summary\n\n")
        output_file.write(get_version_info() + "\n\n")

        output_file.write("## Project Structure\n\n")
        output_file.write("```\n")  # Start of code block
        summarize_directory('.', output_file)
        output_file.write("```\n\n")  # End of code block

        for file in important_files:
            if os.path.exists(file):
                if file == 'README.md':
                    content = read_file(file)
                    output_file.write(extract_readme_sections(content))
                else:
                    process_file(file, output_file)

        for directory in important_dirs:
            if os.path.exists(directory):
                output_file.write(f"\n\n## Directory: {directory}\n\n")
                output_file.write("```\n")  # Start of code block
                summarize_directory(directory, output_file)
                output_file.write("```\n\n")  # End of code block
                process_directory(directory, output_file)

if __name__ == "__main__":
    main()

