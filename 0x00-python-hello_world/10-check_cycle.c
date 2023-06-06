
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - Checks if linked list contains a cycle
 * @list: input linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *t, *h;

	if (list == NULL || list->next == NULL)
		return (0);

	t = list->next;
	h = list->next->next;

	while (t && h && h->next)
	{
		if (t == h)
			return (1);

		t = t->next;
		h = h->next->next;
	}

	return (0);
}
