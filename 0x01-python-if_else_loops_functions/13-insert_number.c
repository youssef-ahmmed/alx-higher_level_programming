#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 * Return: he address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *before, *after, *new_node;

	if (!*head || !head)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	after = *head;

	if (new_node->n < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (*head);
	}

	while (new_node->n > after->n)
	{
		before = after;
		after = after->next;
	}

	new_node->next = after;
	before->next = new_node;

	return (*head);
}
