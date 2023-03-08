#include "lists.h"

int check_cycle(listint_s *list)
{
    if (list == NULL)
        return (1);

    listint_s *Tortoise;
    listint_s *Hare;

    while (Hare != NULL && Hare -> next != NULL )
    {
        Tortoise = Tortoise -> next;
        Hare = Hare -> next -> next;
        if (Tortoise == Hare)
            return (0);
    }
    return (1);
}