#!/usr/bin/env python3
"""Check poem formatting and literal endings, not meter or spoken rhyme."""

import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata


def last_word(text):
    words = re.findall(r"[\w\u064b-\u065f]+", text, flags=re.UNICODE)
    return words[-1] if words else ""


def plain_ending(text):
    return "".join(
        ch for ch in unicodedata.normalize("NFC", text)
        if not unicodedata.combining(ch) and ch != "ـ"
    )


def analyze(text, expected_bayts=6, input_format="bayts"):
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    pairs, issues = [], []
    if input_format == "bayts":
        for number, line in enumerate(lines, 1):
            parts = [part.strip() for part in line.split("#")]
            if len(parts) != 2 or not all(parts):
                issues.append(f"السطر {number}: اكتب شطرين غير فارغين وبينهما #.")
            else:
                pairs.append((number, *parts))
        count = len(lines)
    else:
        count = len(lines) // 2
        if len(lines) % 2:
            issues.append("عدد الأشطر فردي؛ يوجد شطر بلا شطر مقابل.")
        pairs = [(i // 2 + 1, lines[i], lines[i + 1]) for i in range(0, len(lines) - 1, 2)]
    if not lines:
        issues.append("لا يوجد نص شعري للفحص.")
    if count != expected_bayts:
        issues.append(f"عدد الأبيات {count}، والمطلوب {expected_bayts}.")
    endings = []
    for number, sadr, ajuz in pairs:
        if not last_word(sadr) or not last_word(ajuz):
            issues.append(f"البيت {number}: أحد الأشطر لا يحتوي كلمة.")
        endings.append({
            "bayt": number,
            "sadr_last_word": last_word(sadr),
            "ajuz_last_word": last_word(ajuz),
            "ajuz_last_word_without_marks": plain_ending(last_word(ajuz)),
        })
    return {
        "format": input_format,
        "expected_bayts": expected_bayts,
        "observed_bayts": count,
        "complete_bayts": len(pairs),
        "structure_ok": not issues,
        "issues": issues,
        "endings": endings,
        "meter_checked": False,
        "spoken_rhyme_checked": False,
        "note": "فحص تنسيق وعدد فقط؛ لا يثبت الوزن أو القافية المنطوقة أو جودة اللهجة.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", default="-", help="UTF-8 text, or - for stdin")
    parser.add_argument("--expected-bayts", type=int, default=6)
    parser.add_argument("--format", choices=["bayts", "hemistichs"], default="bayts")
    args = parser.parse_args()
    if args.expected_bayts < 1:
        parser.error("--expected-bayts must be positive")
    try:
        text = sys.stdin.read() if args.file == "-" else Path(args.file).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        parser.exit(2, f"Unable to read poem: {error}\n")
    result = analyze(text, args.expected_bayts, args.format)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["structure_ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
