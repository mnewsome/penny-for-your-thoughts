from thoughts.models import Thought

def create_locked_thoughts(quantity_to_create, user):
  for number in range(1, quantity_to_create + 1):
    Thought.objects.create(text="Thought {0}".format(number), user=user)

def create_unlocked_thoughts(quantity_to_create, user):
  for number in range(1, quantity_to_create + 1):
    Thought.objects.create(text="Thought {0}".format(number), user=user, is_locked=False)
