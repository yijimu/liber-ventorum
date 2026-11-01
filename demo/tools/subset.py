"""Subset the OFL fonts to the characters the film uses.
usage: python subset.py <fonts_src_dir> <index.html> <out_dir>
Collects every character between the TEXT markers in index.html (all JS string literals) plus ASCII."""
import re, sys, pathlib
from fontTools import subset

src, page, out = map(pathlib.Path, sys.argv[1:4])
html = page.read_text(encoding="utf-8")
chars = set(re.sub(r"\s", "", "".join(re.findall(r"'([^'\n]*)'|\"([^\"\n]*)\"|`([^`]*)`", html) and
            [a + b + c for a, b, c in re.findall(r"'([^'\n]*)'|\"([^\"\n]*)\"|`([^`]*)`", html)])))
chars |= set(chr(c) for c in range(0x20, 0x7F)) | set("·°♎，。：；、《》“”？！—…前约")
text = "".join(sorted(chars))
jobs = {
    "NotoSerifSC[wght].ttf": "LVSerif.ttf",
    "CormorantSC-Medium.ttf": "LVLatin.ttf",
    "IBMPlexMono-Regular.ttf": "LVMono.ttf",
}
out.mkdir(parents=True, exist_ok=True)
for s, o in jobs.items():
    opts = subset.Options(); opts.layout_features = ["*"]; opts.notdef_outline = True
    f = subset.load_font(str(src / s), opts)
    sub = subset.Subsetter(opts); sub.populate(text=text); sub.subset(f)
    subset.save_font(f, str(out / o), opts)
    print(o, (out / o).stat().st_size // 1024, "KB")
print(len(text), "characters")
