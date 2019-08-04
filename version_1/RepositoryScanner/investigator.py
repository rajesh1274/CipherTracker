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
    page_no = 1
    total_page = 100

    while True:
        res = requests.get(
            f"https://api.github.com/search/repositories?q={keyword}&sort=updated&order=desc&page={page_no}&per_page={total_page}").json()
        repo_items = res.get("items")
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
