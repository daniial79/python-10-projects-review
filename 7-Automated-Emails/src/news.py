from requests import get


class Content:
    def __init__(self, title: str, link: str):
        self.title = title
        self.link = link

class NewsFeed:
    """Representing multiple news as title and link
    """
    
    _base_url = "https://newsapi.org/v2/everything"
    _api_key = "f94d800ca76249e989895ed31142d71b"
    
    def __init__(self, interest: str, from_date: str, to_date: str, language: str="en"):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language
        
    def _generate_url(self) -> str:
        url = f"{self._base_url}?" \
            f"qInTitle={self.interest}" \
            f"&from={self.from_date}" \
            f"&to={self.to_date}" \
            f"&language={self.language}" \
            f"&apiKey={self._api_key}"       
        
        return url 
        
    def get(self) -> list[Content]:
        url = self._generate_url()
        
        contents = []
        response = get(url)
        articles = response.json()["articles"]
        
        for article in articles:
            contents.append(Content(article["title"], article["url"]))
            
        return contents
    
def to_email_body(contents: list[Content]) -> str:
    body = ""
    for content in contents:
        body += content.title + "\n" +  content.link + "\n\n"
    
    return body

