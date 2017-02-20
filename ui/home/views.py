from django.http import HttpResponse

def form(request):
    text = '''
    <h1> Welcome to our home-pricing calculator </h1>
    Here is the form to fill out:
    <br />
    <br />
    FORM
    <br />
    <br />
    <a href='execute/'> Submit </a>
    '''
    return HttpResponse(text)
