def generate_ajax_config(urls):
    """
    מקבל רשימת URL-ים ומחזיר קונפיגורציה בפורמט הרצוי, עם תו \/ במקום /
    """
    conditions = []
    for url in urls:
        url = url.strip()
        if url:
            safe_url = url.replace("/", "\\/")
            condition = f'not(uriMatches(\\S*{safe_url}.*))'
            conditions.append(condition)

    condition_str = f'and(tld,{",".join(conditions)})'

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