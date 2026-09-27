#!/usr/bin/env python3
"""Render README*.md from README.template*.md and the JSON files in data/ (one pass per language)."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
UTM_BASE = "utm_source=github&utm_medium=repo&utm_campaign=2026-09-nsfw-ai-image-prompts"
LANGS = ["", "ja", "ko", "fr", "es"]
LANG = ""          # set per render pass
I18N: dict = {}    # data/i18n/<lang>.json for the current pass
TASK_ABBR = {"text-to-image": "T2I", "edit": "Edit"}


def L(key: str, default: str) -> str:
    return I18N.get("labels", {}).get(key, default)


def site(path: str, content: str) -> str:
    prefix = f"/{LANG}" if LANG else ""
    suffix = f"-{LANG}" if LANG else ""
    return f"https://spicyapi.ai{prefix}{path}?{UTM_BASE}&utm_content={content}{suffix}"


def load(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def anchor(title: str) -> str:
    slug = title.strip().lower()
    slug = re.sub(r"[^\w\- ]", "", slug)
    return slug.replace(" ", "-")


def money(value: float) -> str:
    text = f"{value:.5f}".rstrip("0").rstrip(".")
    if "." in text and len(text.split(".")[1]) == 1:
        text += "0"
    return f"${text}"


def model_link(model: dict, content: str) -> str:
    return f"[{model['name']}]({site('/models/' + model['page'], content)})"


def freedom_cell(fam: dict) -> tuple[str, str]:
    lb = fam.get("leaderboard") or {}
    si, fr = lb.get("spicy_index"), lb.get("freedom")
    si_txt = f"{si:g}" if isinstance(si, (int, float)) else "—"
    if not isinstance(fr, (int, float)):
        return si_txt, "—"
    if (lb.get("freedom_runs") or 0) < 15:
        mark = "🧪"
    else:
        mark = "✅" if fr >= 90 else ("◐" if fr >= 70 else "⚠️")
    return si_txt, f"{mark} {fr:g}"


def render_model_table(catalog: dict) -> str:
    head = (f"| {L('col_model', 'Model')} | {L('col_type', 'Type')} | {L('col_tasks', 'Tasks')} | "
            f"{L('col_from', 'From')} | Spicy Index | Freedom |")
    rows = [head, "|---|---|---|---|---|---|"]
    for fam in catalog["families"]:
        if fam["modality"] != "image":
            continue
        ep = min(fam["endpoints"], key=lambda e: e["from"])
        price = money(ep["from"]) + "/" + L("image_unit", "image")
        tasks = ", ".join(dict.fromkeys(TASK_ABBR.get(e["task"], e["task"]) for e in fam["endpoints"]))
        kind = "🌶️ Spicy" if fam["spicy"] else L("standard", "Standard")
        si, fr = freedom_cell(fam)
        rows.append(f"| [{fam['name']}]({site('/models/' + fam['page'], 'model-table')}) | {kind} | {tasks} | {price} | {si} | {fr} |")
    return "\n".join(rows)


def render_showcase(items: list[dict]) -> str:
    body, seen = [], []
    for it in items:
        if it["family"] not in seen:
            seen.append(it["family"])
    for fam in seen:
        group = [g for g in items if g["family"] == fam]
        page = group[0]["page"]
        kind = (L("spicy_edition", "🌶️ Spicy edition") if group[0]["type"] == "spicy"
                else L("standard_unrestricted", "Standard model, catalog tier: unrestricted"))
        link = site(f"/models/{page}", "showcase")
        body.append(f"### {fam}\n")
        body.append(f"<sub>{kind} · <a href=\"{link}\">{L('model_page', 'model page')}</a></sub>\n")
        body.append("<table>")
        for g in group:
            if g["hidden"]:
                left = (f'<sub>{L("preview_hidden", "Preview not shown on GitHub.")}<br>'
                        f'<a href="{link}">{L("see_on_site", "See it on spicyapi.ai")}</a></sub>')
            else:
                left = (f'<a href="{g["media"]}"><img src="{g["media"]}" alt="{html.escape(g.get("alt") or g["title"])}" '
                        f'width="230"></a>')
            inputs = ""
            if g["input_images"] and not g["hidden"]:
                thumbs = " ".join(f'<a href="{u}"><img src="{u}" width="60" alt="input"></a>' for u in g["input_images"])
                inputs = f"<br><sub>{L('input_images', 'Input image(s)')}{L('colon', ':')}</sub> {thumbs}"
            right = (f'<b>{html.escape(g["title"])}</b><br><sub><code>{g["model"]}</code></sub><br><br>'
                     f'{html.escape(g["prompt"])}{inputs}')
            body.append(f'<tr><td width="250" align="center" valign="top">{left}</td><td valign="top">{right}</td></tr>')
        body.append("</table>\n")
    return "\n".join(body)


def render_prompts(data: dict, models: dict, loras: dict) -> tuple[str, str]:
    toc, body = [], []
    tr_cat = I18N.get("categories", {})
    tr_p = I18N.get("prompts", {})
    levels = I18N.get("labels", {}).get("levels", {})
    colon = L("colon", ":")
    for cat in data["categories"]:
        items = [p for p in data["prompts"] if p["cat"] == cat["key"]]
        title = tr_cat.get(cat["key"], {}).get("title", cat["title"])
        intro = tr_cat.get(cat["key"], {}).get("intro", cat["intro"])
        toc.append(f"  - [{title}](#{anchor(title)}) ({len(items)})")
        body.append(f"### {title}\n\n{intro}\n")
        for p in items:
            m = models[p["model"]]
            t = tr_p.get(p["id"], {})
            if "size" in p:
                w, h = p["size"].split("x")
                params = f"`width={w}` `height={h}`"
                cost = money(m["per_image"])
            else:
                params = f"`aspect_ratio={p['ar']}` `resolution={p['res']}`"
                cost = money(m["prices"][p["res"]])
            if p.get("lora"):
                names = p["lora"].split("+")
                scales = [1] if len(names) == 1 else [0.9, 0.45]
                parts = [f"[{loras[n]['name']}]({loras[n]['page']}) × {s}" for n, s in zip(names, scales)]
                params += " · LoRA: " + " + ".join(parts)
            body.append(f"#### {p['id']} · {t.get('title', p['title'])}\n")
            body.append("```text\n" + p["prompt"] + "\n```\n")
            body.append(f"| {L('col_model', 'Model')} | {L('col_settings', 'Settings')} | "
                        f"{L('col_cost', 'Cost per image')} | {L('col_level', 'Level')} |")
            body.append("|---|---|---|---|")
            body.append(f"| {model_link(m, p['id'].lower())} | {params} | {cost} | {levels.get(p['level'], p['level'])} |\n")
            if p.get("input"):
                body.append(f"**{L('input', 'Input')}{colon}** {t.get('input', p['input'])}  ")
            body.append(f"**{L('tip', 'Tip')}{colon}** {t.get('tip', p['tip'])}\n")
    return "\n".join(toc), "\n".join(body)


def render(lang: str) -> str | None:
    global LANG, I18N
    template_path = ROOT / ("README.template.md" if not lang else f"README.template.{lang}.md")
    if not template_path.exists():
        return None
    LANG = lang
    i18n_path = DATA / "i18n" / f"{lang}.json"
    I18N = json.loads(i18n_path.read_text(encoding="utf-8")) if lang and i18n_path.exists() else {}
    models_doc = load("models.json")
    prompts = load("image-prompts.json")
    showcase = load("showcase.json")["items"]
    toc, body = render_prompts(prompts, models_doc["models"], models_doc["loras"])
    replacements = {
        "{{READ_ON}}": models_doc["read_on"],
        "{{PROMPT_COUNT}}": str(len(prompts["prompts"])),
        "{{EDIT_COUNT}}": str(sum(1 for p in prompts["prompts"] if p["cat"] == "edit")),
        "{{SHOWCASE_COUNT}}": str(len(showcase)),
        "{{MODEL_TABLE}}": render_model_table(load("catalog.json")),
        "{{SHOWCASE}}": render_showcase(showcase),
        "{{PROMPTS_TOC}}": toc,
        "{{PROMPTS}}": body,
    }
    text = template_path.read_text(encoding="utf-8")
    for key, value in replacements.items():
        text = text.replace(key, value)
    leftover = re.findall(r"\{\{[A-Z_]+\}\}", text)
    if leftover:
        raise SystemExit(f"{template_path.name}: unfilled placeholders {leftover}")
    out = ROOT / ("README.md" if not lang else f"README.{lang}.md")
    out.write_text(text, encoding="utf-8")
    return out.name


def main() -> None:
    written = [name for name in (render(lang) for lang in LANGS) if name]
    print("written:", ", ".join(written))


if __name__ == "__main__":
    main()
