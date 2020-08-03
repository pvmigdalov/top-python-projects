import requests
import json
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

from CONFIG import my_config

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
response_dict = r.json()
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars = repo_dict['stargazers_count']
    description = repo_dict['description']
    url_link = repo_dict['html_url']
    if not description:
        description = 'No description'
    plot_dict = {
        'value': stars,
        'label': description,
        'xlink': url_link
    }
    plot_dicts.append(plot_dict)

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python projects on GitHub'
chart.x_labels = names
chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')