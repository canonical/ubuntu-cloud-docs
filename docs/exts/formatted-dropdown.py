from __future__ import annotations
from docutils import nodes
from docutils.parsers.rst import Directive
import re
import json

OPTION_LINE_RE = re.compile(r"^:(?P<key>\w+):\s*(?P<values>.+)$")
VALUE_RE = re.compile(r"^(?P<val>[^{}]+)(?:{(?P<conds>[^}]+)})?$")


class FormattedDropdownNode(nodes.General, nodes.Element):
    pass


class FormattedDropdownDirective(Directive):
    required_arguments = 1
    final_argument_whitespace = True

    def parse_value(self, raw: str):
        """
        Parse value strings like:
        ebs-gp3{release:noble}
        """
        m = VALUE_RE.match(raw.strip())
        if not m:
            return {"value": raw.strip(), "conditions": {}}

        value = m.group("val").strip()
        conds = m.group("conds")
        if not conds:
            return {"value": value, "conditions": {}}

        cond_map = {}
        for cond in conds.split(","):
            cond = cond.strip()
            if not cond:
                continue
            if ":" not in cond:
                continue
            key, val = cond.split(":", 1)
            cond_map.setdefault(key.strip(), []).append(val.strip())

        return {"value": value, "conditions": cond_map}

    def run(self):
        fmt = self.arguments[0].splitlines()[0]
        raw = self.arguments[0].splitlines()[1:]

        opts = {}
        for line in raw:
            m = OPTION_LINE_RE.match(line.strip())
            if not m:
                continue
            key = m.group("key")

            raw_values = [v.strip() for v in m.group("values").split(",")]
            parsed = [self.parse_value(v) for v in raw_values]
            opts[key] = parsed

        node = FormattedDropdownNode()
        node["format"] = fmt
        node["options"] = opts
        return [node]


def visit_formatted_dropdown_html(self, node):
    fmt = node["format"]
    opts = node["options"]

    placeholders = re.findall(r"{(\w+)}", fmt)

    fields_html = ""
    for key in placeholders:
        html_options = "".join(
            f"<option value='{v['value']}'>{v['value']}</option>"
            for v in opts.get(key, [])
        )

        fields_html += f"""
        <div class="dropdown-field" data-field="{key}">
            <select class="dropdown-select" data-key="{key}">
                {html_options}
            </select>
        </div>
        """

    html = f"""
<div class="dropdown-widget"
     data-options='{json.dumps(opts)}'
     data-format="{fmt}">
    <div class="dropdown-controls">
        {fields_html}
    </div>

    <div class="dropdown-code">
        <code class="dropdown-output-text">{fmt}</code>
        <button class="dropdown-copy">Copy</button>
    </div>
</div>
"""
    self.body.append(html)


def depart_formatted_dropdown_html(self, node):
    pass


def visit_dummy(self, node):
    self.body.append("[formatted dropdown not available]")

def depart_dummy(self, node):
    pass


def setup(app):
    app.add_node(
        FormattedDropdownNode,
        html=(visit_formatted_dropdown_html, depart_formatted_dropdown_html),
        latex=(visit_dummy, depart_dummy),
        text=(visit_dummy, depart_dummy),
    )
    app.add_directive("formatted-dropdown", FormattedDropdownDirective)

    app.add_css_file("css/formatted-dropdown.css")
    app.add_js_file("js/formatted-dropdown.js")
    return {"version": "1.1", "parallel_read_safe": True}
