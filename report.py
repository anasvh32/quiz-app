# Gozaresh-e natije-ye halat-haye service. Hich input/print inja nist.
import html

from fake_service import FakeResponse, fake_get, fake_get_timeout
from service import ServerError, ServiceError, ServiceTimeout, fetch_questions


def reply(status, data):
    """yek get-e sakhtegi ke hamishe hamin javab ro mide"""
    return lambda url, timeout=None: FakeResponse(status, data)


# (esm-e halat, get-e sakhtegi, khata-i ke entezar darim; None yaani movafagh)
SCENARIOS = [
    ("movafagh", fake_get, None),
    ("timeout", fake_get_timeout, ServiceTimeout),
    ("status 500", reply(500, {}), ServerError),
    ("status 404", reply(404, {}), ServiceError),
    ("shekl-e eshtebah", reply(200, [1, 2, 3]), ValueError),
]


def run_scenario(get, expected):
    """yek halat ro ejra mikone va (dorost bud?, payam) bar migardoone"""
    try:
        questions = fetch_questions(get=get)
    except Exception as error:
        return type(error) is expected, f"{type(error).__name__}: {error}"
    return expected is None, f"{len(questions)} soal khande shod"


def collect_results():
    return [
        {"name": name, "ok": ok, "message": message}
        for name, get, expected in SCENARIOS
        for ok, message in [run_scenario(get, expected)]
    ]


def build_html(results):
    """yek jadval-e sade (bedune ketabkhane) az natije-ha misaze"""
    passed = sum(r["ok"] for r in results)
    rows = "".join(
        f"<tr><td>{html.escape(r['name'])}</td>"
        f"<td>{'PASS' if r['ok'] else 'FAIL'}</td>"
        f"<td>{html.escape(r['message'])}</td></tr>"
        for r in results
    )
    return (
        "<html><head><meta charset='utf-8'><title>Gozaresh</title></head><body>"
        f"<h2>{passed} az {len(results)} halat dorost bud</h2>"
        "<table border='1' cellpadding='6'>"
        "<tr><th>halat</th><th>natije</th><th>payam</th></tr>"
        f"{rows}</table></body></html>"
    )


def write_report(path="report.html"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_html(collect_results()))
    return path


if __name__ == "__main__":
    write_report()