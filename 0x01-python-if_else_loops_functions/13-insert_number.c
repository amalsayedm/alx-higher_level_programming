
#include "lists.h"

/**
 * insert_node - Inserts a node into a sorted linked list
 * @head: A pointer the head
 * @number: The number to be inserted
 * Return: a pointer to the new node or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newnode;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return (NULL);
	newnode->n = number;

	if (node == NULL || node->n >= number)
	{
		newnode->next = node;
		*head = newnode;
		return (newnode);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	newnode->next = node->next;
	node->next = newnode;

	return (newnode);
}
