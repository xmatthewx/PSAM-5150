# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect
from django.contrib import messages


from census.forms import CensusFork
from census.models import CensusInfo
from census.models import State
from census.results import yourmomma

def censushome(request):
    peoplecount = len(CensusInfo.objects.all())
    return render_to_response(
        'census/main.html', 
        {'people': peoplecount}, 
        context_instance=RequestContext(request) 
        )


def sitecensus(request):
    if request.method == 'POST':
        form = CensusFork(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Your form has been submitted and will be processed in the order it was received")
            return redirect('census_main')
    else:
        form = CensusFork()
    return render_to_response('census/census.html', {'form': form}, context_instance=RequestContext(request))


def censusresults(request):
    peoplecount = len(CensusInfo.objects.all())
    # census.objects.values()
    men = len(CensusInfo.objects.filter(gender="M"))
    males = CensusInfo.objects.filter(gender="M")
    nycount = len(CensusInfo.objects.values('state'))
    return render_to_response('census/results.html', {'people': peoplecount, 'men': men, 'ny': nycount, })


#def statearchive(request, state):
def statearchive(request):
#    s_list = State.objects.filter(state=state)
    s_list = State.objects.filter()
#    return render_to_response('census/state_archive.html', {'state': state, 'people': s_list})
    return render_to_response('census/state_archive.html', {'people': s_list})

    

    

