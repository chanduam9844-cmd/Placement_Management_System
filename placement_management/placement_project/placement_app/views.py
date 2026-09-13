from django.shortcuts import render, redirect

from .models import Student, Company, Application


# HOME PAGE

def home(request):

    return render(request,'index.html')


# STUDENT REGISTER

def register(request):

    if request.method == 'POST':

        student_id = request.POST['student_id']

        name = request.POST['name']

        email = request.POST['email']

        password = request.POST['password']

        branch = request.POST['branch']

        cgpa = request.POST['cgpa']

        existing_student_id = Student.objects.filter(
            student_id=student_id
        ).first()

        existing_email = Student.objects.filter(
            email=email
        ).first()

        if existing_student_id:

            return render(
                request,
                'register.html',
                {
                    'usn_error':'USN already exists',

                    'student_id':student_id,

                    'name':name,

                    'email':email,

                    'password':password,

                    'branch':branch,

                    'cgpa':cgpa
                }
            )

        if existing_email:

            return render(
                request,
                'register.html',
                {
                    'email_error':'Email already exists',

                    'student_id':student_id,

                    'name':name,

                    'email':email,

                    'password':password,

                    'branch':branch,

                    'cgpa':cgpa
                }
            )

        Student.objects.create(

            student_id=student_id,

            name=name,

            email=email,

            password=password,

            branch=branch,

            cgpa=cgpa
        )

        return redirect('/login/')

    return render(request,'register.html')


# STUDENT LOGIN

def login(request):

    if request.method == 'POST':

        email = request.POST['email']

        password = request.POST['password']

        student = Student.objects.filter(
            email=email,
            password=password
        ).first()

        if student:

            request.session['student_id'] = student.student_id

            companies = Company.objects.all()

            applications = Application.objects.filter(
                student=student
            )

            applied_company_ids = []

            for application in applications:

                applied_company_ids.append(
                    application.company.company_id
                )

            return render(
                request,
                'dashboard.html',
                {
                    'companies':companies,

                    'applications':applications,

                    'applied_company_ids':
                    applied_company_ids
                }
            )

        else:

            return render(
                request,
                'login.html',
                {
                    'error':'Invalid Email or Password'
                }
            )

    return render(request,'login.html')


# APPLY COMPANY

def apply_company(request, company_id):

    if 'student_id' not in request.session:

        return redirect('/login/')

    student = Student.objects.get(
        student_id=request.session['student_id']
    )

    company = Company.objects.get(
        company_id=company_id
    )

    if request.method == 'POST':

        resume = request.FILES['resume']

        Application.objects.create(

            student=student,

            company=company,

            resume=resume
        )

        companies = Company.objects.all()

        applications = Application.objects.filter(
            student=student
        )

        applied_company_ids = []

        for application in applications:

            applied_company_ids.append(
                application.company.company_id
            )

        return render(
            request,
            'dashboard.html',
            {
                'companies':companies,

                'applications':applications,

                'applied_company_ids':
                applied_company_ids,

                'success':
                'Applied Successfully'
            }
        )

    return render(
        request,
        'apply_company.html',
        {
            'company':company
        }
    )


# WITHDRAW APPLICATION

def withdraw_application(request, application_id):

    application = Application.objects.get(
        id=application_id
    )

    application.delete()

    student = Student.objects.get(
        student_id=request.session['student_id']
    )

    companies = Company.objects.all()

    applications = Application.objects.filter(
        student=student
    )

    applied_company_ids = []

    for application in applications:

        applied_company_ids.append(
            application.company.company_id
        )

    return render(
        request,
        'dashboard.html',
        {
            'companies':companies,

            'applications':applications,

            'applied_company_ids':
            applied_company_ids,

            'success':
            'Application Withdrawn Successfully'
        }
    )


# ADMIN LOGIN

def admin_login(request):

    if request.method == 'POST':

        username = request.POST['username']

        password = request.POST['password']

        if username == 'admin' and password == 'admin123':

            companies = Company.objects.all()

            applications = Application.objects.all()

            return render(
                request,
                'admin_dashboard.html',
                {
                    'companies':companies,

                    'applications':applications
                }
            )

        else:

            return render(
                request,
                'admin_login.html',
                {
                    'error':'Invalid Username or Password'
                }
            )

    return render(request,'admin_login.html')


# ADD COMPANY

def add_company(request):

    if request.method == 'POST':

        Company.objects.create(

            company_id=request.POST['company_id'],

            company_name=request.POST['company_name'],

            role=request.POST['role'],

            package=request.POST['package']
        )

        companies = Company.objects.all()

        applications = Application.objects.all()

        return render(
            request,
            'admin_dashboard.html',
            {
                'companies':companies,

                'applications':applications,

                'success':'Company Added Successfully'
            }
        )

    return render(request,'add_company.html')


# ADMIN DASHBOARD

def admin_dashboard(request):

    companies = Company.objects.all()

    applications = Application.objects.all()

    return render(
        request,
        'admin_dashboard.html',
        {
            'companies':companies,

            'applications':applications
        }
    )