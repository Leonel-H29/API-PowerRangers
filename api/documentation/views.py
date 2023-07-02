from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from api.settings.base import *
from documentation.readme import convert_md_to_html
from django.shortcuts import render

# Create your views here.


class DocumentationViewSet(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request):

        readme = str(BASE_DIR) + '/README.md'
        html_content = convert_md_to_html(readme)

        return render(request, 'index.html', {'html_content': html_content})
