from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bar, Category, Genre


def home(request):
    return HttpResponse("Hiiya!")


def interface(request):

    context = {}

    context['annotated_list'] = Category.get_annotated_list()
    context['available_list'] = Category.objects.filter(end_element=False)

    return render(request, 'interface.html', context)


def new_item(request):
    context = {}

    category = Category.objects.filter()

    name = request.POST.get('name')
    root_element = request.POST.get('root-element')
    parent_name = request.POST.get('parent')
    end_element = request.POST.get('end-element')
    single_element = request.POST.get('single-element')

    if root_element:
        element = Category.add_root(name=name)  # root
        element.list_of_names = name.lower()
        element.save()

    if parent_name:
        def get(node_id): return Category.objects.get(pk=node_id)

        parent = Category.objects.get(name=parent_name)

        # check unique name and create new element
        if not name in parent.list_of_names:
            element = get(parent.pk).add_child(name=name)  # node
            element.list_of_names = f'{parent.list_of_names} {name.lower()}'
            element.save()

    if end_element:
        element.end_element = True
        element.save()

    # get = lambda node_id: Category.objects.get(pk=node_id)
    # root = Category.add_root(name='Computer Hardware')
    # node = get(root.pk).add_child(name='Memory')
    # get(node.pk).add_sibling(name='Hard Drives')
    # get(node.pk).add_child(name='Desktop Memory')

    return redirect('interface')


def del_item(request):
    context = {}

    item_id = request.POST.get('item')
    if item_id:
        item = Category.objects.filter(id=item_id).last()
        item.delete()

    return redirect('interface')


def show_genres(request):
    return render(request, "genres.html", {'genres': Genre.objects.all()})
