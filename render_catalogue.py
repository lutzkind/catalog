import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
TEMPLATE_PATH = BASE_DIR / "catalogue.template.html"
OUTPUT_PATH = BASE_DIR / "catalogue.html"
VARIABLES_PATH = BASE_DIR / "variables.json"


def load_variables(path: Path) -> dict:
    with path.open(encoding="utf-8") as fp:
        return json.load(fp)


def render_template(template: str, variables: dict) -> str:
    pattern = re.compile(r"{{\s*([a-zA-Z0-9_]+)\s*}}")

    def replace(match: re.Match) -> str:
        key = match.group(1).strip()
        if key not in variables:
            raise KeyError(f"Missing variable: {key}")
        return str(variables[key])

    return pattern.sub(replace, template)


def main() -> None:
    template_text = TEMPLATE_PATH.read_text(encoding="utf-8")
    variables = load_variables(VARIABLES_PATH)
    rendered = render_template(template_text, variables)
    OUTPUT_PATH.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
