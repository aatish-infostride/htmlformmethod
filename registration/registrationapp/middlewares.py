
# from urllib import request
from django.shortcuts import redirect, render


def my_middleware(get_response):
    print("one time initialization")
    def my_function(request):
        print("this is befor view")

        # cookie = request.get_signed_cookie('name', "guest")
        # print(cookie)
        # session= request.session.keys()
        # print(session)

        # if 'user' in request.session:
        #     print('yes')
        #     return redirect('logout')

        # if 'user' in request.session:
        #     current_user = request.session['user']
        #     param = {'current_user': current_user}
        #     # value = User.objects.filter(username= 'aatish')
        #     return render(request, 'base.html', param)

        # elif 'user' not in request.session:
        #     return redirect('login')

        
        response = get_response(request)
        print(response)
        print("this is after view")

        # if 'user' not in request.session:
        #     return redirect('login')

        if 'user' in request.session:
            current_user = request.session['user']
            param = {'current_user': current_user}
            # value = User.objects.filter(username= 'aatish')
            return render(request, 'base.html', param)

        return response
    return my_function
