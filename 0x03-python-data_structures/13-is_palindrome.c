#include "lists.h"

/**
 * reverse_listint - reverses a listint_t linked list
 * @head: pointer to the head of the list
 * Return: pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head != NULL)
	{
		next = (*head)->next;

		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;

	return (*head);
}

/**
 * count_nodes - count the number of nodes in linked list
 * @head: pointer to the head of the list
 * Return: number of nodes
 */
int count_nodes(listint_t **head)
{
	listint_t *current = *head;
	int count = 0;

	while (current != NULL)
	{
		count++;
		current = current->next;
	}

	return (count);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *first_list, *second_list, *current;
	int count, i;

	if (!*head)
		return (PALINDROME);

	count = count_nodes(head);

	current = *head;
	first_list = *head;

	for (i = 0; i < count / 2; i++)
	{
		current = current->next;
	}

	second_list = reverse_listint(&current);

	for (i = 0; i < count / 2 && first_list != NULL && second_list != NULL; i++)
	{
		if (first_list->n != second_list->n)
			return (NOT_PALINDROME);

		first_list = first_list->next;
		second_list = second_list->next;
	}

	return (PALINDROME);
}
