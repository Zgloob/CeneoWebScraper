
def extractComponent(domSubtree, selector, attribute=None):
    try:
        if attribute:
            return opinion.select(selector).pop(0)[attribute].strip()
        if attribute is None:
            return opinion.select(selector).pop(0).get_text().strip()      
        
        return [item.get_text().strip() for item in opinion.select(selector)] 
    except IndexError:
        return None