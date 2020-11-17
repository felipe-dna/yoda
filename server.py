"""
Contains the server start and health configurations.

To see the uvicorn documentation, visit:
https://www.uvicorn.org/
"""
import uvicorn

from django.conf import settings


class ASGIServer:
    """Define the ASGI uvicorn settings configurations."""
    def __init__(self) -> None:
        """
        Initialize the Server configurations.
        """
        self.debug: bool = bool(settings.DEBUG)
        self.default_server_host: str = "127.0.0.1"
        self.default_server_port: int = 8000
        self.server_host: str = settings.SERVER_HOST
        self.server_port: int = settings.SERVER_PORT
        self.asgi_application: str = settings.ASGI_APPLICATION
        self.reload = self.debug

    def __validate_debug(self) -> None:
        """
        Check if the required variables in non debug mode were passed.

        :raises KeyError: If some required parameter were not passed.
        """
        if not self.debug:
            if self.server_host is None or self.server_port is None:
                raise KeyError(
                    "To use debug False, you must specify the HOST and PORT variables."
                )
        else:
            self.server_host = self.default_server_host
            self.server_port = int(self.default_server_port)

    def run(self) -> None:
        """
        Run the server with uvicorn.
        """
        self.__validate_debug()

        uvicorn.run(
            self.asgi_application,
            host=self.server_host,
            port=self.server_port,
            reload=self.reload
        )


if __name__ == '__main__':
    ASGIServer().run()
