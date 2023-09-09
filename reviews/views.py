from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from reviews.forms import TicketForm, UpdateTicketForm
from reviews.models import Ticket


def flux(request):
    tag = "flux"
    tickets = Ticket.objects.all()

    # combine and sort the two types of posts
    all_posts = sorted(tickets, key=lambda ticket: ticket.time_created, reverse=True)
    all_posts = sorted(all_posts, key=lambda ticket: ticket.reserve)
    return render(request, 'reviews/feed.html', context={'all_posts': all_posts,
                                                         'tag': tag,
                                                         })


@login_required
def posts(request):
    tag = "posts"
    tickets = Ticket.objects.all()

    # combine and sort the two types of posts
    all_posts = sorted(tickets, key=lambda ticket: ticket.time_created, reverse=True)

    return render(request, 'reviews/feed.html', {'all_posts': all_posts,
                                                 'tag': tag
                                                 })


@login_required
def create_ticket(request):
    if request.method == 'POST':
        t_form = TicketForm(request.POST, request.FILES)
        if t_form.is_valid():
            try:
                image = request.FILES['image']
            except MultiValueDictKeyError:
                image = None
            Ticket.objects.create(title=request.POST['title'],
                                  lien_cadeau=request.POST['lien_cadeau'],
                                  image=image,
                                  user=request.user)
            return redirect('flux')
    else:
        t_form = TicketForm()

    return render(request, 'reviews/create_ticket.html', {'t_form': t_form})


@login_required
def update_ticket(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    if request.method == 'POST':
        t_form = UpdateTicketForm(request.POST, request.FILES, instance=ticket)
        if t_form.is_valid():
            t_form.save()
            return redirect('posts')
    else:
        t_form = UpdateTicketForm(instance=ticket)

    return render(request, 'reviews/update_ticket.html', {'t_form': t_form})


@login_required
def delete_ticket(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    ticket.delete()
    return redirect('posts')


@login_required
def reserve_ticket(request, pk):
    tag = "flux"
    ticket = get_object_or_404(Ticket, id=pk)
    # if request.method == 'POST':
    #     t_form = TicketForm(request.POST, request.FILES, instance=ticket)
    #     if t_form.is_valid():
    #         t_form.save()
    #         return redirect('posts')
    # else:
    #     t_form = TicketForm(instance=ticket)

    tickets = Ticket.objects.all()

    return render(request, 'reviews/feed.html', {'all_posts': tickets,
                                                 'tag': tag
                                                 })
