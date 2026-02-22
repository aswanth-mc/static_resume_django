from django.shortcuts import render

def resume_view(request):
    resume = {
        "name": "aswanth",
        "age": 21,
        "gender": "male",
        "email": "aswanth@example.com",
        "skills": ["Python", "Django", "HTML","css"],
        "education": {
            "degree": "Bachelor of Science in Computer Science",
            "year": "2025",
            "university": "calicut University"
        }
    }

    return render(request, "resume.html", {"resume": resume})