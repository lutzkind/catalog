import argparse
import json
import re
from pathlib import Path

PLACEHOLDER_PATTERN = re.compile(r"{{\s*([A-Za-z0-9_]+)\s*}}")


def render_template(template_path: Path, variables_path: Path, output_path: Path) -> None:
    variables = json.loads(variables_path.read_text(encoding="utf-8"))
    template = template_path.read_text(encoding="utf-8")

    def replace(match: re.Match) -> str:
        key = match.group(1)
        if key not in variables:
            raise KeyError(f"Missing value for placeholder '{key}' in {variables_path}")
        return str(variables[key])

    rendered = PLACEHOLDER_PATTERN.sub(replace, template)

    remaining = PLACEHOLDER_PATTERN.findall(rendered)
    if remaining:
        missing = ", ".join(sorted(set(remaining)))
        raise KeyError(f"Unreplaced placeholders after render: {missing}")

    output_path.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Render the catalogue template with values from variables.json")
    parser.add_argument("--template", type=Path, default=Path("catalogue.template.html"), help="Path to the template HTML file")
    parser.add_argument("--variables", type=Path, default=Path("variables.json"), help="Path to the JSON variables file")
    parser.add_argument("--output", type=Path, default=Path("catalogue.html"), help="Where to write the rendered HTML")

    args = parser.parse_args()
    render_template(args.template, args.variables, args.output)
