from .forms import SearchBarForm

def SearchBarContext(request):
    return {'searchbar': SearchBarForm()}

def SetCurrentCourses(request):
    user = request.user

    try:
        current_term = user.terms.all().filter(user=user, current=True)[0]
        current_courses = current_term.courses.all()
    except (AttributeError, IndexError):
        current_courses = None

    return {'current_courses': current_courses}
