import app.telegram.miniapp.main as legacy_main
from app.infrastructure.telegram.miniapp.app import app as infra_app
from app.telegram.miniapp import app as package_app


def test_package_exports_infra_app() -> None:
    assert package_app is infra_app


def test_legacy_main_wrapper_delegates_to_asyncio_run(monkeypatch) -> None:
    called: dict[str, bool] = {"runner": False, "asyncio": False}

    async def fake_runner() -> None:
        called["runner"] = True

    def fake_asyncio_run(coro) -> None:
        called["asyncio"] = True
        coro.close()

    monkeypatch.setattr(legacy_main, "run_miniapp_server", fake_runner)
    monkeypatch.setattr(legacy_main.asyncio, "run", fake_asyncio_run)

    legacy_main.main()

    assert called == {"runner": False, "asyncio": True}
