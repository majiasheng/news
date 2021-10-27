from typing import Any, Dict, List


class Headline:
    '''
    e.g.
    {
        'source': {'id': 'cnn', 'name': 'CNN'},
        'author': 'Annie Grayer and Zachary Cohen, CNN',
        'title': 'Liz Cheney calls out Jim Banks for falsely signing letter as the ranking member of January 6 committee - CNN',
        'description': 'GOP Rep. Jim Banks lamented on the House floor that House Speaker Nancy Pelosi prevented him from serving on the House committee investigating the January 6 attack on the US Capitol on Thursday.',
        'url': 'https://www.cnn.com/2021/10/21/politics/jim-banks-liz-cheney-jan-6-committee/index.html',
        'url_to_image': 'https://cdn.cnn.com/cnnnext/dam/assets/211021183403-cheney-banks-split-restricted-super-tease.jpg',
        'published_at': '2021-10-22T00:17:00Z',
        'content': None
    }
    '''

    def __init__(self,
                 source: Dict[str, str],
                 author: str,
                 title: str,
                 description: str,
                 url: str,
                 url_to_image: str,
                 published_at: str,
                 content: str,
                 country: str,
                 category: str) -> None:
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.url_to_image = url_to_image
        self.published_at = published_at
        self.content = content
        self.country = country
        self.category = category

    def _create_id(self) -> str:
        '''
        Url is unique so it's suitable to be id
        '''
        return self.url

    def to_json(self) -> Dict[str, Any]:
        return {
            '_id': self._create_id(),
            'source': self.source,
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'url_to_image': self.url_to_image,
            'published_at': self.published_at,
            'content': self.content,
            'country': self.country,
            'category': self.category
        }
