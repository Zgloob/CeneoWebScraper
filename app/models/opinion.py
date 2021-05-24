from app.utils import extractComponent

class Opinion:

    components = {
        "author":["span.user-post__author-name"],
        "rcmd":["span.user-post__author-recomendation > em"],
        "stars":["span.user-post__score-count"],
        "content":["div.user-post__text"],
        "pros":["[class*=\"positives\"]~ div.review-feature_item", False],
        "cons":["div[class*=\"negatives\"] ~ div.review-feature_item", False],
        "purchased":["div.review-pz"],
        "publishDate":["span.user-post__published > time:nth-child(1)", "datetime"],
        "purchaseDate":["span.user-post__published > time:nth-child(2)", "datetime"],
        "useful":["span[id^='votes-yes']"],
        "useless":["span[id^='votes-no']"]
    }

    def __init__(self, opinionId = None, author = None, rcmd = None, stars = None, content = None, pros = [], cons = [], purchased = None, publishDate = None, purchaseDate = None, useful = None, useless = None):
        self.opinionId = opinionId
        self.author = author
        self.rcmd = rcmd
        self.stars = stars
        self.content = content
        self.pros = pros
        self.cons = cons
        self.purchased = purchased
        self.publishDate = publishDate
        self.purchaseDate = purchaseDate
        self.useful = useful
        self.useless = useless

    def extractOpinion(self, opinion):
        for key, value in self.components.items():
            setattr(self, key, extractComponent(opinion, *value))
        self.opinionId = opinion["data-entry-id"] 
        return self 

    def toDict(self):
        return {key: getattr(self, key) for key in self.components.keys()} | {"opinionId": self.opinionDict}
        
    def __str__(self) -> str:
        return f"opinionId: {self.opinionId}<br>" + "<br>".join(f"{key}: {str(getattr(self, key))}" for key in self.components.keys())

    def __repr__(self) -> str:
        return f"Opinion(opinionId)={self.opinionId}, " + ", ".join(f"{key}: {str(getattr(self, key))}" for key in self.components.keys()) + ")"
