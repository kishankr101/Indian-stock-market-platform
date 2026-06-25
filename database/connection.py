"""
Database Connection Module

Manages database connection and session management.
Provides utilities for database operations.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from config import DB_CONFIG
import os


class DatabaseConnection:
    """
    Manages database connection and session creation.
    """
    
    def __init__(self):
        """
        Initialize database connection based on configuration.
        """
        if DB_CONFIG['ENGINE'] == 'sqlite':
            # Create data directory if it doesn't exist
            db_path = DB_CONFIG['SQLITE_PATH']
            os.makedirs(os.path.dirname(db_path), exist_ok=True)
            
            # SQLite connection string
            connection_string = f"sqlite:///{db_path}"
        
        elif DB_CONFIG['ENGINE'] == 'postgresql':
            # PostgreSQL connection string
            connection_string = (
                f"postgresql://{DB_CONFIG['POSTGRES_USER']}:"
                f"{DB_CONFIG['POSTGRES_PASSWORD']}@"
                f"{DB_CONFIG['POSTGRES_HOST']}:"
                f"{DB_CONFIG['POSTGRES_PORT']}/"
                f"{DB_CONFIG['POSTGRES_DB']}"
            )
        
        else:
            raise ValueError(f"Unsupported database engine: {DB_CONFIG['ENGINE']}")
        
        self.engine = create_engine(connection_string)
        self.SessionLocal = sessionmaker(bind=self.engine)
    
    def get_session(self) -> Session:
        """
        Get a new database session.
        
        Returns:
            SQLAlchemy Session object
        """
        return self.SessionLocal()
    
    def create_all_tables(self):
        """
        Create all tables defined in models.
        
        Returns:
            None
        """
        from database.models import Base
        Base.metadata.create_all(self.engine)
    
    def drop_all_tables(self):
        """
        Drop all tables (use with caution!).
        
        Returns:
            None
        """
        from database.models import Base
        Base.metadata.drop_all(self.engine)
    
    def close(self):
        """
        Close the database connection.
        
        Returns:
            None
        """
        self.engine.dispose()


# Global database connection instance
db = DatabaseConnection()
