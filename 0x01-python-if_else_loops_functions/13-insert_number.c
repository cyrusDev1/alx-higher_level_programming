#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: list
 * @number: element to insert
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new, *tmp;
    listint_t *cur = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    new->n = number;
    new->next = NULL;

    if (*head == NULL || (*head)->n > number)
    {
        new->next = *head;
        *head = new;
        return (*head);
    }
    while (cur && cur->n < number)
    {
        tmp = cur;
        cur = cur->next;
    }
    tmp->next = new;
    new->next = cur;

    return (new); 
}
