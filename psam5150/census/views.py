# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.sites.models import get_current_site
from django.shortcuts import redirect
from django.contrib import messages


from census.forms import CensusFork
from census.models import CensusInfo

def censushome(request):
    return render_to_response('census/main.html', context_instance=RequestContext(request))


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
