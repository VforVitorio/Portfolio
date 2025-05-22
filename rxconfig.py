import reflex as rx

config = rx.Config(
    app_name="Portfolio",  # Actualizado de "portfolio_web"
    # base_path="/harimkang-pages", # Comentado o eliminado si no es necesario
    frontend_only=True,
    build_path=".web",  # Mantener o ajustar según sea necesario
    # static_dir="public", # Comentado o eliminado si no es necesario, assets/ es el predeterminado
    env=rx.Env.PROD,
    # route_prefix="/harimkang-pages", # Comentado o eliminado si no es necesario
    # next_config={ # Comentado o eliminado si no es necesario
    #     "basePath": "/harimkang-pages",
    #     "assetPrefix": "/harimkang-pages",
    #     "trailingSlash": True,
    #     "publicRuntimeConfig": {
    #         "basePath": "/harimkang-pages",
    #     },
    # },
    connect_on_init=False,  # Mantener o ajustar según sea necesario
    disable_ws=True,  # Mantener o ajustar según sea necesario
)
