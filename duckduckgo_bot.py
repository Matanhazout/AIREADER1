import requests

def ask_duckduckgo(query):
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json&no_redirect=1"
        response = requests.get(url)
        data = response.json()

        # תשובה ראשית
        if data.get("AbstractText"):
            return data["AbstractText"]

        # תשובה מ־RelatedTopics
        related = data.get("RelatedTopics", [])
        if related:
            for topic in related:
                if isinstance(topic, dict) and "Text" in topic:
                    return topic["Text"]

        return "לא נמצאה תשובה מתאימה בדאקדאקגו."
    except Exception as e:
        print("שגיאה בשאילת דאקדאקגו:", e)
        return "אירעה שגיאה בעת ניסיון לקבל תשובה מדאקדאקגו."