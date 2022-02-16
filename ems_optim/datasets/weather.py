import yaml, os, mysql.connector
import pandas as pd

class SqlDb:
    def __init__(self):
        """_summary_
        """
        ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__), '../..'))
        self.config_fpath = os.path.join(ROOT_DIR,'config.yml')
        self.config = self.get_system_config()
    def get_system_config(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        with open(self.config_fpath) as yaml_stream:
            return yaml.safe_load(yaml_stream)
    def connect(self,
                db: str = None):
        """_summary_

        Args:
            db (str, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        return mysql.connector.connect(**self.config['database'],database=db)
    def weather(self,
                start: str = None,
                stop: str = None,
                tcol: str = 'ts',
                mod_name: str = 'weather',):
        """_summary_

        Args:
            start (str, optional): _description_. Defaults to None.
            stop (str, optional): _description_. Defaults to None.
            tcol (str, optional): _description_. Defaults to 'ts'.
            mod_name (str, optional): _description_. Defaults to 'weather'.

        Returns:
            _type_: _description_
        """
        db = self.connect(mod_name)
        tcol = self.config[mod_name]['tcol']
        where_str = f' WHERE locationKey = \"{self.config[mod_name]["locationKey"]}\"'
        where_str += f" AND {tcol} >= \"{start}\"" if start is not None else ""
        where_str += f" AND {tcol} <= \"{stop}\"" if stop is not None else ""
        order_str = f"ORDER BY {tcol} DESC"
        query = f"SELECT * FROM {self.config[mod_name]['table']} {where_str} {order_str}"
        df = pd.read_sql_query(query, db)
        df[tcol] = pd.to_datetime(df[tcol], format='%Y-%m-%d %H:%M:%S')
        df.set_index(tcol, inplace=True)
        return df.drop(['locationKey'],axis=1)