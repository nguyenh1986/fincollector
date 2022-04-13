from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

# Create your models here.
class Study(models.Model):
  topic = models.CharField(max_length=50)

  def __str__(self):
    return self.topic

  def get_absolute_url(self):
    return reverse('study_detail', kwargs={'pk': self.id})


class Finch(models.Model):  # Note that parens are optional if not inheriting from another class
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  studys = models.ManyToManyField(Study)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'finch_id': self.id})
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)  

class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default to be 'B'
    default=MEALS[0][0]
  )
  # creates a cat_id column
  finch = models.ForeignKey(
    Finch,
    # automatically delete all feedings with the cat
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

class Meta:
  ordering = ['-date']