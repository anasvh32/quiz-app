import json
from storage import save_result

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