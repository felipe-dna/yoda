# Y.O.D.A.
A simple way to create an API with Django.

## Get started

Create an django project.
```sh
$ django-admin startproject school
```

Start a new app
```sh
$ django-admin startapp disciplines
```

Add the new app and `yoda` to your `settings.py`.

```python
INSTALLED_APPS = [
    ...
    "yoda.apps.YodaConfig",
    "disciplines.apps.DisciplinesConfig"
]
```

Add the `disciplines` apps urls.

```python
# school/school/urls.py
from django.urls import path, include

urlpatterns = [
    ...
    path('', include('disciplines.urls', namespace='disciplines'))
]
```

Now, let's create an simple disciplines model`:

```python
# school/disciplines/models.py
from django.db import models


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    students = models.IntegerField(default=0)

    def __str__(self):
        return self.name
```

And migrate it...

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Now, we will create an response schema using the `pydantic`:

```python
# school/disciplines/schemas.py
from typing import List, Optional

from pydantic import BaseModel


class DisciplineItemResponse(BaseModel):
    id: int
    name: str
    students: int

    class Config:
        orm_mode = True


class DisciplineResponse(BaseModel):
    page: int = 1
    next: Optional[int] = None
    previous: Optional[int] = None
    disciplines: List[DisciplineItemResponse]

```

With the schema in our hands, let's go create an view to list our disciplines.
We just need to import the generic view APIListView from `yoda.views.list` and
create a class based view that inherits from it. Don't forget to specify the
model that will be used to list the data (or the queryset), the schema we just
created (response_schema) and the context_object_name, that in this case, means
that in our response the key where the `discipline list` will be is `disciplines.

```python
# school/disciplines/views.py
from disciplines.models import Discipline
from disciplines.schemas import DisciplineResponse

from yoda.views.list import APIListView


class DisciplineListView(APIListView):
    model = Discipline
    response_schema = DisciplineResponse
    context_object_name = "disciplines"
```

Don't forget the url.

```python
# school/disciplines/urls.py
from django.urls import path

from disciplines.views import DisciplineListView

app_name = "disciplines"


urlpatterns = [
    path("disciplines", DisciplineListView.as_view(), name="discipline_list")
]
```


As response we got something like: 

```json
{
  "page": 10,
  "previous": 9,
  "next": 11,
  "disciplines": [
    {
      "id": 2,
      "name": "Inglês Instrumental",
      "students": 24
    },
    {
      "id": 1,
      "name": "Português Instrumental",
      "students": 20
    },
    ...
  ]
}
```
