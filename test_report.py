# test_report.py
from report import collect_results, write_report


def test_all_scenarios_pass():
    """har panj halat bayad dorost ejra beshe"""
    results = collect_results()

    assert len(results) == 5
    assert all(r["ok"] for r in results)


def test_report_file_is_written(tmp_path):
    """file-e HTML sakhte mishe va jadval-e natije-ha tush hast"""
    path = write_report(str(tmp_path / "report.html"))

    with open(path, encoding="utf-8") as f:
        content = f.read()

    assert "<table" in content
    assert "PASS" in content
    assert "FAIL" not in content