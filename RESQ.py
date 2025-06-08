import sys
import re

def escape_for_regex(url):
    # בריחה בסיסית של תווים ב-URL בשביל regex, אפשר לשפר לפי הצורך
    # בעיקר: לברוח backslash ו-slash
    url = url.replace('\\', '\\\\')
    url = url.replace('/', r'\/')
    return url

def main():
    urls = []
    print("הכנס שורות URL (לסיום Ctrl+D או Ctrl+Z):")
    for line in sys.stdin:
        line = line.strip()
        if line:
            urls.append(line)

    # דוגמה בהתחשב בתבנית הבקשה שלך: כל URL מומר ל־not(uriMatches(\S*/URL.*))
    parts = []
    for url in urls:
        escaped_url = escape_for_regex(url)
        # מייצרים את הביטוי regex כמו בדוגמה שלך
        # מוסיפים .* כדי לתפוס הכל אחרי ה-URL
        part = f"not(uriMatches(\\S*{escaped_url}.*))"
        parts.append(part)

    joined = ",".join(parts)

    template = f"""/* BEGIN ajax */
_cls_config.ajaxRecordMetadata="never";
_cls_config.ajaxRecordRequestBody="and(always,{joined})";
_cls_config.ajaxRecordRequestHeaders="and(always,{joined})";
_cls_config.ajaxRecordResponseBody="and(always,{joined})";
_cls_config.ajaxRecordResponseHeaders="and(always,{joined})";
_cls_config.ajaxRecordStats="and(always,{joined})";
_cls_config.interceptAjax=true;
_cls_config.ajaxRequestBodyMaxLength=24000;
_cls_config.ajaxResponseBodyMaxLength=24000;
/* END ajax */"""

    print(template)

if __name__ == "__main__":
    main()
