from app.infrastructure.runtime.bootstrap import build_runtime_components, init_infrastructure
from app.infrastructure.runtime.supervisor import run_supervised


async def run_application() -> None:
    init_infrastructure()
    components = await build_runtime_components()
    await run_supervised(components)


__all__ = ["run_application"]
