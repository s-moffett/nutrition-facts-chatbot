from abc import ABC, abstractmethod
from blog_post import BlogPost

class VectorDB(ABC):
    
    @abstractmethod
    def query_db(self, query) -> list[BlogPost]:
        return []
