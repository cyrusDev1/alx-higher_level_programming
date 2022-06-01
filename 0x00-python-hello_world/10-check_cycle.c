#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to checked
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
    listint_t *s = list;
    listint_t *f = list;

    if (list == NULL)
        return (0);
    while (s != NULL && f != NULL && f->next)
    {
        s = s->next;
        f = f->next->next;
        if (s == f)
            return (1);
    }
    return (0);

}
