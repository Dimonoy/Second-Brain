import uvicorn
import pytest
from pytest import ExitCode


if __name__ == "__main__":
    ok = pytest.main()
    if ok == ExitCode.OK:
        uvicorn.run("app.app:app", host='localhost', port=8000, reload=True)
