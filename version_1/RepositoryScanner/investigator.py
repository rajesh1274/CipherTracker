import requests



def RepositoryInvestigator(keyword,per_page=30):
    resp = requests.get(
        f"https://api.github.com/search/repositories?q={keyword}&sort=updated&order=desc&per_page={per_page}")
    return {
        "keyword": keyword,
        "status_code": resp.status_code,
        "json_response": resp.json()
    }


def CBIRepositoryInvestigator(keyword):
    repos = []
    repo_count = None
    page_no = 1

    while True:
        res = requests.get(
            f"https://api.github.com/search/repositories?q={keyword}&sort=updated&order=desc&page={page_no}&per_page=100").json()
        repo_items = res.get("items")
        if page_no == 1:
            repo_count = res.get("total_count")
        if not repo_items:
            break
        else:
            repos = repos + repo_items
            page_no = page_no + 1

    return {
        "keyword" : keyword,
        "result_count" : repo_count,
        "result_items" : repo_items,
    }
