from thoughts.models import Thought

def get_thoughts(limit=None, **filters):
	if limit:
		return Thought.objects.filter(**filters)[:limit]
	return Thought.objects.filter(**filters)