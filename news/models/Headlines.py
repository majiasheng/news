from typing import Any, Dict, List


class Headlines:
    def __init__(self, country: str, category: str, date: str, articles: List[Dict[str, Any]]) -> None:
        # TODO: validate params
        self.country = country
        self.date = date
        self.category = category
        self.articles = articles
    
    def to_json(self) -> Dict[str, Any]:
        return {
            'country': self.country,
            'category': self.category,
            'date': self.country,
            'articles': self.articles
        }
