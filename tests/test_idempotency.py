from app.db import has_been_processed, mark_as_processed

def test_idempotency_tracking():
    filename = "testfile.jl"
    assert not has_been_processed(filename)
    mark_as_processed(filename)
    assert has_been_processed(filename)
