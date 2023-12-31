from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from photo_gallery_section.models import fixed_Photo
from custom_booking_section.models import booking_data,departure_city,destination_city
from special_packages_section.models import special_package
from team_section.models import team_members
from footer_section.models import footer_logo,footer_paragraph,footer_number,footer_gmail,footer_location,developer,youtube_url
from all_packages_section.models import all_package
from home_section.models import header_number, facebook_link, instagram_link, youtube_link, header_heading, header_paragraph, header_logo
from itertools import chain
from django.shortcuts import get_object_or_404
from payments.forms import userform
from payments.forms import account_details
from payments.models import CombinedData
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
import base64
from django.contrib.auth import authenticate, login as auth_login,logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q





# @csrf_exempt
# def update_price(request):
#     if request.method == "POST" and request.is_ajax():
#         updated_price = request.POST.get("updated_price")
#         print(update_price)
        
#         # You can process the updated price here as needed
#         # For example, you can store it in a session or a database
        
#         return JsonResponse({"message": "Price updated successfully"})
#     else:
#         return JsonResponse({"message": "Invalid request"}, status=400)
#     return render(request,"test.html")



def test(request):
   pass


# Functions

def home(request):
    # Get Footer Logo
    f_logo = footer_logo.objects.first()
    f_paragraph = footer_paragraph.objects.first()
    f_number = footer_number.objects.first()
    f_gmail = footer_gmail.objects.first()
    f_location = footer_location.objects.first()


    #get all team Members 
    all_team_members=team_members.objects.all()

    # Get all Departure Cities 
    all_departure_city=departure_city.objects.all()
    # Get all Departure Cities 
    all_destination_city=destination_city.objects.all()
    # Get all objects (records) from the special_package model
    all_special_packages = special_package.objects.all()
     # Getting all Photos from the Media Folder
    first_image = fixed_Photo.objects.first()
    second_image = fixed_Photo.objects.all()[1]  
    third_image = fixed_Photo.objects.all()[2]  
    fourth_image = fixed_Photo.objects.all()[3]  
    fifth_image = fixed_Photo.objects.all()[4]  


    # Get footer data from model
    foot_logo = footer_logo.objects.first()
    foot_paragraph=footer_paragraph.objects.first()
    foot_number=footer_number.objects.first()
    foot_gmail=footer_gmail.objects.first()
    foot_location=footer_location.objects.first()
    develop_name=developer.objects.first()
    develop_link=developer.objects.first()
    you_url=youtube_url.objects.first()

  

    # Get header data from model
    head_number=header_number.objects.first()
    face_link=facebook_link.objects.first()
    insta_link=instagram_link.objects.first()
    you_link=youtube_link.objects.first()
    head_heading=header_heading.objects.first()
    head_paragraph=header_paragraph.objects.first()
    head_logo=header_logo.objects.first()

    
    you_url=you_url.url.split("www.youtube.com/watch?v=")[1]

   

    dict={
        'first_image':first_image,
        'second_image':second_image,
        'third_image':third_image,
        'fourth_image':fourth_image,
        'fifth_image':fifth_image,
        'all_special_packages':all_special_packages,
        'all_departure_city':all_departure_city,
        'all_destination_city':all_destination_city,
        'all_team_members':all_team_members,
        'foot_logo':foot_logo,
        'foot_paragraph':foot_paragraph,
        'foot_number':foot_number,
        'head_number':head_number,
        'face_link':face_link,
        'insta_link':insta_link,
        'you_link':you_link,
        'head_heading':head_heading,
        'head_paragraph':head_paragraph,
        'head_logo':head_logo,
        'foot_gmail':foot_gmail,
        'foot_location':foot_location,
        'develop_name':develop_name,
        'develop_link':develop_link,
        'you_url':you_url,

        
    }
  

    return render(request,"index.html",dict)

def custom_booking(request):
     # Getting custom Booking Data
    if request.method=="POST":
        name=request.POST.get("name")
        number=request.POST.get("number")
        departure=request.POST.get("departure")
        destination=request.POST.get("destination")
        travellers=request.POST.get("travellers")
        date=request.POST.get("date")
        destination=request.POST.get("destination")
        destination=request.POST.get("destination")
        new=booking_data(name=name,number=number,departure=departure,destination=destination,travellers=travellers,date=date)
        new.save()
    return render(request,"custom_booking.html")

def all_packages(request):
    # Get all Packages from database
    all_packages = all_package.objects.all()

    #Get all objects (records) from the special_package model
    all_special = special_package.objects.all()

    # Combine objects from both models into one variable
    combined_objects = list(chain(all_packages, all_special))

    print(combined_objects)


    dict={
        'combined_objects':combined_objects
    }
    return render(request,"all_packages.html",dict)



# def paynow(request):
#     return render (request,"paynow.html")


def details(request, test):
    x=userform()
    
    special_packages = list(special_package.objects.all())
    all_packages = list(all_package.objects.all())

    # Combine the objects from two different classes into a single list
    combined_packages = special_packages + all_packages

    try:
        # Try to find the object with the given package_name in the combined list
        package = next(p for p in combined_packages if p.package_url == test)
    except StopIteration:
        # If the object with the given package_name doesn't exist in the combined list, raise a 404 error
        raise Http404("Package not found.")
    
    # Create a list of dictionaries containing the package_name and details for each package
    data_list = [{'package_name': package.package_name, 'details': package.details,'price':package.price}]

    # Extract package names and store them in a variable
    package_names = [item['package_name'] for item in data_list]

    package_names_string = ', '.join(package_names)

    # Extract Package Price and store it in a variable
    package_prices = [item['price'] for item in data_list]

    package_price_string = ', '.join(package_prices)


    # return render(request,"index5.html",)
    dict={

        'data_list': data_list,
        'form':x,
        'package_names_string':package_names_string,
        'package_price_string':package_price_string,
    }


    if request.method == 'POST':
        form_a = userform(request.POST)
        if form_a.is_valid():

            
            # Date / Time Data
            datetimeampm = form_a.cleaned_data['datetimeampm']
            # Convert datetimeampm format to day/month/year hours/minutes/seconds am/pm format
            formatted_datetime = datetimeampm.strftime('%d/%m/%Y %I:%M:%S %p')
            request.session['date_time'] = formatted_datetime
           
            # Other Form a Data
            request.session['full_name'] = form_a.cleaned_data['full_name']
            request.session['no_of_travellers'] = form_a.cleaned_data['no_of_travellers']
            request.session['cnic'] = form_a.cleaned_data['cnic']
            request.session['nationality'] = form_a.cleaned_data['nationality']
            request.session['phone'] = form_a.cleaned_data['phone']

            total_amount_value = form_a.cleaned_data['total_amount']
            # Convert the Decimal to a string
            total_amount_str = str(total_amount_value)
            request.session['total_amount'] = total_amount_str
            request.session['package_names_string'] = package_names_string
            request.session['package_price_string'] = package_price_string

           
           

                   
            print(request.session['full_name'])
            print(request.session['no_of_travellers'])
            print(total_amount_value)
            print(request.session['cnic'])
            print(request.session['nationality'])
            print("Total Amount:", total_amount_value)
            print(request.session['date_time'])
            print(request.session['package_names_string'])
            print(request.session['package_price_string'])
            print(request.session['phone'])
            
            
        
            
         

            return redirect('payment')
    else:
        form_a = userform()

    return render(request, "details.html", dict)




def payment(request):
    y=account_details()
    dict={}
    form_b =account_details()
    
    print('kado 1')
    if request.method == 'POST':
        form_b = account_details(request.POST)
        
        if form_b.is_valid():
           
           
           
           account_name = form_b.cleaned_data['account_name']
           account_number = form_b.cleaned_data['account_number']
           proof_image = form_b.cleaned_data['proof_image']


           
           
           return redirect('success_page')
        else:
            form_b = account_details()

    dict={
        'data':y,
        'form_b': form_b

    }

    return render(request,"payment.html",dict)

    

def payment_view(request):
    if request.method == 'POST':
     
        
        image = request.FILES.get("payment_proof")
        account_name = request.POST.get('account_name')
        account_number = request.POST.get('account_number')
        # payment_proof = request.FILES.get('payment_proof')
        full_name=request.session['full_name']
        no_of_travellers=request.session['no_of_travellers']
        total_amount=request.session['total_amount']
        cnic=request.session['cnic']
        phone=request.session['phone']
        date_time=request.session['date_time']
        nationality=request.session['nationality']
        package_names_string=request.session['package_names_string']
        package_price_string = request.session['package_price_string'] 
    
            
        
       
       
        if  image:
            if image.size <= 1024 * 1024:  # Assuming images smaller than 1 MB will be stored in the database
                image=image
            else:
               
                combined_data.image.save(image.name, image)
       
            # Save the combined data to the database
        combined_data = CombinedData(package_names_string=package_names_string,package_price_string=package_price_string,full_name=full_name, no_of_travellers=no_of_travellers,total_amount=total_amount,cnic=cnic,phone=phone,account_name=account_name,account_number=account_number,image=image,date_time=date_time,nationality=nationality)
        print(combined_data.account_name)
        print(combined_data.image)
        combined_data.save()
        # Perform any validation or processing here
  
        del request.session['full_name']
        del request.session['no_of_travellers']
        del request.session['total_amount']
        del request.session['cnic']


       
    return render(request,"thankyou.html")



@login_required(login_url='login')
# from decimal import Decimal

def childaccess(request):
    status_filter = request.GET.get('status_filter', 'all')
    search_query = request.GET.get('search_query', '')

    combined_data_list = CombinedData.objects.all()

    # Filter by status
    if status_filter != 'all':
        combined_data_list = combined_data_list.filter(status=status_filter)

    # Search by name, CNIC, or account_number
    if search_query:
        combined_data_list = combined_data_list.filter(
            Q(full_name__icontains=search_query) | Q(cnic__icontains=search_query) | Q(account_number__icontains=search_query)
        )

    total_verified = combined_data_list.filter(status='verified').count()
    total_records = combined_data_list.count()

    total_amount_verified = sum(
        Decimal(combined_data.total_amount) for combined_data in combined_data_list if combined_data.status == 'verified'
    )

    context = {
        'combined_data_list': combined_data_list,
        'status_filter': status_filter,
        'total_verified': total_verified,
        'total_records': total_records,
        'total_amount_verified': total_amount_verified,
        'search_query': search_query,
    }
    return render(request, "child_access.html", context)





def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('childaccess')
        else:
            return redirect('login')
    return render(request, "login.html")


def logout(request):
    auth_logout(request)
    return redirect('login')




def update_status_view(request, combined_data_id):
    combined_data = CombinedData.objects.get(pk=combined_data_id)
    
    if combined_data.status == 'verified':
        combined_data.status = 'not_verified'
    else:
        combined_data.status = 'verified'
    
    combined_data.save()
    
    return redirect('childaccess')  # Replace with the appropriate URL name





def custom_404_view(request, exception):
    return render(request, 'custom_404.html', status=404)
    
    
def game(request):
    return render(request,"game.html")