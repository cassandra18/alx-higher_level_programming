#include "lists.h"
/**
 * insert_node - Inserts a number into a sorted singly-linked list.
 * @head: A pointer the head of the linked list.
 * @number: The number to insert.
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the temp node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *temp;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;

	if (node == NULL || node->n >= number)
	{
		temp->next = node;
		*head = temp;
		return (temp);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	temp->next = node->next;
	node->next = temp;

	return (temp);
}

