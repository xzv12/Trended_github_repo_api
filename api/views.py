
import requests
from rest_framework.response import Response
from datetime import date, timedelta
from rest_framework.decorators import api_view











def get_lang_count(lang):
    """ fetch the number of repositories that use a specific programing language by using Github API search endpoint  """
   
    response    = requests.get('https://api.github.com/search/repositories?q=language:{lang}&per_page=1'.format(lang=lang))
    repo        = response.json()
    return repo.get('total_count')




@api_view(['GET'])
def fetch_trend_repos(request):
    """
    fetch the three  most trending GitHub repositories created within ten days ago using GitHub API and return a JSON response
    consist of the three repositories {name, URL, main language, number of repositories that use this language on GitHub }
    """


    fetch_date      = date.today()- timedelta(days = 10)
    response        = requests.get('https://api.github.com/search/repositories?q=created:>{date}&sort=stars&order=desc&per_page=3'.format(date=fetch_date))
    repos           = response.json()
    trend_repos     = repos['items']


    result=[]

    for repo in trend_repos:

        repo_name           = repo.get('name')
        repo_url            = repo.get('html_url')
        repo_language       = repo.get('language')
        language_repo_count = get_lang_count(repo_language)
        temp_colm           = {'name':repo_name,'url':repo_url,'language':repo_language,'language_repos_count':language_repo_count }
        
        result.append(temp_colm)

    return Response(result)