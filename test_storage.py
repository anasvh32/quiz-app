import json
import pytest
from storage import save_result


@pytest.fixture
def result_path(tmp_path):
    """fixture: adres-e yek results.json-e movaghat ro mide"""
    return tmp_path / "results.json"

def test_save_result_creates_file(tmp_path):
    """Vaghti natije ro zakhire mikonim, file dorost sakhte beshe"""
    # tmp_path yek poosheye movaghat ast ke pytest khodesh misazad va bad pak mikonad
    file_path = tmp_path / "test_results.json"
    
    data = {"score": 3, "total": 5, "duration_seconds": 12.5}
    save_result(data, path=str(file_path))
    
    assert file_path.exists()
    
    with open(file_path, encoding="utf-8") as f:
        loaded = json.load(f)
    
    assert loaded["score"] == 3
    assert loaded["total"] == 5
    assert loaded["duration_seconds"] == 12.5
def test_second_save_replaces_first(result_path):
    """azmoon do bar ejra she, faghat natije-ye akhar bayad bemoone"""
    save_result({"score": 1, "total": 5, "duration_seconds": 3.0}, path=str(result_path))
    save_result({"score": 4, "total": 5, "duration_seconds": 8.0}, path=str(result_path))

    loaded = json.loads(result_path.read_text(encoding="utf-8"))
    assert loaded["score"] == 4


def test_persian_text_is_readable(result_path):
    """farsi bayad khanda zakhire she, na be sorat-e kod"""
    save_result({"name": "ایران"}, path=str(result_path))

    assert "ایران" in result_path.read_text(encoding="utf-8")

def test_missing_folder_raises(tmp_path):
    """agar poosheh vojood nadashte bashe bayad FileNotFoundError bede"""
    with pytest.raises(FileNotFoundError):
        save_result({"score": 1}, path=str(tmp_path / "nist" / "results.json"))