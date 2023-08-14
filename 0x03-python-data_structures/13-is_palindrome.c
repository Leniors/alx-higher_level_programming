#include "lists.h"

/**
 * is_palindrome - checks if a linked list is a palinrome
 * @head: head of a list
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *first = *head;

	if (head == NULL)
	{
		return (1);
	}
	current = *head;

	if (current->next == first && first == current->next)
	{
		return (1);
	}

	return (0);
}
