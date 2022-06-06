#include "lists.h"

void reverse_list(listint_t **head);

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer
 * Return: 1 if is palindrome and if is not
 */

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *tmp = *head, *rev = NULL;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (1)
    {
        fast = fast->next->next;
        if (fast == NULL)
        {
            rev = slow->next;
            break;
        }
        if (fast->next == NULL)
        {
            rev = slow->next->next;
            break;
        }
        slow = slow->next;   
    }

    reverse_list(&rev);

    while (rev != NULL && tmp != NULL)
    {
        if (tmp->n == rev->n)
        {
            rev = rev->next;
            tmp = tmp->next;
        }
        else
        {
            return (0);
        } 
    }

    if (rev == NULL)
        return (1);
    return (0);
}

/**
 * reverse_list - reverses list
 * @head: pointer
 * Return: pointer to the first node
 */

void reverse_list(listint_t **head)
{
    listint_t *prec = NULL;
    listint_t *next = NULL;
    listint_t *curr = *head;

    while (curr != NULL){
        next = curr->next;
        curr->next = prec;
        prec = curr;
        curr = next;
    }
    *head = prec;
}
