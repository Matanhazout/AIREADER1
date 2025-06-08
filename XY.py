def generate_ajax_config(urls):
    """
    מקבל רשימת URL-ים ומחזיר קונפיגורציה בפורמט הרצוי
    """
    conditions = [f'not(uriMatches(\\S*{url}.*))' for url in urls if url.strip()]
    condition_str = f'and(always,{",".join(conditions)})'

    config = f"""/* BEGIN ajax */
_cls_config.ajaxRecordMetadata="{condition_str}";
_cls_config.ajaxRecordRequestBody="{condition_str}";
_cls_config.ajaxRecordRequestHeaders="{condition_str}";
_cls_config.ajaxRecordResponseBody="{condition_str}";
_cls_config.ajaxRecordResponseHeaders="{condition_str}";
_cls_config.ajaxRecordStats="{condition_str}";
_cls_config.interceptAjax=true;
_cls_config.ajaxRequestBodyMaxLength=24000;
_cls_config.ajaxResponseBodyMaxLength=24000;
/* END ajax */"""

    return config


if __name__ == "__main__":
    print("הכנס URL-ים (שורה לכל URL). סיים עם שורת רווח ריקה:")
    urls = []
    while True:
        line = input()
        if line.strip() == "":
            break
        urls.append(line.strip())

    print("\nהתוצאה:\n")
    print(generate_ajax_config(urls))
