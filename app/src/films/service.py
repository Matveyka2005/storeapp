#from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotFound


def all_objects(model):
    return model.objects.all()


def all_objects_by_select_related(model, related: str):
    try:
        obj = model.objects.select_related(related).all()
    except Exception as e:
        print(e)
    else:
        return obj

#def single_object(model, **kwargs):
#    return model.objects.get(**kwargs)


def single_obj_or_single_and_select_related(model, related=None, **kwargs):
    if related is not None:
        try:
            obj = model.objects.select_related(related).get(**kwargs)
        except Exception as e:
            print(e)
            return HttpResponseNotFound()
        else:
            return obj
    try:
        obj = model.objects.get(**kwargs)
    except Exception as e:
        print(e)
        return HttpResponseNotFound()
    else:
        return obj
        

def filter_objects(model, **kwargs):
    return model.objects.filter(**kwargs)
