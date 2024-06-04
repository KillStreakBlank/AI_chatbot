from chatterbot.storage.sql_storage import SQLStorageAdapter
from chatterbot.tagging import PosHypernymTagger
from sqlalchemy import create_engine

class CustomSQLStorageAdapter(SQLStorageAdapter):
    def __init__(self, **kwargs):
        # Remove deprecated 'convert_unicode' parameter and initialize directly
        self.database_uri = kwargs.get('database_uri', 'sqlite:///database.sqlite3')
        self.engine = create_engine(self.database_uri)
        self.Session = self.create_session()

        # Add a tagger attribute
        self.tagger = PosHypernymTagger(language=kwargs.get('tagger_language', 'english'))

    def create_session(self):
        from sqlalchemy.orm import sessionmaker
        Session = sessionmaker(bind=self.engine)
        return Session