from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Novel, Vol, Chapter
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
# Create your views here.
#
class IndexView(generic.ListView):
    template_name = 'Novel/index.html'
    context_object_name = 'novel_list'

    def get_queryset(self):
        return Novel.objects.order_by('-title')[:5]

def my_view(request):
    novel_list = Novel.objects.order_by('-title')

    return render_to_response('baseTemplate.html',
                              novel_list,
                              context_instance=RequestContext(request))

class NovelView(generic.DetailView):
    model = Novel
    slug_field = 'novel_slug'
    slug_url_kwarg = 'novel_slug'
    template_name = 'Novel/novel.html'

class ChapterView(generic.DetailView):
    model = Chapter
    slug_field = 'chapter_slug'
    slug_url_kwarg = 'chapter_slug'
    template_name = 'Novel/chapter.html'

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'
#
#
# def vote(request, question_id):
#     p = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = p.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': p,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
