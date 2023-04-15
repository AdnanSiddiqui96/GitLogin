# import requests
# from django.shortcuts import render

# def repositories(request, username):
#     url = f"https://api.github.com/users/{username}/repos"
#     response = requests.get(url)
#     repositories = response.json()

#     return render(request, 'repositories.html', {'repositories': repositories})



# {% extends 'base.html' %}

# {% block title %}{{ user.username }}'s Repositories{% endblock %}

# {% block content %}
#   <h2>Repositories for {{ user.username }}:</h2>
#   <ul>
#     {% for repo in repositories %}
#       <li>
#         <a href="{{ repo.html_url }}">{{ repo.name }}</a>
#         {% if repo.description %}
#           <p>{{ repo.description }}</p>
#         {% endif %}
#         <p>Language: {{ repo.language }}</p>
#         <p>Stars: {{ repo.stargazers_count }}</p>
#       </li>
#     {% endfor %}
#   </ul>
# {% endblock %}

