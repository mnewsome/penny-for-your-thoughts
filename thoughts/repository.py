from thoughts.models import Thought

def get_thoughts(limit=None, **filters):
	if limit:
		return Thought.objects.filter(**filters).order_by('-date_created')[:limit]
	return Thought.objects.filter(**filters).order_by('-date_created')

def locked_thought_count():
	return Thought.objects.filter(is_locked=True).count()

def unlocked_thought_count():
	return Thought.objects.filter(is_locked=False).count()

def next_locked_thought():
	return Thought.objects.filter(is_locked=True).order_by('date_created').first()

def unlock_thoughts(unlocked_pool_size):
	if locked_thought_count() > 0:
		thought_keys = Thought.objects.filter(is_locked=True).order_by('date_created').values('pk')[:unlocked_pool_size]
		return Thought.objects.filter(pk__in=thought_keys).update(is_locked=False)
	return 0

