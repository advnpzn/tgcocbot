import os
from pathlib import Path
import toml

class Config:
    """
    The `Config` class represents the instance of the
    Configuration values, which includes sensitive credentials like
    the Telegram `BOT_TOKEN` and the Clash of Clans Developer `API_KEY`.
    """

    def __init__(self) -> None:

        self.BOT_TOKEN = None
        self.API_KEY = None
        self.PROXY = None

        self.__load_config()

    
    def __load_config(self):
        """
        Load the configuration for the Bot.
        It loads from the `config.toml` file and
        sets the values in the respective class members.

        If `config.toml` is not present, you can load it directly
        from the OS environmental variables itself.
        """

        try:
            config_file = Path("config.toml")

            if config_file.exists():
                config = toml.load(config_file)

                self.PROXY = config['proxy']['proxy_uri']
                self.BOT_TOKEN = config['telegram']['bot_token']
                self.API_KEY = config['clashofclans']['api_key']
            else:
                self.PROXY = os.getenv("COC_PROXY", "https://cocproxy.royaleapi.dev")
                self.BOT_TOKEN = os.getenv("BOT_TOKEN", None)
                self.API_KEY = os.environ.get("COC_API", None)

        except Exception as err:
           raise err